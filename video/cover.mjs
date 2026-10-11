// Renders cover.html to a 16:9 PNG and a 4:3 PNG cropped from the same frame.
//
//   node cover.mjs            -> out/cover_16x9.png (3840x2160), out/cover_4x3.png (2880x2160)
//   node cover.mjs --guides   -> also out/cover_guides.png with the 4:3 safe area outlined

import { existsSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import puppeteer from 'puppeteer-core';

const HERE = dirname(fileURLToPath(import.meta.url));
const OUT = join(HERE, 'out');
const BROWSERS = [
  process.env.BROWSER_PATH,
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  '/usr/bin/google-chrome', '/usr/bin/chromium',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
].filter(Boolean);

mkdirSync(OUT, { recursive: true });
const browser = await puppeteer.launch({
  executablePath: BROWSERS.find(p => existsSync(p)), headless: true,
  args: ['--hide-scrollbars', '--force-color-profile=srgb'],
});
const page = await browser.newPage();
await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 2 });
await page.goto(pathToFileURL(join(HERE, 'cover.html')).href, { waitUntil: 'networkidle0' });
await page.evaluate(() => document.fonts.ready);

await page.screenshot({ path: join(OUT, 'cover_16x9.png'), clip: { x: 0, y: 0, width: 1920, height: 1080 } });
// 4:3 = the centred 1440x1080 safe area of the same frame
await page.screenshot({ path: join(OUT, 'cover_4x3.png'), clip: { x: 240, y: 0, width: 1440, height: 1080 } });
if (process.argv.includes('--guides')) {
  await page.evaluate(() => document.body.classList.add('guides'));
  await page.screenshot({ path: join(OUT, 'cover_guides.png'), clip: { x: 0, y: 0, width: 1920, height: 1080 } });
}
await browser.close();
console.log('Wrote out/cover_16x9.png and out/cover_4x3.png');
