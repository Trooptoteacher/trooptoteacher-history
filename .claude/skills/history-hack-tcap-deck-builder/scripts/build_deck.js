// US History Hack — Unit 1 Flagship TCAP Lecture Deck (v2)
// Brand: History Hack navy/red/gold blended with America250 patriotic feel
// v2: primary-source imagery, click-reveal EOC checks (two-slide), layered answer keys
//     (speaker notes + teacher-key slides), per-standard student activities.
const fs = require('fs');
const path = require('path');
const pptxgen = require('pptxgenjs');

// ---------- PATH CONFIG (parameterized for Units 1–11) ----------
// Override per unit via env vars or CLI args. Defaults to the bundled Unit 1 example.
//   UNIT_DATA_DIR : directory holding _build.json, _images.json, _activities.json
//   DECK_OUT      : output .pptx file path
//   UNIT_SUBJECT  : document subject/metadata line
// CLI:  node build_deck.js <UNIT_DATA_DIR> <DECK_OUT>
const DATA_DIR = process.argv[2]
  || process.env.UNIT_DATA_DIR
  || path.join(__dirname, '..', 'assets', 'unit1-example');
const OUT_FILE = process.argv[3]
  || process.env.DECK_OUT
  || path.join(process.cwd(), 'US_History_Hack_Unit1_TCAP_Lecture_Deck.pptx');
const SUBJECT = process.env.UNIT_SUBJECT
  || 'Unit 1 — The Rise of Industrialization, 1877–1900 (US.01–US.07)';

const D = JSON.parse(fs.readFileSync(path.join(DATA_DIR,'_build.json'),'utf8'));
const IMGS = JSON.parse(fs.readFileSync(path.join(DATA_DIR,'_images.json'),'utf8'));
const ACTS = JSON.parse(fs.readFileSync(path.join(DATA_DIR,'_activities.json'),'utf8'));

// Resolve each image `file` path: absolute paths are used as-is; relative paths
// (e.g. "img/foo.jpg" in the bundled example) resolve against the data dir so the
// generator is portable across units regardless of where it is invoked from.
IMGS.forEach(im => {
  if (im.file && !path.isAbsolute(im.file)) im.file = path.join(DATA_DIR, im.file);
  // Auto-placeholder: if the resolved image file isn't present yet (a verified public-domain
  // source awaiting drop-in), reserve its exact footprint with a labeled placeholder box
  // rather than crash the build. Drop the file at im.file and rebuild to render the photo.
  if (im.file && !fs.existsSync(im.file)) im._placeholder = true;
});

// index images by standard
const IMG_BY_STD = {};
IMGS.forEach(im => (im.standardIds||[]).forEach(sid => {
  (IMG_BY_STD[sid] = IMG_BY_STD[sid] || []).push(im);
}));
const imgById = id => IMGS.find(i => i.id === id);

// ---------- BRAND SYSTEM ----------
// America 250 palette (LOCKED — migrated Aug 2026; matches STUDENT_WORKBOOK_PLATINUM_STANDARD.md §3)
const NAVY   = '1F3A5F';   // Heritage Blue (was 1A2332)
const NAVY2  = '2C3E63';
const A250BLUE = '002858';
const RED    = 'B22234';   // Patriot Red (was C62828)
const A250RED = 'C8102E';
const GOLD   = 'C9A227';   // Muted Gold (was C9A84C)
const GOLDBR = 'F9A825';   // Phoenix Gold accent (broader America 250 token)
const CREAM  = 'F8F5EF';   // Founders Cream (was F7F4EC)
const WHITE  = 'FFFFFF';
const INK    = '1F2430';
const MUTE   = '5C6470';
const SLATE  = 'A7BACB';
const SLATEL = 'C7D4E0';
const LINEC  = 'DAD3C2';
const KEYGRN = '1B5E20';   // teacher-key accent (deep green)
const KEYGRNL= 'E3F0E4';   // light green panel

const HEAD = 'Georgia';
const BODY = 'Calibri';
const LABEL= 'Trebuchet MS';

const pptx = new pptxgen();
pptx.defineLayout({ name:'HH', width:13.333, height:7.5 });
pptx.layout = 'HH';
pptx.author = 'TroopToTeacher Technologies LLC';
pptx.company = 'U.S. History Hack';
pptx.subject = SUBJECT;

const W = 13.333, H = 7.5;
const FOOT = 'U.S. History Hack  ·  TroopToTeacher Technologies LLC  ·  Aligned to TN Academic Standards & TCAP EOC';

// ---------- helpers ----------
function footer(slide, page, dark) {
  const c = dark ? SLATEL : MUTE;
  slide.addText(FOOT, { x:0.5, y:H-0.42, w:11.0, h:0.3, fontFace:LABEL, fontSize:8, color:c, align:'left', valign:'middle' });
  slide.addText(`${page}`, { x:W-1.1, y:H-0.42, w:0.6, h:0.3, fontFace:LABEL, fontSize:9, color:c, align:'right', valign:'middle' });
}
function kicker(slide, txt, x, y, color) {
  slide.addText(txt.toUpperCase(), { x, y, w:8, h:0.3, fontFace:LABEL, fontSize:12, color:color||RED, charSpacing:2, bold:true, align:'left' });
}
function sourceLine(slide, name, url, y, w) {
  slide.addText([{text:'Source: ', options:{color:MUTE}},{text:name, options:{color:A250BLUE, hyperlink:{url}, italic:true}}],
    { x:0.6, y:y, w:w||8.5, h:0.3, fontFace:BODY, fontSize:9, align:'left', valign:'middle' });
}
// Place an image inside a fixed box with a source caption beneath it.
// box: {x,y,w,h}. Caption sits in capH below. Returns nothing.
function imageWithCaption(slide, im, box, opts) {
  opts = opts || {};
  const frame = opts.frame !== false;
  const capH = opts.capH != null ? opts.capH : 0.62;
  const imgH = box.h - capH;
  if (frame) {
    slide.addShape(pptx.ShapeType.rect, { x:box.x-0.04, y:box.y-0.04, w:box.w+0.08, h:imgH+0.08, fill:{color:WHITE}, line:{color:LINEC, width:1} });
  }
  slide.addImage({ path: im.file, x:box.x, y:box.y, w:box.w, h:imgH, sizing:{ type:'contain', w:box.w, h:imgH } });
  // caption: short label + linked source
  const capColor = opts.onDark ? SLATEL : MUTE;
  const cap = opts.caption || (im.creator + (im.year ? ', ' + im.year : ''));
  slide.addText([
    { text: (opts.label ? opts.label + '  ' : ''), options:{ bold:true, color: opts.onDark ? GOLDBR : RED } },
    { text: cap + '  ', options:{ italic:true, color:capColor } },
    { text: im.hostingInstitution.split(',')[0], options:{ color: opts.onDark ? SLATEL : A250BLUE, hyperlink:{ url: im.catalogUrl }, italic:true } }
  ], { x:box.x, y:box.y + imgH + 0.06, w:box.w, h:capH-0.06, fontFace:BODY, fontSize: opts.capFs || 8.5, align:'left', valign:'top', lineSpacingMultiple:1.0 });
}

const PRACTICE = {
  'close-reading':'Close Reading','sourcing':'Sourcing','argumentation':'Argumentation',
  'contextualization':'Contextualization','corroboration':'Corroboration'
};

// TN Social Studies Practices (TDOE, Grades 9-12). Short on-slide labels map to the
// canonical full text in data/frameworks/tn-ssp-grades-9-12.md. SSP.01-04 are the
// inquiry cycle; SSP.05-06 are the historical/geographic awareness hooks.
const SSP_LABEL = {
  'SSP.01':'Collect sources',
  'SSP.02':'Examine a source',
  'SSP.03':'Synthesize sources',
  'SSP.04':'Build an argument',
  'SSP.05':'Historical awareness',
  'SSP.06':'Geographic awareness',
};

// Page counter aligned to the true slide index. The cover is slide 1 and intentionally
// carries no footer number, so we start at 1: the first ++page (on the agenda, slide 2)
// yields 2, keeping every printed page number equal to its slide position (Visual #4).
let page = 1;

// ===================================================================
// 1. COVER
// ===================================================================
(function cover(){
  const s = pptx.addSlide();
  s.background = { color: NAVY };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:GOLD} });
  s.addShape(pptx.ShapeType.rect, { x:W-0.16, y:0, w:0.16, h:H, fill:{color:RED} });
  s.addText('U.S. HISTORY HACK', { x:0.9, y:1.5, w:11, h:0.5, fontFace:LABEL, fontSize:18, color:GOLDBR, charSpacing:5, bold:true });
  s.addText('Unit 1', { x:0.9, y:2.0, w:11, h:0.9, fontFace:HEAD, fontSize:60, color:WHITE, bold:true });
  s.addText('The Rise of Industrialization', { x:0.9, y:3.05, w:11.2, h:0.7, fontFace:HEAD, fontSize:34, color:WHITE, bold:true });
  s.addText('Westward Expansion · The Gilded Age · Immigration   ·   1877–1900', { x:0.9, y:3.78, w:11.4, h:0.5, fontFace:HEAD, fontSize:19, color:SLATEL, italic:true });
  s.addText('Standards US.01 – US.07', { x:0.9, y:4.3, w:11, h:0.45, fontFace:BODY, fontSize:18, color:SLATE });
  const stds = Object.keys(D);
  let cx = 0.9;
  stds.forEach(code=>{
    const wch = 1.15;
    s.addShape(pptx.ShapeType.roundRect, { x:cx, y:4.9, w:wch, h:0.5, rectRadius:0.08, fill:{color:NAVY2}, line:{color:GOLD, width:1} });
    s.addText(code, { x:cx, y:4.9, w:wch, h:0.5, fontFace:LABEL, fontSize:13, color:GOLDBR, bold:true, align:'center', valign:'middle' });
    cx += wch + 0.18;
  });
  s.addText('TCAP EOC LECTURE DECK  ·  Tennessee Academic Standards for U.S. History', { x:0.9, y:6.4, w:11.5, h:0.4, fontFace:LABEL, fontSize:12, color:SLATE, charSpacing:1 });
  s.addText('TroopToTeacher Technologies LLC', { x:0.9, y:6.85, w:11.5, h:0.3, fontFace:BODY, fontSize:11, color:SLATE });
  s.addNotes('Unit 1 TCAP EOC lecture deck. Each standard runs as a full lesson: divider (standard + I Can), hook, direct instruction with a verified primary-source image, key figures, vocabulary, a student activity (paired to a printable worksheet), a TCAP-style check (question slide, then click to the reveal/answer-key slide), and a wrap-up with a teacher answer key in the speaker notes. All images are public-domain, captioned, and linked to the Library of Congress / National Archives.');
})();

// ===================================================================
// 2. UNIT AGENDA
// ===================================================================
(function agenda(){
  const s = pptx.addSlide();
  s.background = { color: CREAM };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:NAVY} });
  kicker(s, 'Unit Roadmap', 0.6, 0.5);
  s.addText('Where We Are Headed', { x:0.6, y:0.85, w:12, h:0.6, fontFace:HEAD, fontSize:34, color:NAVY, bold:true });
  s.addText('Unit 1 · The Rise of Industrialization (1877–1900)  —  Westward Expansion, the Gilded Age & Immigration', { x:0.6, y:1.48, w:12.1, h:0.35, fontFace:BODY, fontSize:13, italic:true, color:MUTE });
  const items = Object.entries(D).map(([code,v])=>({code, title:v.title}));
  const colX = [0.6, 6.9];
  const colItems = [items.slice(0,4), items.slice(4)];
  const cardH = 1.05, cardStep = 1.22, cardW = 5.85, codeW = 1.3;
  colItems.forEach((col, ci)=>{
    let y = 2.0;
    col.forEach((it, ri)=>{
      const x = colX[ci];
      s.addShape(pptx.ShapeType.rect, { x, y, w:cardW, h:cardH, fill:{color:WHITE}, line:{color:LINEC, width:1} });
      s.addShape(pptx.ShapeType.rect, { x, y, w:codeW, h:cardH, fill:{color:NAVY} });
      s.addText(it.code, { x, y, w:codeW, h:cardH, fontFace:HEAD, fontSize:19, color:GOLDBR, bold:true, align:'center', valign:'middle' });
      s.addText(it.title, { x:x+1.5, y:y, w:4.2, h:cardH, fontFace:BODY, fontSize:13.5, color:INK, valign:'middle', bold:true });
      // Visual #3 — sequential connection cue: a small down-chevron in the navy code
      // strip between each card and the next shows the standards build in order.
      if(ri < col.length-1){
        s.addShape(pptx.ShapeType.triangle, { x:x+codeW/2-0.11, y:y+cardH+0.015, w:0.22, h:0.17, rotate:180, fill:{color:GOLD}, line:{type:'none'} });
      }
      y += cardStep;
    });
  });
  // bridge cue: col 1 flows into col 2 (US.04 → US.05). A gold chevron in the gap.
  s.addShape(pptx.ShapeType.roundRect, { x:6.05, y:2.32, w:0.72, h:0.42, rectRadius:0.06, fill:{color:NAVY} });
  s.addText('then', { x:6.05, y:2.32, w:0.72, h:0.42, fontFace:LABEL, fontSize:9, color:GOLDBR, bold:true, align:'center', valign:'middle' });
  s.addShape(pptx.ShapeType.triangle, { x:6.78, y:2.46, w:0.18, h:0.16, rotate:90, fill:{color:GOLD}, line:{type:'none'} });
  s.addShape(pptx.ShapeType.roundRect, { x:6.9, y:5.66, w:5.85, h:1.05, rectRadius:0.06, fill:{color:'FBEFD0'}, line:{color:GOLD,width:1} });
  s.addText('Standards build in sequence (US.01 → US.07). Each runs as a full lesson: TN standard · “I Can” · direct instruction · verified primary source · vocabulary · guided + independent practice · TCAP-style check with reveal key.',
    { x:7.1, y:5.7, w:5.5, h:0.97, fontFace:BODY, fontSize:11, italic:true, color:'5A4A1E', valign:'middle', lineSpacingMultiple:1.08 });
  footer(s, ++page, false);
})();

// ===================================================================
// 3. UNIT HOOK
// ===================================================================
(function hook(){
  const s = pptx.addSlide();
  s.background = { color: A250BLUE };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:GOLD} });
  kicker(s, 'Bell Ringer · Hook', 0.7, 0.7, GOLDBR);
  s.addText('In 1865, most Americans lived on farms.\nBy 1920, most lived in cities.', { x:0.7, y:1.4, w:11.8, h:1.8, fontFace:HEAD, fontSize:36, color:WHITE, bold:true, lineSpacingMultiple:1.05 });
  s.addText('What forces could move an entire nation off the land and into the factory in just 55 years?',
    { x:0.7, y:3.5, w:11.8, h:1.0, fontFace:HEAD, fontSize:24, color:GOLDBR, italic:true });
  s.addShape(pptx.ShapeType.roundRect, { x:0.7, y:4.85, w:11.9, h:1.55, rectRadius:0.1, fill:{color:NAVY2}, line:{color:GOLD,width:1} });
  s.addText('TURN & TALK', { x:1.0, y:5.05, w:3, h:0.35, fontFace:LABEL, fontSize:13, color:GOLDBR, bold:true, charSpacing:2 });
  s.addText([
    {text:'With a partner, list ', options:{}},
    {text:'three things', options:{bold:true, color:GOLDBR}},
    {text:' that might pull people toward cities — and ', options:{}},
    {text:'three things', options:{bold:true, color:GOLDBR}},
    {text:' that might push them off the farm. Keep your list; we will return to it at the end of the unit.', options:{}}
  ], { x:1.0, y:5.4, w:11.3, h:0.9, fontFace:BODY, fontSize:16, color:WHITE, valign:'top', lineSpacingMultiple:1.05 });
  s.addNotes('Bell ringer (5 min). Push factors: drought/crop failure, falling crop prices, farm debt/mechanization, lack of land. Pull factors: factory jobs, higher wages, electricity, entertainment, immigrant communities. Collect lists; revisit on the closing slide.');
  footer(s, ++page, true);
})();

// ===================================================================
// PER-STANDARD LESSON BUILDER
// ===================================================================
function standardDivider(code, v){
  const s = pptx.addSlide();
  s.background = { color: NAVY };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:0.35, h:H, fill:{color:RED} });
  s.addShape(pptx.ShapeType.rect, { x:0.35, y:0, w:0.12, h:H, fill:{color:GOLD} });
  s.addText('STANDARD', { x:1.0, y:1.1, w:6, h:0.4, fontFace:LABEL, fontSize:15, color:GOLDBR, charSpacing:4, bold:true });
  s.addText(code, { x:0.95, y:1.45, w:6, h:1.5, fontFace:HEAD, fontSize:88, color:WHITE, bold:true });
  // When SSP pills occupy the upper-right, constrain the subtitle to the LEFT zone
  // (stop before the pill column at x≈7.45) so it can never run under the pills.
  // fit:'shrink' is unreliable in LibreOffice, so size the font by length and give
  // the box two lines of height to wrap cleanly instead of clipping.
  const ssps = v.ssps || [];
  const titleW = ssps.length ? 6.1 : 11.3;
  const titleFs = v.title.length>46 ? (ssps.length?22:26) : (ssps.length && v.title.length>30 ? 24 : 30);
  s.addText(v.title, { x:1.0, y:2.92, w:titleW, h:1.35, fontFace:HEAD, fontSize:titleFs, color:GOLDBR, italic:true, valign:'top', lineSpacingMultiple:1.02 });
  // Social Studies Practices this standard exercises (TDOE SSP). Pill row in the
  // upper-right whitespace beside the big standard numeral.
  if(ssps.length){
    s.addText('SOCIAL STUDIES PRACTICES', { x:7.45, y:1.18, w:4.9, h:0.3, fontFace:LABEL, fontSize:11, color:SLATE, bold:true, charSpacing:2, align:'left' });
    let py = 1.55;
    ssps.forEach(code2=>{
      s.addShape(pptx.ShapeType.roundRect, { x:7.45, y:py, w:1.18, h:0.32, rectRadius:0.06, fill:{color:GOLD} });
      s.addText(code2, { x:7.45, y:py, w:1.18, h:0.32, fontFace:LABEL, fontSize:11, color:NAVY, bold:true, align:'center', valign:'middle' });
      s.addText(SSP_LABEL[code2]||'', { x:8.72, y:py, w:3.6, h:0.32, fontFace:BODY, fontSize:11.5, color:WHITE, valign:'middle' });
      py += 0.37;
    });
  }
  s.addShape(pptx.ShapeType.roundRect, { x:1.0, y:4.15, w:11.3, h:1.32, rectRadius:0.08, fill:{color:NAVY2}, line:{color:SLATE,width:0.75} });
  s.addText('TN ACADEMIC STANDARD', { x:1.25, y:4.28, w:6, h:0.3, fontFace:LABEL, fontSize:11, color:SLATE, bold:true, charSpacing:2 });
  const tnTxt = v.tnStandard.replace(/^US\.\d+\s*[–-]\s*/,'');
  s.addText(tnTxt, { x:1.25, y:4.60, w:10.8, h:0.82, fontFace:BODY, fontSize: tnTxt.length>230?11.5:13, color:WHITE, valign:'top', lineSpacingMultiple:1.0 });
  // I CAN box auto-sizes font to the statement length so nothing clips at the slide edge.
  const iCanFs = v.iCan.length>220 ? 11.5 : (v.iCan.length>160 ? 12.5 : 13.5);
  s.addShape(pptx.ShapeType.roundRect, { x:1.0, y:5.60, w:11.3, h:1.30, rectRadius:0.08, fill:{color:GOLD} });
  s.addText('I CAN', { x:1.25, y:5.72, w:2, h:0.32, fontFace:LABEL, fontSize:13, color:NAVY, bold:true, charSpacing:2 });
  s.addText(v.iCan, { x:1.25, y:6.02, w:10.8, h:0.82, fontFace:BODY, fontSize:iCanFs, color:NAVY, bold:true, valign:'top', lineSpacingMultiple:1.0 });
  footer(s, ++page, true);
}

// Daily/spaced retrieval slide (Rosenshine P1 & P10). Opens each standard by
// pulling forward 2-3 prompts from PRIOR standards before new material begins.
function reviewSlide(code, review){
  const s = pptx.addSlide();
  s.background = { color: CREAM };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:GOLD} });
  kicker(s, `${code} · Quick Review`, 0.6, 0.45, RED);
  s.addText('Do You Remember?', { x:0.6, y:0.8, w:12, h:0.7, fontFace:HEAD, fontSize:30, color:NAVY, bold:true });
  s.addText([
    {text:'Retrieve from memory first — no notes.  ', options:{italic:true, color:MUTE}},
    {text:'✍ Write each answer in full sentences on your Flight Log · “Do You Remember” page.', options:{bold:true, color:NAVY}}
  ], { x:0.6, y:1.52, w:12.1, h:0.5, fontFace:BODY, fontSize:13, valign:'top', lineSpacingMultiple:1.02 });
  const prompts = review.prompts;
  const top = 2.25, gap = 0.18;
  const cardH = Math.min(1.35, (4.0 - (prompts.length-1)*gap)/prompts.length);
  prompts.forEach((p,i)=>{
    const y = top + i*(cardH+gap);
    s.addShape(pptx.ShapeType.rect, { x:0.6, y:y, w:12.1, h:cardH, fill:{color:WHITE}, line:{color:LINEC,width:1} });
    s.addShape(pptx.ShapeType.rect, { x:0.6, y:y, w:0.85, h:cardH, fill:{color:NAVY} });
    s.addText(String(i+1), { x:0.6, y:y, w:0.85, h:cardH, fontFace:HEAD, fontSize:20, color:GOLDBR, bold:true, align:'center', valign:'middle' });
    s.addText([{text:(p.from? p.from+'  ' : ''), options:{bold:true, color:RED}},{text:p.q, options:{color:INK}}],
      { x:1.65, y:y, w:10.9, h:cardH, fontFace:BODY, fontSize:13.5, valign:'middle', lineSpacingMultiple:1.04 });
  });
  s.addNotes('SPACED RETRIEVAL ('+code+'). Cold-call or whiteboards, 3-4 min, low stakes. Answers — '+
    prompts.map((p,i)=>(i+1)+') '+p.a).join('  '));
  footer(s, ++page, false);
}

// Do You Remember — ANSWER REVEAL. Advance to this after students have committed and
// logged their answers on the Flight Log, so the teacher can give the answers on the
// next slide (Sean). Answers live in REVIEW[code].prompts[].a.
function reviewRevealSlide(code, review){
  const s = pptx.addSlide();
  s.background = { color: CREAM };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:GOLD} });
  kicker(s, `${code} · Quick Review — Answers`, 0.6, 0.45, KEYGRN);
  s.addText('Do You Remember? — Answers', { x:0.6, y:0.8, w:12, h:0.7, fontFace:HEAD, fontSize:30, color:NAVY, bold:true });
  s.addText('Check your Flight Log. Fix anything you missed in a different color — that correction is the point.',
    { x:0.6, y:1.55, w:12.1, h:0.4, fontFace:BODY, fontSize:13, italic:true, color:MUTE });
  const prompts = review.prompts;
  const top = 2.25, gap = 0.18;
  const cardH = Math.min(1.7, (4.0 - (prompts.length-1)*gap)/prompts.length);
  prompts.forEach((p,i)=>{
    const y = top + i*(cardH+gap);
    s.addShape(pptx.ShapeType.rect, { x:0.6, y:y, w:12.1, h:cardH, fill:{color:WHITE}, line:{color:LINEC,width:1} });
    s.addShape(pptx.ShapeType.rect, { x:0.6, y:y, w:0.85, h:cardH, fill:{color:KEYGRN} });
    s.addText('✓', { x:0.6, y:y, w:0.85, h:cardH, fontFace:HEAD, fontSize:20, color:WHITE, bold:true, align:'center', valign:'middle' });
    s.addText([
      {text:(p.from? p.from+'  ' : ''), options:{bold:true, color:RED}},
      {text:p.q+'\n', options:{color:MUTE}},
      {text:'Answer:  ', options:{bold:true, color:KEYGRN}},
      {text:p.a, options:{color:INK, bold:true}}
    ], { x:1.65, y:y+0.06, w:10.9, h:cardH-0.12, fontFace:BODY, fontSize:12.5, valign:'middle', lineSpacingMultiple:1.05 });
  });
  s.addNotes('DO YOU REMEMBER — ANSWER KEY ('+code+'). Reveal after students commit + log on the Flight Log. '+
    prompts.map((p,i)=>(i+1)+') '+p.a).join('  '));
  footer(s, ++page, false);
}

// TCAP #1 — DOK 1 "Confidence Check" warm-up. A single low-floor recall item run
// after the Quick Review and before direct instruction, so the standard's check
// sequence ramps DOK 1 -> DOK 2/3. Builds momentum / secures a high success rate
// for striving + EL students (Rosenshine P3 Ask Questions, P7 High Success Rate).
function confidenceCheckSlide(code, w){
  // LOCKED — Sean: the answer must NEVER share a slide with its question. Two-slide pair:
  // (A) question only (students commit), then advance to (B) the reveal.
  // ---- Slide A: QUESTION ONLY ----
  const s = pptx.addSlide();
  s.background = { color: CREAM };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:GOLD} });
  kicker(s, `${code} · Confidence Check`, 0.6, 0.45, RED);
  s.addText('Warm-Up — Quick Recall', { x:0.6, y:0.8, w:8.6, h:0.7, fontFace:HEAD, fontSize:30, color:NAVY, bold:true });
  s.addShape(pptx.ShapeType.roundRect, { x:9.5, y:0.86, w:1.25, h:0.5, rectRadius:0.1, fill:{color:'FBEFD0'}, line:{color:GOLD,width:1.25} });
  s.addText('DOK 1', { x:9.5, y:0.86, w:1.25, h:0.5, fontFace:LABEL, fontSize:12, color:RED, bold:true, align:'center', valign:'middle' });
  s.addShape(pptx.ShapeType.roundRect, { x:10.9, y:0.86, w:1.8, h:0.5, rectRadius:0.1, fill:{color:NAVY} });
  s.addText('LOW STAKES', { x:10.9, y:0.86, w:1.8, h:0.5, fontFace:LABEL, fontSize:11, color:GOLDBR, bold:true, align:'center', valign:'middle' });
  s.addText([
    {text:'Write it on your whiteboard or desk.  ', options:{bold:true, color:NAVY}},
    {text:'You may confer with your group for 30 seconds — then COMMIT your answer before the reveal.', options:{italic:true, color:MUTE}}
  ], { x:0.6, y:1.5, w:12.1, h:0.45, fontFace:BODY, fontSize:13.5, valign:'top', lineSpacingMultiple:1.02 });
  s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:2.35, w:12.1, h:2.9, rectRadius:0.1, fill:{color:NAVY} });
  s.addText(w.q, { x:1.1, y:2.65, w:11.1, h:2.3, fontFace:HEAD, fontSize:26, color:WHITE, bold:true, valign:'middle', align:'center', lineSpacingMultiple:1.1 });
  s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:5.55, w:12.1, h:0.6, rectRadius:0.08, fill:{color:WHITE}, line:{color:GOLD,width:1} });
  s.addText([
    {text:'COMMIT FIRST:  ', options:{bold:true, color:RED, fontFace:LABEL, charSpacing:1}},
    {text:'everyone answers now — then advance to reveal. This is the DOK 1 floor; the graded check later rises to DOK 2–3.', options:{color:MUTE}}
  ], { x:0.9, y:5.55, w:11.5, h:0.6, fontFace:BODY, fontSize:11.5, italic:true, valign:'middle' });
  s.addNotes('CONFIDENCE CHECK — QUESTION ('+code+', DOK 1). 60-90 sec. EVERY student commits (thumbs / whiteboard / choral) BEFORE you advance to the reveal slide. Do not show the answer yet. (Answer is on the next slide.)');
  footer(s, ++page, false);
  // ---- Slide B: REVEAL ----
  const r = pptx.addSlide();
  r.background = { color: CREAM };
  r.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:GOLD} });
  kicker(r, `${code} · Confidence Check — Reveal`, 0.6, 0.45, KEYGRN);
  r.addText('Warm-Up — Answer', { x:0.6, y:0.8, w:9.5, h:0.7, fontFace:HEAD, fontSize:30, color:NAVY, bold:true });
  // restate the question (smaller) so the reveal stands alone
  r.addShape(pptx.ShapeType.roundRect, { x:0.6, y:1.7, w:12.1, h:1.5, rectRadius:0.1, fill:{color:NAVY} });
  r.addText(w.q, { x:1.0, y:1.85, w:11.3, h:1.2, fontFace:HEAD, fontSize:17, color:WHITE, bold:true, valign:'middle', align:'center', lineSpacingMultiple:1.05 });
  r.addShape(pptx.ShapeType.roundRect, { x:0.6, y:3.5, w:12.1, h:2.6, rectRadius:0.1, fill:{color:'FBEFD0'}, line:{color:GOLD,width:1.5} });
  r.addText('✓ ANSWER', { x:1.0, y:3.72, w:3, h:0.4, fontFace:LABEL, fontSize:13, color:KEYGRN, bold:true, charSpacing:2 });
  r.addText(w.a, { x:1.0, y:4.2, w:11.3, h:1.75, fontFace:BODY, fontSize:18, color:INK, valign:'top', lineSpacingMultiple:1.12 });
  if(w.term) r.addText([{text:'Key term:  ', options:{bold:true, color:RED, fontFace:LABEL}}, {text:w.term, options:{color:NAVY, bold:true}}],
    { x:0.6, y:6.25, w:12.1, h:0.4, fontFace:BODY, fontSize:12.5, valign:'middle' });
  r.addNotes('CONFIDENCE CHECK — REVEAL ('+code+', DOK 1). Reveal only after every student has committed. Answer: '+w.a+' Key term to listen for: '+(w.term||'—')+'. Celebrate the early win, then move into new content.');
  footer(r, ++page, false);
}

function hookSlide(code, v, hookText, prompt){
  const s = pptx.addSlide();
  s.background = { color: CREAM };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:RED} });
  kicker(s, `${code} · Hook`, 0.6, 0.5);
  s.addText('Think About It', { x:0.6, y:0.85, w:12, h:0.7, fontFace:HEAD, fontSize:30, color:NAVY, bold:true });
  // Optional data chart beside the hook (Sean: "move the blue tab left, put the chart
  // next to it"). Native PptxGenJS chart — stays editable in PowerPoint, no image needed.
  const chart = (typeof HOOK_CHART !== 'undefined') ? HOOK_CHART[code] : null;
  const hookBoxW = chart ? 7.0 : 12.1;
  s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:1.85, w:hookBoxW, h:2.4, rectRadius:0.1, fill:{color:NAVY} });
  s.addText(hookText, { x:1.0, y:2.05, w:hookBoxW-0.75, h:2.0, fontFace:HEAD, fontSize: chart?21:26, color:WHITE, italic:true, valign:'middle', lineSpacingMultiple:1.08 });
  if(chart){
    const cx = 7.85, cw = 4.85;
    s.addText(chart.title, { x:cx, y:1.66, w:cw, h:0.3, fontFace:LABEL, fontSize:10, color:NAVY, bold:true, align:'center', charSpacing:0.5 });
    s.addChart(pptx.ChartType.doughnut, chart.data, {
      x:cx+0.95, y:1.98, w:cw-1.9, h:1.9, holeSize:60,
      chartColors:[RED, SLATE], showLegend:false, showValue:false, showTitle:false,
      dataBorder:{ pt:1.5, color:'FFFFFF' }
    });
    s.addText(chart.big || '90%', { x:cx+0.95, y:1.98, w:cw-1.9, h:1.9, fontFace:HEAD, fontSize:24, color:RED, bold:true, align:'center', valign:'middle' });
    s.addText([
      {text:'■ ', options:{color:RED}}, {text:'Standard Oil     ', options:{color:INK}},
      {text:'■ ', options:{color:SLATE}}, {text:'all other refiners', options:{color:MUTE}}
    ], { x:cx, y:3.9, w:cw, h:0.24, fontFace:BODY, fontSize:9, align:'center', valign:'middle' });
    s.addText(chart.source, { x:cx, y:4.16, w:cw, h:0.3, fontFace:BODY, fontSize:7, italic:true, color:MUTE, align:'center', valign:'top', lineSpacingMultiple:0.95 });
  }
  s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:4.5, w:12.1, h:1.95, rectRadius:0.1, fill:{color:WHITE}, line:{color:GOLD, width:1.5} });
  s.addText('DISCUSS', { x:1.0, y:4.7, w:3, h:0.35, fontFace:LABEL, fontSize:13, color:RED, bold:true, charSpacing:2 });
  // Facilitation timing pill — gives the teacher an explicit Turn & Talk routine,
  // wait time, and cold-call protocol so the hook stays tight (parity with the
  // DI TEACHER CUE box; Rosenshine P3/P6 + structured discourse).
  s.addShape(pptx.ShapeType.roundRect, { x:8.5, y:4.62, w:4.0, h:0.5, rectRadius:0.1, fill:{color:NAVY} });
  s.addText('TIMING:  Turn & Talk 60 sec \u2192 cold-call 2 pairs', { x:8.5, y:4.62, w:4.0, h:0.5, fontFace:LABEL, fontSize:10.5, color:GOLDBR, bold:true, align:'center', valign:'middle' });
  s.addText(prompt, { x:1.0, y:5.18, w:11.3, h:1.2, fontFace:BODY, fontSize:16, color:INK, valign:'top', lineSpacingMultiple:1.1 });
  s.addNotes('HOOK ('+code+'). Run tight: pose the provocation, give a silent 10-second think, then Turn & Talk 60 seconds. Cold-call 2\u20133 pairs (not volunteers) for a sentence-starter answer \u2014 "One force was ___ because ___" \u2014 then bridge to the standard. Keep total to ~4 minutes; do not let it sprawl. Return to this question at the unit close for an evidence-based answer.');
  footer(s, ++page, false);
}

// Robust sentence splitter: does NOT break on abbreviations (U.S., Lt., etc.)
// or on periods inside quotation marks. Protects known patterns, splits on
// sentence-ending punctuation + space + capital/quote, then restores.
function splitSentences(text){
  if(!text) return [];
  // Protect abbreviations and decimals by swapping the period for a sentinel.
  const ABBR = ['U.S.A','U.S','Lt','Capt','Gen','Col','Sgt','Maj','Mr','Mrs','Ms','Dr','St','Jr','Sr','vs','Rev','Hon','Co','Inc','No','Mt','Ft','D.C','Sec','Art','Amend','approx','est','c'];
  let t = text;
  ABBR.forEach(a=>{
    const re = new RegExp(a.replace(/\./g,'\\.')+'\\.', 'g');
    t = t.replace(re, a.replace(/\./g,'\u0001')+'\u0001');
  });
  // Protect decimals like 90.5 and single-letter initials A. B.
  t = t.replace(/(\d)\.(\d)/g, '$1\u0001$2');
  t = t.replace(/\b([A-Z])\.(?=\s)/g, '$1\u0001');
  // Protect "v." in case names (Plessy v. Ferguson, Brown v. Board): lowercase v
  // followed by a period and a space + capitalized word is a citation, not a sentence end.
  t = t.replace(/\b([Vv])\.(?=\s+[A-Z])/g, '$1\u0001');
  // Protect periods/punctuation inside straight or curly double quotes.
  t = t.replace(/[“"][^”"]*[”"]/g, m => m.replace(/([.!?])/g, (mm)=> mm==='.'?'\u0001': (mm==='!'?'\u0002':'\u0003')));
  // Split after sentence-ending punctuation followed by whitespace + capital/quote/open.
  const parts = t.split(/(?<=[.!?])\s+(?=[A-Z“"'\u2014])/);
  // Restore sentinels.
  return parts
    .map(p => p.replace(/\u0001/g,'.').replace(/\u0002/g,'!').replace(/\u0003/g,'?').trim())
    .filter(p => p.length>0);
}

// Content slide — text on left, period image on right (when available)
function contentSlide(code, v, sec, idx, total, heroImg){
  const s = pptx.addSlide();
  s.background = { color: CREAM };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:NAVY} });
  kicker(s, `${code} · Direct Instruction`, 0.6, 0.45);
  s.addText(sec.heading, { x:0.6, y:0.8, w:12.1, h:0.95, fontFace:HEAD, fontSize:30, color:NAVY, bold:true, valign:'top' });
  // progress dots + explicit "N of M" numeral (do not rely on color alone — WCAG 1.4.1)
  let dx = W-0.6-(total*0.32);
  for(let i=0;i<total;i++){
    s.addShape(pptx.ShapeType.ellipse, { x:dx+i*0.32, y:0.55, w:0.16, h:0.16, fill:{color: i===idx?RED:SLATE} });
  }
  s.addText(`${idx+1} of ${total}`, { x:W-0.6-(total*0.32)-1.05, y:0.45, w:1.0, h:0.36, fontFace:LABEL, fontSize:10, color:MUTE, bold:true, align:'right', valign:'middle' });
  const hasImg = !!heroImg;
  const textW = hasImg ? 7.4 : 12.1;
  const sentences = splitSentences(sec.content);
  const bullets = sentences.map(t=>({text:t.trim(), options:{bullet:{code:'2022', indent:18}, paraSpaceAfter:9}}));
  const hasTN = sec.tn;
  const bodyTop = 1.95;
  // ELL #3 — reserve a sentence-frame strip at the bottom of the body box on the
  // FIRST DI slide of the standard (academic-language scaffold for EL + striving writers).
  const frame = (idx===0) ? SENTENCE_FRAME[code] : null;
  // Taller strip so 2–3 wrapped lines never clip (fixed clipping on the longer frames).
  const frameH = frame ? 1.34 : 0;
  const bodyH = hasTN ? 2.95 : 4.45;
  const bulletsH = bodyH - 0.55 - frameH;
  s.addShape(pptx.ShapeType.rect, { x:0.6, y:bodyTop, w:textW, h:bodyH, fill:{color:WHITE}, line:{color:LINEC,width:1} });
  // Size the bullets to the content volume so a dense standard (image + TN box + 4 bullets,
  // e.g. US.05 Industrial Titans) never pushes the last line out of the box (Sean: the
  // "Cornelius Vanderbilt" line was running out of the white box).
  const bodyFs = hasImg ? ((hasTN || sentences.length>=4) ? 13.5 : 15.5) : (sentences.length>=5 ? 15 : 17);
  s.addText(bullets, { x:1.0, y:bodyTop+0.3, w:textW-0.7, h:bulletsH, fontFace:BODY, fontSize:bodyFs, color:INK, valign:'top', lineSpacingMultiple:1.08 });
  if(frame){
    const fy = bodyTop + bodyH - frameH;
    s.addShape(pptx.ShapeType.roundRect, { x:0.95, y:fy, w:textW-0.7, h:frameH-0.14, rectRadius:0.06, fill:{color:'EEF3F7'}, line:{color:SLATE,width:1} });
    s.addText([
      {text:'SENTENCE FRAME  ', options:{bold:true, color:A250BLUE, fontFace:LABEL, fontSize:9, charSpacing:1}},
      {text:'(EL & writing support)  ', options:{italic:true, color:MUTE, fontSize:8.5}}
    ], { x:1.12, y:fy+0.06, w:textW-1.0, h:0.26, valign:'middle' });
    s.addText(frame, { x:1.12, y:fy+0.34, w:textW-0.5, h:frameH-0.62, fontFace:BODY, fontSize:hasImg?10.5:11.5, italic:true, color:INK, valign:'top', lineSpacingMultiple:1.04 });
  }
  // If a TEACHER CUE box will sit in the bottom-right, shorten the image so its caption
  // clears the cue box (prevents the caption/cue overlap on the first DI slide).
  const cueHere = (idx===0 && v.facilitation);
  if(hasImg){
    const imgH = cueHere ? 3.75 : 4.45;
    imageWithCaption(s, heroImg, { x:8.3, y:bodyTop, w:4.45, h:imgH }, { label:'', capFs:8 });
  }
  if(hasTN){
    s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:5.15, w:textW, h:1.25, rectRadius:0.08, fill:{color:'FBEFD0'}, line:{color:GOLD,width:1.5} });
    s.addText('★ TENNESSEE CONNECTION', { x:0.95, y:5.3, w:6, h:0.3, fontFace:LABEL, fontSize:12, color:RED, bold:true, charSpacing:1 });
    s.addText(tnConnection(code), { x:0.95, y:5.6, w:textW-0.7, h:0.75, fontFace:BODY, fontSize:13, color:INK, valign:'top', lineSpacingMultiple:1.05 });
  }
  // Teacher facilitation cue on the FIRST DI slide of the standard: a compact on-slide
  // instructor prompt (chunk-and-check) plus the full think-aloud / cold-call script in
  // speaker notes (Rosenshine P3 Ask Questions, P6 Check for Understanding).
  if(idx===0 && v.facilitation){
    if(hasImg){
      s.addShape(pptx.ShapeType.roundRect, { x:8.3, y:5.95, w:4.45, h:0.78, rectRadius:0.06, fill:{color:NAVY} });
      s.addText([{text:'TEACHER CUE  ', options:{bold:true, color:GOLDBR, fontFace:LABEL}},{text:'Chunk → cold-call → confirm before advancing.', options:{color:WHITE}}],
        { x:8.5, y:5.99, w:4.05, h:0.7, fontFace:BODY, fontSize:9.5, valign:'middle', lineSpacingMultiple:1.02 });
    }
    s.addNotes('FACILITATION ('+code+'). '+v.facilitation+' Teach in small steps; pause and check for understanding before the next chunk (aim 80%+ before moving on).');
  }
  footer(s, ++page, false);
}

function tnConnection(code){
  const map = {
    'US.01':'Buffalo Soldier George Jordan of Williamson County, Tennessee earned the Medal of Honor for his frontier service — a direct Tennessee link to westward expansion.',
    'US.05':'Cornelius Vanderbilt\u2019s $1 million gift founded Vanderbilt University in Nashville (1873), tying the era\u2019s industrial fortunes directly to Tennessee.',
  };
  return map[code] || '';
}

// Concept visual — vertical vs. horizontal integration, drawn with native shapes
// (Sean: "create an image of what vertical and horizontal integration look like").
// Editable in PowerPoint; no external image required.
function integrationDiagramSlide(code){
  const s = pptx.addSlide();
  s.background = { color: CREAM };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:NAVY} });
  kicker(s, `${code} · Concept Visual`, 0.6, 0.45, RED);
  s.addText('Two Ways to Dominate an Industry', { x:0.6, y:0.8, w:12.1, h:0.7, fontFace:HEAD, fontSize:29, color:NAVY, bold:true });

  // LEFT — VERTICAL INTEGRATION (a top-to-bottom production chain)
  const LX=0.6, LW=5.95;
  s.addShape(pptx.ShapeType.roundRect, { x:LX, y:1.75, w:LW, h:4.9, rectRadius:0.1, fill:{color:WHITE}, line:{color:LINEC,width:1} });
  s.addShape(pptx.ShapeType.roundRect, { x:LX, y:1.75, w:LW, h:0.62, rectRadius:0.1, fill:{color:NAVY} });
  s.addText('VERTICAL INTEGRATION', { x:LX+0.2, y:1.79, w:LW-0.4, h:0.5, fontFace:LABEL, fontSize:15, color:WHITE, bold:true, valign:'middle', charSpacing:1 });
  s.addText('Carnegie · steel — own every STEP of production', { x:LX+0.2, y:2.48, w:LW-0.4, h:0.3, fontFace:BODY, fontSize:11.5, italic:true, color:MUTE });
  const steps = ['Iron ore mines','Coal & coke','Steel mills','Rail & shipping','Finished steel sold'];
  let sy = 2.98; const bh=0.5, bw=LW-1.0, bx=LX+0.5;
  steps.forEach((t,i)=>{
    const last = i===steps.length-1;
    s.addShape(pptx.ShapeType.roundRect, { x:bx, y:sy, w:bw, h:bh, rectRadius:0.05, fill:{color: last?GOLD:NAVY2}, line:{color:LINEC,width:0.5} });
    s.addText(t, { x:bx, y:sy, w:bw, h:bh, fontFace:BODY, fontSize:12, color: last?NAVY:WHITE, bold:true, align:'center', valign:'middle' });
    if(!last) s.addShape(pptx.ShapeType.triangle, { x:LX+LW/2-0.1, y:sy+bh+0.01, w:0.2, h:0.15, rotate:180, fill:{color:RED}, line:{type:'none'} });
    sy += bh + 0.2;
  });

  // RIGHT — HORIZONTAL INTEGRATION (competitors merge into one firm)
  const RX=6.78, RW=5.95;
  s.addShape(pptx.ShapeType.roundRect, { x:RX, y:1.75, w:RW, h:4.9, rectRadius:0.1, fill:{color:WHITE}, line:{color:LINEC,width:1} });
  s.addShape(pptx.ShapeType.roundRect, { x:RX, y:1.75, w:RW, h:0.62, rectRadius:0.1, fill:{color:A250BLUE} });
  s.addText('HORIZONTAL INTEGRATION', { x:RX+0.2, y:1.79, w:RW-0.4, h:0.5, fontFace:LABEL, fontSize:15, color:WHITE, bold:true, valign:'middle', charSpacing:1 });
  s.addText('Rockefeller · oil — buy up your COMPETITORS at the same step', { x:RX+0.2, y:2.48, w:RW-0.4, h:0.3, fontFace:BODY, fontSize:11, italic:true, color:MUTE });
  const comps=['Refiner A','Refiner B','Refiner C','Refiner D'];
  const cw=1.25, cgap=0.16, crow=RX+0.35, cy=3.02;
  comps.forEach((t,i)=>{
    const cxx = crow + i*(cw+cgap);
    s.addShape(pptx.ShapeType.roundRect, { x:cxx, y:cy, w:cw, h:0.6, rectRadius:0.05, fill:{color:SLATE}, line:{color:LINEC,width:0.5} });
    s.addText(t, { x:cxx, y:cy, w:cw, h:0.6, fontFace:BODY, fontSize:10.5, color:NAVY, bold:true, align:'center', valign:'middle' });
    s.addShape(pptx.ShapeType.triangle, { x:cxx+cw/2-0.09, y:cy+0.64, w:0.18, h:0.42, rotate:180, fill:{color:RED}, line:{type:'none'} });
  });
  s.addShape(pptx.ShapeType.roundRect, { x:RX+0.6, y:4.42, w:RW-1.2, h:0.92, rectRadius:0.08, fill:{color:A250BLUE} });
  s.addText('STANDARD OIL — one firm controls the market', { x:RX+0.6, y:4.42, w:RW-1.2, h:0.92, fontFace:BODY, fontSize:13, color:WHITE, bold:true, align:'center', valign:'middle', lineSpacingMultiple:1.02 });
  s.addText('→ fewer competitors → sets prices (monopoly / trust)', { x:RX+0.35, y:5.5, w:RW-0.7, h:0.5, fontFace:BODY, fontSize:11, italic:true, color:MUTE, align:'center', valign:'middle' });

  s.addNotes('CONCEPT VISUAL ('+code+'). VERTICAL (Carnegie): one company owns every stage of production, raw materials → finished product. HORIZONTAL (Rockefeller): one company buys out competitors at the SAME stage to control the market (monopoly / trust). Have students label each diagram and add both terms to their Flight Log Frayer models.');
  footer(s, ++page, false);
}

// Primary source slide — now shows the ACTUAL document/image alongside the excerpt.
function primarySourceSlide(code, ps){
  const s = pptx.addSlide();
  s.background = { color: CREAM };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:A250BLUE} });
  kicker(s, `${code} · Primary Source Analysis`, 0.6, 0.45, A250BLUE);
  s.addText(ps.title, { x:0.6, y:0.8, w:9.5, h:0.7, fontFace:HEAD, fontSize:25, color:NAVY, bold:true, valign:'top' });
  const pr = PRACTICE[ps.practice] || 'Analysis';
  s.addShape(pptx.ShapeType.roundRect, { x:10.3, y:0.85, w:2.4, h:0.5, rectRadius:0.1, fill:{color:A250BLUE} });
  s.addText(pr, { x:10.3, y:0.85, w:2.4, h:0.5, fontFace:LABEL, fontSize:12, color:WHITE, bold:true, align:'center', valign:'middle' });
  s.addText(`${ps.author}  ·  ${ps.date}`, { x:0.6, y:1.46, w:11, h:0.3, fontFace:BODY, fontSize:12, italic:true, color:MUTE });

  const im = ps._image ? imgById(ps._image) : null;
  const panelTop = 1.9, panelBot = 5.45, panelH = panelBot - panelTop;

  if (im) {
    // three-zone: image (left), excerpt (middle), context+analyze (right)
    // The close-looking prompt sits BELOW the image, not on top of it (Sean: "you can't
    // zoom in — it's in the way"). Image height is trimmed so the prompt strip clears it.
    const imgH = panelH - 0.62;
    imageWithCaption(s, im, { x:0.6, y:panelTop, w:3.5, h:imgH }, { capFs:7.5, capH:0.66 });
    s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:panelTop+imgH+0.06, w:3.5, h:0.5, rectRadius:0.06, fill:{color:GOLD}, line:{color:NAVY,width:1} });
    s.addText([
      {text:'LOOK CLOSELY  ', options:{fontFace:LABEL, fontSize:9, color:NAVY, bold:true, charSpacing:1}},
      {text:'find one DEEP detail that surprises you \u2014 be ready to name it.', options:{fontFace:BODY, fontSize:8.5, color:NAVY, italic:true}}
    ], { x:0.75, y:panelTop+imgH+0.09, w:3.24, h:0.44, valign:'middle', lineSpacingMultiple:0.95 });
    // excerpt
    s.addShape(pptx.ShapeType.rect, { x:4.3, y:panelTop, w:3.85, h:panelH, fill:{color:WHITE}, line:{color:LINEC,width:1} });
    s.addShape(pptx.ShapeType.rect, { x:4.3, y:panelTop, w:0.1, h:panelH, fill:{color:GOLD} });
    const exFs = ps.excerpt.length > 360 ? 11.5 : 12.5;
    s.addText('"'+ps.excerpt+'"', { x:4.55, y:panelTop+0.2, w:3.5, h:panelH-0.4, fontFace:HEAD, fontSize:exFs, italic:true, color:INK, valign:'top', lineSpacingMultiple:1.12 });
  } else {
    s.addShape(pptx.ShapeType.rect, { x:0.6, y:panelTop, w:7.5, h:panelH, fill:{color:WHITE}, line:{color:LINEC,width:1} });
    s.addShape(pptx.ShapeType.rect, { x:0.6, y:panelTop, w:0.12, h:panelH, fill:{color:GOLD} });
    const exFs = ps.excerpt.length > 360 ? 13 : 14;
    s.addText('"'+ps.excerpt+'"', { x:0.95, y:panelTop+0.22, w:6.95, h:panelH-0.42, fontFace:HEAD, fontSize:exFs, italic:true, color:INK, valign:'top', lineSpacingMultiple:1.14 });
  }

  // Right column = CONTEXT (top) + ANALYZE (bottom). Size CONTEXT to its content so
  // the freed space goes to ANALYZE — long analyze questions were being clipped at the
  // bottom edge (and colliding with the new SOURCE IT FIRST band below).
  const ctxTop = panelTop;
  const ctxLen = (ps.context||'').length;
  const qLen = (ps.analyzeQuestion||ps.question||'').length;
  // Sean: CONTEXT is the primary (larger) box; ANALYZE is compact but sized to its
  // question so it never clips into the SOURCE IT FIRST band below.
  const desiredAnaH = qLen > 150 ? 1.5 : qLen > 100 ? 1.3 : qLen > 70 ? 1.1 : 0.95;
  let ctxH = (panelBot - ctxTop) - 0.2 - desiredAnaH;
  s.addShape(pptx.ShapeType.roundRect, { x:8.3, y:ctxTop, w:4.4, h:ctxH, rectRadius:0.08, fill:{color:NAVY} });
  s.addText('CONTEXT', { x:8.55, y:ctxTop+0.13, w:4, h:0.3, fontFace:LABEL, fontSize:11, color:GOLDBR, bold:true, charSpacing:2 });
  // tier the font so the FULL context sentence fits without mid-sentence truncation.
  // The right column is ~3.95" wide; cap context length to what the box height holds and
  // add a small tier for very long contexts so the last sentence never clips.
  const ctxFs = ctxLen > 700 ? 7.8 : ctxLen > 560 ? 8.5 : ctxLen > 440 ? 9.5 : 10.5;
  const ctxCap = ctxLen > 700 ? 760 : 700;
  s.addText(trunc(ps.context, ctxCap), { x:8.55, y:ctxTop+0.44, w:3.95, h:ctxH-0.56, fontFace:BODY, fontSize:ctxFs, color:WHITE, valign:'top', lineSpacingMultiple:0.98 });
  const anaTop = ctxTop + ctxH + 0.2, anaH = panelBot - anaTop;
  s.addShape(pptx.ShapeType.roundRect, { x:8.3, y:anaTop, w:4.4, h:anaH, rectRadius:0.08, fill:{color:GOLD} });
  s.addText(ps.analyzeLabel || 'ANALYZE', { x:8.55, y:anaTop+0.13, w:4, h:0.3, fontFace:LABEL, fontSize:11, color:NAVY, bold:true, charSpacing:2 });
  // size the analyze question so long stems fit the box without clipping
  const anaFs = qLen > 175 ? 11 : qLen > 130 ? 12 : 12.5;
  s.addText(ps.analyzeQuestion || ps.question, { x:8.55, y:anaTop+0.46, w:3.95, h:anaH-0.58, fontFace:BODY, fontSize:anaFs, color:NAVY, bold:true, valign:'top', lineSpacingMultiple:1.03 });

  // SOURCE IT FIRST — Rosenshine P8 scaffold + SSP.02 (Examine a primary or secondary source).
  // Sourcing routine students run BEFORE interpreting: Who made it? When? Why does that matter?
  const sif = ps._sourceItFirst;
  if(sif){
    const sbY = 5.6, sbH = 0.92;
    s.addShape(pptx.ShapeType.rect, { x:0.6, y:sbY, w:12.1, h:sbH, fill:{color:WHITE}, line:{color:A250BLUE,width:1.25} });
    s.addShape(pptx.ShapeType.rect, { x:0.6, y:sbY, w:2.65, h:sbH, fill:{color:A250BLUE} });
    s.addText('SOURCE IT', { x:0.72, y:sbY+0.13, w:2.4, h:0.3, fontFace:LABEL, fontSize:12.5, color:WHITE, bold:true, charSpacing:1 });
    s.addText('FIRST', { x:0.72, y:sbY+0.40, w:2.4, h:0.3, fontFace:LABEL, fontSize:12.5, color:GOLDBR, bold:true, charSpacing:1 });
    s.addText('SSP.02 · before you interpret', { x:0.72, y:sbY+0.66, w:2.45, h:0.22, fontFace:BODY, fontSize:7.5, italic:true, color:'C7D4E0' });
    const segW = 3.0, gap = 0.05, sx0 = 3.45;
    const segs = [['WHO made it?', sif.who],['WHEN?', sif.when],['WHY does it matter?', sif.why]];
    segs.forEach((seg,i)=>{
      const sx = sx0 + i*(segW+gap);
      s.addText(seg[0], { x:sx, y:sbY+0.10, w:segW, h:0.24, fontFace:LABEL, fontSize:9, color:A250BLUE, bold:true });
      s.addText(trunc(seg[1], 130), { x:sx, y:sbY+0.34, w:segW, h:sbH-0.42, fontFace:BODY, fontSize:9.5, color:INK, valign:'top', lineSpacingMultiple:0.98 });
    });
    sourceLine(s, (ps.citation && ps.citation.archiveName) || 'National Archives', ps.url, 6.62, 7.5);
  } else {
    sourceLine(s, (ps.citation && ps.citation.archiveName) || 'National Archives', ps.url, 5.62, 7.5);
  }
  s.addNotes('Primary-source analysis. SOURCE IT FIRST (SSP.02) — model the sourcing routine aloud before students interpret: WHO made this source? (' + (sif?sif.who:'—') + ') WHEN? (' + (sif?sif.when:'—') + ') WHY does that matter? (' + (sif?sif.why:'—') + ') Only then move to the ANALYZE question. Suggested answer: ' + (ps.explanation || 'See teacher key.') + ' Practice skill: ' + pr + '.');
  footer(s, ++page, false);
}

function vocabSlide(code, v){
  const s = pptx.addSlide();
  s.background = { color: CREAM };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:NAVY} });
  kicker(s, `${code} · Vocabulary Pre-Teach & Word Wall`, 0.6, 0.45);
  s.addText('Word Wall', { x:0.6, y:0.8, w:12, h:0.7, fontFace:HEAD, fontSize:30, color:NAVY, bold:true });
  const terms = v.vocab.slice(0,6);
  const cols = 2;
  const rows = Math.ceil(terms.length/cols);
  const cw = 6.0;
  const colGap = 0.25;
  const topY = 1.8, bandH = 4.5, gap = 0.18;
  const ch = Math.min(2.05, (bandH - (rows-1)*gap)/rows);
  // Taller header so the English term, the EN pronunciation respelling (ELL #1),
  // and the Spanish term all fit without collision.
  const hdrH = 0.74;
  const lastRowCount = terms.length - (rows-1)*cols; // items on the final row
  terms.forEach((t,i)=>{
    const rowIdx = Math.floor(i/cols);
    const colIdx = i%cols;
    const isLastRow = rowIdx === rows-1;
    // center the final partial row so there is never a visibly empty cell
    let cx;
    if(isLastRow && lastRowCount < cols){
      const rowW = lastRowCount*cw + (lastRowCount-1)*colGap;
      const startX = (W - rowW)/2;
      cx = startX + colIdx*(cw+colGap);
    } else {
      cx = 0.6 + colIdx*(cw+colGap);
    }
    const cy = topY + rowIdx*(ch+gap);
    s.addShape(pptx.ShapeType.rect, { x:cx, y:cy, w:cw, h:ch, fill:{color:WHITE}, line:{color:LINEC,width:1} });
    s.addShape(pptx.ShapeType.rect, { x:cx, y:cy, w:cw, h:hdrH, fill:{color:NAVY} });
    // English term (top of header)
    s.addText(t.term, { x:cx+0.15, y:cy+0.06, w:cw-2.85, h:0.34, fontFace:BODY, fontSize:13.5, color:WHITE, bold:true, valign:'middle', fit:'shrink' });
    // ELL #1 — pronunciation respelling beneath the term (stressed syllable in CAPS),
    // labeled "say:" (text label renders reliably on any school computer; no glyph).
    const pron = PRONOUNCE[t.term] || PRONOUNCE[(t.term||'').toLowerCase()];
    if(pron) s.addText([
      {text:'say:  ', options:{bold:true, color:SLATEL, fontFace:LABEL, fontSize:8.5}},
      {text:pron, options:{italic:true, color:SLATEL, fontFace:BODY, fontSize:9.5}}
    ], { x:cx+0.15, y:cy+0.40, w:cw-2.85, h:0.28, valign:'middle', fit:'shrink' });
    // Spanish term (right side of header, vertically centered)
    if(t.es) s.addText(t.es, { x:cx+cw-2.55, y:cy, w:2.4, h:hdrH, fontFace:BODY, fontSize:10, italic:true, color:GOLDBR, align:'right', valign:'middle', fit:'shrink' });
    // (LOCKED — Sean: NO per-term initials chip on the word wall. Removed the "HA"-style
    // dual-coding initials anchor; the definition fills the full card width instead.)
    s.addText(trunc(t.def, 240), { x:cx+0.15, y:cy+hdrH+0.08, w:cw-0.30, h:ch-hdrH-0.18, fontFace:BODY, fontSize:11, color:INK, valign:'top', lineSpacingMultiple:1.04 });
  });
  s.addText('PRE-TEACH before reading — students capture each term as a Frayer model in their Flight Log. "say:" respelling (stressed syllable in CAPS) aids newcomer ELs; Spanish terms included.',
    { x:0.6, y:6.45, w:12.1, h:0.35, fontFace:BODY, fontSize:10, italic:true, color:MUTE });
  footer(s, ++page, false);
}

function bioSlide(code, bios){
  const s = pptx.addSlide();
  s.background = { color: CREAM };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:RED} });
  kicker(s, `${code} · People Who Shaped the Era`, 0.6, 0.45);
  s.addText(bios.length>1?'Key Figures':'Key Figure', { x:0.6, y:0.8, w:12, h:0.7, fontFace:HEAD, fontSize:30, color:NAVY, bold:true });
  const show = bios.slice(0,5);
  const n = show.length;
  // Visual #1 — when there are 4-5 figures, switch from a single cramped row to a
  // 2-ROW grid so each card is far wider and fonts stay legible from the back row.
  // Row 1 = ceil(n/2) cards, Row 2 = the rest (centered). Single row for n<=3.
  const twoRow = n >= 4;
  const r1 = twoRow ? Math.ceil(n/2) : n;
  const r2 = n - r1;
  const stratH = 0.6;
  const cardTop = 1.78;
  const cardH = twoRow ? 2.18 : 4.5;
  const rowGap = 0.22;
  const perRow = Math.max(r1, r2);
  const nameFs = perRow <= 2 ? 18 : (perRow === 3 ? 16 : 14);
  const bodyFs = perRow <= 2 ? 13 : (perRow === 3 ? 12 : 11);
  const roleFs = perRow <= 3 ? 11 : 9.5;
  const hdrH = twoRow ? 0.6 : 0.95;
  const bullets = twoRow ? 2 : 3;
  const layoutRow = (rowBios, count, cy) => {
    const cw = (12.1 - (count-1)*0.3)/count;
    const rowW = count*cw + (count-1)*0.3;
    const x0 = 0.6 + (12.1 - rowW)/2;
    rowBios.forEach((b,i)=>{
      const cx = x0 + i*(cw+0.3);
      s.addShape(pptx.ShapeType.rect, { x:cx, y:cy, w:cw, h:cardH, fill:{color:WHITE}, line:{color:LINEC,width:1} });
      s.addShape(pptx.ShapeType.rect, { x:cx, y:cy, w:cw, h:hdrH, fill:{color:NAVY} });
      if(twoRow){
        // wide card: name left, primary role right of the same header band
        s.addText(b.name, { x:cx+0.15, y:cy+0.03, w:cw*0.62, h:hdrH-0.06, fontFace:HEAD, fontSize:nameFs, color:WHITE, bold:true, valign:'middle', lineSpacingMultiple:0.95, fit:'shrink' });
        const role0 = Array.isArray(b.role)?b.role[0]:b.role;
        s.addText(role0, { x:cx+cw*0.62, y:cy+0.03, w:cw*0.38-0.15, h:hdrH-0.06, fontFace:LABEL, fontSize:roleFs, color:GOLDBR, align:'right', valign:'middle', fit:'shrink' });
      } else {
        s.addText(b.name, { x:cx+0.13, y:cy, w:cw-0.26, h:hdrH-0.26, fontFace:HEAD, fontSize:nameFs, color:WHITE, bold:true, valign:'middle', lineSpacingMultiple:0.95, fit:'shrink' });
        const role = Array.isArray(b.role)?b.role.slice(0,2).join(' · '):b.role;
        s.addText(role, { x:cx+0.13, y:cy+hdrH-0.3, w:cw-0.26, h:0.3, fontFace:LABEL, fontSize:roleFs, color:GOLDBR, valign:'middle', fit:'shrink' });
      }
      const acc = Array.isArray(b.accomplish)?b.accomplish.slice(0,bullets):[b.accomplish];
      const bodyTop = cy + hdrH + (twoRow?0.08:0.12);
      const bodyH2 = cy + cardH - (b.strategy ? stratH + 0.05 : 0.16) - bodyTop;
      s.addText(acc.map(a=>({text:a, options:{bullet:{code:'2022',indent:12}, paraSpaceAfter:twoRow?3:6}})),
        { x:cx+0.16, y:bodyTop, w:cw-0.32, h:bodyH2, fontFace:BODY, fontSize:bodyFs, color:INK, valign:'middle', lineSpacingMultiple:1.05 });
      if(b.strategy){
        const sy = cy + cardH - stratH - 0.05;
        s.addShape(pptx.ShapeType.roundRect, { x:cx+0.13, y:sy, w:cw-0.26, h:stratH-0.04, rectRadius:0.06, fill:{color:'FBEFD0'}, line:{color:GOLD,width:1.25} });
        s.addText([
          {text:'STRATEGY  ', options:{fontFace:LABEL, fontSize:8, color:RED, bold:true, charSpacing:1}},
          {text:b.strategy, options:{fontFace:BODY, fontSize:twoRow?10.5:11, color:NAVY, bold:true}}
        ], { x:cx+0.22, y:sy+0.03, w:cw-0.42, h:stratH-0.1, valign:'middle', lineSpacingMultiple:0.92, fit:'shrink' });
      }
    });
  };
  layoutRow(show.slice(0, r1), r1, cardTop);
  if(twoRow && r2>0) layoutRow(show.slice(r1), r2, cardTop + cardH + rowGap);
  footer(s, ++page, false);
}

// GUIDED PRACTICE — "We Do" worked example (Rosenshine P4 Provide Models & P5 Guide
// Practice). Sits BETWEEN direct instruction and the independent student activity so
// students watch the target skill modeled before they attempt it on their own.
function weDoSlide(code, wd){
  const s = pptx.addSlide();
  s.background = { color: CREAM };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:NAVY} });
  kicker(s, `${code} · Guided Practice — We Do It Together`, 0.6, 0.45, RED);
  s.addText('Let’s Work One Together', { x:0.6, y:0.8, w:9.4, h:0.7, fontFace:HEAD, fontSize:29, color:NAVY, bold:true, valign:'top' });
  // skill chip (names the thinking move being modeled)
  s.addShape(pptx.ShapeType.roundRect, { x:9.7, y:0.9, w:3.0, h:0.5, rectRadius:0.1, fill:{color:NAVY} });
  s.addText(wd.skill, { x:9.7, y:0.9, w:3.0, h:0.5, fontFace:LABEL, fontSize:11, color:GOLDBR, bold:true, align:'center', valign:'middle' });
  // the prompt being modeled
  s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:1.7, w:12.1, h:0.95, rectRadius:0.08, fill:{color:NAVY2}, line:{color:SLATE,width:0.5} });
  s.addText([{text:'MODEL PROMPT:  ', options:{bold:true, color:GOLDBR}},{text:wd.modeledPrompt, options:{color:WHITE}}],
    { x:0.9, y:1.82, w:11.5, h:0.7, fontFace:BODY, fontSize:15, valign:'middle', lineSpacingMultiple:1.04 });
  // the worked answer (gold = teacher models this live)
  s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:2.85, w:12.1, h:1.7, rectRadius:0.08, fill:{color:GOLD} });
  s.addText('WORKED EXAMPLE  (teacher models this aloud)', { x:0.9, y:2.98, w:11, h:0.32, fontFace:LABEL, fontSize:11, color:NAVY, bold:true, charSpacing:1 });
  s.addText(wd.modeled, { x:0.9, y:3.32, w:11.5, h:1.1, fontFace:BODY, fontSize:14.5, color:NAVY, bold:true, valign:'top', lineSpacingMultiple:1.08 });
  // the think-aloud (why the move works)
  s.addShape(pptx.ShapeType.rect, { x:0.6, y:4.7, w:12.1, h:1.5, fill:{color:WHITE}, line:{color:LINEC,width:1} });
  s.addText('THINK ALOUD', { x:0.9, y:4.82, w:5, h:0.3, fontFace:LABEL, fontSize:11, color:RED, bold:true, charSpacing:2 });
  s.addText(wd.think, { x:0.9, y:5.14, w:11.5, h:1.0, fontFace:BODY, fontSize:13, color:INK, italic:true, valign:'top', lineSpacingMultiple:1.08 });
  // hand-off to the activity
  s.addText([{text:'\u2192 Now you try:  ', options:{bold:true, color:NAVY}},{text:wd.thenYou, options:{italic:true, color:A250BLUE}}],
    { x:0.6, y:6.32, w:12.1, h:0.4, fontFace:BODY, fontSize:12, valign:'middle' });
  s.addNotes('GUIDED PRACTICE / WE DO ('+code+'). Skill modeled: '+wd.skill+'. Model the worked example aloud using the THINK ALOUD as your script, then release students to the activity ("'+wd.thenYou+'"). This is the I Do → We Do → You Do bridge — do not skip it; aim for 80%+ success before independent work.');
  footer(s, ++page, false);
}

// Student activity slide — on-slide task + paired printable worksheet.
function activitySlide(code, a, im){
  const s = pptx.addSlide();
  s.background = { color: CREAM };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:GOLD} });
  kicker(s, `${code} · Student Activity`, 0.6, 0.45, RED);
  s.addText(a.title, { x:0.6, y:0.8, w:12.1, h:0.85, fontFace:HEAD, fontSize:27, color:NAVY, bold:true, valign:'top' });
  // meta chips
  const chips = [a.grouping, a.minutes];
  let cxp = 0.6;
  chips.forEach(c=>{
    const wch = 0.3 + c.length*0.092;
    s.addShape(pptx.ShapeType.roundRect, { x:cxp, y:1.62, w:wch, h:0.4, rectRadius:0.08, fill:{color:NAVY} });
    s.addText(c, { x:cxp, y:1.62, w:wch, h:0.4, fontFace:LABEL, fontSize:10.5, color:GOLDBR, bold:true, align:'center', valign:'middle' });
    cxp += wch + 0.18;
  });
  const hasImg = !!im;
  const taskW = hasImg ? 7.4 : 12.1;
  // task card
  s.addShape(pptx.ShapeType.rect, { x:0.6, y:2.25, w:taskW, h:2.55, fill:{color:WHITE}, line:{color:LINEC,width:1} });
  s.addText('YOUR TASK', { x:0.9, y:2.4, w:5, h:0.3, fontFace:LABEL, fontSize:11, color:RED, bold:true, charSpacing:2 });
  s.addText(a.prompt, { x:0.9, y:2.72, w:taskW-0.6, h:2.0, fontFace:BODY, fontSize:13.5, color:INK, valign:'top', lineSpacingMultiple:1.12 });
  if(hasImg){
    imageWithCaption(s, im, { x:8.3, y:2.25, w:4.45, h:2.55 }, { capFs:7.5, capH:0.6 });
  }
  // deliverable + differentiation row
  s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:4.95, w:6.0, h:1.45, rectRadius:0.08, fill:{color:NAVY} });
  s.addText('DELIVERABLE', { x:0.85, y:5.08, w:5, h:0.3, fontFace:LABEL, fontSize:10.5, color:GOLDBR, bold:true, charSpacing:2 });
  s.addText(a.deliverable, { x:0.85, y:5.38, w:5.5, h:0.95, fontFace:BODY, fontSize:12.5, color:WHITE, valign:'top', lineSpacingMultiple:1.05 });
  s.addShape(pptx.ShapeType.roundRect, { x:6.75, y:4.95, w:5.95, h:1.45, rectRadius:0.08, fill:{color:'FBEFD0'}, line:{color:GOLD,width:1.25} });
  s.addText('DIFFERENTIATION', { x:7.0, y:5.08, w:5, h:0.3, fontFace:LABEL, fontSize:10.5, color:RED, bold:true, charSpacing:2 });
  s.addText(a.differentiation, { x:7.0, y:5.38, w:5.5, h:0.95, fontFace:BODY, fontSize:12, color:INK, valign:'top', lineSpacingMultiple:1.05 });
  // paired worksheet line
  s.addText([{text:'Companion printable:  ', options:{bold:true, color:NAVY}},{text:a.worksheet, options:{italic:true, color:A250BLUE}}],
    { x:0.6, y:6.5, w:12.1, h:0.35, fontFace:BODY, fontSize:10.5, valign:'middle' });
  s.addNotes('Student activity for '+code+'. Pair with the printable: '+a.worksheet+'. Timing: '+a.minutes+'. Deliverable: '+a.deliverable);
  footer(s, ++page, false);
}

// EOC check — QUESTION slide (no answer shown). Advance (click) to the reveal slide.
function checkQuestionSlide(code, ps){
  const s = pptx.addSlide();
  s.background = { color: NAVY };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:GOLD} });
  kicker(s, `${code} · Check for Understanding`, 0.6, 0.5, GOLDBR);
  s.addText('TCAP-Style Question', { x:0.6, y:0.85, w:7.4, h:0.6, fontFace:HEAD, fontSize:28, color:WHITE, bold:true });
  const dok = ps.dokLevel || 'DOK 1';
  s.addShape(pptx.ShapeType.roundRect, { x:8.35, y:0.9, w:1.25, h:0.5, rectRadius:0.1, fill:{color:NAVY2}, line:{color:GOLD,width:1} });
  s.addText(dok, { x:8.35, y:0.9, w:1.25, h:0.5, fontFace:LABEL, fontSize:12, color:GOLDBR, bold:true, align:'center', valign:'middle' });
  s.addShape(pptx.ShapeType.roundRect, { x:9.7, y:0.9, w:3.0, h:0.5, rectRadius:0.1, fill:{color:RED} });
  s.addText('EOC PRACTICE', { x:9.7, y:0.9, w:3.0, h:0.5, fontFace:LABEL, fontSize:12, color:WHITE, bold:true, align:'center', valign:'middle' });
  s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:1.7, w:12.1, h:1.15, rectRadius:0.08, fill:{color:NAVY2}, line:{color:SLATE,width:0.5} });
  s.addText(ps.question, { x:0.9, y:1.85, w:11.5, h:0.85, fontFace:BODY, fontSize:16, color:WHITE, bold:true, valign:'middle', lineSpacingMultiple:1.05 });
  const letters=['A','B','C','D'];
  ps.options.slice(0,4).forEach((o,i)=>{
    const oy = 3.0 + i*0.82;
    s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:oy, w:12.1, h:0.72, rectRadius:0.06, fill:{color:'2C384F'}, line:{color:'3A475E', width:1} });
    s.addShape(pptx.ShapeType.ellipse, { x:0.78, y:oy+0.16, w:0.4, h:0.4, fill:{color:'1A2332'} });
    s.addText(letters[i], { x:0.78, y:oy+0.16, w:0.4, h:0.4, fontFace:LABEL, fontSize:14, color:SLATE, bold:true, align:'center', valign:'middle' });
    s.addText(o.text, { x:1.35, y:oy, w:10.6, h:0.72, fontFace:BODY, fontSize:13.5, color:WHITE, valign:'middle', lineSpacingMultiple:1.0 });
  });
  // reveal prompt (instead of answer)
  s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:6.25, w:12.1, h:0.55, rectRadius:0.08, fill:{color:NAVY2}, line:{color:GOLD,width:1} });
  s.addText([
    {text:'ANSWER FIRST:  ', options:{bold:true, color:GOLDBR, fontFace:LABEL, charSpacing:1}},
    {text:'students commit — then click / advance to reveal the correct answer and explanation.', options:{color:SLATEL}}
  ], { x:0.9, y:6.25, w:11.5, h:0.55, fontFace:BODY, fontSize:12, italic:true, valign:'middle' });
  const correctLetter = letters[ps.options.findIndex(o=>o.isCorrect)];
  s.addNotes('CHECK FOR UNDERSTANDING ('+code+', '+dok+'). Have students commit to an answer (whiteboards, hand signal, or turn-and-talk) BEFORE advancing. Correct answer: '+correctLetter+'. The next slide reveals it. Why: '+(ps.explanation||''));
  footer(s, ++page, true);
}

// EOC check — REVEAL slide (correct answer highlighted + Why). This is also the answer key.
function checkRevealSlide(code, ps){
  const s = pptx.addSlide();
  s.background = { color: NAVY };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:GOLD} });
  kicker(s, `${code} · Answer Reveal`, 0.6, 0.5, GOLDBR);
  s.addText('TCAP-Style Question', { x:0.6, y:0.85, w:9, h:0.6, fontFace:HEAD, fontSize:28, color:WHITE, bold:true });
  s.addShape(pptx.ShapeType.roundRect, { x:9.4, y:0.9, w:3.3, h:0.5, rectRadius:0.1, fill:{color:KEYGRN} });
  s.addText('✓ ANSWER KEY', { x:9.4, y:0.9, w:3.3, h:0.5, fontFace:LABEL, fontSize:12, color:WHITE, bold:true, align:'center', valign:'middle' });
  s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:1.7, w:12.1, h:1.05, rectRadius:0.08, fill:{color:NAVY2}, line:{color:SLATE,width:0.5} });
  s.addText(ps.question, { x:0.9, y:1.82, w:11.5, h:0.8, fontFace:BODY, fontSize:15, color:WHITE, bold:true, valign:'middle', lineSpacingMultiple:1.02 });
  const letters=['A','B','C','D'];
  ps.options.slice(0,4).forEach((o,i)=>{
    const oy = 2.9 + i*0.72;
    const correct = o.isCorrect;
    s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:oy, w:12.1, h:0.62, rectRadius:0.06, fill:{color: correct?GOLD:'2C384F'}, line:{color: correct?GOLDBR:'3A475E', width:1} });
    s.addShape(pptx.ShapeType.ellipse, { x:0.78, y:oy+0.12, w:0.38, h:0.38, fill:{color: correct?NAVY:'1A2332'} });
    s.addText(letters[i], { x:0.78, y:oy+0.12, w:0.38, h:0.38, fontFace:LABEL, fontSize:13, color: correct?GOLDBR:SLATE, bold:true, align:'center', valign:'middle' });
    s.addText(o.text, { x:1.33, y:oy, w:10.4, h:0.62, fontFace:BODY, fontSize:13, color: correct?NAVY:WHITE, bold:correct, valign:'middle', lineSpacingMultiple:1.0 });
    if(correct){ s.addText('✓', { x:12.05, y:oy, w:0.5, h:0.62, fontFace:BODY, fontSize:17, color:NAVY, bold:true, align:'center', valign:'middle' }); }
  });
  // Why panel
  const correctLetter = letters[ps.options.findIndex(o=>o.isCorrect)];
  s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:5.95, w:12.1, h:0.95, rectRadius:0.08, fill:{color:NAVY2}, line:{color:GOLDBR,width:1} });
  s.addText([
    {text:'Correct answer: '+correctLetter+'.  ', options:{bold:true, color:GOLDBR}},
    {text:'Why: ', options:{bold:true, color:GOLDBR}},
    {text:trunc(ps.explanation,300), options:{color:SLATEL}}
  ], { x:0.9, y:6.05, w:11.5, h:0.78, fontFace:BODY, fontSize:11.5, valign:'middle', lineSpacingMultiple:1.04 });
  s.addNotes('ANSWER KEY ('+code+'). Correct: '+correctLetter+'. '+(ps.explanation||''));
  footer(s, ++page, true);
}

function summarySlide(code, v){
  const s = pptx.addSlide();
  s.background = { color: CREAM };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:NAVY} });
  kicker(s, `${code} · Wrap-Up`, 0.6, 0.45);
  s.addText('What You Need to Know for TCAP', { x:0.6, y:0.8, w:12.1, h:0.7, fontFace:HEAD, fontSize:28, color:NAVY, bold:true });
  // Sean: takeaways must NAME the specifics, not just the category. A per-standard
  // `keyTakeaways` array overrides the bare section headings when present.
  const takeaways = (v.keyTakeaways && v.keyTakeaways.length) ? v.keyTakeaways : v.sections.map(sec=>sec.heading);
  // Left column split into KEY TAKEAWAYS (top) + HONORS / EXTENSION (bottom) so the
  // wrap-up offers a DOK-3 challenge for early finishers / advanced learners (TCAP rigor).
  s.addShape(pptx.ShapeType.rect, { x:0.6, y:1.85, w:7.7, h:3.25, fill:{color:WHITE}, line:{color:LINEC,width:1} });
  s.addText('KEY TAKEAWAYS', { x:0.95, y:2.02, w:6, h:0.35, fontFace:LABEL, fontSize:12, color:RED, bold:true, charSpacing:2 });
  s.addText(takeaways.map(t=>({text:t, options:{bullet:{code:'2022',indent:16}, paraSpaceAfter:8}})),
    { x:0.95, y:2.42, w:7.1, h:2.55, fontFace:BODY, fontSize:15, color:INK, valign:'top', lineSpacingMultiple:1.05 });
  // HONORS / EXTENSION band (DOK 3 argumentation, keyed to SSP.04). Pulls from EXIT[code].honors.
  const honorsQ = (EXIT[code] && EXIT[code].honors) ? EXIT[code].honors : null;
  s.addShape(pptx.ShapeType.roundRect, { x:0.6, y:5.25, w:7.7, h:1.1, rectRadius:0.08, fill:{color:'F3EAD0'}, line:{color:GOLD,width:1} });
  s.addText([
    {text:'\u2605 HONORS / EXTENSION  ', options:{fontFace:LABEL, fontSize:11, color:'7A5C12', bold:true, charSpacing:1}},
    {text:'DOK 3 \u00b7 SSP.04 Argumentation', options:{fontFace:LABEL, fontSize:9.5, color:MUTE, bold:true}}
  ], { x:0.9, y:5.36, w:7.1, h:0.3, valign:'middle' });
  s.addText(honorsQ || 'Construct an evidence-based argument that extends today\u2019s objective; defend your claim with at least two specific pieces of evidence.',
    { x:0.9, y:5.66, w:7.1, h:0.62, fontFace:BODY, fontSize:12.5, color:INK, italic:true, valign:'top', lineSpacingMultiple:1.0 });
  s.addShape(pptx.ShapeType.roundRect, { x:8.55, y:1.85, w:4.15, h:4.5, rectRadius:0.1, fill:{color:NAVY} });
  const et = EXIT[code] || { dok:'DOK 2', q:'In one sentence, restate the "I Can" objective for '+code+' in your own words, using at least one key term from today.', model:'Restates the objective and uses a key term.' };
  s.addText('EXIT TICKET', { x:8.85, y:2.1, w:2.5, h:0.35, fontFace:LABEL, fontSize:12, color:GOLDBR, bold:true, charSpacing:2 });
  s.addShape(pptx.ShapeType.roundRect, { x:11.35, y:2.06, w:1.05, h:0.4, rectRadius:0.08, fill:{color:NAVY2}, line:{color:GOLD,width:0.75} });
  s.addText(et.dok, { x:11.35, y:2.06, w:1.05, h:0.4, fontFace:LABEL, fontSize:10, color:GOLDBR, bold:true, align:'center', valign:'middle' });
  s.addText(et.q, { x:8.85, y:2.6, w:3.55, h:1.5, fontFace:BODY, fontSize:13.5, color:WHITE, valign:'top', lineSpacingMultiple:1.1 });
  // Sean: give students CHOICE in how they answer — then route them to one place to record it.
  s.addText([
    {text:'CHOOSE ONE  ', options:{bold:true, color:GOLDBR, fontFace:LABEL, fontSize:9, charSpacing:1}},
    {text:'write it · tell a partner · sketch it', options:{italic:true, color:'C7D4E0', fontSize:9.5}}
  ], { x:8.85, y:4.16, w:3.55, h:0.6, valign:'top', lineSpacingMultiple:1.0 });
  s.addShape(pptx.ShapeType.line, { x:8.9, y:5.02, w:3.4, h:0, line:{color:SLATE, width:1, dashType:'dash'} });
  s.addShape(pptx.ShapeType.line, { x:8.9, y:5.62, w:3.4, h:0, line:{color:SLATE, width:1, dashType:'dash'} });
  s.addText('↪ Record it on your Flight Log · exit page.', { x:8.85, y:6.0, w:3.6, h:0.3, fontFace:BODY, fontSize:9.5, italic:true, color:GOLDBR, valign:'middle' });
  // exit-ticket model answer + ROUTED reteach trigger for the teacher (speaker notes).
  // The diagnostic names the exact reteach path so the exit ticket closes a feedback loop
  // (Hattie & Timperley: assess -> identify gap -> targeted reteach -> re-assess).
  const cornell = (ACTS[code] && ACTS[code].worksheet) ? ACTS[code].worksheet : (code+' Cornell Notes');
  const firstSec = takeaways[0] || 'the standard opener';
  s.addNotes('WRAP-UP / EXIT-TICKET KEY ('+code+', '+et.dok+'). Prompt: '+et.q+'  Model answer: '+et.model+
    '  RETEACH TRIGGER — if a student misses this exit ticket: (1) <50% of class miss → spiral it into the next standard’s Quick Review opener (see the '+code+' review prompts). '+
    '(2) Individual/small group → reteach with the "'+firstSec+'" direct-instruction slide + re-run the SOURCE IT FIRST routine on the '+code+' primary source, then assign the paired printable: '+cornell+'. '+
    '(3) Re-assess with the '+code+' check-for-understanding reveal slide as a do-now the next day. Reteach anchors (this standard’s sections): '+takeaways.join('; ')+'. I Can objective: '+v.iCan+
    (honorsQ ? '  HONORS / EXTENSION (DOK 3, for early finishers or advanced learners): '+honorsQ+' — look for a clear claim plus two specific pieces of evidence.' : ''));
  footer(s, ++page, false);
}

function trunc(t, n){
  if(!t) return '';
  if(t.length<=n) return t;
  let cut = t.slice(0, n);
  const sp = cut.lastIndexOf(' ');
  if(sp > n*0.6) cut = cut.slice(0, sp);
  return cut.replace(/[\s,;:.\-]+$/,'') + '…';
}

// Spaced retrieval prompts per standard (interleaved, pull from PRIOR standards).
// US.01 activates prior knowledge from the unit hook; later standards review earlier ones.
const REVIEW = {
  'US.01': { prompts: [
    { from:'Unit Hook', q:'Name one PUSH factor and one PULL factor that moved Americans from farms to cities.', a:'Push: drought/debt/falling prices. Pull: factory jobs, higher wages, city amenities.' },
    { from:'Prior', q:'What major war had just ended in 1865, and what region was being rebuilt?', a:'The Civil War; the South was being rebuilt during Reconstruction.' },
  ]},
  'US.02': { prompts: [
    { from:'US.01', q:'How did the Homestead Act and the railroads change WHO lived on western land?', a:'They drew settlers/immigrants west onto land taken from American Indians.' },
    { from:'US.01', q:'Define “Manifest Destiny” in one sentence.', a:'The belief the U.S. was destined to expand across the continent.' },
  ]},
  'US.03': { prompts: [
    { from:'US.02', q:'What was the main effect of the Dawes Act on tribal land?', a:'It broke up communal land into allotments, causing massive Native land loss.' },
    { from:'US.01', q:'What does “reservation” mean?', a:'Land set aside by the federal government for American Indian tribes.' },
  ]},
  'US.04': { prompts: [
    { from:'US.03', q:'What ended Reconstruction, and what replaced Black voting rights in the South?', a:'The Compromise of 1877; Jim Crow laws and disenfranchisement replaced those rights.' },
    { from:'US.03', q:'What did the Supreme Court decide in Plessy v. Ferguson?', a:'It upheld “separate but equal,” legalizing segregation.' },
  ]},
  'US.05': { prompts: [
    { from:'US.04', q:'What was a political machine, and how did bosses like Tweed stay in power?', a:'A party organization that traded jobs/services for votes, often through corruption.' },
    { from:'US.04', q:'What problem did the Pendleton Act fix?', a:'It ended the spoils system’s forced political contributions; created merit hiring.' },
  ]},
  'US.06': { prompts: [
    { from:'US.05', q:'Explain vertical vs. horizontal integration in one sentence each.', a:'Vertical: control all production stages. Horizontal: buy out competitors in the same industry.' },
    { from:'US.05', q:'What was Carnegie’s “Gospel of Wealth”?', a:'The idea the rich should live modestly and give surplus wealth to benefit society.' },
  ]},
  'US.07': { prompts: [
    { from:'US.06', q:'Why did cities grow so fast during industrialization?', a:'Factory jobs drew rural Americans and immigrants into urban centers (urbanization).' },
    { from:'US.06', q:'What was a tenement?', a:'A crowded, often unsafe urban apartment building housing poor and immigrant families.' },
  ]},
};

// Per-standard exit tickets with DOK variety (replaces the identical 7x prompt).
// Each entry now carries a CORE prompt (the on-slide exit ticket, DOK 2–3) AND an
// `honors` DOK 3 extension (TCAP #2) for students who finish early or need more
// rigor — surfaced on the wrap-up slide as an optional “Honors / Extension” box and
// keyed to argumentation (SSP.04). Keeps every standard offering a DOK 3 path.
const EXIT = {
  'US.01': { dok:'DOK 2', q:'Explain ONE way the Homestead Act or the railroad helped settlers AND ONE way it harmed American Indians.', model:'E.g., free 160-acre claims/rail access drew settlers; the same land was taken from American Indian nations, who were pushed onto reservations.', honors:'Argue: was westward expansion mainly “opportunity” or mainly “dispossession”? Defend your claim with TWO specific pieces of evidence.' },
  'US.02': { dok:'DOK 3', q:'A policy can claim one goal but cause another. Using the Dawes Act, give the stated goal and one real consequence.', model:'Stated: “assimilate”/“civilize” Native peoples; consequence: communal land broken into allotments → massive Native land loss.', honors:'Evaluate: did assimilation policy and the Dawes Act share the same underlying assumption about Native cultures? Support with evidence from both.' },
  'US.03': { dok:'DOK 3', q:'Rights can exist on paper but be denied in practice. Name one tool used to deny Black Americans rights after 1877 and explain how it worked.', model:'E.g., poll taxes/literacy tests disenfranchised voters; Jim Crow laws + Plessy legalized segregation despite the 14th/15th Amendments.', honors:'Construct an argument: which did MORE to undo Reconstruction — legal tools (Plessy, Jim Crow laws) or extralegal force (violence, intimidation)? Cite evidence.' },
  'US.04': { dok:'DOK 2', q:'Why might poor city residents SUPPORT a corrupt political machine? Give one reason and one cost of that support.', model:'Reason: machines gave jobs, food, services to immigrants; cost: graft, higher taxes, corrupt government (e.g., Tweed).', honors:'Argue: were political machines a net good or a net harm for new immigrants? Take a position and weigh services against costs with evidence.' },
  'US.05': { dok:'DOK 3', q:'Was a figure like Rockefeller a “robber baron” or a “captain of industry”? Take a position and cite ONE piece of evidence.', model:'Either defensible: robber baron (crushed competitors, low wages) OR captain of industry (efficiency, cheaper goods, philanthropy). Must cite evidence.', honors:'Evaluate the “Gospel of Wealth”: does large-scale philanthropy justify how the fortune was earned? Defend your judgment with evidence.' },
  'US.06': { dok:'DOK 2', q:'Explain ONE cause of rapid urbanization AND ONE problem it created in cities.', model:'Cause: factory jobs drew rural + immigrant workers; problem: overcrowded tenements, disease, strained sanitation.', honors:'Argue: who bore the greatest cost of rapid urbanization — immigrants, workers, or city governments? Defend with TWO pieces of evidence.' },
  'US.07': { dok:'DOK 3', q:'Compare a PUSH factor for a “new” immigrant with a reason native-born Americans reacted with nativism. Which surprises you more and why?', model:'Push: poverty/persecution in S./E. Europe or Asia; nativism: job competition + prejudice (e.g., Chinese Exclusion Act). Reasoning required.', honors:'Construct an argument: was the Chinese Exclusion Act an economic policy or a racial one? Use specific evidence to defend your claim.' },
};

// ---------------------------------------------------------------------------
// v3.2 RIGOR + ELL SCAFFOLDS
// ---------------------------------------------------------------------------
// TCAP #1 — per-standard DOK 1 "Confidence Check" warm-up. A low-floor recall
// item run AFTER the Quick Review and BEFORE direct instruction, so the check
// sequence ramps DOK 1 (here) -> DOK 2/3 (the graded check). Rosenshine P3/P7
// (ask questions, secure a high success rate before new material).
const WARMUP = {
  'US.01': { q:'TRUE or FALSE: The Homestead Act offered free public land to settlers who farmed it.', a:'TRUE — 160 acres after five years of living on and improving the claim.', term:'Homestead Act' },
  'US.02': { q:'In one word: what kind of school tried to erase Native languages and culture?', a:'A boarding (assimilation) school — e.g., Carlisle.', term:'assimilation' },
  'US.03': { q:'Finish the phrase: the 1896 Supreme Court rule was "separate but _____" (one word).', a:'"equal" — Plessy v. Ferguson legalized segregation.', term:'segregation' },
  'US.04': { q:'What do we call a party organization that traded jobs and favors for votes?', a:'A political machine (e.g., Tammany Hall under Boss Tweed).', term:'political machine' },
  'US.05': { q:'Owning every step from raw material to finished product is called ____ integration.', a:'Vertical integration (Carnegie in steel).', term:'vertical integration' },
  'US.06': { q:'What word means the fast growth of cities as people move in?', a:'Urbanization.', term:'urbanization' },
  'US.07': { q:'TRUE or FALSE: “New” immigrants (1880–1920) came mostly from southern & eastern Europe.', a:'TRUE — plus Asia; “old” immigrants came earlier from N./W. Europe.', term:'new immigrants' },
};

// ELL #1 — pronunciation guides for the hardest multisyllabic / proper-noun terms.
// Syllable breaks + stressed syllable in CAPS (a print-friendly respelling, not IPA,
// so any teacher or newcomer EL can decode it aloud). Keyed by the exact vocab term.
const PRONOUNCE = {
  'Homestead Act':'HOHM-sted', 'transcontinental railroad':'tranz-kon-tih-NEN-tul RAYL-rohd',
  'manifest destiny':'MAN-ih-fest DES-tih-nee', 'westward expansion':'WEST-werd ek-SPAN-shun',
  'land grant':'LAND grant',
  'assimilation':'uh-sim-ih-LAY-shun', 'reservation':'rez-er-VAY-shun',
  'Dawes Act':'DAWZ', 'segregation':'seg-rih-GAY-shun',
  'disenfranchisement':'dis-en-FRAN-chyz-ment', 'sharecropping':'SHAIR-krop-ing',
  'political machine':'puh-LIT-ih-kul muh-SHEEN', 'patronage':'PAY-truh-nij',
  'vertical integration':'VUR-tih-kul in-teh-GRAY-shun', 'monopoly':'muh-NOP-uh-lee',
  'philanthropy':'fih-LAN-thruh-pee', 'urbanization':'ur-bun-ih-ZAY-shun',
  'tenement':'TEN-uh-ment', 'nativism':'NAY-tiv-iz-um',
  'immigration':'im-ih-GRAY-shun',
};

// ELL #2 — second-modality picture cue (a single Unicode pictograph) per vocab term.
// ELL #3 — a content-specific sentence frame per standard, surfaced on the first DI
// slide so EL + striving writers have an academic-language scaffold for note-taking
// (WIDA writing support; Rosenshine P8 scaffolds). The ___ blanks cue the key idea.
const SENTENCE_FRAME = {
  'US.01':'The Homestead Act and the railroad ________ western settlement because ________.',
  'US.02':'Federal Indian policy claimed to ________, but in practice it ________.',
  'US.03':'After Reconstruction ended, Black Americans lost rights because ________ was used to ________.',
  'US.04':'A political machine stayed in power by ________, which helped ________ but harmed ________.',
  'US.05':'________ used ________ integration to dominate the ________ industry.',
  'US.06':'Cities grew rapidly because ________, which created the problem of ________.',
  'US.07':'“New” immigrants came to the U.S. because ________, but some native-born Americans reacted with ________.',
};

// custom hooks per standard
const HOOKS = {
  'US.01': ['160 acres of land — free — to almost anyone willing to farm it for five years.','If the government offered you free land out West in 1862, would you go? What would you have to give up — and who already lived there?'],
  'US.02': ['"Kill the Indian in him, and save the man."\n— Capt. Richard H. Pratt, 1892','What does it mean for a government to try to erase a culture? As you read today, watch for the difference between what these policies claimed to do and what they actually did — and use the evidence to judge for yourself.'],
  'US.03': ['In 1877, the last federal troops left the South. Within 20 years, segregation was the law of the land.','How can rights that were written into the Constitution be taken away in practice? Predict: what tools might a government use to deny rights without changing the Constitution?'],
  'US.04': ['One New York political boss stole an estimated $200 million — and almost no one stopped him.','Why might city residents support a corrupt political machine? What might they get in return? List two possibilities.'],
  'US.05': ['One man controlled 90% of all the oil refined in the United States.','Is it possible to be both a "robber baron" and a "captain of industry" at the same time? Hold that question as we meet the people who built modern America.'],
  'US.06': ['Chicago went from 30,000 people to over 1,000,000 in just 40 years.','What does a city need to grow that fast — and what problems would explode along with the population? Brainstorm three of each.'],
  'US.07': ['Between 1880 and 1920, more than 20 million immigrants arrived in the United States.','Why do people leave everything behind to start over in a new country? And why might native-born Americans react with fear? We will see both sides today.'],
};

// Optional data chart beside the hook, keyed by standard. Real figures, cited on-slide.
const HOOK_CHART = {
  'US.05': {
    data: [{ name:'U.S. oil refining', labels:['Standard Oil','All other refiners'], values:[90, 10] }],
    big: '90%',
    title: "ONE FIRM'S GRIP — U.S. oil refining, c. 1880",
    source: 'Standard Oil controlled ≈90% of U.S. refining capacity, c.1880. Est. from Tarbell, History of the Standard Oil Co. (1904) & Chernow, Titan (1998).',
  },
};

// Standards that get a native concept-visual slide after direct instruction.
const CONCEPT_VISUAL = { 'US.05': true };   // vertical vs. horizontal integration

// Per-SECTION hero image, keyed "CODE:sectionIndex" so the image matches the
// section topic (not just sec0/sec1). Only sections with a strong topical match
// get an image; others render text-only.
const SECTION_IMG = {
  // US.01 Westward expansion
  'US.01:0': 'transcontinental-railroad-ceremony', // Sequence expansion -> Golden Spike 1869
  'US.01:1': 'railroad-map-1890',                  // Western Settlement -> 1890 rail network
  // US.02 American Indian policy
  'US.02:1': 'tom-torlino-carlisle',               // Assimilation & Boarding Schools -> Tom Torlino
  // US.03 End of Reconstruction
  'US.03:0': 'freedmens-bureau-1868',              // End of Reconstruction -> Freedmen's Bureau
  'US.03:1': 'nast-worse-than-slavery',            // Jim Crow / lynching -> Nast "Worse than Slavery"
  // US.04 Gilded Age politics
  'US.04:0': 'bosses-of-the-senate',               // Political machines / trusts -> Bosses of the Senate
  // US.05 Industrialization
  'US.05:1': 'andrew-carnegie-portrait',           // Industrial Titans -> Carnegie
  'US.05:2': 'madam-cj-walker',                    // African American Entrepreneurs -> Madam C.J. Walker
  // US.06 Urbanization
  'US.06:0': 'map-wage-earners-1890',              // Major Industrial Centers -> manufactures map
  'US.06:2': 'map-foreign-born-1890',              // Geographic factors -> foreign-born diagram
  // US.07 Immigration
  'US.07:0': 'ellis-island-immigrants',            // Old & New Immigrants -> Ellis Island inspection
};
// Image to attach to each primary-source slide. Chosen to match the source
// being analyzed and to avoid duplicating that standard's section hero.
const PS_IMAGE = {
  'US.01': 'rawding-sod-house',            // Homestead Act -> homestead family on the Plains
  'US.02': null,                            // Dawes Act = statute text itself; Tom Torlino already anchors the assimilation instruction slide -> clean text-focused statute analysis (avoids duplicate image)
  'US.03': 'radical-members-sc-legislature',// Plessy era -> SC Reconstruction legislators
  'US.04': null,                            // Pendleton Act = statute text itself; no period-accurate civil-service image in asset set (Standard Oil octopus is a 1904 monopoly cartoon, not spoils-system) -> clean text-focused statute analysis
  'US.05': 'standard-oil-octopus',         // Gospel of Wealth / industrial titans -> Standard Oil monopoly (period-accurate for trusts theme)
  'US.06': 'five-cents-a-spot-riis',       // How the Other Half Lives -> Riis tenement photo
  'US.07': null,                            // Chinese Exclusion Act = statute text itself; Ellis Island photo is European-immigrant subject (wrong for Chinese exclusion) and already used on the instruction slide -> clean text-focused statute analysis
};
// Image to feature on the activity slide (varied from that standard's other images).
const ACT_IMAGE = {
  'US.01': 'railroad-map-1890',
  'US.03': 'radical-members-sc-legislature',
  'US.04': 'bosses-of-the-senate',
  'US.05': 'andrew-carnegie-portrait',
  'US.06': 'map-wage-earners-1890',
  'US.07': 'five-cents-a-spot-riis',
};

// BUILD ALL STANDARDS
Object.entries(D).forEach(([code,v])=>{
  standardDivider(code, v);
  if(REVIEW[code]){ reviewSlide(code, REVIEW[code]); reviewRevealSlide(code, REVIEW[code]); }
  // DOK 1 confidence-check warm-up ramps the check sequence before DI (TCAP #1)
  if(WARMUP[code]) confidenceCheckSlide(code, WARMUP[code]);
  const hk = HOOKS[code];
  hookSlide(code, v, hk[0], hk[1]);
  // direct instruction with imagery on topically matched sections
  v.sections.forEach((sec,i)=>{
    let hero = null;
    const key = `${code}:${i}`;
    if(SECTION_IMG[key]) hero = imgById(SECTION_IMG[key]);
    contentSlide(code, v, sec, i, v.sections.length, hero);
  });
  // optional concept visual (native diagram) after the direct-instruction sequence
  if(typeof CONCEPT_VISUAL !== 'undefined' && CONCEPT_VISUAL[code]) integrationDiagramSlide(code);
  if(v.bios && v.bios.length) bioSlide(code, v.bios);
  if(v.primarySources && v.primarySources[0]){
    const ps = v.primarySources[0];
    ps._image = PS_IMAGE[code];
    ps._sourceItFirst = v.sourceItFirst || null;
    primarySourceSlide(code, ps);
  }
  if(v.vocab && v.vocab.length) vocabSlide(code, v);
  // guided practice (We Do) bridges direct instruction and the independent activity
  if(v.weDo) weDoSlide(code, v.weDo);
  // student activity (on-slide + paired printable)
  if(ACTS[code]) activitySlide(code, ACTS[code], imgById(ACT_IMAGE[code]));
  // TCAP check: question slide -> click/advance -> reveal (answer key) slide
  if(v.primarySources && v.primarySources[0]){
    // The graded Check-for-Understanding uses the HIGHEST-DOK question item available
    // for the standard (EOC analysis simulation). The DOK 1 recall item still runs as
    // the separate Confidence-Check warm-up, so foundational standards no longer cap
    // their graded check at DOK 1.
    const dokNum = q => parseInt(((q && q.dokLevel) || 'DOK 1').replace(/[^0-9]/g,''),10) || 1;
    const checkPs = v.primarySources
      .filter(q => q && q.options && q.options.length)
      .sort((a,b)=> dokNum(b)-dokNum(a))[0] || v.primarySources[0];
    checkQuestionSlide(code, checkPs);
    checkRevealSlide(code, checkPs);
  }
  summarySlide(code, v);
});

// ===================================================================
// CLOSING
// ===================================================================
(function closing(){
  const s = pptx.addSlide();
  s.background = { color: NAVY };
  s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:W, h:0.16, fill:{color:GOLD} });
  s.addShape(pptx.ShapeType.rect, { x:0, y:H-0.16, w:W, h:0.16, fill:{color:RED} });
  s.addText('Unit 1 Complete', { x:0.9, y:1.6, w:11.5, h:1.0, fontFace:HEAD, fontSize:48, color:WHITE, bold:true });
  s.addText('The Rise of Industrialization (1877–1900) — from the open frontier to the crowded city: westward expansion, the Gilded Age, and a nation remade by immigration.',
    { x:0.9, y:2.8, w:11.5, h:1.1, fontFace:HEAD, fontSize:21, color:GOLDBR, italic:true, lineSpacingMultiple:1.1 });
  s.addText([
    {text:'Revisit your unit hook: ', options:{bold:true, color:WHITE}},
    {text:'What forces moved a nation off the land and into the factory? You can now answer with evidence — from the Homestead Act to the Chinese Exclusion Act.', options:{color:SLATEL}}
  ], { x:0.9, y:3.9, w:11.5, h:1.2, fontFace:BODY, fontSize:16, valign:'top', lineSpacingMultiple:1.15 });
  s.addText('Next: Unit 2 — Progressivism & American Imperialism', { x:0.9, y:5.4, w:11.5, h:0.5, fontFace:LABEL, fontSize:14, color:GOLDBR, charSpacing:1, bold:true });
  s.addText('U.S. History Hack  ·  TroopToTeacher Technologies LLC  ·  All primary sources verified against National Archives, Library of Congress, and U.S. Senate records. All images public domain.',
    { x:0.9, y:6.5, w:11.6, h:0.5, fontFace:BODY, fontSize:10, color:MUTE, valign:'middle' });
})();

pptx.writeFile({ fileName: OUT_FILE }).then(f=>{
  console.log('WROTE', f, 'pages(content):', page);
});
