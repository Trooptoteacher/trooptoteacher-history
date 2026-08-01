const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType,
  PageOrientation, PageBreak,
} = require("docx");
const fs = require("fs");

// ---- layout constants (landscape US Letter, 0.5in margins) ----
const USABLE = 14400; // 15840 - 2*720
const COLS = [4300, 5600, 1600, 2900]; // Requirement | How HH meets it | Status | Evidence
const GRAY = "D9D9D9";
const LIGHT = "F2F2F2";

const border = { style: BorderStyle.SINGLE, size: 4, color: "999999" };
const CELL_BORDERS = { top: border, bottom: border, left: border, right: border };

function runs(text, opts = {}) {
  return new TextRun({ text, size: opts.size || 17, bold: !!opts.bold, italics: !!opts.italics, color: opts.color });
}
function para(children, opts = {}) {
  return new Paragraph({
    children: Array.isArray(children) ? children : [children],
    spacing: { after: opts.after == null ? 40 : opts.after, before: opts.before || 0 },
    alignment: opts.align,
  });
}
// cell content: array of paragraph-specs. Each spec = {t, bold, bullet, italics, color}
function cell(specs, colIdx, opts = {}) {
  const paras = specs.map((s) => {
    if (typeof s === "string") s = { t: s };
    const children = [];
    if (s.bullet) children.push(runs("•  ", { size: 17 }));
    if (s.label) children.push(runs(s.label + " ", { bold: true, size: 17 }));
    children.push(runs(s.t, { bold: s.bold, italics: s.italics, color: s.color, size: 17 }));
    return new Paragraph({ children, spacing: { after: 40 }, indent: s.bullet ? { left: 150, hanging: 130 } : undefined });
  });
  return new TableCell({
    width: { size: COLS[colIdx], type: WidthType.DXA },
    borders: CELL_BORDERS,
    shading: opts.fill ? { type: ShadingType.CLEAR, fill: opts.fill, color: "auto" } : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    children: paras,
  });
}
function headerRow() {
  const mk = (t, i) => new TableCell({
    width: { size: COLS[i], type: WidthType.DXA },
    borders: CELL_BORDERS,
    shading: { type: ShadingType.CLEAR, fill: GRAY, color: "auto" },
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    children: [new Paragraph({ children: [runs(t, { bold: true, size: 18 })] })],
  });
  return new TableRow({
    tableHeader: true,
    children: ["Requirement & Citation", "How U.S. History Hack Meets It", "Status", "Evidence"].map(mk),
  });
}
// row = [reqSpecs, howSpecs, statusText, evidenceSpecs]
function dataRow(row, shade) {
  const fill = shade ? LIGHT : undefined;
  return new TableRow({
    children: [
      cell(row[0], 0, { fill }),
      cell(row[1], 1, { fill }),
      cell([{ t: row[2], bold: true }], 2, { fill }),
      cell(row[3], 3, { fill }),
    ],
  });
}
function matrix(rows) {
  const trs = [headerRow()];
  rows.forEach((r, i) => trs.push(dataRow(r, i % 2 === 1)));
  return new Table({ columnWidths: COLS, width: { size: USABLE, type: WidthType.DXA }, rows: trs });
}
function h(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 240, after: 100 }, children: [runs(text, { bold: true, size: 24, color: "1A2332" })] });
}
function sub(text) {
  return para([runs(text, { italics: true, size: 17, color: "444444" })], { after: 100 });
}
function spacer() { return para([runs("", {})], { after: 120 }); }

// ============================ CONTENT ============================
const A = [
  [
    [{ label: "No targeted advertising —", t: "Tenn. SOPPA, T.C.A. § 49-1-708. Operators may not use covered student information for targeted advertising." }],
    [{ t: "U.S. History Hack contains no advertising of any kind — no behavioral ads, no interest profiles, no retargeting on other sites." }],
    "Meets (self-attested)",
    [{ t: "FERPA/TN Student Data Privacy Statement §5; Privacy Policy" }],
  ],
  [
    [{ label: "No sale of student data —", t: "Tenn. SOPPA § 49-1-708." }],
    [{ t: "The vendor does not and will not sell, rent, or trade student information — in identified, de-identified, or aggregated form." }],
    "Meets (self-attested)",
    [{ t: "TN Data Privacy Statement §6" }],
  ],
  [
    [{ label: "No non-educational profiling —", t: "Tenn. SOPPA § 49-1-708." }],
    [{ t: "Student data is used only to deliver U.S. History instruction; no profiling of interests/behaviors for any non-educational purpose." }],
    "Meets (self-attested)",
    [{ t: "TN Data Privacy Statement §7" }],
  ],
  [
    [{ label: "Reasonable security —", t: "Tenn. SOPPA § 49-1-708(b)(4); Tenn. DATAA § 49-1-706." }],
    [
      { t: "TLS 1.2+ in transit; AES-256 transparent data encryption at rest (Azure SQL); Microsoft Entra ID Conditional Access + MFA for admin access; per-district row-level tenant isolation; Microsoft Defender for Cloud + GitHub Advanced Security (CodeQL, Dependabot, secret scanning). Independent third-party penetration testing is committed (not yet completed) per the Pentest Plan. The § 9 control set is stated as of the June 1, 2026 general-availability date." },
    ],
    "Meets (self-attested)",
    [{ t: "TN Data Privacy Statement §9; Breach Response Plan; annual-pentest-plan.md" }],
  ],
  [
    [{ label: "Data minimization —", t: "Tenn. DATAA § 49-1-703 (student data definitions)." }],
    [{ t: "Collects only roster identity (via district IdP) + learning records. No SSN, DOB, home address, biometrics, or precise geolocation. Demographics are not collected directly by the platform." }],
    "Meets (self-attested)",
    [{ t: "TN Data Privacy Statement §1" }],
  ],
  [
    [{ label: "On-device (unauthenticated) data —", t: "Data-minimization best practice under DATAA/SOPPA." }],
    [{ t: "For public/preview use, student progress is stored only in the browser's localStorage on the student's own device and is never transmitted to vendor servers." }],
    "Meets (self-attested)",
    [{ t: "TN Data Privacy Statement §1.5; lib/progress-store" }],
  ],
  [
    [{ label: "Deletion on request —", t: "Tenn. SOPPA § 49-1-708." }],
    [{ t: "Student information is deleted within 30 calendar days of a verified request from an authorized official, parent, or eligible student." }],
    "Meets (self-attested)",
    [{ t: "TN Data Privacy Statement §10; Data Disposal & Retention Policy" }],
  ],
  [
    [{ label: "Breach notification —", t: "T.C.A. § 47-18-2107 (TN Breach Notification Act); SOPPA § 49-1-708." }],
    [{ t: "Documented Security Incident & Breach Response Plan with a 72-hour district-notification commitment; cooperates with each district's FERPA notification duties." }],
    "Meets (self-attested)",
    [{ t: "TN Data Privacy Statement §9(g) & Certification #9 (FERPA breach §4); Breach Response Plan" }],
  ],
  [
    [{ label: "FERPA \"school official\" / direct control —", t: "20 U.S.C. § 1232g; 34 CFR § 99.31(a)(1)(i)(B)." }],
    [{ t: "Operates as a school official with legitimate educational interests, under district control; uses records only for the educational service; no redisclosure without district authorization." }],
    "Meets (self-attested)",
    [{ t: "TN Data Privacy Statement Part III" }],
  ],
  [
    [{ label: "Data-sharing / processing agreement —", t: "Tenn. DATAA § 49-1-701 et seq." }],
    [{ t: "Vendor executes a Data Processing / Data Sharing Agreement with the district; the controls are in place before the first student record is written, and the DPA incorporates the SOPPA/FERPA commitments." }],
    "Meets (self-attested)",
    [{ t: "TN Data Privacy Statement §2.2 & Certification #12; docs/data-processing-agreement.md" }],
  ],
  [
    [{ label: "COPPA (under 13) —", t: "15 U.S.C. §§ 6501-6506; 16 CFR Part 312." }],
    [{ t: "Designed for grades 9-12 (ages 14-18); not directed to children under 13. Any under-13 access relies on the school-authorization doctrine, with the district as consent intermediary." }],
    "Meets / limited scope",
    [{ t: "TN Data Privacy Statement Part VI" }],
  ],
];

const B = [
  [
    [{ label: "Acceptable Use Policy — updated requirements + annual audit —", t: "HB1886 (2026, amends Title 49); T.C.A. § 49-1-221. LEAs must maintain an internet AUP, obtain an annual third-party audit and post it publicly, and notify parents when an under-18 student reaches a site that violates the policy." }],
    [{ t: "This is a district obligation. U.S. History Hack is built to fit any district AUP: instructional-only content, no open-web browsing, no student-to-public posting, no advertising, and content governed by a documented content-governance policy." }],
    "District-configured (HH compatible)",
    [{ t: "docs/compliance/content-governance-policy.md" }],
  ],
  [
    [{ label: "Block social-media access on school internet —", t: "\"Teen Social Media and Internet Safety Act,\" HB825/SB811. From 2025-26, LEAs must prohibit student access to social-media platforms on LEA-provided internet except when a teacher authorizes it for educational purposes." }],
    [
      { t: "U.S. History Hack is not a social-media platform and embeds no social-media platforms (Facebook / X / Instagram / TikTok). Instructional video is limited to curated YouTube embeds surfaced as district curriculum content. The optional \"Study Squads\" peer feature is a closed, roster-scoped study group — not a public social network — and ships default-OFF behind a feature flag." },
    ],
    "Meets (does not route students to social media)",
    [{ t: "lib/feature-flags/optional-features.ts (study-groups default off); Curriculum Hub uses curated YouTube embeds only" }],
  ],
  [
    [{ label: "Internet Safety Curriculum, K-12 —", t: "T.C.A. § 49-1-221; DOE 6-12 safety guidance (HB825/SB811, due Jan 1, 2026)." }],
    [{ t: "District curriculum obligation. U.S. History Hack content is curated, standards-aligned, and free of external unsafe links; it supports safe, supervised use but does not deliver the required safety curriculum itself." }],
    "Supports district obligation",
    [{ t: "docs/compliance/content-governance-policy.md" }],
  ],
  [
    [{ label: "Content filtering —", t: "CIPA, 47 U.S.C. § 254(h)." }],
    [{ t: "All content is pre-authored, curated U.S. History with cited public-domain media; no open search, no third-party ad/analytics networks. Fully compatible with district CIPA content filters." }],
    "Meets / compatible",
    [{ t: "TN Data Privacy Statement §12; content-governance-policy.md" }],
  ],
];

const C = [
  [
    [{ label: "K-5 digital-device restriction + electronic-testing ban + device-use policy —", t: "HB2393/SB2310, Public Chapter 808 (eff. July 1, 2026). Restricts digital-device access, digital instruction, and electronic testing for grades K-5, and requires an age-appropriate device-use policy. Exempts virtual schools and students with disabilities (IEP/504)." }],
    [{ t: "U.S. History Hack serves grades 9-12 (Tennessee EOC U.S. History, US.01-US.95). The K-5 device-access and electronic-testing restrictions do not reach grades 9-12. If a district were to use U.S. History Hack in an elementary setting, the district's device-use policy and the statute's exceptions would govern." }],
    "N/A — out of grade scope (9-12)",
    [{ t: "Product scope: grades 9-12; TN Data Privacy Statement Part I" }],
  ],
];

const D = [
  [
    [{ label: "LEA/charter AI-use policy governs student- and staff-facing AI —", t: "2024 TN AI-policy requirement (Title 49; cf. § 49-7-185 higher-ed analog)." }],
    [{ t: "U.S. History Hack uses NO runtime or generative AI in the student experience. Students never interact with a language model; all questions, feedback, definitions, and content are static, pre-authored, and human-reviewed. No student data is sent to any AI system — so there is no student-facing AI for a district AI-use policy to restrict." }],
    "Meets / compatible",
    [{ t: "docs/ai-disclosure.md; TN Data Privacy Statement Part V" }],
  ],
  [
    [{ label: "Age-appropriate student AI instruction —", t: "SB0514/HB0531 (2025); AI instruction beginning 2026-27, with DOE guidance + teacher PD." }],
    [{ t: "A district curriculum obligation, not a vendor requirement. U.S. History Hack's clear labeling (human-authored content, no AI generation) gives teachers an honest, transparent example to support AI-literacy instruction." }],
    "Supports district obligation",
    [{ t: "docs/ai-disclosure.md" }],
  ],
  [
    [{ label: "AI transparency / disclosure —", t: "TN responsible-AI expectations." }],
    [{ t: "Publicly discloses the authoring-time AI tools used during content development: a large language model (Anthropic Claude) drafted text content and quiz questions, and an OpenAI image-generation model produced illustrations only (workbook covers, the \"C-Q130\"/\"CORE\" narrative characters, avatar-store images, and icons). Every AI-assisted item was reviewed and approved by a qualified educator. No student-AI interaction at runtime; the AI-generated avatar images are currently paused pending a provenance and copyright review." }],
    "Meets (self-attested)",
    [{ t: "docs/ai-disclosure.md" }],
  ],
];

const E = [
  [
    [{ label: "WCAG 2.1 AA conformance —", t: "ADA Title II (DOJ 2024 rule; compliance dates Apr 2026 / Apr 2027); applies to public-school digital content." }],
    [{ t: "Self-assessed VPAT 2.5 / Accessibility Conformance Report targeting WCAG 2.2 AA (meets or exceeds the ADA Title II WCAG 2.1 AA baseline); automated axe-core checks run in CI on every pull request to main; assistive-technology testing report (external verification scheduled)." }],
    "Self-assessed + continuous axe-core CI",
    [{ t: "docs/compliance/VPAT-2.5-ACR.md; a11y-evidence workflow; axe-core CI" }],
  ],
  [
    [{ label: "Equal access / UDL / accommodations —", t: "Section 504, 29 U.S.C. § 794." }],
    [{ t: "Bilingual English/Spanish throughout; read-aloud (text-to-speech); UDL supports; print alternatives for on-screen activities; keyboard-accessible interactive elements." }],
    "Meets (self-attested)",
    [{ t: "docs/accessibility-statement.md; assistive-technology-testing-report.md" }],
  ],
  [
    [{ label: "Section 508 —", t: "29 U.S.C. § 794d (federally funded programs)." }],
    [{ t: "VPAT 2.5 self-assessment documents conformance against the Section 508 / WCAG 2.x AA criteria; remediation tracked in a district-facing remediation log." }],
    "Self-assessed (VPAT 2.5)",
    [{ t: "docs/compliance/VPAT-2.5-ACR.md; docs/a11y/district-remediation-2026-07.md" }],
  ],
];

// ============================ DOCUMENT ============================
const children = [];

children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [runs("U.S. History Hack — Tennessee Technology-in-the-Classroom Law Compliance Matrix", { bold: true, size: 30, color: "1A2332" })] }));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [runs("TroopToTeacher Technologies, LLC  ·  app.ushistoryhack.com  ·  Tennessee EOC U.S. History (grades 9-12)", { size: 18, color: "444444" })] }));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 160 }, children: [runs("Prepared July 2026  ·  Reflects Tennessee law through the 114th General Assembly (2025-2026)", { size: 18, color: "444444" })] }));

// Disclaimer box (single-cell table for a shaded callout)
const disc = new Table({
  columnWidths: [USABLE], width: { size: USABLE, type: WidthType.DXA },
  rows: [new TableRow({ children: [new TableCell({
    width: { size: USABLE, type: WidthType.DXA }, borders: CELL_BORDERS,
    shading: { type: ShadingType.CLEAR, fill: "FBF3E0", color: "auto" },
    margins: { top: 100, bottom: 100, left: 140, right: 140 },
    children: [
      new Paragraph({ spacing: { after: 60 }, children: [runs("How to read this document.  ", { bold: true, size: 18 }), runs("This is a vendor self-assessment and compliance-mapping aid prepared by TroopToTeacher Technologies. It is NOT legal advice and NOT a third-party certification, audit, or accreditation. Entries marked \"self-attested\" are the vendor's own representations that a control is in place; they have not been verified by an outside agency. Where a control is forward-looking (e.g., independent penetration testing, external assistive-technology verification), it is labeled as committed or scheduled rather than completed; accessibility conformance is self-assessed via VPAT 2.5, not independently certified. Statutory citations reflect good-faith research as of July 2026 and should be confirmed with district counsel before reliance.", { size: 17 })] }),
      new Paragraph({ children: [runs("Scope.  ", { bold: true, size: 18 }), runs("U.S. History Hack serves grades 9-12. Several 2026 Tennessee laws (e.g., the K-5 device restriction, Public Chapter 808) fall outside that grade band and are marked accordingly. A district's own Acceptable Use, AI, and technology policies may impose additional local requirements not captured here; those can be mapped in a second pass.", { size: 17 })] }),
    ],
  })] })],
});
children.push(disc);
children.push(spacer());

// Legend
children.push(para([
  runs("Status legend:  ", { bold: true, size: 17 }),
  runs("Meets (self-attested)", { bold: true, size: 17 }), runs(" = vendor attests the control is in place.  ", { size: 17 }),
  runs("Compatible / District-configured", { bold: true, size: 17 }), runs(" = the legal duty is the district's; U.S. History Hack is built to fit it.  ", { size: 17 }),
  runs("Supports", { bold: true, size: 17 }), runs(" = U.S. History Hack assists a district obligation.  ", { size: 17 }),
  runs("N/A — out of scope", { bold: true, size: 17 }), runs(" = the law targets a grade band or actor outside U.S. History Hack's use.", { size: 17 }),
], { after: 160 }));

children.push(h("A.  Student Data Privacy & Security"));
children.push(sub("Tenn. DATAA (§ 49-1-701 et seq.) · Tenn. SOPPA (§ 49-1-708) · FERPA · COPPA · CIPA · TN Breach Notification Act (§ 47-18-2107)"));
children.push(matrix(A));

children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(h("B.  Internet Safety, Acceptable Use & Content Filtering  (2026 changes)"));
children.push(sub("HB1886 (2026 AUP overhaul + annual audit) · Teen Social Media & Internet Safety Act, HB825/SB811 · T.C.A. § 49-1-221 · CIPA (47 U.S.C. § 254(h))"));
children.push(matrix(B));
children.push(spacer());

children.push(h("C.  Digital Devices & Screen Time  (2026 change)"));
children.push(sub("HB2393/SB2310, Public Chapter 808 — K-5 digital-device and electronic-testing restriction (effective July 1, 2026)"));
children.push(matrix(C));

children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(h("D.  Artificial Intelligence"));
children.push(sub("2024 LEA/charter AI-use-policy requirement · SB0514/HB0531 (2025) — student AI instruction (2026-27), DOE guidance, teacher PD"));
children.push(matrix(D));
children.push(spacer());

children.push(h("E.  Accessibility"));
children.push(sub("ADA Title II (DOJ 2024 rule, WCAG 2.1 AA) · Section 504 (29 U.S.C. § 794) · Section 508 (29 U.S.C. § 794d)"));
children.push(matrix(E));

children.push(spacer());
children.push(para([runs("Prepared by TroopToTeacher Technologies, LLC. Contact: Sean Reynolds, Founder — sean.reynolds@trooptoteacher.com. This matrix is a self-attestation and compliance-mapping aid, not legal advice or third-party certification; confirm citations and applicability with district counsel.", { italics: true, size: 16, color: "555555" })]));

const doc = new Document({
  styles: { default: { document: { run: { font: "Calibri", size: 18 } } } },
  sections: [{
    properties: { page: {
      size: { width: 12240, height: 15840, orientation: PageOrientation.LANDSCAPE },
      margin: { top: 720, bottom: 720, left: 720, right: 720 },
    } },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  const out = "/tmp/claude-0/-home-user-trooptoteacher-history/c27aff16-3c79-5004-bf4a-470896c27424/scratchpad/History-Hack-TN-Compliance-Matrix.docx";
  fs.writeFileSync(out, buf);
  console.log("WROTE " + out + " (" + buf.length + " bytes)");
});
