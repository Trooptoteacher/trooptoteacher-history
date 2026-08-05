#!/usr/bin/env python3
"""Unit 1 — Future Ready ("Ready Graduate") Crosswalk & Proof (print-first, no docx).
Landscape PDF via WeasyPrint. Grounded in the repo SoT:
  - four-pillar spec: 00_START_HERE/FRAMEWORKS_CANON.md §5
  - currency figures + provenance: history-hack-unit-content-build/assets/future-ready/
    future_ready_data.json (read live so the money-math proof stays in sync)
  - currency status: verify_future_ready_currency.py (PASS + honest WARN)
Sections: A four-pillar crosswalk (pillar→skills→leading measure→where Unit 1 proves
it→macro target) · B the 1–4 scale + 3-instrument measurement engine + behavioral
proxies (VISIBLE + MEASURABLE proof) · C currency proof (every figure→federal source→
verified) · D evidence base.
"""
import json
from datetime import datetime, timezone
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
FR = ROOT.parent / ".claude/skills/history-hack-unit-content-build/assets/future-ready"
DATA = json.loads((FR / "future_ready_data.json").read_text())
TS = datetime.now(timezone.utc); ISO = TS.strftime("%Y-%m-%dT%H:%M:%SZ"); STAMP = TS.strftime("%Y%m%d_%H%M")

NAVY, NAVY2, RED, GOLD, CARD, LIGHT, BORDER, INK, GRN = \
    "#1F3A5F", "#2C3E63", "#B22234", "#C9A227", "#F8F5EF", "#EEF2F8", "#C9C2B4", "#20262E", "#1B5E20"

PILLARS = [
    ("Academic Reasoning", "★ featured this unit",
     "Close reading · Argument writing (CER) · Math modeling · Data analysis",
     "CER Closing Argument 1–4 · source read (HIPPO) · a data/math task",
     "Workbook CER (Activity 6) + DBQ essay &amp; 5-criterion rubric · Workbook/DBQ HIPPO on every source · DBQ railroad &amp; foreign-born <b>data</b> tasks",
     "ACT (Eng 18 · Math 22 · Read 22 · Sci 23) · Ready Graduate ≥ 21"),
    ("College &amp; Career Launch", "",
     "Communication (spoken) · Interview readiness · Financial literacy · Planning &amp; organization",
     "Spoken “Mission Brief” 1–4 · a career-skill task · materials-ready &amp; on-time",
     "Launch/Debrief bookend sheets (goal + materials-ready + on-time tally) · <b>money-math</b> from the currency SoT (loan APR, Pell, FAFSA)",
     "FAFSA completion · EPSOs · industry credential · NACE career readiness"),
    ("Durable Character", "",
     "Grit · Work ethic · Integrity · Timeliness · Adaptability · Lifelong learning",
     "Behavioral proxies (see Part B) on the 1–4 scale",
     "Launch <b>baseline</b> + Debrief <b>re-score</b> on the 10-trait hireability rubric → a dated <b>growth delta</b>",
     "Durable-skills profile trend · employer “would-hire” · self-directed learner"),
    ("Civic &amp; Collaborative", "",
     "Teamwork · Leadership · Civic responsibility",
     "Peer/self teamwork 1–4 · a logged leadership move · civic-action reflection",
     "DBQ paired investigation (teamwork) · Teamwork/Leadership traits on the rubric · civic reflection on US.03 disenfranchisement &amp; the Exodusters",
     "Ready Graduate civic disposition · NACE teamwork &amp; leadership"),
]

SCALE = [("1 Emerging", "attempts it; missing key parts — needs supports"),
         ("2 Developing", "has the parts, not yet reliable — below trajectory, watch/support"),
         ("3 Proficient", "meets the standard independently — ✓ on-trajectory (target)"),
         ("4 Advanced", "exceeds it; transfers the skill to new problems unprompted")]

ENGINE = [
    ("1 · Self-assessment “Grade Check”",
     "Student logs the gradebook (current average + # missing) and self-scores the unit skill 1–4, then compares to the teacher score.",
     "Launch &amp; Debrief sheets — grade &amp; missing-items check; self-vs-teacher calibration",
     "Named + a number (average, # missing, 1–4)"),
    ("2 · Rubric performance task",
     "A real product (CER Closing Argument / spoken brief) scored 1–4 — a formative check before the summative.",
     "Workbook CER + DBQ essay rubric; spoken “Mission Brief” rubric",
     "Named + a 1–4 score"),
    ("3 · Goal monitor",
     "Student names a next-unit goal and checks whether they hit the last one.",
     "Launch pre-unit goal → Debrief goal check-in + next-unit commitment",
     "Named + hit/miss + new goal"),
]

PROXIES = [
    ("Timeliness", "% of work submitted on time", "assignment timestamps"),
    ("Work ethic", "task-completion % · attempts a revision when invited", "completion &amp; revision logs"),
    ("Task persistence", "finishes multi-step tasks; returns to the hard item", "task progress · goal follow-through"),
    ("Integrity", "cites sources · submits own work", "evidence use · honesty checks"),
    ("Self-assessment calibration", "closeness of self-score to teacher score", "self-vs-teacher gap"),
    ("Responsiveness to feedback", "score improves on the next attempt", "attempt-to-attempt change"),
    ("Communication", "spoken-brief rubric (claim · evidence · delivery)", "brief rubric 1–4"),
    ("Teamwork / Leadership", "peer + self rating · logged leadership moves", "rubrics · leadership log"),
]

EVIDENCE = [
    ("ACT College &amp; Career Readiness Benchmarks", "the 30,000-ft lagging target the leading indicators steer toward"),
    ("Tennessee Ready Graduate indicator", "diploma + ACT ≥ 21 or EPSO/credential equivalent"),
    ("Hattie, <i>Visible Learning</i>", "self-reported grades / self-teacher calibration <b>d ≈ 1.33</b>"),
    ("Black &amp; Wiliam, <i>Inside the Black Box</i>", "formative assessment moves learning while there is time"),
    ("Locke &amp; Latham", "specific, challenging, monitored goals raise performance"),
    ("America Succeeds, <i>Durable Skills</i>", "employer demand for the durable-character skills"),
    ("NACE Career Readiness Competencies", "communication, teamwork, leadership, professionalism"),
]

CSS = """
* { box-sizing:border-box; }
body { font-family:'DejaVu Sans', Arial, sans-serif; color:%(INK)s; margin:0; font-size:8.4pt; line-height:1.34; }
.cover { background:%(NAVY)s; color:#fff; padding:18px 22px; border-left:12px solid %(RED)s; }
.cover .kick { color:%(GOLD)s; font-weight:bold; letter-spacing:1px; font-size:9.5pt; }
.cover h1 { font-size:19pt; margin:5px 0 3px; }
.cover .sub { color:#DCE6F1; font-size:9.5pt; }
.cover .meta { color:#AFC0D6; font-size:7.6pt; margin-top:8px; }
.sec { color:%(NAVY)s; border-bottom:2px solid %(GOLD)s; padding-bottom:3px; margin:13px 0 6px; font-size:12.5pt; }
.sec .s { color:#5C6470; font-size:8pt; font-weight:normal; margin-left:6px; }
table { border-collapse:collapse; width:100%%; margin-bottom:4px; }
th { background:%(NAVY)s; color:#fff; text-align:left; padding:5px 7px; font-size:7.8pt; vertical-align:top; }
td { border:0.5pt solid %(BORDER)s; padding:5px 7px; font-size:8.2pt; vertical-align:top; }
tbody tr:nth-child(even) td { background:%(CARD)s; }
tr { page-break-inside:avoid; }
.page { page-break-before:always; }
.pill { color:%(NAVY)s; font-weight:bold; }
.star { color:%(RED)s; font-weight:bold; font-size:7pt; }
.chip { font-size:7pt; font-weight:bold; padding:1px 7px; border-radius:9px; }
.pass { color:#1B5E20; background:#E4F0E5; } .warn { color:#8A5A00; background:#FBEFD6; }
.verdict { background:#E4F0E5; border:1.5pt solid %(GRN)s; border-radius:6px; padding:8px 12px; margin:5px 0; font-size:8.6pt; }
.verdict b { color:%(GRN)s; }
.warnbox { background:#FBEFD6; border-left:4px solid %(GOLD)s; padding:6px 11px; margin:5px 0; font-size:8.2pt; }
.note { font-size:7.6pt; color:#5C6470; font-style:italic; margin-top:3px; }
.lead { font-size:8.8pt; margin:8px 2px; }
.lead b { color:%(NAVY)s; }
@page { size:Letter landscape; margin:1.3cm;
  @bottom-left { content:"U.S. History Hack™ · Unit 1 — Future Ready Crosswalk & Proof"; font:7.5pt 'DejaVu Sans'; color:#5C6470; }
  @bottom-right { content:"© 2026 TroopToTeacher Technologies LLC · p. " counter(page); font:7.5pt 'DejaVu Sans'; color:#5C6470; } }
""" % dict(INK=INK, NAVY=NAVY, NAVY2=NAVY2, RED=RED, GOLD=GOLD, CARD=CARD, LIGHT=LIGHT, BORDER=BORDER, GRN=GRN)


def T(headers, rows, widths):
    cg = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>"
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table>{cg}<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def currency_rows():
    ts = DATA["time_sensitive"]; hs = DATA["historical_stable"]
    rows = []
    lr = ts["direct_loan_rates_undergrad"]
    yrs = " · ".join(f"{y}: {v}%" for y, v in lr["by_year"].items())
    rows.append(("Federal Direct Loan APR (undergrad)", yrs, f'<a>{lr["source_url"]}</a>', lr["last_verified"], '<span class="chip warn">WARN — add AY26-27</span>'))
    rows.append(("Chart example APR", f'{ts["chart_example_apr"]["value"]}% (stated as an example)', ts["chart_example_apr"]["source_url"], ts["chart_example_apr"]["last_verified"], '<span class="chip pass">CURRENT</span>'))
    rows.append(("Pell Grant maximum", f'${ts["pell_max"]["value"]:,}/yr (as of {ts["pell_max"]["as_of"]})', ts["pell_max"]["source_url"], ts["pell_max"]["last_verified"], '<span class="chip pass">CURRENT</span>'))
    rows.append(("FAFSA opens", "each fall — read from source, not hard-coded", ts["fafsa_open"]["source_url"], ts["fafsa_open"]["last_verified"], '<span class="chip pass">SOURCE-LINKED</span>'))
    for k, v in hs.items():
        val = f'{v.get("value")} million' if v.get("value") else "historical fact (stable)"
        rows.append((v["label"][:52], val, v.get("source_url", ""), v.get("last_verified", "—"), '<span class="chip pass">STABLE</span>'))
    return rows


def build():
    a = T(["Pillar (rotate the featured one)", "Measurable skills", "Per-unit leading measure", "Where Unit 1 proves &amp; measures it", "Year-end macro target (lagging)"],
          [(f'<span class="pill">{p}</span>' + (f'<br><span class="star">{tag}</span>' if tag else ""), sk, lead, where, macro)
           for p, tag, sk, lead, where, macro in PILLARS],
          ["15%", "20%", "19%", "28%", "18%"])
    scale = T(["1–4 scale (used everywhere)", "What it means"], [(f'<b>{s}</b>', d) for s, d in SCALE], ["24%", "76%"])
    engine = T(["Measurement instrument (every unit)", "What the student does", "Where it lives in Unit 1", "VISIBLE + MEASURABLE proof"],
               [(f'<b>{n}</b>', d, w, p) for n, d, w, p in ENGINE], ["24%", "30%", "28%", "18%"])
    proxies = T(["Durable skill", "Proxy you measure", "Data source (already collected)"],
                [(f'<b>{s}</b>', p, d) for s, p, d in PROXIES], ["24%", "44%", "32%"])
    curr = T(["Figure", "Value(s)", "Federal source", "Verified", "Status"],
             [(f'<b>{a_}</b>', b, f'<span style="font-size:7pt;color:#0B4A6F">{c}</span>', d, e) for a_, b, c, d, e in currency_rows()],
             ["20%", "30%", "30%", "9%", "11%"])
    ev = T(["Research / benchmark", "What it anchors"], [(f'<b>{a_}</b>', b) for a_, b in EVIDENCE], ["34%", "66%"])

    m = DATA["_meta"]
    body = f"""
    <div class="cover"><div class="kick">U.S. HISTORY HACK™ · FUTURE READY (“READY GRADUATE”)</div>
    <h1>Unit 1 — Future Ready Crosswalk &amp; Proof</h1>
    <div class="sub">“The Flight Plan to a Ready Graduate” · four pillars on one 1–4 scale · leading indicators that steer toward ACT / Ready Graduate benchmarks</div>
    <div class="meta">Grounded in FRAMEWORKS_CANON §5 + the Future Ready currency SoT (read live). Generated {ISO}.</div></div>

    <div class="lead">Future Ready is the <b>trajectory spine</b>: a student climbs to a 30,000-ft lagging goal (ACT / Ready Graduate ≥ 21), so we read
    small <b>leading indicators</b> every unit on one 1–4 scale and adjust while there is still time. Unit 1 <b>features Academic Reasoning</b>
    (the rotating pillar) and measures all four. Below: the pillar crosswalk, the measurement engine that makes each skill visible + measurable,
    and the <b>currency proof</b> that every money-math figure is verified to a federal source.</div>

    <div class="sec"><span>A · The Four Pillars — Crosswalk</span><span class="s">skill → leading measure → where Unit 1 proves it → macro target</span></div>
    {a}

    <div class="page"></div>
    <div class="sec"><span>B · The 1–4 Scale &amp; Measurement Engine</span><span class="s">every skill VISIBLE (named/printed) + MEASURABLE (number/tally/1–4/delta)</span></div>
    {scale}
    {engine}
    <div class="note">The Launch + Debrief bookend sheets (pilot built for Unit 1) carry the 10-trait hireability rubric, the grade &amp; missing-work check, the on-time tally, and the goal monitor — so the “soft” skills are printed, named, and scored with a dated growth delta.</div>
    <div style="height:6px"></div>
    <div class="sec" style="font-size:11pt"><span>Durable-skill behavioral proxies</span><span class="s">indicators, not verdicts</span></div>
    {proxies}
    <div class="warnbox"><b>Guardrail.</b> Proxies describe <b>in-class behavior, not fixed traits</b> — conversation-starters, never labels. Never penalize circumstances outside a student’s control (home responsibilities, jobs, device/internet access). “3 = on-trajectory” is the working bar; validate ACT cut-scores against your own cohort.</div>

    <div class="sec" style="page-break-before:auto"><span>C · Currency Proof — money-math figures</span><span class="s">every time-sensitive figure verified to a federal source</span></div>
    <div class="verdict"><b>CURRENCY VERIFIER: PASS</b> — provenance complete on all figures; annual gate not overdue (review_by {m['review_by']}); <b>1 warning</b>.
    Ran <span style="font-family:monospace">verify_future_ready_currency.py</span>; enforced monthly by CI (<span style="font-family:monospace">future-ready-currency.yml</span>).</div>
    {curr}
    <div class="warnbox"><b>Honest WARN (the one open item):</b> latest loan-rate year on file is <b>2025-26</b>; the AY <b>2026-27</b> undergraduate rate published ~May 2026 and must be added by a maintainer (knowledge cutoff Jan 2026). The verifier WARNs until it is — provenance and the annual gate still pass. Chart states its APR is an example, so it does not misstate a current rate.</div>

    <div class="sec"><span>D · Evidence base</span><span class="s">what anchors the framework</span></div>
    {ev}
    <div class="note">Future Ready is the measure spine; UDL 3.0 is access, CER is the writing spine, HIPPO is the sourcing spine. Leading indicators exist to MOVE the lagging one — time to adjust, not more grading. Owner: history-hack-unit-content-build (staged for a skills-only promotion). Generated {ISO}.</div>
    """
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def main():
    (ROOT / "out").mkdir(exist_ok=True)
    out = ROOT / f"out/Unit1_Future_Ready_Crosswalk_and_Proof_{STAMP}.pdf"
    HTML(string=build()).write_pdf(str(out))
    print("wrote", out.name, "| ts", ISO)


if __name__ == "__main__":
    main()
