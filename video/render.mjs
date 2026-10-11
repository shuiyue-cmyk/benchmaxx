// Renders scene.html frame by frame with headless Edge/Chrome and encodes it with ffmpeg.
//
//   node render.mjs                      full render -> out/benchmaxx_intro.mp4
//   node render.mjs --stills 3.5,25.8    write PNG stills for the given timestamps to out/stills/
//
// Requires: ffmpeg on PATH, Python 3 + numpy (for the soundtrack), Edge or Chrome installed.

import { spawn, spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import puppeteer from 'puppeteer-core';

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, '..');
const OUT = join(HERE, 'out');
const FPS = 30;

const BROWSERS = [
  process.env.BROWSER_PATH,
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  '/usr/bin/google-chrome', '/usr/bin/chromium',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
].filter(Boolean);

function sceneData() {
  const r = JSON.parse(readFileSync(join(ROOT, 'results', 'latest.json'), 'utf-8'));
  const best = new Map();
  for (const m of r.models) {
    if (m.gi == null) continue;
    const cur = best.get(m.vendor);
    if (!cur || m.gi > cur.gi || (m.gi === cur.gi && m.released > cur.released)) best.set(m.vendor, m);
  }
  const champions = [...best.values()]
    .sort((a, b) => b.gi - a.gi || a.canonical_name.localeCompare(b.canonical_name))
    .slice(0, 7)
    .map(m => ({ name: m.canonical_name, vendor: m.vendor, gi: m.gi, raw: m.gi_raw }));
  const excludedTotal = Object.values(r.census.excluded).reduce((a, b) => a + b, 0);
  return {
    catalogue: r.census.catalogue_size,
    excluded: r.census.excluded,
    afterExclusion: r.census.catalogue_size - excludedTotal,
    evaluated: r.census.evaluated_models,
    callable: r.census.evaluated_models,
    snapshot: r.meta.snapshot_date,
    velocity: r.statistics.velocity,
    champions,
  };
}

function srtTime(s) {
  const ms = Math.round(s * 1000);
  const p = (n, w = 2) => String(n).padStart(w, '0');
  return `${p(Math.floor(ms / 3600000))}:${p(Math.floor(ms / 60000) % 60)}:${p(Math.floor(ms / 1000) % 60)},${p(ms % 1000, 3)}`;
}

function writeSubtitles(subs) {
  const make = pick => subs.map((c, i) => `${i + 1}\n${srtTime(c[0])} --> ${srtTime(c[1])}\n${pick(c)}\n`).join('\n');
  writeFileSync(join(OUT, 'benchmaxx_intro.zh.srt'), make(c => c[2]), 'utf-8');
  writeFileSync(join(OUT, 'benchmaxx_intro.en.srt'), make(c => c[3]), 'utf-8');
  writeFileSync(join(OUT, 'benchmaxx_intro.bilingual.srt'), make(c => `${c[2]}\n${c[3]}`), 'utf-8');
}

function run(cmd, args) {
  const r = spawnSync(cmd, args, { stdio: 'inherit' });
  if (r.status !== 0) throw new Error(`${cmd} exited with ${r.status}`);
}

async function main() {
  mkdirSync(OUT, { recursive: true });
  const stillsArg = process.argv.indexOf('--stills');
  const stills = stillsArg > 0 ? process.argv[stillsArg + 1].split(',').map(Number) : null;

  const executablePath = BROWSERS.find(p => existsSync(p));
  if (!executablePath) throw new Error('No Edge/Chrome found; set BROWSER_PATH.');
  const browser = await puppeteer.launch({
    executablePath, headless: true,
    args: ['--hide-scrollbars', '--force-color-profile=srgb', '--allow-file-access-from-files'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  const data = sceneData();
  await page.evaluateOnNewDocument(d => { window.__RENDERING__ = true; window.DATA = d; }, data);
  await page.goto(pathToFileURL(join(HERE, 'scene.html')).href, { waitUntil: 'networkidle0' });
  await page.evaluate(() => window.ready);
  const { DURATION, SUBS } = await page.evaluate(() => window.TIMELINE);
  const canvas = await page.$('canvas');

  if (stills) {
    mkdirSync(join(OUT, 'stills'), { recursive: true });
    for (const t of stills) {
      await page.evaluate(t => window.renderAt(t), t);
      await canvas.screenshot({ path: join(OUT, 'stills', `t${t.toFixed(2)}.png`) });
    }
    await browser.close();
    console.log(`Wrote ${stills.length} stills to out/stills/`);
    return;
  }

  writeSubtitles(SUBS);

  // Soundtrack (no voice): procedurally generated, synced to scene cues.
  run('python', [join(HERE, 'soundtrack.py'), join(OUT, 'soundtrack.wav'), String(DURATION)]);

  const silent = join(OUT, 'video_only.mp4');
  const ff = spawn('ffmpeg', [
    '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'png', '-i', '-',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p',
    '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-movflags', '+faststart', silent,
  ], { stdio: ['pipe', 'inherit', 'inherit'] });
  const done = new Promise((res, rej) => ff.on('close', c => (c === 0 ? res() : rej(new Error(`ffmpeg ${c}`)))));

  const frames = Math.round(DURATION * FPS);
  const started = Date.now();
  for (let f = 0; f < frames; f++) {
    await page.evaluate(t => window.renderAt(t), f / FPS);
    const png = await canvas.screenshot({ type: 'png' });
    if (!ff.stdin.write(png)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 150 === 0) process.stdout.write(`frame ${f}/${frames}  (${((Date.now() - started) / 1000).toFixed(0)}s)\n`);
  }
  ff.stdin.end();
  await done;
  await browser.close();

  // Mux: picture + soundtrack + soft subtitle tracks (zh, en). Bilingual captions are also burned in.
  const final = join(OUT, 'benchmaxx_intro.mp4');
  run('ffmpeg', [
    '-y', '-loglevel', 'error', '-i', silent, '-i', join(OUT, 'soundtrack.wav'),
    '-i', join(OUT, 'benchmaxx_intro.zh.srt'), '-i', join(OUT, 'benchmaxx_intro.en.srt'),
    '-map', '0:v', '-map', '1:a', '-map', '2:s', '-map', '3:s',
    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-c:s', 'mov_text',
    '-metadata:s:s:0', 'language=chi', '-metadata:s:s:0', 'title=中文',
    '-metadata:s:s:1', 'language=eng', '-metadata:s:s:1', 'title=English',
    '-metadata', 'title=BenchMaxx: A Nomenclature-Centric Evaluation of Large Language Models',
    '-movflags', '+faststart', final,
  ]);
  console.log(`Done: ${final}`);
}

main().catch(e => { console.error(e); process.exit(1); });
