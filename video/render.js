// Renders an animated HTML page (with window.setT(t)) to JPEG frames.
// Usage: node render.js <page.html> <out-dir> <seconds> [fps] [t1,t2,... for previews only]
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const [page, outDir, seconds, fps = '30', only] = process.argv.slice(2);
  if (!page || !outDir || !seconds) {
    console.error('usage: node render.js <page.html> <out-dir> <seconds> [fps] [t1,t2,...]');
    process.exit(1);
  }
  fs.mkdirSync(outDir, { recursive: true });
  const times = only
    ? only.split(',').map(Number)
    : [...Array(Math.round(+seconds * +fps)).keys()].map(i => i / +fps);

  const browser = await chromium.launch();
  const p = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.resolve(page));
  await p.waitForTimeout(500);
  for (let i = 0; i < times.length; i++) {
    await p.evaluate(t => setT(t), times[i]);
    const name = (only ? 'prev' : 'f') + String(i).padStart(5, '0') + '.jpg';
    await p.screenshot({ path: path.join(outDir, name), type: 'jpeg', quality: 92 });
  }
  await browser.close();
})();
