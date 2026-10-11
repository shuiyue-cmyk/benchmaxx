"""Procedural soundtrack for the BenchMaxx intro (no vocals).

Soft pad progression in D major, a pluck on every on-screen "event", typewriter clicks
while text is typed, and quiet ticks while Track B counts characters. Cue times mirror
the timeline in scene.html.

    python soundtrack.py out.wav 71
"""

import sys
import wave

import numpy as np

SR = 48_000
rng = np.random.default_rng(20261010)


def note(name: str) -> float:
    names = {"C": -9, "C#": -8, "D": -7, "D#": -6, "E": -5, "F": -4, "F#": -3, "G": -2, "G#": -1, "A": 0, "A#": 1, "B": 2}
    pitch, octave = name[:-1], int(name[-1])
    return 440.0 * 2 ** ((names[pitch] + 12 * (octave - 4)) / 12)


def pad(duration: float) -> np.ndarray:
    chords = [
        ["D3", "A3", "C#4", "E4", "F#4"],   # Dmaj9
        ["B2", "F#3", "A3", "C#4", "D4"],   # Bm9
        ["G2", "D3", "F#3", "A3", "B3"],    # Gmaj9
        ["A2", "E3", "F#3", "B3", "C#4"],   # A6/9
    ]
    n = int(duration * SR)
    out = np.zeros((n, 2))
    span = duration / 8
    t = np.arange(n) / SR
    for i in range(8):
        start, end = i * span, (i + 1) * span
        env = np.clip((t - (start - 1.5)) / 3.0, 0, 1) * np.clip(((end + 1.5) - t) / 3.0, 0, 1)
        env = np.sin(env * np.pi / 2) ** 2
        mask = env > 0
        tt = t[mask]
        for j, nm in enumerate(chords[i % 4]):
            f = note(nm)
            for ch, detune in enumerate((-0.6, 0.6)):
                phase = rng.uniform(0, 2 * np.pi)
                v = np.sin(2 * np.pi * (f + detune) * tt + phase) + 0.18 * np.sin(2 * np.pi * 2 * (f + detune) * tt)
                # slow breathing tremolo, different per voice
                v *= 0.8 + 0.2 * np.sin(2 * np.pi * (0.07 + 0.013 * j) * tt + j)
                out[mask, ch] += v * env[mask] * (0.9 if j == 0 else 0.55)
    return out * 0.035


def pluck(freq: float, length: float = 2.2, gain: float = 0.22) -> np.ndarray:
    t = np.arange(int(length * SR)) / SR
    env = np.exp(-t * 3.2) * np.clip(t / 0.004, 0, 1)
    tone = np.sin(2 * np.pi * freq * t) + 0.35 * np.sin(2 * np.pi * 2 * freq * t) * np.exp(-t * 6) \
        + 0.12 * np.sin(2 * np.pi * 3.01 * freq * t) * np.exp(-t * 9)
    return tone * env * gain


def click(gain: float = 0.05) -> np.ndarray:
    n = int(0.012 * SR)
    noise = rng.standard_normal(n)
    noise = np.diff(noise, prepend=0)  # crude high-pass: keep it crisp
    return noise * np.exp(-np.arange(n) / (0.0025 * SR)) * gain


def tick(freq: float = 2100, gain: float = 0.045) -> np.ndarray:
    t = np.arange(int(0.05 * SR)) / SR
    return np.sin(2 * np.pi * freq * t) * np.exp(-t * 90) * gain


def place(buf: np.ndarray, sig: np.ndarray, at: float, pan: float = 0.0) -> None:
    i = int(at * SR)
    if i >= len(buf):
        return
    sig = sig[: len(buf) - i]
    left, right = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    buf[i:i + len(sig), 0] += sig * left
    buf[i:i + len(sig), 1] += sig * right


def reverb(dry: np.ndarray, seconds: float = 2.6, wet: float = 0.28) -> np.ndarray:
    m = int(seconds * SR)
    ir_t = np.arange(m) / SR
    out = np.empty_like(dry)
    for ch in range(2):
        ir = rng.standard_normal(m) * np.exp(-ir_t * 3.0)
        ir /= np.sqrt(np.sum(ir ** 2))
        size = 1 << int(np.ceil(np.log2(len(dry) + m)))
        conv = np.fft.irfft(np.fft.rfft(dry[:, ch], size) * np.fft.rfft(ir, size), size)[: len(dry)]
        out[:, ch] = dry[:, ch] * (1 - wet) + conv * wet
    return out


def main(path: str, duration: float) -> None:
    n = int(duration * SR)
    fx = np.zeros((n, 2))

    # Typewriter: premise lines type at 22 chars/s; "is called." at 16 chars/s.
    for start, count, cps in [(0.3, 24, 22), (1.55, 20, 22), (4.0, 10, 16)]:
        for k in range(count):
            place(fx, click(0.05 + 0.015 * rng.random()), start + k / cps + 0.004 * rng.random(), pan=rng.uniform(-0.3, 0.3))

    # Track B character counter: 35 ticks between 34.9 s and 38.2 s, rising gently in pitch.
    for k in range(35):
        place(fx, tick(1800 + 14 * k, 0.035), 34.9 + k * (3.3 / 35), pan=-0.5 + k / 35)

    # Plucks on key events (D major pentatonic).
    pent = ["D5", "E5", "F#5", "A5", "B5", "D6"]
    events = [
        (3.3, "A4"), (4.0, "F#5"), (6.6, "D5"), (7.4, "A5"),
        (12.3, "D5"), (13.9, "B4"), (16.6, "E5"), (17.6, "A5"), (18.0, "F#5"),
        (21.6, "D5"), (24.0, "B4"), (24.5, "A4"), (25.5, "F#5"), (26.0, "D6"),
        (27.9, "E5"), (29.0, "F#5"), (30.1, "A5"), (31.1, "B5"), (32.3, "A4"),
        (34.5, "D5"), (38.2, "A5"),
        (42.6, "D5"), (46.0, "A5"), (47.8, "D6"), (50.2, "F#5"),
        (54.5, "D5"), (57.3, "F#5"), (60.1, "B4"),
        (63.3, "D5"), (64.0, "E5"), (64.7, "A5"), (66.3, "D6"), (67.4, "A5"),
    ]
    for i, (at, nm) in enumerate(events):
        place(fx, pluck(note(nm), gain=0.16), at, pan=[-0.35, 0.0, 0.35][i % 3])
    # a soft closing arpeggio
    for k, nm in enumerate(pent[::-1]):
        place(fx, pluck(note(nm), 3.0, 0.08), 68.4 + k * 0.18, pan=0.4 - k * 0.16)

    mix = reverb(pad(duration) + fx)
    # master fades and normalisation
    t = np.arange(n) / SR
    fade = np.clip(t / 1.2, 0, 1) * np.clip((duration - t) / 2.5, 0, 1)
    mix *= fade[:, None]
    mix *= 0.84 / np.max(np.abs(mix))  # peak at about -1.5 dBFS (~-15.5 LUFS integrated)
    pcm = (np.clip(mix, -1, 1) * 32767).astype("<i2")
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


if __name__ == "__main__":
    main(sys.argv[1], float(sys.argv[2]))
