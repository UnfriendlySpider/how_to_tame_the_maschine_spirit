// Turn a diagram spec in the Excalidraw MCP's simplified format (shapes with
// `label`, arrows with `label`, cameraUpdate pseudo-elements) into a real
// .excalidraw file and a PNG, rendered by @excalidraw/utils in Chromium.
// Usage: node export.mjs spec.json out-prefix [scale] [padding]
// The paper's diagrams use scale 3 and padding 10 (README.md in this folder).
import { createRequire } from 'node:module';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';

const { chromium } = createRequire(import.meta.url)('playwright');   // the preinstalled copy, found through NODE_PATH

const [specPath, outPrefix, scaleArg] = process.argv.slice(2);
const SCALE = Number(scaleArg || 4);
const PAD = Number(process.argv[5] ?? 12);
const LIB = path.join(path.dirname(new URL(import.meta.url).pathname), 'lib');
// Nothing is loaded from lib/ before its three files match lib.sha256.
for (const line of fs.readFileSync(path.join(path.dirname(LIB), 'lib.sha256'), 'utf8').split('\n')) {
  const [want, name] = line.trim().split(/\s+/);
  if (!name) continue;
  const file = path.join(LIB, name);
  const got = fs.existsSync(file) ? crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex') : null;
  if (got !== want) {
    console.error(`tools/diagrams/lib/${name} is ${got === null ? 'missing' : 'not the pinned file'}: run tools/diagrams/fetch-lib.sh`);
    process.exit(1);
  }
}
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));

let seed = 1;
const base = (e) => ({
  angle: 0, strokeColor: '#1e1e1e', backgroundColor: 'transparent', fillStyle: 'solid',
  strokeWidth: 2, strokeStyle: 'solid', roughness: 1, opacity: 100, groupIds: [],
  frameId: null, roundness: null, seed: seed, version: 1, versionNonce: seed++,
  isDeleted: false, boundElements: null, updated: 1, link: null, locked: false, ...e,
});

// An `image` element names a PNG file in `src`; it is embedded as a data URL.
// Without a width, the width follows the PNG's aspect ratio at the given height.
const files = {};
const pngSize = (buf) => ({ w: buf.readUInt32BE(16), h: buf.readUInt32BE(20) });
const elements = [];
for (const raw of spec) {
  if (raw.type === 'image') {
    const buf = fs.readFileSync(raw.src);
    const { w, h } = pngSize(buf);
    const fileId = `img-${raw.id}`;
    files[fileId] = { mimeType: 'image/png', id: fileId, dataURL: `data:image/png;base64,${buf.toString('base64')}`, created: 1 };
    const { src, ...rest } = raw;
    elements.push(base({ ...rest, width: rest.width ?? (rest.height * w) / h, fileId, status: 'saved',
      scale: [1, 1], strokeColor: 'transparent', backgroundColor: 'transparent' }));
    continue;
  }
  if (raw.type === 'cameraUpdate' || raw.type === 'delete' || raw.type === 'restoreCheckpoint') continue;
  const { label, bg, ...shape } = raw;
  if (bg && raw.type === 'text') {
    elements.push(base({ type: 'rectangle', id: `${raw.id}-bg`, x: raw.x, y: raw.y, width: 1, height: 1,
      strokeColor: 'transparent', backgroundColor: '#ffffff', roughness: 0, bgFor: raw.id, bgPad: bg }));
  }
  const el = base(shape);
  if (el.type === 'arrow' || el.type === 'line') {
    el.points = el.points || [[0, 0], [el.width, el.height]];
    el.lastCommittedPoint = null;
    el.startArrowhead = el.startArrowhead ?? null;
    el.endArrowhead = el.endArrowhead === undefined ? (el.type === 'arrow' ? 'arrow' : null) : el.endArrowhead;
    el.startBinding = null; el.endBinding = null;   // keep the drawn geometry as given
  }
  if (el.type === 'text') {
    Object.assign(el, { fontSize: el.fontSize || 20, fontFamily: el.fontFamily || 1, textAlign: el.textAlign || 'left',
      verticalAlign: 'top', containerId: null, originalText: el.text, lineHeight: 1.25, autoResize: true });
  }
  elements.push(el);
  if (label) {
    const t = base({
      type: 'text', id: `${el.id}-label`, x: el.x, y: el.y, width: 10, height: 10,
      text: label.text, originalText: label.text, fontSize: label.fontSize || 20,
      fontFamily: label.fontFamily || 1, textAlign: 'center', verticalAlign: 'middle',
      containerId: el.id, lineHeight: 1.25, strokeColor: label.strokeColor || el.strokeColor || '#1e1e1e',
      autoResize: true,
    });
    el.boundElements = [...(el.boundElements || []), { type: 'text', id: t.id }];
    elements.push(t);
  }
}

const font = (f) => fs.readFileSync(path.join(LIB, f)).toString('base64');
const html = `<!doctype html><html><head><style>
@font-face { font-family: Virgil; src: url(data:font/woff2;base64,${font('Virgil.woff2')}) format('woff2'); }
@font-face { font-family: Cascadia; src: url(data:font/woff2;base64,${font('Cascadia.woff2')}) format('woff2'); }
</style></head><body></body></html>`;

const browser = await chromium.launch();
const page = await browser.newPage();
await page.setContent(html);
await page.addScriptTag({ path: path.join(LIB, 'excalidraw-utils.min.js') });
const result = await page.evaluate(async ({ elements, files, SCALE, PAD }) => {
  const FAMILY = { 1: 'Virgil', 2: 'Helvetica', 3: 'Cascadia' };
  for (const f of ['Virgil', 'Cascadia']) await document.fonts.load(`20px ${f}`);
  const ctx = document.createElement('canvas').getContext('2d');
  const measure = (t) => {
    ctx.font = `${t.fontSize}px ${FAMILY[t.fontFamily] || 'Virgil'}`;
    const lines = t.text.split('\n');
    return { w: Math.max(...lines.map((l) => ctx.measureText(l).width)), h: lines.length * t.fontSize * t.lineHeight };
  };
  const byId = Object.fromEntries(elements.map((e) => [e.id, e]));
  for (const t of elements.filter((e) => e.type === 'text')) {
    const { w, h } = measure(t);
    t.width = w; t.height = h; t.baseline = Math.round(t.fontSize * 0.9);
    const c = t.containerId && byId[t.containerId];
    if (!c) continue;
    if (c.type === 'arrow' || c.type === 'line') {
      const [p0, p1] = [c.points[0], c.points[c.points.length - 1]];
      t.x = c.x + (p0[0] + p1[0]) / 2 - w / 2; t.y = c.y + (p0[1] + p1[1]) / 2 - h / 2;
    } else {
      t.x = c.x + (c.width - w) / 2; t.y = c.y + (c.height - h) / 2;
    }
  }
  for (const r of elements.filter((e) => e.bgFor)) {
    const t = byId[r.bgFor];
    Object.assign(r, { x: t.x - r.bgPad, y: t.y, width: t.width + 2 * r.bgPad, height: t.height });
    delete r.bgFor; delete r.bgPad;
  }
  const blob = await ExcalidrawUtils.exportToBlob({
    elements, files, mimeType: 'image/png', exportPadding: PAD,
    appState: { exportBackground: true, viewBackgroundColor: '#ffffff', exportWithDarkMode: false },
    getDimensions: (w, h) => ({ width: w * SCALE, height: h * SCALE, scale: SCALE }),
  });
  const buf = new Uint8Array(await blob.arrayBuffer());
  let bin = ''; for (const b of buf) bin += String.fromCharCode(b);
  return { png: btoa(bin), elements };
}, { elements, files, SCALE, PAD });
await browser.close();

fs.writeFileSync(`${outPrefix}.png`, Buffer.from(result.png, 'base64'));
fs.writeFileSync(`${outPrefix}.excalidraw`, JSON.stringify({
  type: 'excalidraw', version: 2, source: 'https://excalidraw.com',
  elements: result.elements, appState: { viewBackgroundColor: '#ffffff', gridSize: null }, files,
}, null, 1));
console.log(`wrote ${outPrefix}.png and ${outPrefix}.excalidraw (${result.elements.length} elements)`);
