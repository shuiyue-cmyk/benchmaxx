# BenchMaxx introduction video

A 71-second, 1080p30 introduction with bilingual (Chinese / English) burned-in captions and a procedurally generated soundtrack (no voice).

Every frame is a pure function of time (`renderAt(t)` in [`scene.html`](scene.html)). The renderer drives headless Edge/Chrome frame by frame and pipes the frames into ffmpeg, so the output is deterministic. The data comes from [`../results/latest.json`](../results/latest.json).

```bash
npm install
node render.mjs                    # -> out/benchmaxx_intro.mp4 (+ zh / en / bilingual .srt)
node render.mjs --stills 25.8,48   # preview individual frames
```

Requirements: Node 18+, ffmpeg on `PATH`, Python 3 with numpy (for the soundtrack), and Edge or Chrome (set `BROWSER_PATH` if they are not auto-detected).

To preview the animation in real time, open `scene.html` directly in a browser.
