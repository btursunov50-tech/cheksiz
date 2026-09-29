import json, subprocess
import numpy as np
from scipy.signal import butter, sosfilt
from timeline import *

FF = '/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2'
RAW = '/root/.claude/uploads/82f3e155-e852-5839-900d-40d183fb7b67/481f9a55-____________20MB.mp4'
SR = 48000
rng = np.random.default_rng(11)


def load_raw():
    p = subprocess.run([FF, '-v', 'error', '-i', RAW, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True)
    return np.frombuffer(p.stdout, np.float32).copy()


def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, hi], 'bandpass', fs=SR, output='sos'), x)


def hp(x, f, order=2):
    return sosfilt(butter(order, f, 'highpass', fs=SR, output='sos'), x)


def lp(x, f, order=2):
    return sosfilt(butter(order, f, 'lowpass', fs=SR, output='sos'), x)


def env(n, a, d):
    t = np.arange(n) / SR
    return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / d)


def db(x):
    return 10 ** (x / 20)


# ---------------- voice ----------------
def voice_track(total_s):
    raw = load_raw()
    raw = hp(raw, 80).astype(np.float32)
    out = []
    fade = int(0.008 * SR)
    for a, b in CF:
        seg = raw[int(a / FPS * SR):int(b / FPS * SR)].copy()
        seg[:fade] *= np.linspace(0, 1, fade)
        seg[-fade:] *= np.linspace(1, 0, fade)
        out.append(seg)
    v = np.concatenate(out)
    full = np.zeros(int(total_s * SR), np.float32)
    full[:len(v)] = v
    return full


# ---------------- music (lo-fi house, 100 BPM, Am-F-C-G) ----------------
def music(total_s):
    n = int(total_s * SR)
    L = np.zeros(n); R = np.zeros(n)
    bpm = 100
    beat = 60 / bpm
    bar = beat * 4
    chords = [(57, [57, 60, 64]), (53, [53, 57, 60]), (48, [55, 60, 64]), (55, [55, 59, 62])]
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)

    def add(sig, t0, pan=0.0, gain=1.0):
        i = int(t0 * SR)
        if i >= n:
            return
        s = sig[:n - i] * gain
        L[i:i + len(s)] += s * (1 - pan) ** 0.5
        R[i:i + len(s)] += s * (1 + pan) ** 0.5

    tk = np.arange(int(0.3 * SR)) / SR
    kick = np.sin(2 * np.pi * np.cumsum(45 + 90 * np.exp(-tk / 0.03)) / SR) * np.exp(-tk / 0.12)
    tc = int(0.15 * SR)
    clap = bp(rng.normal(0, 1, tc), 900, 3500) * env(tc, 0.002, 0.05)
    th = int(0.05 * SR)
    hat = hp(rng.normal(0, 1, th), 7000) * env(th, 0.0005, 0.012)
    nb = int(np.ceil(total_s / bar)) + 1
    for b in range(nb):
        t0 = b * bar
        root, tones = chords[b % 4]
        for q in range(4):
            add(kick, t0 + q * beat, 0, 0.9 if q in (0, 2) else 0.55)
            if q in (1, 3):
                add(clap, t0 + q * beat, 0, 0.35)
            for e in (0, 0.5):
                add(hat, t0 + (q + e) * beat, 0.3 if e else -0.3, 0.25 if e else 0.15)
            # bass: root on 8ths
            for e in (0, 0.5):
                dur = int(beat * 0.45 * SR)
                tt = np.arange(dur) / SR
                f = hz(root - 12)
                bs = (np.sin(2 * np.pi * f * tt) + 0.25 * np.sin(4 * np.pi * f * tt)) * env(dur, 0.005, 0.18)
                add(bs, t0 + (q + e) * beat, 0, 0.5 if e == 0 else 0.3)
            # off-beat chord pluck
            dur = int(0.5 * SR)
            tt = np.arange(dur) / SR
            pl = sum(np.sign(np.sin(2 * np.pi * hz(m + 12) * tt)) * 0.3 + np.sin(2 * np.pi * hz(m + 12) * tt) for m in tones)
            pl = lp(pl * env(dur, 0.004, 0.14), 2500)
            add(pl, t0 + (q + 0.5) * beat, 0.15 * (-1) ** q, 0.12)
        # soft pad per bar
        dur = int(bar * SR)
        tt = np.arange(dur) / SR
        pad = sum(np.sin(2 * np.pi * hz(m) * tt + 0.3 * np.sin(2 * np.pi * 0.3 * tt)) for m in tones)
        pad *= np.minimum(1, tt / 0.3) * np.minimum(1, (bar - tt) / 0.3)
        add(lp(pad, 1800), t0, 0, 0.05)
    return np.stack([L, R], 1)


MP3 = '/root/.claude/uploads/82f3e155-e852-5839-900d-40d183fb7b67/ca6424b8-SMART_wallpaper________________________________.mp3'


def track_music(total_s, offset=2.0):
    p = subprocess.run([FF, '-v', 'error', '-ss', str(offset), '-t', str(total_s), '-i', MP3, '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True)
    m = np.frombuffer(p.stdout, np.float32).reshape(-1, 2).astype(np.float64)
    n = int(total_s * SR)
    out = np.zeros((n, 2)); out[:min(n, len(m))] = m[:n]
    fi = int(0.06 * SR); out[:fi] *= np.linspace(0, 1, fi)[:, None]
    return out


# ---------------- SFX ----------------
def sfx(name):
    if name == 'pop':
        d = int(0.09 * SR); t = np.arange(d) / SR
        f = 380 + 420 * np.exp(-t / 0.02)
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(d, 0.002, 0.03) * db(-22)
    if name == 'whoosh':
        d = int(0.42 * SR); t = np.arange(d) / SR
        x = rng.normal(0, 1, d)
        x = bp(x, 500, 4000)
        e = np.sin(np.pi * np.clip(t / 0.42, 0, 1)) ** 2
        return x * e * db(-30)
    if name == 'click':
        d = int(0.04 * SR); t = np.arange(d) / SR
        x = hp(rng.normal(0, 1, d), 2500) * env(d, 0.0003, 0.004) + np.sin(2 * np.pi * 2800 * t) * env(d, 0.0005, 0.008)
        return x * db(-20)
    if name == 'scribble':
        d = int(0.36 * SR); t = np.arange(d) / SR
        x = bp(rng.normal(0, 1, d), 1800, 6000) * (0.55 + 0.45 * np.sin(2 * np.pi * 22 * t)) * np.sin(np.pi * t / 0.36)
        return x * db(-30)
    if name == 'coin':
        d = int(0.5 * SR); t = np.arange(d) / SR
        a = (np.sin(2 * np.pi * 2093 * t) + 0.6 * np.sin(2 * np.pi * 4186 * t)) * env(d, 0.001, 0.08)
        b = np.zeros(d)
        o = int(0.07 * SR)
        b[o:] = (np.sin(2 * np.pi * 2637 * t[:d - o]) + 0.5 * np.sin(2 * np.pi * 5274 * t[:d - o])) * env(d - o, 0.001, 0.16)
        return (a + b) * db(-24)
    if name == 'ding':
        d = int(1.2 * SR); t = np.arange(d) / SR
        x = sum(w * np.sin(2 * np.pi * 1318.5 * r * t) * np.exp(-t / (0.5 / r ** 0.5)) for r, w in ((1, 1), (2.0, .4), (2.76, .25), (5.4, .1)))
        return x * env(d, 0.001, 10) * db(-20)
    raise ValueError(name)


def main():
    total = TOTAL / FPS + 0.3
    n = int(total * SR)
    v = voice_track(total)
    m = track_music(total)
    ev = json.load(open('events.json'))
    fx = np.zeros(n)
    for t, name in ev:
        s = sfx(name)
        i = int(max(0, t) * SR)
        e = min(n, i + len(s))
        fx[i:e] += s[:e - i]
    # voice level ~ normalise speech RMS
    vr = np.sqrt(np.mean(v[np.abs(v) > 1e-3] ** 2))
    v = v * (0.1 / vr)
    # ducking envelope from voice
    w = int(0.05 * SR)
    e = np.sqrt(np.convolve(v ** 2, np.ones(w) / w, 'same'))
    e = np.convolve(e, np.ones(int(0.25 * SR)) / int(0.25 * SR), 'same')
    duck = 1 - 0.6 * np.clip(e / 0.05, 0, 1)
    mus_gain = np.full(n, db(-17))
    cta = int(CTA_START / FPS * SR) - int(0.3 * SR)
    ramp = int(0.4 * SR)
    mus_gain[cta:cta + ramp] = np.linspace(db(-17), db(-7), ramp)
    mus_gain[cta + ramp:] = db(-7)
    tail = int((TOTAL / FPS - 0.8) * SR)
    mus_gain[tail:] *= np.linspace(1, 0, n - tail)
    mn = m / (np.sqrt(np.mean(m ** 2)) + 1e-9) * 0.1
    mix = np.zeros((n, 2))
    mix += (v + fx)[:, None]
    mix += mn * (mus_gain * duck)[:, None]
    mix = mix.astype(np.float32)
    mix.tofile('mix.f32')
    print('mixed', n / SR)


if __name__ == '__main__':
    main()
