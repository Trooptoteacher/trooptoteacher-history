// US History Hack — Lean Student Deck (US.01 sample)
// Assertion-Evidence layout: bold assertion headline + large evidence image.
// Brand-locked (History Hack navy/red/gold + America250). System fonts only.
// Narrative LOCKED at v3.2 — assertion headlines are summary-labels only.
const fs = require('fs');
const path = require('path');
const pptxgen = require('pptxgenjs');

const DATA_DIR = process.argv[2] || path.join(__dirname, 'us01-lean');
const OUT_FILE = process.argv[3] || path.join(process.cwd(), 'US_History_Hack_Unit1_Lean_Deck.pptx');
const IMG_DIR  = process.argv[4] || path.join(__dirname, 'hh-web', 'public');

const D = JSON.parse(fs.readFileSync(path.join(DATA_DIR, '_build.json'), 'utf8'));
const resolveImg = ref => path.join(IMG_DIR, D.imageRefs[ref]);

// ---------- BRAND SYSTEM (locked) ----------
const NAVY   = '1A2332';
const A250BLUE = '002858';
const RED    = 'C62828';
const GOLD   = 'C9A84C';
const GOLDBR = 'F9A825';
const CREAM  = 'F7F4EC';
const WHITE  = 'FFFFFF';
const INK    = '1F2430';
const MUTE   = '5C6470';
const SLATEL = 'C7D4E0';
const KEYGRN = '1B5E20';

const HEAD = 'Georgia';
const BODY = 'Calibri';
const LABEL = 'Trebuchet MS';

const pptx = new pptxgen();
pptx.defineLayout({ name: 'HH', width: 13.333, height: 7.5 });
pptx.layout = 'HH';
pptx.author = 'TroopToTeacher Technologies LLC';
pptx.company = 'U.S. History Hack';
pptx.subject = process.env.UNIT_SUBJECT || 'Unit 1 — Lean Student Deck (US.01–US.07)';

const W = 13.333, H = 7.5;
const FOOT = 'U.S. History Hack  ·  TroopToTeacher Technologies LLC  ·  Aligned to TN Academic Standards & TCAP EOC';

function footer(slide, page, dark) {
  const c = dark ? SLATEL : MUTE;
  slide.addText(FOOT, { x: 0.5, y: H - 0.42, w: 11.0, h: 0.3, fontFace: LABEL, fontSize: 8, color: c, align: 'left', valign: 'middle' });
  slide.addText(`${page}`, { x: W - 1.1, y: H - 0.42, w: 0.6, h: 0.3, fontFace: LABEL, fontSize: 9, color: c, align: 'right', valign: 'middle' });
}

function kindPill(slide, txt, x, y, fill) {
  slide.addText(txt.toUpperCase(), {
    x, y, w: 3.6, h: 0.4, fontFace: LABEL, fontSize: 11, bold: true, color: WHITE,
    fill: { color: fill || RED }, align: 'center', valign: 'middle', charSpacing: 1
  });
}

function stdBadge(slide, x, y, code) {
  slide.addText(code || 'US.01', {
    x, y, w: 1.1, h: 0.4, fontFace: LABEL, fontSize: 12, bold: true, color: NAVY,
    fill: { color: GOLD }, align: 'center', valign: 'middle'
  });
}

// Standard Divider — introduces a new standard: code + TN standard text + "I Can"
function standardDividerSlide(s, page) {
  const slide = pptx.addSlide();
  slide.background = { color: NAVY };
  slide.addShape(pptx.ShapeType.rect, { x: 0, y: 2.55, w: W, h: 0.08, fill: { color: GOLD } });
  slide.addText(s.standard, {
    x: 0.5, y: 0.6, w: 3.2, h: 1.3, fontFace: HEAD, fontSize: 60, bold: true, color: GOLD, valign: 'middle'
  });
  slide.addText(s.title, {
    x: 3.8, y: 0.6, w: 9.0, h: 1.3, fontFace: HEAD, fontSize: 26, bold: true, color: WHITE, valign: 'middle'
  });
  // TN standard text
  slide.addText('TN STANDARD', { x: 0.5, y: 2.9, w: 12.3, h: 0.3, fontFace: LABEL, fontSize: 12, bold: true, color: GOLD, charSpacing: 2 });
  slide.addText(s.tnStandard, { x: 0.5, y: 3.28, w: 12.3, h: 1.85, fontFace: BODY, fontSize: 16, color: SLATEL, valign: 'top', lineSpacingMultiple: 1.05 });
  // I Can bar
  slide.addShape(pptx.ShapeType.rect, { x: 0.5, y: 5.35, w: 12.3, h: 1.35, fill: { color: GOLD } });
  slide.addText('I CAN', { x: 0.7, y: 5.5, w: 12.0, h: 0.3, fontFace: LABEL, fontSize: 12, bold: true, color: NAVY, charSpacing: 2 });
  slide.addText(s.iCan, { x: 0.7, y: 5.8, w: 11.9, h: 0.82, fontFace: BODY, fontSize: 14, bold: true, color: NAVY, valign: 'top' });
  footer(slide, page, true);
  return slide;
}

// Zoom hint pill for primary-source images (matches web viewer zoom feature)
function zoomPill(slide, x, y) {
  slide.addText('ZOOM IN', {
    x, y, w: 1.3, h: 0.32, fontFace: LABEL, fontSize: 9, bold: true, color: NAVY,
    fill: { color: GOLDBR }, align: 'center', valign: 'middle', charSpacing: 1
  });
}

// Standard assertion-evidence slide: headline band + big image right/full
function assertionEvidenceSlide(s, page) {
  const slide = pptx.addSlide();
  slide.background = { color: CREAM };
  // top color band
  slide.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: W, h: 1.9, fill: { color: NAVY } });
  slide.addShape(pptx.ShapeType.rect, { x: 0, y: 1.9, w: W, h: 0.06, fill: { color: GOLD } });
  kindPill(slide, s.kind, 0.5, 0.35, s.kind === 'Hook' ? RED : A250BLUE);
  stdBadge(slide, 4.25, 0.35, s.standard);
  slide.addText(s.assertion, {
    x: 0.5, y: 0.85, w: 12.3, h: 0.95, fontFace: HEAD, fontSize: 23, bold: true,
    color: WHITE, align: 'left', valign: 'middle'
  });
  // evidence image (large, centered under band)
  const img = resolveImg(s.image);
  slide.addImage({ path: img, x: 3.0, y: 2.25, w: 7.33, h: 4.55, sizing: { type: 'contain', w: 7.33, h: 4.55 } });
  zoomPill(slide, 3.0, 2.3);
  slide.addText(s.footer, { x: 0.5, y: 6.85, w: 9, h: 0.3, fontFace: LABEL, fontSize: 10, italic: true, color: MUTE });
  footer(slide, page, false);
  return slide;
}

// Source-It-First primary source slide
function sourceItFirstSlide(s, page) {
  const slide = pptx.addSlide();
  slide.background = { color: CREAM };
  slide.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: W, h: 1.7, fill: { color: A250BLUE } });
  slide.addShape(pptx.ShapeType.rect, { x: 0, y: 1.7, w: W, h: 0.06, fill: { color: GOLD } });
  kindPill(slide, 'Source It First', 0.5, 0.3, RED);
  stdBadge(slide, 4.25, 0.3, s.standard);
  slide.addText(s.assertion, {
    x: 0.5, y: 0.78, w: 12.3, h: 0.85, fontFace: HEAD, fontSize: 20, bold: true, color: WHITE, valign: 'middle'
  });
  // WHO / WHEN / WHY band
  const sf = s.sourceItFirst;
  const cols = [['WHO', sf.who], ['WHEN', sf.when], ['WHY', sf.why]];
  cols.forEach((c, i) => {
    const x = 0.5 + i * 4.15;
    slide.addText(c[0], { x, y: 1.95, w: 3.9, h: 0.35, fontFace: LABEL, fontSize: 12, bold: true, color: WHITE, fill: { color: NAVY }, align: 'center', valign: 'middle' });
    slide.addText(c[1], { x, y: 2.3, w: 3.9, h: 1.0, fontFace: BODY, fontSize: 12, color: INK, fill: { color: WHITE }, align: 'left', valign: 'top', margin: 6, line: { color: 'DAD3C2', width: 1 } });
  });
  // two statute excerpts
  s.sources.forEach((src, i) => {
    const x = 0.5 + i * 6.25;
    slide.addShape(pptx.ShapeType.rect, { x, y: 3.5, w: 6.05, h: 2.9, fill: { color: WHITE }, line: { color: GOLD, width: 1.5 } });
    slide.addText(src.title, { x: x + 0.15, y: 3.6, w: 5.75, h: 0.35, fontFace: HEAD, fontSize: 14, bold: true, color: A250BLUE });
    slide.addText(`${src.author} · ${src.date}`, { x: x + 0.15, y: 3.95, w: 5.75, h: 0.3, fontFace: LABEL, fontSize: 9, italic: true, color: MUTE });
    slide.addText(`"${src.excerpt}"`, { x: x + 0.15, y: 4.3, w: 5.75, h: 1.75, fontFace: BODY, fontSize: 11, color: INK, valign: 'top' });
    slide.addText(src.archiveName, { x: x + 0.15, y: 6.05, w: 5.75, h: 0.28, fontFace: LABEL, fontSize: 9, color: A250BLUE, hyperlink: { url: src.url } });
  });
  footer(slide, page, false);
  return slide;
}

// Three Perspectives synthesis slide (verbatim shipped framing)
function threePerspectivesSlide(s, page) {
  const slide = pptx.addSlide();
  slide.background = { color: NAVY };
  kindPill(slide, 'Three Perspectives', 0.5, 0.3, RED);
  stdBadge(slide, 4.25, 0.3, s.standard);
  slide.addText(s.framingIntro, {
    x: 0.5, y: 0.85, w: 12.3, h: 0.9, fontFace: HEAD, fontSize: 17, italic: true, color: SLATEL, valign: 'middle'
  });
  const lensColors = [KEYGRN, RED, A250BLUE];
  s.perspectives.forEach((p, i) => {
    const x = 0.5 + i * 4.15;
    slide.addShape(pptx.ShapeType.rect, { x, y: 1.95, w: 3.9, h: 4.6, fill: { color: WHITE } });
    slide.addShape(pptx.ShapeType.rect, { x, y: 1.95, w: 3.9, h: 0.6, fill: { color: lensColors[i] } });
    slide.addText(p.lens, { x, y: 1.95, w: 3.9, h: 0.6, fontFace: HEAD, fontSize: 16, bold: true, color: WHITE, align: 'center', valign: 'middle' });
    slide.addText(p.prompt, { x: x + 0.15, y: 2.65, w: 3.6, h: 0.95, fontFace: BODY, fontSize: 11, italic: true, color: MUTE, valign: 'top' });
    slide.addText(`${s.standard}:`, { x: x + 0.15, y: 3.6, w: 3.6, h: 0.3, fontFace: LABEL, fontSize: 10, bold: true, color: '8A6D1A' });
    slide.addText(p.answer || p.us01, { x: x + 0.15, y: 3.9, w: 3.6, h: 2.5, fontFace: BODY, fontSize: 12, color: INK, valign: 'top' });
  });
  slide.addText(`Anchor: ${s.primarySourceAnchor}`, { x: 0.5, y: 6.7, w: 12, h: 0.3, fontFace: LABEL, fontSize: 10, italic: true, color: SLATEL });
  footer(slide, page, true);
  return slide;
}

// We Do guided practice slide
function weDoSlide(s, page) {
  const slide = pptx.addSlide();
  slide.background = { color: CREAM };
  slide.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: W, h: 1.6, fill: { color: NAVY } });
  slide.addShape(pptx.ShapeType.rect, { x: 0, y: 1.6, w: W, h: 0.06, fill: { color: GOLD } });
  kindPill(slide, 'We Do', 0.5, 0.3, GOLDBR);
  stdBadge(slide, 4.25, 0.3, s.standard);
  slide.addText(s.assertion, { x: 0.5, y: 0.75, w: 12.3, h: 0.8, fontFace: HEAD, fontSize: 20, bold: true, color: WHITE, valign: 'middle' });
  const wd = s.weDo;
  // left: image
  slide.addImage({ path: resolveImg(s.image), x: 0.5, y: 1.85, w: 4.3, h: 4.4, sizing: { type: 'contain', w: 4.3, h: 4.4 } });
  zoomPill(slide, 0.5, 1.9);
  // right: modeled chain
  const rx = 5.1;
  slide.addText('MODELED PROMPT', { x: rx, y: 1.85, w: 7.6, h: 0.3, fontFace: LABEL, fontSize: 10, bold: true, color: RED });
  slide.addText(wd.modeledPrompt, { x: rx, y: 2.15, w: 7.6, h: 0.5, fontFace: BODY, fontSize: 13, bold: true, color: INK });
  slide.addText('CAUSE → EFFECT → CONSEQUENCE', { x: rx, y: 2.75, w: 7.6, h: 0.3, fontFace: LABEL, fontSize: 10, bold: true, color: A250BLUE });
  slide.addText(wd.modeled, { x: rx, y: 3.05, w: 7.6, h: 1.5, fontFace: BODY, fontSize: 12, color: INK, fill: { color: WHITE }, valign: 'top', margin: 6, line: { color: 'DAD3C2', width: 1 } });
  slide.addText('TEACHER THINK-ALOUD', { x: rx, y: 4.65, w: 7.6, h: 0.3, fontFace: LABEL, fontSize: 10, bold: true, color: KEYGRN });
  slide.addText(wd.think, { x: rx, y: 4.95, w: 7.6, h: 1.0, fontFace: BODY, fontSize: 11, italic: true, color: MUTE, valign: 'top' });
  slide.addText(`Then you try:  ${wd.thenYou}`, { x: rx, y: 5.95, w: 7.6, h: 0.4, fontFace: BODY, fontSize: 11, bold: true, color: NAVY });
  footer(slide, page, false);
  return slide;
}

// Tennessee Connection — celebrated, bold
function tennesseeSlide(s, page) {
  const slide = pptx.addSlide();
  slide.background = { color: NAVY };
  // bold red banner
  slide.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: W, h: 1.7, fill: { color: RED } });
  slide.addShape(pptx.ShapeType.rect, { x: 0, y: 1.7, w: W, h: 0.08, fill: { color: GOLD } });
  slide.addText('TENNESSEE CONNECTION  ·  WILLIAMSON COUNTY', {
    x: 0.5, y: 0.25, w: 12.3, h: 0.4, fontFace: LABEL, fontSize: 13, bold: true, color: WHITE, charSpacing: 2
  });
  slide.addText(s.assertion, {
    x: 0.5, y: 0.7, w: 12.3, h: 0.95, fontFace: HEAD, fontSize: 22, bold: true, color: WHITE, valign: 'middle'
  });
  // left: 1878 Williamson County map (where Jordan lived)
  slide.addShape(pptx.ShapeType.rect, { x: 0.45, y: 1.95, w: 6.2, h: 4.5, fill: { color: WHITE }, line: { color: GOLD, width: 2 } });
  slide.addImage({ path: resolveImg(s.image), x: 0.6, y: 2.1, w: 5.9, h: 3.9, sizing: { type: 'contain', w: 5.9, h: 3.9 } });
  zoomPill(slide, 0.6, 2.15);
  slide.addText(s.mapNote, { x: 0.6, y: 6.02, w: 5.9, h: 0.4, fontFace: LABEL, fontSize: 9, italic: true, color: MUTE });
  // right: 9th cavalry image + facts
  slide.addImage({ path: resolveImg(s.secondaryImage), x: 6.9, y: 1.95, w: 6.0, h: 2.0, sizing: { type: 'contain', w: 6.0, h: 2.0 } });
  zoomPill(slide, 6.9, 2.0);
  slide.addText('9th U.S. Cavalry NCOs, 1889 (Buffalo Soldiers)', { x: 6.9, y: 3.95, w: 6.0, h: 0.3, fontFace: LABEL, fontSize: 9, italic: true, color: SLATEL });
  let fy = 4.35;
  s.tnFacts.forEach((f) => {
    slide.addText([
      { text: '★  ', options: { color: GOLDBR, bold: true } },
      { text: f.claim, options: { color: WHITE } }
    ], { x: 6.9, y: fy, w: 6.0, h: 0.72, fontFace: BODY, fontSize: 12, bold: true, valign: 'top' });
    fy += 0.72;
  });
  footer(slide, page, true);
  return slide;
}

// ---------- BUILD ----------
D.slides.forEach((s) => {
  const page = s.n;
  switch (s.kind) {
    case 'Standard Divider': standardDividerSlide(s, page); break;
    case 'Primary Source Analysis': sourceItFirstSlide(s, page); break;
    case 'Three Perspectives Synthesis': threePerspectivesSlide(s, page); break;
    case 'We Do': weDoSlide(s, page); break;
    case 'Tennessee Connection': tennesseeSlide(s, page); break;
    default: assertionEvidenceSlide(s, page); break;
  }
});

pptx.writeFile({ fileName: OUT_FILE }).then(() => {
  console.log('WROTE', OUT_FILE, '(' + D.slides.length + ' slides)');
});
