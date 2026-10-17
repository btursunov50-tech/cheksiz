import React from 'react';
import {AbsoluteFill, Sequence, interpolate, spring, useCurrentFrame, useVideoConfig, Easing} from 'remotion';

const C = {
  bg1: '#0A1424',
  bg2: '#11294A',
  blue: '#2AABEE',
  red: '#FF4D4F',
  gold: '#E8B85B',
  white: '#F5F8FC',
  muted: '#9FB3CC',
};
const FONT = '"Inter Display", "Inter", "DejaVu Sans", sans-serif';

// Sahnaga kirish va chiqish (yumshoq)
const useInOut = (dur: number) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({frame: f, fps, config: {damping: 16, stiffness: 120}});
  const exit = interpolate(f, [dur - 8, dur], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return {f, fps, enter, exit};
};

const Background: React.FC = () => {
  const f = useCurrentFrame();
  const shift = interpolate(f, [0, 210], [0, 120]);
  return (
    <AbsoluteFill style={{background: `linear-gradient(160deg, ${C.bg1} 0%, ${C.bg2} 100%)`}}>
      {/* sekin suzib yuruvchi doiralar */}
      {[0, 1, 2].map((i) => (
        <div
          key={i}
          style={{
            position: 'absolute',
            width: 700 - i * 160,
            height: 700 - i * 160,
            borderRadius: '50%',
            border: `3px solid ${C.blue}`,
            opacity: 0.08 + i * 0.03,
            left: 190 + i * 80 + Math.sin((f + i * 40) / 40) * 30,
            top: 1150 - shift + i * 90,
          }}
        />
      ))}
    </AbsoluteFill>
  );
};

const Warning: React.FC = () => {
  const {f, enter, exit} = useInOut(45);
  const pulse = 1 + Math.sin(f / 4) * 0.06;
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center', opacity: exit, padding: 80}}>
      <div style={{transform: `scale(${enter * pulse})`, marginBottom: 60}}>
        <svg width="260" height="230" viewBox="0 0 260 230">
          <path d="M130 10 L250 220 L10 220 Z" fill={C.red} stroke={C.white} strokeWidth="8" strokeLinejoin="round" />
          <rect x="120" y="80" width="20" height="80" rx="8" fill={C.white} />
          <circle cx="130" cy="188" r="12" fill={C.white} />
        </svg>
      </div>
      <div style={{fontFamily: FONT, fontWeight: 900, fontSize: 64, letterSpacing: 8, color: C.red, opacity: enter}}>DIQQAT!</div>
      <div
        style={{
          fontFamily: FONT,
          fontWeight: 800,
          fontSize: 96,
          lineHeight: 1.08,
          color: C.white,
          textAlign: 'center',
          marginTop: 30,
          transform: `translateY(${(1 - enter) * 80}px)`,
          opacity: enter,
        }}
      >
        Telegramingizni o'g'irlashlari mumkin
      </div>
    </AbsoluteFill>
  );
};

const Shield: React.FC = () => {
  const {f, enter, exit} = useInOut(60);
  const draw = interpolate(f, [0, 30], [1, 0], {extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic)});
  const tick = interpolate(f, [22, 40], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center', opacity: exit, padding: 80}}>
      <svg width="420" height="480" viewBox="0 0 420 480" style={{transform: `scale(${0.8 + enter * 0.2})`}}>
        <path
          d="M210 20 L390 90 V230 C390 350 310 430 210 465 C110 430 30 350 30 230 V90 Z"
          fill="rgba(42,171,238,0.15)"
          stroke={C.blue}
          strokeWidth="18"
          strokeLinejoin="round"
          pathLength={1}
          strokeDasharray={1}
          strokeDashoffset={draw}
        />
        <path d="M130 245 L190 305 L300 185" fill="none" stroke={C.white} strokeWidth="30" strokeLinecap="round" strokeLinejoin="round" pathLength={1} strokeDasharray={1} strokeDashoffset={tick} />
      </svg>
      <div style={{fontFamily: FONT, fontWeight: 800, fontSize: 104, color: C.white, textAlign: 'center', marginTop: 60, lineHeight: 1.05, opacity: enter}}>
        <span style={{color: C.blue}}>1 daqiqada</span>
        <br />
        himoya qiling
      </div>
    </AbsoluteFill>
  );
};

const steps = ['Sozlamalar', 'Maxfiylik va xavfsizlik', 'Ikki bosqichli tekshiruv'];

const Steps: React.FC = () => {
  const {f, fps, exit} = useInOut(60);
  return (
    <AbsoluteFill style={{justifyContent: 'center', padding: '0 70px', opacity: exit, gap: 36}}>
      {steps.map((s, i) => {
        const p = spring({frame: f - i * 12, fps, config: {damping: 15, stiffness: 140}});
        return (
          <div
            key={s}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 34,
              background: 'rgba(255,255,255,0.07)',
              border: `3px solid ${i === 2 ? C.blue : 'rgba(255,255,255,0.15)'}`,
              borderRadius: 36,
              padding: '34px 40px',
              transform: `translateX(${(1 - p) * 900}px)`,
              opacity: p,
            }}
          >
            <div
              style={{
                width: 110,
                height: 110,
                minWidth: 110,
                borderRadius: '50%',
                background: C.blue,
                color: C.bg1,
                fontFamily: FONT,
                fontWeight: 900,
                fontSize: 64,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
            >
              {i + 1}
            </div>
            <div style={{fontFamily: FONT, fontWeight: 800, fontSize: 64, color: C.white, lineHeight: 1.1}}>{s}</div>
          </div>
        );
      })}
      <div style={{fontFamily: FONT, fontWeight: 700, fontSize: 56, color: C.gold, textAlign: 'center', marginTop: 20, opacity: interpolate(f, [30, 40], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})}}>
        → bulutli parol qo'ying
      </div>
    </AbsoluteFill>
  );
};

const Final: React.FC = () => {
  const {f, enter} = useInOut(9999);
  const sub = interpolate(f, [14, 26], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center', padding: 80}}>
      <div style={{fontFamily: FONT, fontWeight: 900, fontSize: 104, lineHeight: 1.05, color: C.white, textAlign: 'center', transform: `scale(${0.85 + enter * 0.15})`, opacity: enter}}>
        SMS kodni <span style={{color: C.red}}>hech kimga</span> bermang!
      </div>
      <div style={{fontFamily: FONT, fontWeight: 600, fontSize: 52, color: C.muted, textAlign: 'center', marginTop: 50, opacity: sub, lineHeight: 1.3}}>
        Saqlab qo'ying va yaqinlaringizga yuboring
      </div>
      <div style={{position: 'absolute', bottom: 140, fontFamily: FONT, fontWeight: 700, fontSize: 44, color: C.gold, opacity: sub, letterSpacing: 2}}>
        ∞ Infinite AI &amp; Me
      </div>
    </AbsoluteFill>
  );
};

export const Telegram: React.FC = () => (
  <AbsoluteFill>
    <Background />
    <Sequence durationInFrames={45}><Warning /></Sequence>
    <Sequence from={45} durationInFrames={60}><Shield /></Sequence>
    <Sequence from={105} durationInFrames={60}><Steps /></Sequence>
    <Sequence from={165}><Final /></Sequence>
  </AbsoluteFill>
);
