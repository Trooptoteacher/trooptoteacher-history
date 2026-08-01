const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType,
  LevelFormat, PositionalTab, PositionalTabAlignment, PositionalTabLeader,
} = require("docx");
const fs = require("fs");

const NAVY = "1F3A5F";
const GREY = "444444";
const LIGHT = "F2F5F8";
const RULE = "C9D3DD";

function runs(text, opts = {}) { return new TextRun({ text, ...opts }); }

// ---- reusable builders -------------------------------------------------
function bodyPara(children, opts = {}) {
  return new Paragraph({ spacing: { after: 160, line: 276 }, children, ...opts });
}
function sectionHead(text) {
  return new Paragraph({
    spacing: { before: 200, after: 100 },
    children: [runs(text, { bold: true, size: 24, color: NAVY })],
  });
}
function bullet(children) {
  return new Paragraph({ numbering: { reference: "b", level: 0 }, spacing: { after: 90, line: 268 }, children });
}

// ---- meta row (label: value) ------------------------------------------
function metaLine(label, value) {
  return new Paragraph({
    spacing: { after: 40 },
    children: [runs(label + "  ", { bold: true, size: 19, color: NAVY }), runs(value, { size: 19, color: "222222" })],
  });
}

// ---- two-column role table --------------------------------------------
function cell(text, { header = false, w } = {}) {
  return new TableCell({
    width: { size: w, type: WidthType.DXA },
    shading: header ? { type: ShadingType.CLEAR, fill: NAVY, color: "auto" } : { type: ShadingType.CLEAR, fill: "FFFFFF", color: "auto" },
    margins: { top: 80, bottom: 80, left: 120, right: 120 },
    children: [new Paragraph({ children: Array.isArray(text) ? text : [runs(text, { size: 19, bold: header, color: header ? "FFFFFF" : "222222" })] })],
  });
}
const TW = 9360, C1 = 2600, C2 = TW - C1;
function roleTable() {
  const border = { style: BorderStyle.SINGLE, size: 4, color: RULE };
  const borders = { top: border, bottom: border, left: border, right: border, insideHorizontal: border, insideVertical: border };
  return new Table({
    width: { size: TW, type: WidthType.DXA },
    columnWidths: [C1, C2],
    borders,
    rows: [
      new TableRow({ tableHeader: true, children: [cell("Tool", { header: true, w: C1 }), cell("What it was actually used for", { header: true, w: C2 })] }),
      new TableRow({ children: [
        cell([runs("Anthropic Claude", { bold: true, size: 19 }), runs(" (large language model)", { size: 18, color: GREY })], { w: C1 }),
        cell([runs("Drafting ", { size: 19 }), runs("text", { bold: true, size: 19 }), runs(" — instructional content and quiz questions.", { size: 19 })], { w: C2 }),
      ] }),
      new TableRow({ children: [
        cell([runs("OpenAI image-", { bold: true, size: 19 }), runs("generation model", { bold: true, size: 19 })], { w: C1 }),
        cell([runs("Producing ", { size: 19 }), runs("illustrations only", { bold: true, size: 19 }), runs(" — printed workbook cover art, the narrative-story characters “C-Q130” and “CORE,” the in-app avatar images, and decorative icons.", { size: 19 })], { w: C2 }),
      ] }),
    ],
  });
}

// ---- document ----------------------------------------------------------
const children = [];

// Letterhead
children.push(new Paragraph({ spacing: { after: 20 }, children: [runs("TroopToTeacher Technologies, LLC", { bold: true, size: 26, color: NAVY })] }));
children.push(new Paragraph({
  border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: NAVY, space: 6 } },
  spacing: { after: 200 },
  children: [runs("U.S. History Hack · U.S. History for Tennessee High Schools", { size: 18, color: GREY })],
}));

// Title
children.push(new Paragraph({
  spacing: { after: 60 },
  children: [runs("Correction Notice — AI-Tool Disclosure in U.S. History Hack Compliance Materials", { bold: true, size: 28, color: "222222" })],
}));
children.push(new Paragraph({
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 6 } },
  spacing: { after: 200 },
  children: [runs("", { size: 4 })],
}));

// Meta block
children.push(metaLine("From:", "Sean Reynolds, TroopToTeacher Technologies, LLC"));
children.push(metaLine("Contact:", "sean.reynolds@trooptoteacher.com"));
children.push(metaLine("Date:", "July 31, 2026"));
children.push(new Paragraph({
  spacing: { after: 200 },
  children: [
    runs("Re:  ", { bold: true, size: 19, color: NAVY }),
    runs("Correction to how two AI authoring tools were described in previously shared compliance documents (AI Disclosure, Privacy Policy, Terms of Service, Data Processing Agreement, FERPA / Student-Data-Privacy Statement, and the Tennessee Compliance Matrix).", { size: 19, color: "222222" }),
  ],
}));

// Summary
children.push(sectionHead("Summary"));
children.push(bodyPara([
  runs("In materials already shared with the district, our AI disclosures grouped two authoring-time AI tools — ", { size: 20 }),
  runs("Anthropic Claude", { size: 20, bold: true }),
  runs(" and an ", { size: 20 }),
  runs("OpenAI", { size: 20, bold: true }),
  runs(" model — together, which implied both were used to generate written content. That was imprecise. This notice states the correct division of use. ", { size: 20 }),
  runs("No underlying practice changed", { size: 20, bold: true }),
  runs(" — only the description of which tool did what. We are sending this proactively in the interest of full transparency.", { size: 20 }),
]));

// What the documents said
children.push(sectionHead("What the documents said"));
children.push(bodyPara([
  runs("Earlier versions described “third-party large language models (Anthropic Claude and OpenAI)” as authoring-time tools used to help draft content, without distinguishing their roles.", { size: 20 }),
]));

// What is accurate
children.push(sectionHead("What is accurate"));
children.push(roleTable());
children.push(new Paragraph({ spacing: { before: 140, after: 160, line: 276 }, children: [
  runs("Every AI-assisted item — text and image alike — was reviewed, fact-checked, and approved by a qualified human educator before inclusion.", { size: 20 }),
] }));

// What did NOT change
children.push(sectionHead("What did not change"));
children.push(bullet([runs("No AI runs at runtime.", { size: 20, bold: true }), runs(" Students never interact with a language model or any AI system. All questions, feedback, definitions, hints, and adaptive logic are static, pre-authored, and deterministic (rule-based) — not machine-learning or LLM-driven.", { size: 20 })]));
children.push(bullet([runs("No student data is ever sent to any AI tool", { size: 20, bold: true }), runs(" — not to Anthropic, not to OpenAI, not to any other AI provider, at any time. Both tools were used only at authoring time, on public / non-PII inputs.", { size: 20 })]));
children.push(bullet([runs("No image depicts a named or real person.", { size: 20, bold: true }), runs(" All AI-generated imagery is fictional or generic.", { size: 20 })]));

// Avatars paused
children.push(sectionHead("Additional step we have taken (AI-generated avatars paused)"));
children.push(bodyPara([
  runs("Out of an abundance of caution, the in-app ", { size: 20 }),
  runs("AI-generated avatar images are currently paused / hidden", { size: 20, bold: true }),
  runs(" in the product pending completion of an internal AI-provenance and copyright review. Students and all other users cannot see or select them while paused. This is reversible; we will not re-enable them until that review is complete. Provenance for each AI-generated image (tool, and — once confirmed from our archive — model version, prompts, and generation dates) is being recorded internally.", { size: 20 }),
]));

// Corrected documents
children.push(sectionHead("Corrected documents"));
children.push(bodyPara([runs("We have corrected the description across all affected materials and can re-share updated copies on request:", { size: 20 })], { spacing: { after: 90, line: 276 } }));
[
  "Public AI Disclosure page (English and Spanish)",
  "Privacy Policy",
  "Terms of Service",
  "Data Processing Agreement (sub-processor list)",
  "FERPA / Tennessee Student-Data-Privacy Statement",
  "Tennessee State Law Compliance Matrix (AI-in-instruction row)",
].forEach((t) => children.push(bullet([runs(t, { size: 20 })])));

children.push(new Paragraph({ spacing: { before: 160, after: 160, line: 276 }, children: [
  runs("If it would be helpful, we are glad to walk through any of these with your technology or curriculum team.", { size: 20 }),
] }));

// Signature
children.push(new Paragraph({ spacing: { before: 200, after: 40 }, children: [runs("Respectfully,", { size: 20 })] }));
children.push(new Paragraph({ spacing: { after: 0 }, children: [runs("Sean Reynolds", { size: 20, bold: true, color: NAVY })] }));
children.push(new Paragraph({ spacing: { after: 0 }, children: [runs("TroopToTeacher Technologies, LLC", { size: 19, color: "222222" })] }));
children.push(new Paragraph({ spacing: { after: 200 }, children: [runs("sean.reynolds@trooptoteacher.com", { size: 19, color: "222222" })] }));

// Disclaimer footer
children.push(new Paragraph({
  border: { top: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 6 } },
  spacing: { before: 120 },
  children: [runs("This notice is provided for transparency and does not constitute legal advice.", { italics: true, size: 17, color: GREY })],
}));

const doc = new Document({
  numbering: {
    config: [{
      reference: "b",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { run: { color: NAVY }, paragraph: { indent: { left: 360, hanging: 220 } } } }],
    }],
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, bottom: 1080, left: 1440, right: 1440 } } },
    children,
  }],
});

const out = "/tmp/claude-0/-home-user-trooptoteacher-history/c27aff16-3c79-5004-bf4a-470896c27424/scratchpad/District-AI-Disclosure-Correction-Notice.docx";
Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(out, buf); console.log("WROTE " + out + " (" + buf.length + " bytes)"); });
