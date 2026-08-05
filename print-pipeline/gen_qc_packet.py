#!/usr/bin/env python3
"""Unit 1 — Quality Control & Alignment Packet (print-first, no docx).
Renders a landscape PDF via WeasyPrint. Five matrices, all grounded in repo data:
  1. QC Process Matrix (honest status of THIS build)
  2. Assessment <-> Standards Crosswalk (56 items, DOK) — from Unit1 Assessment Book
  3. Standards Crosswalk (standard -> SSP -> workbook activity -> deck)
  4. UDL 3.0 Crosswalk (CAST 2024)
  5. Planned Technology Crosswalk (Educational-Impact Gate: strategy + Hattie d)
Run: python3 gen_qc_packet.py
"""
import json
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
DECK = ROOT.parent / ".claude/skills/history-hack-tcap-deck-builder/assets/unit1-example"
BUILD = json.loads((DECK / "_build.json").read_text())
ACTS = json.loads((DECK / "_activities.json").read_text())
OUT = ROOT / "out/Unit1_QC_and_Alignment_Packet.pdf"

# America 250 palette
NAVY, RED, GOLD, CREAM, INK = "#1F3A5F", "#B22234", "#C9A227", "#F8F5EF", "#20262E"

# DOK distribution per standard — extracted from Unit1_Assessment_Book_Teacher.pdf (56 items)
DOK = {
    "US.01": {"1": 0, "2": 8, "3": 0}, "US.02": {"1": 3, "2": 5, "3": 0},
    "US.03": {"1": 3, "2": 5, "3": 0}, "US.04": {"1": 0, "2": 8, "3": 0},
    "US.05": {"1": 3, "2": 5, "3": 0}, "US.06": {"1": 3, "2": 3, "3": 2},
    "US.07": {"1": 1, "2": 4, "3": 3},
}
SSP_LABEL = {"SSP.01": "Collect sources", "SSP.02": "Examine a source",
             "SSP.03": "Synthesize evidence", "SSP.04": "Construct an argument",
             "SSP.05": "Historical awareness", "SSP.06": "Geographic awareness"}


def esc(s):
    import html
    return html.escape(str(s), quote=False)


def chip(status):
    m = {"pass": ("PASS", "#1B5E20", "#E4F0E5"), "partial": ("PARTIAL", "#8A5A00", "#FBEFD6"),
         "open": ("OPEN", "#8B1E2D", "#F7E1E4"), "notrun": ("NOT YET RUN", "#5C6470", "#ECEFF3"),
         "prog": ("IN PROGRESS", "#0B4A6F", "#DDEBF4")}
    t, fg, bg = m[status]
    return f'<span class="chip" style="color:{fg};background:{bg}">{t}</span>'


# ---- Matrix 1: QC Process ----
QC_ROWS = [
    ("0", "Platinum standard loaded", "Mission + decision rule (100% alignment → Schedule F → adoption) frame every choice", "history-hack-platinum-standard", "pass"),
    ("0A", "Image / primary-source inventory", "Every referenced image present, public-domain, historian-verified, captioned", "tcap-deck-builder GATE 0A", "pass"),
    ("0B", "Content reuse (no invent)", "Deck + workbook built from the locked repo content, matched verbatim", "tcap-deck-builder GATE 0B", "pass"),
    ("1", "America 250 palette migration", "Brand tokens Heritage Blue/Patriot Red/Muted Gold/Founders Cream", "tcap-deck-builder", "pass"),
    ("2", "Deck build — native .pptx", "pptxgenjs, layout set before slides; 109 slides generated", "tcap-deck-builder", "pass"),
    ("3", "Deck render → PDF", "LibreOffice Impress convert; 109 pages, no load error", "LibreOffice", "pass"),
    ("4", "Deck content dump (markitdown)", "Slide count / order / no placeholder-lorem / no truncation", "history-hack-text-integrity-qc", "notrun"),
    ("5", "Deck package integrity", "validate.py — no orphan/duplicate parts; round-trip", "pptx skill", "notrun"),
    ("6", "Deck full per-slide visual QC", "Every slide read for overflow/clipping (Gate 3, MANDATORY before ship)", "tcap-deck-builder Gate 3", "partial"),
    ("7", "Workbook generated from deck SoT", "unit-01.json emitted from the deck's _build.json → match by construction", "history-hack-unit-content-build", "pass"),
    ("8", "Workbook JSON schema validate", "Loads; 7 standards, valid block types", "print-pipeline", "pass"),
    ("9", "Workbook render (WeasyPrint)", "Locked workbook.css contract; 35 pages", "print-pipeline", "pass"),
    ("10", "Workbook blank-page scan", "0 near-blank pages across 35", "QC", "pass"),
    ("11", "Workbook visual QC", "Every page read for overflow/clipping", "QC", "partial"),
    ("12", "Lesson-flow QC (deck↔workbook)", "Every workbook activity resolves to an EXACT slide, in order", "history-hack-lesson-flow-qc", "open"),
    ("13", "Text-integrity QC", "No clipped / placeholder / dangling-ellipsis text", "history-hack-text-integrity-qc", "notrun"),
    ("14", "Historian fact-check (Policy 2.600)", "Every date/name/statute verified vs primary sources", "historian-factcheck-agent", "partial"),
    ("15", "Schedule F self-score", "TDOE Social Studies rubric / adoption panel review", "tn-textbook-adoption-agent", "notrun"),
    ("16", "Accessibility — WCAG 2.2 AA", "508 / ADA Title II gate (code + content)", "accessibility-qc-agent", "notrun"),
    ("17", "Human QC (your review)", "Final human gate on the matched Unit 1 set", "YOU", "prog"),
]

# ---- Matrix 4: UDL 3.0 ----
UDL_ROWS = [
    ("Engagement<br><span class='sub'>the “why” of learning</span>", "Recruit interest",
     "Essential Question per standard · unit hook / Turn &amp; Talk · TN &amp; Williamson-Co. relevance (George Jordan, Medal of Honor)",
     "Deck hooks · Workbook Cornell front EQ"),
    ("", "Sustain effort &amp; persistence",
     "Success criteria stated up front · DOK 1→3 ramp within each standard · exit tickets", "Deck wrap-ups · Assessment Book"),
    ("", "Emotional capacity / self-regulation",
     "Confidence-check warm-up (early win) · CER self-grade → app feedback → revise loop", "Deck warm-ups · Workbook CER"),
    ("Representation<br><span class='sub'>the “what” of learning</span>", "Perception",
     "Public-domain primary-source images, captioned · ZOOM-IN close-looking signal", "Deck primary-source slides"),
    ("", "Language &amp; symbols",
     "EN/ES vocabulary · plain-language “simple” definitions · pronunciation respelling (say:) · Español column",
     "Deck word wall · Workbook vocab table"),
    ("", "Build knowledge",
     "Close-Read chunking · section headings as anchors · dual-coding initials chips", "Workbook Activity 4 · Deck DI"),
    ("Action &amp; Expression<br><span class='sub'>the “how” of learning</span>", "Interaction &amp; physical action",
     "Cornell notes · reproducible graphic organizers · write-in response tables", "Workbook · Organizer Toolkit"),
    ("", "Expression &amp; communication",
     "CER argument frames · HIPPO source analysis · multiple response formats", "Workbook Activities 5–6"),
    ("", "Strategy development / executive function",
     "Guided Cornell (25/75) · Source-It-First scaffold · timed activity boxes", "Workbook · Deck We-Do"),
]

# ---- Matrix 5: Technology (Educational-Impact Gate) ----
TECH_ROWS = [
    ("Parallel test-data analytics", "Live roll-ups of the 56-item bank at district · PLC · teacher · student",
     "Providing formative evaluation <b>d≈0.48</b>; Feedback <b>d≈0.70</b>", "All US.01–US.07 (Assessment Book)",
     "Paper can’t aggregate or roll up cross-class response data in real time"),
    ("Real-time standard mastery", "Per-standard mastery meter updates as students respond",
     "Mastery learning <b>d≈0.57</b>; Feedback <b>d≈0.70</b>", "US.01–US.07 formative checkpoints",
     "Paper shows no live mastery state to act on mid-lesson"),
    ("Reteaching / auto-remediation", "Auto-routes a student to the right reteach on a miss",
     "Response to Intervention <b>d≈1.07</b>", "US.02 / 03 / 05 / 06 reteach routes",
     "Paper can’t branch per-student in real time"),
    ("Lesson-plan builder", "Assembles a plan vs. TEAM rubric + pacing; every activity tagged with its strategy + effect size + UDL/MTSS; outputs a print ZIP",
     "Teacher clarity <b>d≈0.75</b>; Collective teacher efficacy <b>d≈1.36</b>", "Whole unit",
     "Paper can’t recompute a plan to one teacher’s schedule — teacher keeps full power"),
    ("Gamification + read-aloud", "Gamified spaced review + first-party read-aloud (closed-loop, no link-out)",
     "Spaced / retrieval practice <b>d≈0.60</b>; read-aloud = UDL access", "Vocabulary + review, US.01–US.07",
     "Paper can’t schedule adaptive spacing or read text aloud"),
]


def table(headers, rows, cls="", widths=None):
    cg = ""
    if widths:
        cg = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>"
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = ""
    for r in rows:
        body += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return f'<table class="{cls}">{cg}<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def build_html():
    # Matrix 1
    m1 = table(["#", "QC gate", "What it verifies", "Owner", "This build"],
               [(n, f"<b>{esc(g)}</b>", esc(w), f'<span class="own">{esc(o)}</span>', chip(s)) for n, g, w, o, s in QC_ROWS],
               "qc", ["4%", "20%", "44%", "18%", "14%"])

    # Matrix 2 — assessment ↔ standards
    a_rows = []
    tot = {"1": 0, "2": 0, "3": 0, "n": 0}
    for code in [f"US.0{i}" for i in range(1, 8)]:
        v = BUILD[code]; d = DOK[code]; n = d["1"] + d["2"] + d["3"]
        tot["1"] += d["1"]; tot["2"] += d["2"]; tot["3"] += d["3"]; tot["n"] += n
        a_rows.append((f"<b>{code}</b>", esc(v["title"]), str(n),
                       str(d["1"]) or "—", str(d["2"]) or "—", str(d["3"]) or "—",
                       "Form A + Form B (parallel)"))
    a_rows.append((f"<b>TOTAL</b>", "<b>7 standards · balanced bank</b>", f"<b>{tot['n']}</b>",
                   f"<b>{tot['1']}</b>", f"<b>{tot['2']}</b>", f"<b>{tot['3']}</b>", "<b>+ Item Analysis + Reteach</b>"))
    m2 = table(["Std", "Standard title", "Items", "DOK 1", "DOK 2", "DOK 3", "Summative coverage"],
               a_rows, "asmt", ["6%", "34%", "8%", "8%", "8%", "8%", "28%"])

    # Matrix 3 — standards crosswalk
    s_rows = []
    for code in [f"US.0{i}" for i in range(1, 8)]:
        v = BUILD[code]
        ssp = " · ".join(f"{s} {SSP_LABEL.get(s,'')}" for s in v.get("ssps", []))
        act = ACTS.get(code, {})
        wb = "A4 Close Read · A5 Primary Source (HIPPO) · A6 " + esc(act.get("title", "Apply")) + " · Cornell Notes"
        s_rows.append((f"<b>{code}</b>", esc(v.get("tnStandard", "").split("–", 1)[-1].strip()),
                       esc(ssp), wb, f"Deck {code} section"))
    m3 = table(["Std", "TN standard (official text)", "TN Social Studies Practices", "Workbook activities", "Deck"],
               s_rows, "std", ["5%", "34%", "26%", "27%", "8%"])

    m4 = table(["UDL 3.0 principle", "Guideline", "How Unit 1 delivers it", "Where"],
               UDL_ROWS, "udl", ["17%", "17%", "48%", "18%"])

    m5 = table(["App capability (planned)", "What it adds beyond print", "High-impact strategy (Hattie d)", "Standards / activities", "Print can’t because…"],
               TECH_ROWS, "tech", ["16%", "24%", "20%", "18%", "22%"])

    def section(num, title, sub, body):
        return (f'<section><div class="sec"><span class="num">{num}</span>'
                f'<span class="t">{title}</span><span class="s">{sub}</span></div>{body}</section>')

    css = """
    @page { size: Letter landscape; margin: 1.5cm 1.4cm 1.6cm 1.4cm;
      @bottom-left { content:"U.S. History Hack™ · Unit 1 — QC & Alignment Packet"; font:8pt 'DejaVu Sans'; color:#5C6470; }
      @bottom-right { content:"© 2026 TroopToTeacher Technologies LLC · Page " counter(page); font:8pt 'DejaVu Sans'; color:#5C6470; } }
    * { box-sizing:border-box; }
    body { font-family:'DejaVu Sans', Arial, sans-serif; color:%(INK)s; font-size:8.4pt; margin:0; }
    .cover { background:%(NAVY)s; color:#fff; padding:22px 24px; border-left:10px solid %(RED)s; margin-bottom:14px; }
    .cover h1 { margin:0 0 4px; font-size:20pt; }
    .cover .sub { color:%(GOLD)s; font-size:11pt; font-weight:bold; }
    .cover .meta { color:#C7D2E0; font-size:8.5pt; margin-top:8px; line-height:1.5; }
    .sec { border-bottom:2px solid %(GOLD)s; margin:16px 0 7px; padding-bottom:3px; page-break-after:avoid; }
    .sec .num { background:%(NAVY)s; color:#fff; font-weight:bold; padding:1px 8px; border-radius:3px; margin-right:8px; font-size:9pt; }
    .sec .t { color:%(NAVY)s; font-weight:bold; font-size:12pt; }
    .sec .s { color:#5C6470; font-size:8pt; margin-left:8px; }
    table { border-collapse:collapse; width:100%%; margin-bottom:4px; page-break-inside:auto; }
    th { background:%(NAVY)s; color:#fff; text-align:left; padding:5px 7px; font-size:8pt; vertical-align:top; }
    td { border:0.5pt solid #CBD2DE; padding:4px 7px; vertical-align:top; line-height:1.32; }
    tbody tr:nth-child(even) td { background:%(CREAM)s; }
    tr { page-break-inside:avoid; }
    .own { color:#5C6470; font-size:7.4pt; }
    .chip { font-size:6.8pt; font-weight:bold; padding:1px 6px; border-radius:8px; white-space:nowrap; letter-spacing:.3px; }
    .sub { color:#7A8494; font-weight:normal; font-size:7pt; font-style:italic; }
    .asmt td:nth-child(n+3):nth-child(-n+6) { text-align:center; font-variant-numeric:tabular-nums; }
    .legend { font-size:7.6pt; color:#5C6470; margin:6px 0 2px; }
    .note { font-size:7.6pt; color:#5C6470; font-style:italic; margin-top:3px; }
    .std td:nth-child(2) { font-size:7.6pt; }
    """ % dict(NAVY=NAVY, RED=RED, GOLD=GOLD, CREAM=CREAM, INK=INK)

    body = f"""
    <div class="cover">
      <div class="sub">U.S. HISTORY HACK™ · America 250</div>
      <h1>Unit 1 — Quality Control &amp; Alignment Packet</h1>
      <div class="sub" style="color:#fff;font-size:10pt">The Rise of Industrialization, 1877–1900 · US.01–US.07 · Course Standard Edition</div>
      <div class="meta">Covers the matched Unit 1 set — Teacher lecture deck (109 slides) · Student workbook (35 pp, no .docx) · Graphic-organizer toolkits ·
      Assessment Book (56 items).&nbsp; Every cell traces to repo data or named doctrine. <b>QC statuses are reported honestly</b> —
      what actually ran this build vs. what is still pending human review.</div>
    </div>

    {section("1", "QC Process Matrix", "the pipeline this build passed through — honest status", m1)}
    <div class="legend">{chip('pass')} verified &nbsp; {chip('partial')} spot-checked / inherited &nbsp; {chip('open')} known gap, tracked &nbsp; {chip('notrun')} defined gate, not run this session &nbsp; {chip('prog')} human review underway</div>
    <div class="note">Nothing is claimed as shipped. Gates 4–5, 13, 15–16 are the release gates that still run before adoption submission; 12 (exact deck↔workbook slide keying) is the one open alignment item.</div>

    {section("2", "Assessment ↔ Standards Crosswalk", "Unit 1 Assessment Book — 56 items, DOK-balanced", m2)}
    <div class="note">Items are pre-field-test (pre-calibrated 3PL); first administration generates the response data that calibrates them (FERPA/COPPA-safe pipeline). Two parallel summative forms (A/B) support pre/post + retakes.</div>

    {section("3", "Standards Crosswalk", "standard → SSP → workbook activity → deck", m3)}

    {section("4", "UDL 3.0 Crosswalk", "CAST 2024 — three principles across the Unit 1 set", m4)}

    {section("5", "Planned Technology Crosswalk", "Educational-Impact Gate — a named high-impact strategy (Hattie d ≥ 0.40 hinge) that print physically can’t deliver", m5)}
    <div class="note">Effect sizes are Hattie <i>Visible Learning</i> meta-analytic averages (hinge d≈0.40); local results calibrate as data accrues. Every capability is gated on adding value print can’t — the anti-overuse rule. All video is first-party, self-hosted, closed-loop (CIPA/COPPA/FERPA).</div>
    """

    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=build_html()).write_pdf(str(OUT))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
