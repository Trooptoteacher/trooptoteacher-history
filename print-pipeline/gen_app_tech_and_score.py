#!/usr/bin/env python3
"""Two print-first crosswalks (WeasyPrint, no docx):
  1. Unit1_App_Technology_HighImpact_Crosswalk.pdf — PROOF that each app feature is an
     INTENTIONAL high-impact choice: feature → SAMR/PICRAT (kind) → named strategy +
     Hattie d ≥ 0.40 (the value proof) → framework served → why print can't (the gate)
     → evidence-based research. Grounded in PRODUCT_MODEL_DOCTRINE / FRAMEWORKS_CANON.
  2. Unit1_ScheduleF_ScoreLift_Crosswalk.pdf — the plan to raise the Schedule F self-score
     from 82.7% (43/52) to ≥90%: action → indicator(s) fixed → current→target → +points →
     effort → owner → running total, with the 90% line marked.
"""
from datetime import datetime, timezone
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
TS = datetime.now(timezone.utc); ISO = TS.strftime("%Y-%m-%dT%H:%M:%SZ"); STAMP = TS.strftime("%Y%m%d_%H%M")
NAVY, NAVY2, RED, GOLD, CARD, LIGHT, BORDER, INK, GRN = \
    "#1F3A5F", "#2C3E63", "#B22234", "#C9A227", "#F8F5EF", "#EEF2F8", "#C9C2B4", "#20262E", "#1B5E20"

CSS = """
* { box-sizing:border-box; }
body { font-family:'DejaVu Sans', Arial, sans-serif; color:%(INK)s; margin:0; font-size:8.2pt; line-height:1.32; }
.cover { background:%(NAVY)s; color:#fff; padding:18px 22px; border-left:12px solid %(RED)s; }
.cover .kick { color:%(GOLD)s; font-weight:bold; letter-spacing:1px; font-size:9.5pt; }
.cover h1 { font-size:19pt; margin:5px 0 3px; }
.cover .sub { color:#DCE6F1; font-size:9.5pt; }
.cover .meta { color:#AFC0D6; font-size:7.6pt; margin-top:8px; }
.sec { color:%(NAVY)s; border-bottom:2px solid %(GOLD)s; padding-bottom:3px; margin:12px 0 6px; font-size:12pt; }
.sec .s { color:#5C6470; font-size:8pt; font-weight:normal; margin-left:6px; }
table { border-collapse:collapse; width:100%%; margin-bottom:4px; }
th { background:%(NAVY)s; color:#fff; text-align:left; padding:5px 6px; font-size:7.6pt; vertical-align:top; }
td { border:0.5pt solid %(BORDER)s; padding:5px 6px; font-size:8pt; vertical-align:top; }
tbody tr:nth-child(even) td { background:%(CARD)s; }
tr { page-break-inside:avoid; }
.d { color:%(RED)s; font-weight:bold; }
.tag { font-size:6.8pt; font-weight:bold; padding:1px 5px; border-radius:8px; background:%(LIGHT)s; color:%(NAVY2)s; }
.gate { background:#E4F0E5; color:#1B5E20; font-weight:bold; font-size:6.8pt; padding:1px 6px; border-radius:8px; }
.cross { background:#FBEFD6; }
.cross td { border-top:1.5pt solid %(GOLD)s; border-bottom:1.5pt solid %(GOLD)s; }
.lead { font-size:8.8pt; margin:8px 2px; } .lead b { color:%(NAVY)s; }
.note { font-size:7.4pt; color:#5C6470; font-style:italic; margin-top:3px; }
.verdict { background:#E4F0E5; border:1.5pt solid %(GRN)s; border-radius:6px; padding:8px 12px; margin:5px 0; font-size:8.8pt; }
.verdict b { color:%(GRN)s; }
@page { size:Letter landscape; margin:1.3cm;
  @bottom-right { content:"© 2026 TroopToTeacher Technologies LLC · p. " counter(page); font:7.5pt 'DejaVu Sans'; color:#5C6470; } }
""" % dict(INK=INK, NAVY=NAVY, NAVY2=NAVY2, RED=RED, GOLD=GOLD, CARD=CARD, LIGHT=LIGHT, BORDER=BORDER, GRN=GRN)


def table(headers, rows, widths, rowcls=None):
    cg = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>"
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = ""
    for i, r in enumerate(rows):
        rc = f' class="{rowcls[i]}"' if rowcls and rowcls[i] else ""
        body += f"<tr{rc}>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return f'<table>{cg}<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


# ---- App technology intentional-use crosswalk ----
APP = [
    ("Parallel test-data analytics", "Live roll-ups of the 5,041-item IRT bank at district · PLC · teacher · student",
     "SAMR Redefinition · PICRAT Transform", "Providing formative evaluation <b>d≈0.48</b>; Feedback <b>d≈0.70</b>",
     "Future Ready (measure)", "Can’t aggregate/roll up live cross-class response data", "Black &amp; Wiliam 1998; Hattie"),
    ("Real-time standard mastery", "Per-student, per-standard mastery (US.01–US.95) from the 3PL IRT bank",
     "SAMR Modification→Redefinition · PICRAT Transform", "Mastery learning <b>d≈0.57</b>; Feedback <b>d≈0.70</b>",
     "Future Ready (measure)", "No live mastery state to act on mid-lesson", "Bloom mastery learning; Hattie"),
    ("Reteaching / auto-remediation", "Gap auto-identified the moment it appears, routed to the right reteach",
     "SAMR Redefinition · PICRAT Transform", "Response to Intervention <b>d≈1.07</b>",
     "UDL 3.0 / MTSS", "Can’t branch per-student in real time", "Hattie (RTI); MTSS"),
    ("Lesson-plan builder", "Assembles a TEAM-aligned, pacing-fit plan; every activity tagged w/ strategy + effect size + UDL/MTSS → print ZIP",
     "SAMR Augmentation→Modification · PICRAT Amplify", "Teacher clarity <b>d≈0.75</b>; Collective teacher efficacy <b>d≈1.36</b>",
     "All frameworks", "Can’t recompute a plan to one teacher’s schedule", "Fendick; Eells/Hattie"),
    ("Gamification + spaced review", "Engagement mechanics driving distributed retrieval over time",
     "SAMR Modification · PICRAT Interactive", "Distributed (spaced) practice <b>d≈0.60</b>; retrieval practice",
     "Future Ready / CER", "Can’t schedule adaptive spacing", "Dunlosky 2013; Roediger &amp; Karpicke 2006"),
    ("Read-aloud (first-party TTS)", "On-demand audio for any passage or item; closed-loop, no link-out",
     "SAMR Augmentation · PICRAT Interactive", "UDL Representation access; Mayer <b>modality</b> effect",
     "UDL 3.0 (access)", "Paper can’t read text aloud", "CAST UDL 3.0 (2024); Mayer 2009"),
    ("Closed-loop first-party video", "Self-hosted instructional video — no recommendations, comments, ads, or link-outs",
     "SAMR Augmentation · PICRAT Interactive", "Multimedia learning; UDL Representation (image+narration+captions)",
     "UDL 3.0 (access) + child-safety", "Moving image + narration paper can’t deliver; CIPA/COPPA/FERPA", "Mayer 2009; CIPA/COPPA/FERPA"),
    ("IRT 3PL item bank (5,041)", "Pre-field-test-parameterized items; FERPA/COPPA-safe calibration that field-calibrates as data accrues",
     "SAMR Redefinition · PICRAT Transform", "Adaptive precision → formative evaluation <b>d≈0.48</b>",
     "Future Ready (measure)", "Paper can’t IRT-calibrate or adapt difficulty", "Item Response Theory (Lord; Hambleton)"),
]


def app_html():
    rows = [(f"<b>{f}</b>", w, f'<span class="tag">{k}</span>', st, fr, f'<span class="gate">PRINT CAN’T:</span> {pc}', rs)
            for f, w, k, st, fr, pc, rs in APP]
    tbl = table(["App feature", "What it does", "Kind (SAMR / PICRAT)", "High-impact strategy (Hattie d) — the value proof", "Framework served", "Why print can’t (the Educational-Impact Gate)", "Evidence / research"],
                rows, ["13%", "18%", "13%", "18%", "10%", "16%", "12%"])
    body = f"""
    <div class="cover"><div class="kick">U.S. HISTORY HACK™ · INTENTIONAL-TECH PROOF</div>
    <h1>App Technology — Intentional High-Impact Use Crosswalk</h1>
    <div class="sub">Every app feature proven as a deliberate, evidence-based choice — not tech for tech’s sake</div>
    <div class="meta">Grounded in PRODUCT_MODEL_DOCTRINE + FRAMEWORKS_CANON. Generated {ISO}.</div></div>

    <div class="lead">Each feature must pass the <b>three-question intentionality gate</b> before it earns a screen:
    <b>Q1 — what kind of integration?</b> (SAMR/PICRAT — descriptor only, <i>not</i> proof) · <b>Q2 — does it clear the Educational-Impact Gate?</b>
    (a named high-impact strategy with an effect size ≥ Hattie’s hinge <b>d≈0.40</b> that print physically can’t deliver — <i>this</i> is the value proof) ·
    <b>Q3 — which framework does it serve?</b> (UDL 3.0 access · CER/HIPPO performance · Future Ready measure). No framework + no gate → it’s a paper question in disguise and stays on paper.</div>

    <div class="sec"><span>The crosswalk</span><span class="s">feature → kind → strategy + effect size → framework → why print can’t → research</span></div>
    {tbl}
    <div class="note"><b>Anti-overuse rule (LOCKED):</b> all technology must exclusively bring value and prove it with evidence; used only if it cannot be done in print. SAMR/TPACK/PICRAT describe the <i>move</i>; the Educational-Impact Gate (Q2) proves it earns the screen. Every row above clears Q1–Q3 — that is the proof of intentional, high-impact use. Effect sizes are Hattie <i>Visible Learning</i> meta-analytic averages unless a specific study is named; local results calibrate as data accrues.</div>
    """
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


# ---- Score-lift crosswalk (82.7% -> 90%+) ----
# (action, indicators fixed, cur->tgt, +pts, effort, owner)
BASE_PTS = 43; MAXP = 52
STEPS = [
    ("Produce a NIMAS-compliant file set", "4.2 NIMAS", "0 → 2", 2, "Med", "accessibility-qc-agent + production"),
    ("Run WCAG 2.2 AA gate on digital + remediate", "4.1 ADA/WCAG", "1 → 2", 1, "Med", "accessibility-qc-agent"),
    ("Build the printable Teacher Answer-Key PDF + pedagogy notes", "2.8 Teacher support", "1 → 2", 1, "Low", "tcap-deck-builder + unit-content-build"),
    ("Bring US.02–07 workbook prose to US.01 depth", "1.2 Depth of treatment", "1 → 2", 1, "Med", "history-hack-unit-content-build"),
    ("Test read-aloud with screen readers / alt input", "4.5 Assistive tech", "1 → 2", 1, "Low", "accessibility-qc-agent"),
    ("Capture functional-digital proof (mastery/analytics/reteach live)", "2.9 Digital integration", "1 → 2", 1, "Med", "district-edition + unit-qc"),
    ("Add a full 180-day pacing guide (review/assessment windows)", "2.7 Pacing", "1 → 2", 1, "Low", "instructional-design-specialist"),
    ("Add a dedicated cost-benefit economic-reasoning task", "3.6 Economic reasoning", "1 → 2", 1, "Low", "tn-content-specialist"),
]


def score_html():
    rows = []; rowcls = []; run = BASE_PTS; crossed = False
    for act, ind, ct, pts, eff, owner in STEPS:
        run += pts; pct = run / MAXP * 100
        mark = ""
        if pct >= 90 and not crossed:
            crossed = True; mark = " ✅ crosses 90%"; rowcls.append("cross")
        else:
            rowcls.append("")
        rows.append((f"<b>{act}</b>", ind, ct, f'<span class="d">+{pts}</span>', eff, owner,
                     f"<b>{run}/{MAXP}</b>", f"<b>{pct:.1f}%</b>{mark}"))
    tbl = table(["Action", "Indicator(s) fixed", "Score", "+pts", "Effort", "Owner skill", "Running total", "Overall %"],
                rows, ["27%", "15%", "7%", "5%", "6%", "18%", "9%", "13%"], rowcls=rowcls)
    final = (BASE_PTS + sum(s[3] for s in STEPS)); finalpct = final / MAXP * 100
    body = f"""
    <div class="cover"><div class="kick">U.S. HISTORY HACK™ · ADOPTION SCORE PLAN</div>
    <h1>Schedule F Score-Lift Crosswalk — 82.7% → 90%+</h1>
    <div class="sub">The exact, prioritized path from 43/52 to ≥ 47/52 (RECOMMENDED with margin)</div>
    <div class="meta">Built from the Unit 1 Schedule F deficiency memo. Each step still must produce the stated evidence to earn the 2. Generated {ISO}.</div></div>

    <div class="verdict"><b>Start: 43/52 = 82.7% (RECOMMENDED).</b> &nbsp; The 90% line = <b>46.8/52</b> → need <b>47/52 = 90.4%</b> (a +4-point gain).
    The first three actions below (highest leverage, low/med effort) reach it; completing all eight reaches <b>{final}/{MAXP} = {finalpct:.1f}%</b>.</div>

    <div class="sec"><span>The prioritized plan</span><span class="s">ordered by points-per-effort; the row that crosses 90% is highlighted</span></div>
    {tbl}
    <div class="lead"><b>Reading it:</b> actions are ordered by leverage. <b>NIMAS (+2)</b> is the single biggest lever; adding the <b>WCAG pass (+1)</b> and the
    <b>teacher answer-key PDF (+1)</b> crosses the 90% line at <b>47/52 (90.4%)</b>. The remaining five actions build margin toward 100%.</div>
    <div class="note">Honest framing: these are self-score <i>projections</i>. A projected 2 is only earned once the evidence exists (a real NIMAS file, a passing WCAG report, the built answer key, etc.). None of the eight is a values or accuracy fix — the material already clears the gateways; this is production + accessibility completion. Verbatim rubric cross-check against the official TDOE HS Social Studies rubric is still pending (tn.gov PDF blocked in this environment).</div>
    """
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def main():
    (ROOT / "out").mkdir(exist_ok=True)
    HTML(string=app_html()).write_pdf(str(ROOT / "out/Unit1_App_Technology_HighImpact_Crosswalk.pdf"))
    HTML(string=score_html()).write_pdf(str(ROOT / "out/Unit1_ScheduleF_ScoreLift_Crosswalk.pdf"))
    print("wrote app-tech + score-lift crosswalks | ts", ISO)


if __name__ == "__main__":
    main()
