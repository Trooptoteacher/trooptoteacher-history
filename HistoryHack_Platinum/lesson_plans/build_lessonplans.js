/*
 * U.S. History Hack — TEAM-Aligned Lesson Plan Generator
 * TroopToTeacher Technologies, LLC
 *
 * Deterministic, print-first generator. Reads a unit content JSON
 * (the same file that drives the Course Standard workbook) and emits one
 * TEAM-aligned lesson plan (DOCX) per standard, plus a combined unit binder.
 * No per-run variance: same input -> byte-identical structure every time.
 *
 * Usage:
 *   node build_lessonplans.js <unit_content.json> <out_dir> [--minutes=47] [--unit="Unit 1"]
 *
 * Every fact in a plan is pulled from the unit content data (standard text,
 * I-CAN, criteria, vocabulary, primary sources, check-for-understanding,
 * Tennessee connection). Pedagogy scaffolding (differentiation, environment,
 * reflection) is constant TEAM structure; nothing subject-specific is invented.
 */
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, Header, Footer,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType,
  LevelFormat, PageNumber, PageBreak,
} = require("docx");
const fs = require("fs");
const path = require("path");

const NAVY = "1F3A5F", GREY = "555555", RULE = "C9D3DD", LIGHT = "EEF2F6", ACCENT = "7A1F2B";
const R = (text, o = {}) => new TextRun({ text, ...o });
const COPYRIGHT = "© 2026 TroopToTeacher Technologies, LLC · U.S. History Hack™ · All rights reserved.";

// ---------- args ----------
const argv = process.argv.slice(2);
const positional = argv.filter(a => !a.startsWith("--"));
const flags = Object.fromEntries(argv.filter(a => a.startsWith("--")).map(a => {
  const [k, v] = a.replace(/^--/, "").split("="); return [k, v === undefined ? true : v];
}));
const CONTENT_PATH = positional[0];
const OUT_DIR = positional[1];
if (!CONTENT_PATH || !OUT_DIR) { console.error("Usage: node build_lessonplans.js <unit_content.json> <out_dir> [--minutes=47] [--unit=\"Unit 1\"]"); process.exit(1); }
const MINUTES = parseInt(flags.minutes || "47", 10);
fs.mkdirSync(OUT_DIR, { recursive: true });

const data = JSON.parse(fs.readFileSync(CONTENT_PATH, "utf8"));
const ORDER = data.order || Object.keys(data.standards);
const UNIT_LABEL = flags.unit || "Unit 1";

// ---------- pacing model (segments scale to the block length) ----------
// weights sum to 1.0; minutes are rounded and the largest segment absorbs rounding
function pacing(total) {
  const segs = [
    { w: 0.106, seg: (ctx) => `Warm-Up / Bell-Ringer — ${ctx.warm}; frame today's question`, mat: "Guided Notes (Do-Now box)" },
    { w: 0.085, seg: (ctx) => `Hook — ${ctx.hook}`, mat: "Teacher Deck" },
    { w: 0.255, seg: () => "Direct Instruction — teacher models close reading of the core content; students capture guided notes", mat: "Teacher Deck + Guided Notes" },
    { w: 0.213, seg: () => "Guided Practice — Cornell Notes + a comparison/analysis organizer", mat: "Cornell Notes · organizer" },
    { w: 0.234, seg: () => "Primary Source / HIPP — analyze the source; begin CER", mat: "Primary-Source Packet · HIPP · CER organizer" },
    { w: 0.107, seg: (ctx) => `Exit Ticket & Closure — 2-question check; ${ctx.preview}`, mat: "Exit Ticket (EN/ES)" },
  ];
  let mins = segs.map(s => Math.max(3, Math.round(s.w * total)));
  const diff = total - mins.reduce((a, c) => a + c, 0);
  const biggest = mins.indexOf(Math.max(...mins));
  mins[biggest] += diff; // absorb rounding so segments sum exactly to the block
  return segs.map((s, i) => ({ min: mins[i], ...s }));
}

// ---------- helpers ----------
function head(text) {
  return new Paragraph({
    spacing: { before: 220, after: 90 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 4 } },
    children: [R(text, { bold: true, size: 22, color: NAVY })],
  });
}
const body = (children, o = {}) => new Paragraph({ spacing: { after: 120, line: 264 }, children, ...o });
const bullet = (children) => new Paragraph({ numbering: { reference: "b", level: 0 }, spacing: { after: 70, line: 258 }, children });
const kv = (label, value) => new Paragraph({ spacing: { after: 40 }, children: [R(label + "  ", { bold: true, size: 18, color: NAVY }), R(value, { size: 18, color: "222222" })] });
function tcell(content, { w, header = false, fill } = {}) {
  const kids = Array.isArray(content) ? content : [new Paragraph({ children: [R(String(content), { size: 17, bold: header, color: header ? "FFFFFF" : "222222" })] })];
  return new TableCell({
    width: { size: w, type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, color: "auto", fill: header ? NAVY : (fill || "FFFFFF") },
    margins: { top: 60, bottom: 60, left: 100, right: 100 }, children: kids,
  });
}
function table(colWidths, rows) {
  const b = { style: BorderStyle.SINGLE, size: 4, color: RULE };
  return new Table({
    width: { size: colWidths.reduce((a, c) => a + c, 0), type: WidthType.DXA }, columnWidths: colWidths,
    borders: { top: b, bottom: b, left: b, right: b, insideHorizontal: b, insideVertical: b }, rows,
  });
}
const cellP = (runs) => new Paragraph({ children: runs });
const firstSentence = (s) => { if (!s) return ""; const m = String(s).match(/^[^.!?]*[.!?]/); return (m ? m[0] : String(s)).trim(); };
const stripTrailingPeriod = (s) => String(s || "").replace(/\.\s*$/, "");
const endPunct = (s) => { s = String(s || "").trim(); return /[.?!]$/.test(s) ? s : s + "."; };
const withThe = (t) => /^(the|a|an)\b/i.test(t) ? t : "the " + t;

// ---------- build one standard's plan (returns children[]) ----------
function buildPlan(code, s, idx) {
  const c = [];
  const prev = idx > 0 ? data.standards[ORDER[idx - 1]] : null;
  const next = idx < ORDER.length - 1 ? ORDER[idx + 1] : null;
  const vocab0 = (s.vocab && s.vocab[0]) ? s.vocab[0].term : null;
  const src0 = (s.sources && s.sources[0]) ? s.sources[0] : null;
  const criteria = (s.criteria && s.criteria.length) ? s.criteria : (s.targets || []);
  const stdText = s.tn || s.target || "";
  const essentialQ = (() => { const m = String(s.hook || "").match(/[^.?!]*\?\s*$/); return m ? m[0].trim() : "Who gained, who was left out — and why does it still matter?"; })();
  const tnShort = firstSentence(s.tn_connection);

  // ---- Title block ----
  c.push(new Paragraph({ spacing: { after: 20 }, children: [R("TEAM-Aligned Lesson Plan", { bold: true, size: 30, color: "222222" })] }));
  c.push(new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: NAVY, space: 6 } }, spacing: { after: 160 },
    children: [R("U.S. History (Grades 9–12) · Franklin High School · Williamson County Schools", { size: 18, color: GREY })],
  }));
  c.push(kv("Standard:", `${code} — ${s.title}`));
  c.push(kv("Schedule:", `Regular block — ${MINUTES} minutes   ·   Date: ______________   ·   Teacher: ______________`));
  c.push(new Paragraph({ spacing: { after: 120 }, children: [
    R("TN Standard (full text): ", { bold: true, size: 17, color: NAVY }),
    R(stdText, { size: 17, italics: true }),
  ] }));

  // ---- 1 Standards & Objectives ----
  c.push(head("1 · Standards & Objectives"));
  c.push(body([R("Learning objective (I-CAN): ", { bold: true, size: 18 }), R(`“${s.ican}”`, { size: 18 })]));
  c.push(body([R("Sub-objectives (sequenced from the standard's criteria):", { bold: true, size: 18 })], { spacing: { after: 60 } }));
  criteria.forEach(t => c.push(bullet([R(stripTrailingPeriod(t) + ".", { size: 17 })])));
  if (prev) c.push(body([R("Connection to prior learning: ", { bold: true, size: 17, color: NAVY }), R(`Builds on ${ORDER[idx - 1]} (${prev.title}) — students carry yesterday's understanding into today's standard.`, { size: 17 })]));
  else c.push(body([R("Connection to prior learning: ", { bold: true, size: 17, color: NAVY }), R("Opens the unit — activate prior knowledge from the prior course/unit and preview the arc ahead.", { size: 17 })]));
  if (tnShort) c.push(body([R("Tennessee connection: ", { bold: true, size: 17, color: ACCENT }), R(s.tn_connection, { size: 17 })]));

  // ---- 2 Assessment ----
  c.push(head("2 · Assessment & Evidence of Mastery"));
  c.push(body([R("Measured in multiple ways (TEAM: 3+ measures with clear criteria):", { bold: true, size: 17 })], { spacing: { after: 60 } }));
  c.push(bullet([R("Selected-response + short constructed: ", { bold: true, size: 17 }), R(`${code} Formative Assessment (with teacher answer key).`, { size: 17 })]));
  c.push(bullet([R("Extended writing: ", { bold: true, size: 17 }), R(`CER organizer — claim, evidence, reasoning on ${withThe(s.title)}.`, { size: 17 })]));
  c.push(bullet([R("Primary-source analysis: ", { bold: true, size: 17 }), R(`HIPP organizer on ${src0 ? `“${src0.title}” (${src0.who}${src0.date ? ", " + src0.date : ""})` : "a primary source"}.`, { size: 17 })]));
  c.push(bullet([R("Exit ticket (EN + ES): ", { bold: true, size: 17 }), R("2-question check for understanding, bilingual.", { size: 17 })]));
  c.push(body([R("Success criteria: ", { bold: true, size: 17, color: NAVY }), R(`Student cites at least two specific pieces of evidence and can ${s.target ? stripTrailingPeriod(s.target) : "explain the impact of the standard's content"}.`, { size: 17 })]));

  // ---- 3 Structure & Pacing ----
  c.push(head(`3 · Lesson Structure & Pacing (${MINUTES}-minute Regular block)`));
  const ctx = {
    warm: prev ? `recall ${prev.title} (${ORDER[idx - 1]})` : "activate prior knowledge",
    hook: tnShort ? `${stripTrailingPeriod(tnShort)}: ${essentialQ}` : essentialQ,
    preview: next ? `preview ${next}` : "preview the next unit",
  };
  const CW = [1300, 4700, 3360];
  const segRows = [new TableRow({ tableHeader: true, children: [tcell("Min", { w: CW[0], header: true }), tcell("Segment & what happens", { w: CW[1], header: true }), tcell("Material", { w: CW[2], header: true })] })];
  pacing(MINUTES).forEach((seg, i) => segRows.push(new TableRow({ children: [
    tcell(String(seg.min), { w: CW[0], fill: i % 2 ? LIGHT : "FFFFFF" }),
    tcell([cellP([R(seg.seg(ctx), { size: 16 })])], { w: CW[1], fill: i % 2 ? LIGHT : "FFFFFF" }),
    tcell([cellP([R(seg.mat, { size: 16 })])], { w: CW[2], fill: i % 2 ? LIGHT : "FFFFFF" }),
  ] })));
  c.push(table(CW, segRows));
  c.push(new Paragraph({ spacing: { before: 40 }, children: [R(`Total: ${MINUTES} minutes (segments sum-verified to the block length; auto-adjusts to 43-min Activities or 41-min Late-Start).`, { size: 15, italics: true, color: GREY })] }));

  // ---- 4 Activities & Materials ----
  c.push(head("4 · Activities & Materials (teacher-selected)"));
  const acts = [
    "Guided Notes — scaffolded direct-instruction capture",
    "Cornell Notes — cue/notes/summary for retention",
    "Comparison / analysis organizer — structure student thinking on the core content",
    `Primary-Source Packet + HIPP organizer — sourcing & analysis${src0 ? ` of “${src0.title}”` : ""}`,
    "CER organizer — evidence-based extended writing",
    "Formative Assessment + Exit Ticket (EN/ES) — checks for understanding",
  ];
  if (s.geo && String(s.geo).trim()) acts.splice(3, 0, "Geographer's Lens map task — locate and explain the places that shaped this standard");
  acts.forEach(t => c.push(bullet([R(t, { size: 17 })])));
  if (vocab0) c.push(body([R("Word Bank (key vocabulary): ", { bold: true, size: 16, color: NAVY }), R(s.vocab.map(v => v.term).join(" · "), { size: 16 })]));
  c.push(body([R("Complex text, student choice (organizer format), primary sources, and student-to-student discussion are built in — satisfying the TEAM Activities & Materials indicators.", { size: 16, italics: true, color: GREY })]));

  // ---- 5 Questioning ----
  c.push(head("5 · Questioning Plan (DOK ladder, text-based, cite evidence)"));
  const QW = [1500, 7560];
  const cfuStem = (s.cfu && s.cfu.stem) ? s.cfu.stem : `Analyze the most significant impact of ${withThe(s.title)}.`;
  const qLadder = [
    ["DOK 1", vocab0 ? `Define the key term “${vocab0}” and identify when it occurred.` : `Recall the key facts of ${withThe(s.title)}.`],
    ["DOK 2", `In your own words, summarize ${withThe(s.title)} and explain why it mattered.`],
    ["DOK 3", endPunct(cfuStem)],
    ["DOK 4", `Evaluate the long-term impact of ${withThe(s.title)} — support your claim with evidence from the source(s).`],
  ];
  const qRows = [new TableRow({ tableHeader: true, children: [tcell("Level", { w: QW[0], header: true }), tcell(`Example question (${code})`, { w: QW[1], header: true })] })];
  qLadder.forEach((r, i) => qRows.push(new TableRow({ children: [
    tcell(r[0], { w: QW[0], fill: (i + 1) % 2 ? LIGHT : "FFFFFF" }),
    tcell([cellP([R(r[1], { size: 16 })])], { w: QW[1], fill: (i + 1) % 2 ? LIGHT : "FFFFFF" }),
  ] })));
  c.push(table(QW, qRows));
  c.push(new Paragraph({ spacing: { before: 40 }, children: [R(`Anchored to the ${code} content and item bank (DOK 1–4). Majority of questions are text-based; students cite evidence. Teacher may swap in additional bank items.`, { size: 15, italics: true, color: GREY })] }));

  // ---- 6 Thinking ----
  c.push(head("6 · Thinking & Problem-Solving"));
  c.push(bullet([R("Analytical thinking: ", { bold: true, size: 17 }), R(`compare and contrast perspectives within ${withThe(s.title)}.`, { size: 17 })]));
  c.push(bullet([R("Research-based thinking: ", { bold: true, size: 17 }), R(`evaluate ${src0 ? `“${src0.title}” and related sources` : "the primary sources"}.`, { size: 17 })]));
  c.push(bullet([R("Problem-solving (drawing conclusions / justifying): ", { bold: true, size: 17 }), R("students build and defend a claim in the CER.", { size: 17 })]));

  // ---- 7 Grouping & Feedback ----
  c.push(head("7 · Grouping & Feedback  [teacher selects]"));
  c.push(bullet([R("Grouping: ", { bold: true, size: 17 }), R("pairs for the CER organizer; whole-class for the primary-source model; individual exit ticket.", { size: 17 })]));
  c.push(bullet([R("Feedback checkpoints: ", { bold: true, size: 17 }), R("circulate during Guided Practice and Primary-Source segments; use exit-ticket results to adjust tomorrow's opening.", { size: 17 })]));

  // ---- 8 Differentiation ----
  c.push(head("8 · Differentiation (Knowledge of Students)"));
  c.push(bullet([R("ELL / WIDA: ", { bold: true, size: 17 }), R("UDL/WIDA overlay + sentence frames; Spanish exit ticket for entering/emerging levels.", { size: 17 })]));
  c.push(bullet([R("IEP / 504: ", { bold: true, size: 17 }), R("chunked guided notes, extended time, read-aloud (browser TTS), reduced-item formative option.", { size: 17 })]));

  // ---- 9 Environment ----
  c.push(head("9 · Environment Reminders (teacher-implemented)"));
  c.push(body([R("A lesson plan supports — but cannot manufacture — the TEAM Environment domain. Reminders:", { size: 16, italics: true, color: GREY })], { spacing: { after: 60 } }));
  ["Set high expectations; frame content with dignity and historical accuracy.",
   "Establish discussion norms before the primary-source analysis.",
   "Display current student work; keep materials accessible for the pair activity."].forEach(t => c.push(bullet([R(t, { size: 17 })])));

  // ---- 10 Materials & Where to Print ----
  c.push(head("10 · Materials & Where to Print"));
  c.push(body([R("Included in today's print ZIP ", { bold: true, size: 17 }), R(`(${code} — print-ready PDF + editable DOCX):`, { size: 17 })], { spacing: { after: 60 } }));
  const MW = [4530, 4530];
  const mRows = [new TableRow({ tableHeader: true, children: [tcell("Student (print & copy)", { w: MW[0], header: true }), tcell("Teacher (your copy)", { w: MW[1], header: true })] })];
  [["Guided Notes", "Teacher Lesson Plan (this doc)"],
   ["Cornell Notes", "Formative Assessment — Answer Key"],
   ["Comparison / analysis organizer", "Primary-Source Teacher Guide"],
   ["CER organizer", "UDL / WIDA overlay"],
   ["HIPP organizer", "File Map & Print Guide"],
   ["Primary-Source Packet", ""],
   ["Formative Assessment", ""],
   ["Exit Ticket — English & Spanish", ""]].forEach((r, i) => mRows.push(new TableRow({ children: [
    tcell([cellP([R(r[0], { size: 16 })])], { w: MW[0], fill: i % 2 ? "FFFFFF" : LIGHT }),
    tcell([cellP([R(r[1], { size: 16, color: r[1] ? "222222" : "FFFFFF" })])], { w: MW[1], fill: i % 2 ? "FFFFFF" : LIGHT }),
  ] })));
  c.push(table(MW, mRows));
  c.push(new Paragraph({ spacing: { before: 100, after: 40 }, children: [R("Slides (download once for the unit):", { bold: true, size: 17, color: NAVY })] }));
  c.push(body([R(`${UNIT_LABEL} Teacher Deck — ${code} slides. Download from Teacher Tools → Lecture Decks → ${UNIT_LABEL}. (Decks are reused all unit, so they are not bundled in the daily ZIP.)`, { size: 16 })]));

  // ---- 11 Reflection & Next Steps ----
  c.push(head("11 · Reflection & Next Steps"));
  c.push(body([R("Teacher reflection (complete after teaching):", { bold: true, size: 17, color: NAVY })], { spacing: { after: 60 } }));
  ["Did students meet the I-CAN? Cite the evidence — exit-ticket % correct, CER quality.",
   "What worked, and what would I change next time?",
   "Which sub-objective still needs another touch tomorrow?"].forEach(t => c.push(bullet([R(t, { size: 17 })])));
  c.push(body([R("Extension / enrichment ", { bold: true, size: 17, color: NAVY }), R("(for students who mastered it):", { size: 17 })], { spacing: { before: 40, after: 60 } }));
  c.push(bullet([R(`Deeper source work: analyze a second primary source with the HIPP organizer.`, { size: 17 })]));
  if (next) c.push(bullet([R(`Connect forward: how does ${withThe(s.title)} set up ${next} (${data.standards[next].title})?`, { size: 17 })]));
  else c.push(bullet([R(`Connect forward: how does this standard set up the next unit?`, { size: 17 })]));
  c.push(body([R("If it's not working ", { bold: true, size: 17, color: ACCENT }), R("(reteach / intervention path):", { size: 17 })], { spacing: { before: 40, after: 60 } }));
  c.push(bullet([R("Below ~70% mastery on the exit ticket / formative → reteach with entry-tier materials (guided notes + a shorter source) in a small group — MTSS Tier 2.", { size: 17 })]));
  c.push(bullet([R(`One click — “Remediate ${code}”: `, { bold: true, size: 17 }), R("assembles a reteach pack (entry-tier worksheet, targeted DOK 1–2 questions, ELL/IEP supports) as a fresh print ZIP.", { size: 17 })]));
  c.push(bullet([R("Mid-lesson trouble: ", { bold: true, size: 17 }), R("if pacing slips, protect the 5-min Exit Ticket — it's tomorrow's data — and move the CER to homework or the next day.", { size: 17 })]));

  // ---- Appendix: TEAM mapping ----
  c.push(head("Appendix · How this plan maps to the TEAM rubric"));
  const AW = [3600, 5460];
  const aRows = [new TableRow({ tableHeader: true, children: [tcell("TEAM indicator", { w: AW[0], header: true }), tcell("Where addressed", { w: AW[1], header: true })] })];
  [["Standards & Objectives", "§1 — I-CAN + sequenced sub-objectives + prior learning"],
   ["Motivating Students", "§3 Hook — Tennessee relevance"],
   ["Presenting Content", "§3 DI — deck visuals + guided notes + modeling"],
   ["Lesson Structure & Pacing", `§3 — ${MINUTES}-min segmented, warm-up → closure`],
   ["Activities & Materials", "§4 — varied, choice, primary sources, complex text"],
   ["Questioning", "§5 — DOK 1–4 ladder, text-based, cite evidence"],
   ["Feedback", "§7 — checkpoints during guided practice"],
   ["Grouping", "§7 — pairs + whole-class + individual"],
   ["Teacher Content Knowledge", "§1/§4 — accurate, standards-aligned content"],
   ["Knowledge of Students", "§8 — UDL/WIDA + IEP/504"],
   ["Thinking / Problem-Solving", "§6 — analytical, research-based, justify a claim"],
   ["PLANNING: Instructional Plans", "Whole plan — sequenced, accommodations, closure"],
   ["PLANNING: Student Work", "§2 — CER + HIPP extended writing"],
   ["PLANNING: Assessment", "§2 — multiple measures + clear criteria"],
   ["Environment (3 indicators)", "§9 — reminders (teacher-implemented; not auto-generated)"],
  ].forEach((r, i) => aRows.push(new TableRow({ children: [
    tcell([cellP([R(r[0], { size: 15, bold: r[0].startsWith("PLANNING"), color: r[0].startsWith("PLANNING") ? ACCENT : "222222" })])], { w: AW[0], fill: i % 2 ? LIGHT : "FFFFFF" }),
    tcell([cellP([R(r[1], { size: 15 })])], { w: AW[1], fill: i % 2 ? LIGHT : "FFFFFF" }),
  ] })));
  c.push(table(AW, aRows));
  c.push(new Paragraph({ spacing: { before: 80 }, children: [R("The three PLANNING indicators (highlighted) are what a written plan is directly scored on — this template earns them structurally. The Instruction indicators are documented so the teacher walks in ready; the Environment domain is prompted, not generated.", { size: 15, italics: true, color: GREY })] }));

  return c;
}

// ---------- document wrapper ----------
function makeDoc(children, titleMeta, subjectMeta, headerRight) {
  return new Document({
    creator: "TroopToTeacher Technologies, LLC",
    title: titleMeta, subject: subjectMeta,
    description: COPYRIGHT + " Generated by U.S. History Hack. Not for redistribution.",
    keywords: `U.S. History Hack, TroopToTeacher, U.S. History, TEAM, lesson plan, ${UNIT_LABEL}, copyright 2026 TroopToTeacher Technologies LLC`,
    numbering: { config: [{ reference: "b", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { run: { color: NAVY }, paragraph: { indent: { left: 340, hanging: 200 } } } }] }] },
    sections: [{
      properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1000, bottom: 1080, left: 1080, right: 1080 } } },
      headers: { default: new Header({ children: [new Paragraph({
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 4 } },
        tabStops: [{ type: "right", position: 10080 }],
        children: [R("U.S. History Hack", { bold: true, size: 16, color: NAVY }), R("™", { size: 12, color: NAVY, superScript: true }), R("  ·  TEAM-Aligned Lesson Plan", { size: 16, color: GREY }), R(`\t${headerRight}`, { size: 15, color: GREY })],
      })] }) },
      footers: { default: new Footer({ children: [new Paragraph({
        border: { top: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 4 } },
        tabStops: [{ type: "right", position: 10080 }],
        children: [R(COPYRIGHT, { size: 13, color: GREY }), new TextRun({ children: ["\tPage ", PageNumber.CURRENT], size: 13, color: GREY })],
      })] }) },
      children,
    }],
  });
}

// ---------- run ----------
(async () => {
  const manifest = [];
  const binderChildren = [];
  for (let i = 0; i < ORDER.length; i++) {
    const code = ORDER[i];
    const s = data.standards[code];
    const plan = buildPlan(code, s, i);
    // individual doc
    const doc = makeDoc(plan, `${code} TEAM-Aligned Lesson Plan — U.S. History Hack`, `TEAM-Aligned Lesson Plan (${code})`, `${code} · U.S. History`);
    const fname = `${code.replace(".", "")}_TEAM_Lesson_Plan.docx`;
    const buf = await Packer.toBuffer(doc);
    fs.writeFileSync(path.join(OUT_DIR, fname), buf);
    manifest.push({ code, title: s.title, file: fname });
    console.log(`WROTE ${fname} (${buf.length} bytes)`);
    // binder: append with a page break between plans
    if (i > 0) binderChildren.push(new Paragraph({ children: [new PageBreak()] }));
    binderChildren.push(...plan);
  }
  const binder = makeDoc(binderChildren, `${UNIT_LABEL} — TEAM-Aligned Lesson Plans — U.S. History Hack`, `TEAM-Aligned Lesson Plans (${UNIT_LABEL})`, `${UNIT_LABEL} · U.S. History`);
  const binderBuf = await Packer.toBuffer(binder);
  const binderName = `${UNIT_LABEL.replace(/\s+/g, "")}_TEAM_Lesson_Plans_Binder.docx`;
  fs.writeFileSync(path.join(OUT_DIR, binderName), binderBuf);
  console.log(`WROTE ${binderName} (${binderBuf.length} bytes)`);
  fs.writeFileSync(path.join(OUT_DIR, "manifest.json"), JSON.stringify({ unit: UNIT_LABEL, minutes: MINUTES, plans: manifest, binder: binderName }, null, 2));
  console.log("DONE: " + manifest.length + " plans + binder");
})();
