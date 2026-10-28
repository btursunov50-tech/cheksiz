---
name: seedance-30s-infinite
description: Seedance 2.5 single 30-second vertical 9:16 mini-drama videos for the "Infinite AI & Me" channel (Usta & Diyor series and similar). Use when the user asks for a Seedance / 30-second / 30 soniyalik video, sends scene images or character reference images, or pastes a scene list or Veo prompts. One call = one complete 30-second video. Talks to the user in Uzbek (Latin).
---

# Seedance 2.5 — 30 s, Infinite AI & Me

Adapted from the owner's "seedance-2-5-30s" skill for our channel (2026-10-28).
The user is the channel owner. Write every message to them in **Uzbek (Latin)**, short and simple, with small tables.

## Hard lock
- `model_version: "seedance_2.5"` in every call.
- `duration: 30` (only if the user asks for a shorter length, use that length, 5–30 s). Always ONE call = ONE complete video.
- `ratio: "9:16"` unless the user names another ratio (our Shorts/Reels are vertical).
- At most 2 videos per reply.
- Do not offer to split the video into parts. If the tool itself returns an error or a shorter video, tell the user plainly what happened (honesty first), then retry once with the same single 30-second call.

## Our channel rules (put them into every prompt)
1. **Characters stay the same.** Attach the character reference images first and describe them in the prompt every time:
   - USTA: calm man about 30, fuller face, short neat full jet-black beard, black Uzbek doppi skullcap with a white arch pattern, dark embroidered chapan robe with a red sash, young smooth hands.
   - DIYOR: naive guy about 20, round boyish face, big innocent eyes, messy straight jet-black hair (never curly, never brown), dark navy hoodie, black backpack, jeans, sneakers, a thin cyan-blue glow outline.
   - Write: "Keep every character exactly as in the reference images for the whole 30 seconds: same faces, same age, same clothes, five fingers on each hand. Different people never share one face."
   - Other characters (e.g. a girl) are fictional; never a real person's face.
2. **Style:** hand-painted semi-realistic cartoon illustration, exactly like the attached scene images; only 2–3 main colours per shot (taken from the images); street lamps keep their cool neon-blue glass when the images show it.
3. **Every shot has a clear camera move** (push-in, arc, orbit, crane, dolly, handheld, snap zoom) and the camera is never static. Neighbouring shots use different moves. Emotional lines get a close-up with a detailed facial expression (eyes, eyebrows, cheeks, smile).
4. **Characters move clearly** (gestures, turning, walking, hands working). Movements keep their direction and never reverse (someone who walks out of frame does not come back). Background passers-by stay small, blurred, faceless and keep walking.
5. **Dialogue:** the speaker's exact Uzbek line goes into the prompt as `Usta says in Uzbek: "..."` so the lips follow the real words; the listener keeps his mouth closed. Our own voice file (Manus) is laid over the video later, so the timing of each line matters more than the generated sound.
6. **Never:** text, letters, numbers, subtitles, logos, brand names, watermark, flags, extra people in focus, real people's faces.

## Workflow

### 1. Read what the user sent
- Look at every image with `Read` before writing anything (scene images in order + character references).
- If the user pastes a scene list / Veo prompts / a voice script, use those lines and their order.

### 2. Plan ONE 30-second arc
Split the 30 s into 3–5 shots that follow the scene images in order, with the Uzbek line of each shot and its target length (Uzbek speech ≈ 2.5–3 syllables per second; leave ~0.5 s between lines). Example:

| Vaqt | Kadr (rasm) | Kamera | Gap |
|---|---|---|---|
| 0–6 s | 1-rasm | sekin yaqinlashish | Usta: «…» |
| 6–13 s | 2-rasm | qo'lda, yengil chayqalish | Diyor: «…» |
| 13–20 s | 3-rasm | yoy bo'ylab | Usta: «…» — Diyor: «…» |
| 20–30 s | 4-rasm | oldinga suzish | Usta: «…» |

### 3. Confirmation (in Uzbek) — wait for «ha / boshla / go»
Show: duration 30 s, model Seedance 2.5, ratio 9:16, style, characters, the shot table above, lighting, negative list, and this audio note: «Video ovozsiz yoki AI ovozi bilan chiqadi; Usta va Diyorning asl ovozi montajda qo'yiladi».

### 4. Generate
- Upload local images with `FileBatchUpload`; use only the returned URLs.
- Order in `image_reference_url_list`: scene images first (1, 2, 3, …), then USTA reference, then DIYOR reference (and any other reference). Say in the prompt which image is which ("Image 5 is USTA, image 6 is DIYOR").
- Call:
```
image_to_video(
  model_version: "seedance_2.5",
  duration: 30,
  ratio: "9:16",
  prompt: "<full prompt, template below>",
  image_reference_url_list: ["<scene1>", "<scene2>", "...", "<usta_ref>", "<diyor_ref>"]
)
```
- Deliver with `NotifyHuman` including the video URL / file. Add one Uzbek line: what to check (faces, watermark) and «faylni Claude'ga yuboring, tekshirib montajga qo'shadi».

## Prompt template (fill every <…>; keep the whole text in ONE prompt)
```
Vertical 9:16, 30 seconds, one continuous mini-drama in <N> shots, hand-painted semi-realistic cartoon style exactly like the attached images, <light and 2–3 main colours>, <lamps / special details>. Use image 1 … <N> as the shots in this order. Image <N+1> is USTA and image <N+2> is DIYOR: keep both characters exactly as in these reference images for the whole 30 seconds — Usta about 30, fuller face, short neat full black beard, black doppi with a white arch pattern, dark embroidered chapan with a red sash; Diyor about 20, round boyish face, big eyes, messy straight jet-black hair, navy hoodie, black backpack, thin cyan-blue glow outline. Same faces and the same background place in every shot, five fingers on each hand.

SHOT 1 (<0–6 s>, image 1): <camera move>. <who speaks, expression, gestures; listener's action, mouth closed>. Usta says in Uzbek, in a calm deep warm male voice of about 30-35: "<line>"
SHOT 2 (<…>, image 2): <camera move>. <action>. Diyor says in Uzbek, in a lighter young male voice of about 22: "<line>"
…

Every shot has a clear camera move and the camera is never static. The speaker's lips and jaw move with the Uzbek words; the listener keeps his mouth closed. Background passers-by stay small, blurred and faceless and keep walking. No text, no subtitles, no logos, no watermark.
```

## Lessons from our tests
- Dola/Seedance test (2026-10-28): asked 30 s, got 15 s → write the time of every shot explicitly and repeat "30 seconds" at the start and the end.
- In the same test shot 2 moved Diyor to another street and made his face older/realistic → the prompt must say "the same background place in every shot" and repeat Diyor's round boyish cartoon face.
