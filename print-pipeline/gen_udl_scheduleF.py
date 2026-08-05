#!/usr/bin/env python3
"""Two print-first deliverables (WeasyPrint, no docx):
  1. Unit1_UDL_in_Action.pdf — expanded UDL: the full stack lesson-plan→student's desk,
     a two-lens (Teacher ∥ Student) minute-by-minute lesson walkthrough, and the
     evidence base (Hattie d, Rosenshine, CAST UDL 3.0, Mayer, Black & Wiliam, Dunlosky,
     Roediger, McNeill & Krajcik).
  2. Unit1_Schedule_F_SelfScore_<ts>.pdf — TDOE Social Studies scoring rubric (the real
     4 tables / 26 indicators, 0-1-2) self-scored HONESTLY with proof + a deficiency memo.
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
body { font-family:'DejaVu Sans', Arial, sans-serif; color:%(INK)s; margin:0; font-size:9pt; line-height:1.4; }
.cover { background:%(NAVY)s; color:#fff; padding:20px 24px; border-left:12px solid %(RED)s; }
.cover .kick { color:%(GOLD)s; font-weight:bold; letter-spacing:1px; font-size:10pt; }
.cover h1 { font-size:22pt; margin:6px 0 4px; }
.cover .sub { color:#DCE6F1; font-size:10.5pt; }
.cover .meta { color:#AFC0D6; font-size:8pt; margin-top:10px; }
.sec { color:%(NAVY)s; border-bottom:2px solid %(GOLD)s; padding-bottom:3px; margin:14px 0 7px; font-size:13pt; }
.sec .s { color:#5C6470; font-size:8pt; font-weight:normal; margin-left:6px; }
table { border-collapse:collapse; width:100%%; margin-bottom:5px; }
th { background:%(NAVY)s; color:#fff; text-align:left; padding:5px 7px; font-size:8pt; vertical-align:top; }
td { border:0.5pt solid %(BORDER)s; padding:5px 7px; font-size:8.4pt; vertical-align:top; line-height:1.32; }
tbody tr:nth-child(even) td { background:%(CARD)s; }
tr { page-break-inside:avoid; }
.page { page-break-before:always; }
.d { color:%(RED)s; font-weight:bold; }
.two td.tch { background:%(LIGHT)s; }
.two td.stu { background:#FBF6EC; }
.two th.tch { background:%(NAVY)s; } .two th.stu { background:%(NAVY2)s; }
.chip { font-size:7pt; font-weight:bold; padding:1px 6px; border-radius:8px; white-space:nowrap; }
.s2 { color:#1B5E20; background:#E4F0E5; } .s1 { color:#8A5A00; background:#FBEFD6; } .s0 { color:#8B1E2D; background:#F7E1E4; }
.verdict { background:#E4F0E5; border:1.5pt solid %(GRN)s; border-radius:6px; padding:10px 14px; margin:6px 0; }
.verdict b { color:%(GRN)s; }
.gap { background:#FBEFD6; border-left:4px solid %(GOLD)s; padding:7px 11px; margin:5px 0; font-size:8.6pt; }
.note { font-size:7.8pt; color:#5C6470; font-style:italic; }
.lead { font-size:9.2pt; margin:8px 2px; }
.lead b { color:%(NAVY)s; }
@page { size:Letter portrait; margin:0.6in 0.6in 0.7in 0.6in;
  @bottom-right { content:"© 2026 TroopToTeacher Technologies LLC · p. " counter(page); font:7.5pt 'DejaVu Sans'; color:#5C6470; } }
""" % dict(INK=INK, NAVY=NAVY, NAVY2=NAVY2, RED=RED, GOLD=GOLD, CARD=CARD, LIGHT=LIGHT, BORDER=BORDER, GRN=GRN)


def tbl(headers, rows, cls="", widths=None, hcls=None):
    cg = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>" if widths else ""
    hc = hcls or [""] * len(headers)
    head = "".join(f'<th class="{hc[i]}">{h}</th>' for i, h in enumerate(headers))
    body = "".join("<tr>" + "".join(f'<td class="{c[0]}">{c[1]}</td>' if isinstance(c, tuple) else f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}">{cg}<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


# ---------------- Deliverable 1: UDL in Action ----------------
STACK = [
    ("① Lesson-Plan Builder", "Teacher assembles the lesson; each activity is tagged with its high-impact strategy + effect size + UDL/MTSS support; outputs a print ZIP.",
     "Provides multiple means by design; teacher picks against TEAM rubric + pacing.", "Receives one coherent, standards-aligned lesson — no guesswork.",
     "Teacher clarity <b>d≈0.75</b>; Collective teacher efficacy <b>d≈1.36</b>"),
    ("② Teacher Lecture Deck", "I-do/we-do slides, EN/ES word wall, primary sources, teacher-cue boxes, two-slide click-reveal checks.",
     "Models expert thinking aloud; signals what matters (ZOOM-IN).", "Sees + hears content in multiple representations; watches the model before trying.",
     "Direct instruction <b>d≈0.60</b>; Worked examples <b>d≈0.57</b>; Mayer signaling"),
    ("③ Student Workbook", "Guided Cornell (25/75), Close-Read TDQs, Primary-Source HIPPO, CER apply, vocab table.",
     "Facilitates; releases responsibility gradually.", "Organizes notes, analyzes sources, writes an argument on paper.",
     "Concept mapping <b>d≈0.64</b>; CER (McNeill &amp; Krajcik); note-taking"),
    ("④ Graphic-Organizer Toolkit", "Best-fit reproducible organizers (Venn, cause-effect, HIPPO, CER, TN Connection).",
     "Assigns the right organizer for the thinking task.", "Makes thinking visible; multiple means of action &amp; expression.",
     "Graphic organizers / concept mapping <b>d≈0.64</b>"),
    ("⑤ The Platform (App)", "Read-aloud (first-party), real-time standard mastery, district/PLC/teacher/student analytics, auto-reteach, gamified spaced review.",
     "Monitors the live roll-up; acts on mastery mid-lesson.", "Gets instant feedback, text read aloud, and a reteach the moment they miss.",
     "Feedback <b>d≈0.70</b>; RTI <b>d≈1.07</b>; Spaced practice <b>d≈0.60</b>; Formative eval <b>d≈0.48</b>"),
    ("⑥ Assessment", "Formative checkpoints (per standard) + parallel summative Forms A/B + the DBQ essay.",
     "Uses results to reteach or extend; multiple item types.", "Shows learning several ways; retrieval strengthens memory.",
     "Formative assessment (Black &amp; Wiliam) <b>d≈0.48</b>; Practice testing (Roediger)"),
]

LESSON = [
    ("Retrieval warm-up", "Projects a DOK-1 confidence check on the prior standard; 30-sec solo, then reveal.",
     "Answers a low-stakes recall; earns an early win; surfaces a shaky spot.",
     "Engagement — self-regulation", "Retrieval practice (Roediger &amp; Karpicke, 2006); Spaced practice <b>d≈0.60</b>"),
    ("Hook", "Poses the Essential Question; runs 10-sec think → 60-sec Turn &amp; Talk → cold-calls 2–3 pairs.",
     "Thinks, then talks it through with a partner using a sentence starter.",
     "Engagement — recruit interest", "Classroom discussion <b>d≈0.82</b>"),
    ("Vocabulary front-load", "Pre-teaches the 2 flagged terms — EN/ES, pronunciation respelling, a visual anchor.",
     "Anchors the terms; dual-codes with the initials chip; hears the word.",
     "Representation — language &amp; symbols", "Vocabulary programs <b>d≈0.62</b>; Mayer dual-coding"),
    ("I do (direct instruction)", "Thinks aloud through the content + a primary source using the teacher-cue box.",
     "Watches the expert model; annotates the source; follows the ZOOM-IN cue.",
     "Representation — build knowledge", "Direct instruction <b>d≈0.60</b>; Worked examples <b>d≈0.57</b>"),
    ("We do (guided practice)", "Models one CER/HIPPO prompt, then “now you try” with support still up.",
     "Practices with the frame + word bank; gets corrective feedback.",
     "Action &amp; Expression — executive function", "Rosenshine guided practice; Scaffolding + fading"),
    ("You do (apply)", "Circulates; gives targeted feedback; keeps scaffolds faded for later sources.",
     "Writes a CER on paper; self-grades on the printed rubric.",
     "Action &amp; Expression — expression", "Feedback <b>d≈0.70</b>; CER (McNeill &amp; Krajcik)"),
    ("Workbook ⇄ app handoff", "Has students enter the CER for real-time feedback + read-aloud, then revise.",
     "Receives instant feedback, hears it read aloud, revises the argument.",
     "All three principles", "Feedback <b>d≈0.70</b>; Formative evaluation <b>d≈0.48</b>"),
    ("Check + reteach", "Reads the live mastery roll-up; small-groups the students who missed.",
     "If they missed, the app auto-routes the reteach; re-attempts to mastery.",
     "Engagement — sustain effort", "Response to Intervention <b>d≈1.07</b>; Feedback <b>d≈0.70</b>"),
]

EVIDENCE = [
    ("Response to Intervention", "Hattie, <i>Visible Learning</i>", "d≈1.07", "App auto-reteach routes missers to targeted support"),
    ("Collective teacher efficacy", "Eells / Hattie", "d≈1.36", "Lesson-plan builder + PLC-level mastery roll-ups"),
    ("Classroom discussion", "Hattie", "d≈0.82", "Turn &amp; Talk hooks; cold-call routine"),
    ("Teacher clarity", "Fendick / Hattie", "d≈0.75", "“I can” + success criteria + teacher-cue boxes"),
    ("Feedback", "Hattie", "d≈0.70", "App real-time feedback + printed-rubric self-grade"),
    ("Concept mapping / organizers", "Hattie", "d≈0.64", "Organizer toolkit + guided Cornell notes"),
    ("Vocabulary programs", "Hattie", "d≈0.62", "EN/ES word wall — taught, practiced, assessed"),
    ("Direct instruction", "Hattie", "d≈0.60", "Teacher deck I-do think-alouds"),
    ("Distributed (spaced) practice", "Dunlosky et al. 2013; Hattie", "d≈0.60 · high-utility", "Gamified spaced review; Quick-Review slides"),
    ("Worked examples", "Sweller; Hattie", "d≈0.57", "We-do modeled CER / HIPPO"),
    ("Formative assessment", "Black &amp; Wiliam 1998; Hattie", "d≈0.48", "Per-standard checkpoints + live mastery meter"),
    ("Retrieval practice (testing effect)", "Roediger &amp; Karpicke 2006", "robust LT retention", "Confidence-check warm-ups + formative checks"),
    ("CER argumentation", "McNeill &amp; Krajcik 2012", "raises argument quality", "Workbook CER + DBQ essay + rubric"),
    ("Universal Design for Learning", "CAST Guidelines 3.0 (2024)", "expert, self-directed learners", "Embedded across deck, workbook, DBQ, app"),
    ("Multimedia learning", "Mayer 2009", "lowers cognitive load", "Signaling (ZOOM-IN), dual-coding chips"),
    ("Principles of Instruction", "Rosenshine 2012", "10 research-based principles", "Review→model→guide→check→independent arc"),
]


def udl_html():
    stack = tbl(["Layer (lesson-plan → desk)", "What it is", "What the teacher does", "What the student receives", "Evidence (effect size)"],
                [(l, w, t, s, e) for l, w, t, s, e in STACK], widths=["16%", "26%", "20%", "20%", "18%"])
    lesson = tbl(["Phase", "Teacher does", "Student receives", "UDL principle", "Pedagogy evidence"],
                 [(("", p), ("tch", t), ("stu", s), ("", u), ("", e)) for p, t, s, u, e in LESSON],
                 cls="two", widths=["13%", "24%", "24%", "17%", "22%"],
                 hcls=["", "tch", "stu", "", ""])
    ev = tbl(["High-value strategy", "Research source", "Finding", "Where Unit 1 uses it"],
             [(("", a), ("", b), (("d", c) if c.startswith("d") else ("", c)), d) for a, b, c, d in EVIDENCE],
             widths=["24%", "22%", "16%", "38%"])
    body = f"""
    <div class="cover"><div class="kick">U.S. HISTORY HACK™ · TEACHER + STUDENT REALITY</div>
    <h1>UDL 3.0 in Action — From the Lesson Plan to the Student’s Desk</h1>
    <div class="sub">Unit 1 · How the print + platform tools work together in the classroom — and how a student receives them · evidence-backed</div>
    <div class="meta">Every move is tied to a UDL 3.0 principle (CAST 2024) and a high-value research finding. Effect sizes are Hattie <i>Visible Learning</i> meta-analytic averages (hinge d≈0.40) unless a specific study is named. Generated {ISO}.</div></div>

    <div class="lead">UDL here is not a worksheet you add — it is <b>the architecture of the whole lesson</b>. The teacher assembles the plan, the deck models,
    the workbook makes thinking visible, and the platform gives feedback, read-aloud, and reteach in real time. Below: the full stack top-to-bottom,
    then a single Unit 1 lesson through <b>both</b> lenses, then the research that backs each move.</div>

    <div class="sec"><span>The full stack</span><span class="s">where UDL lives, lesson-plan → desk</span></div>
    {stack}

    <div class="page"></div>
    <div class="sec"><span>One Unit 1 lesson — Teacher ∥ Student</span><span class="s">the same 45 minutes, both lenses</span></div>
    {lesson}
    <div class="note">Left = what the teacher does; right = what the student experiences at the same moment. The lesson follows the gradual-release arc
    (I do → we do → you do) with scaffolds that fade — exactly the Rosenshine sequence.</div>

    <div class="page"></div>
    <div class="sec"><span>The evidence base</span><span class="s">high-value research behind every tool</span></div>
    {ev}
    <div class="lead" style="margin-top:8px"><b>The seamless loop:</b> write a CER on paper → self-grade on the printed rubric → enter it in the app for real-time feedback + read-aloud → revise;
    miss a check → the mastery meter auto-routes the reteach while you watch the roll-up. Every video is first-party, self-hosted, closed-loop (CIPA/COPPA/FERPA).
    <b>Tech-value rule:</b> each tool earns its place only by adding what paper can’t — the anti-overuse standard. The page always stands alone; the app raises the ceiling.</div>
    """
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


# ---------------- Deliverable 2: Schedule F self-score ----------------
# (score, evidence/proof, justification) — HONEST self-grade; not all 2s.
T1 = [  # Alignment of Content (per US.01–07 group)
    ("1.1 Standard Coverage", 2, "Coverage crosswalk: 7/7 standards directly addressed across deck, workbook, DBQ, and the 56-item bank.", "All US.01–07 knowledge + skills covered."),
    ("1.2 Depth of Treatment", 1, "US.01 workbook prose is hand-authored/deep; US.02–07 workbook prose is a generated skeleton (deck + DBQ carry full depth).", "Depth strong in deck/DBQ; workbook-prose parity is a known enhancement."),
    ("1.3 Accuracy", 2, "Content sourced from locked repo data + verified public-domain primaries; no known error.", "Historian fact-check full pass still scheduled (see memo)."),
    ("1.4 Sequence Alignment", 2, "Scope-and-sequence places Unit 1 (industrialization, 1877–1900) first, US.01–07 in order.", "Matches TN pacing."),
    ("1.5 Assessment Alignment", 2, "56 items tagged to standard + DOK; formative per standard + parallel summative; assessment crosswalk.", "Assessments measure the standard taught."),
]
T2 = [  # Instructional Focus (9)
    ("2.1 Rigor", 2, "DBQ essay (DOK 3–4) + CER every standard; DOK ramp in deck wrap-ups.", "Fixed-form bank DOK-3 concentrates in US.06/07 (memo)."),
    ("2.2 Higher-Order Thinking", 2, "Close-Read, HIPPO, CER, DBQ are majority analysis/eval/synthesis.", "Higher-order ≥50% of activities."),
    ("2.3 Primary Sources", 2, "DBQ: 8 verified documents with scaffolded HIPPO/OPTIC; deck + workbook primaries.", "Systematic, not decorative."),
    ("2.4 Vocabulary", 2, "EN/ES word wall taught (pronunciation, dual-code), workbook vocab table, assessed in bank.", "Taught + practiced + assessed."),
    ("2.5 Differentiation", 2, "EN/ES, faded scaffolds, DBQ scaffold companion, organizer toolkit, DOK ramp, MTSS guide.", "Comprehensive — a differentiator."),
    ("2.6 Assessment", 2, "Formative checkpoints + summative Forms A/B + DBQ; multiple item types.", "Robust, standards-aligned."),
    ("2.7 Pacing", 1, "10-unit scope-sequence exists; full 180-day pacing guide with review/assessment windows not proven in this Unit 1 set.", "Partial — see memo."),
    ("2.8 Teacher Support", 1, "Teacher deck + MTSS guide + reteach routing present; the printable teacher answer-key PDF + deeper pedagogy notes still pending.", "Partial — see memo."),
    ("2.9 Digital Integration", 1, "Platform (analytics/mastery/reteach/read-aloud) is described and built at platform level; not demonstrated functional inside this print artifact set.", "Partial — needs functional proof."),
]
T3 = [  # SSPs (7)
    ("3.1 Sourcing", 2, "DBQ HIPPO/OPTIC on every document + deck Source-It-First WHO/WHEN/WHY.", "Systematic sourcing."),
    ("3.2 Contextualization", 2, "Deck DI + workbook Close-Read supply historical context per standard.", "Consistent."),
    ("3.3 Corroboration", 2, "DBQ evidence-planning compares 8 documents across three perspectives.", "2+ sources per key topic."),
    ("3.4 Close Reading", 2, "Structured Close-Read TDQ protocol + DBQ annotation frames.", "Structured protocol present."),
    ("3.5 Argumentation", 2, "CER every standard + DBQ essay + 5-criterion rubric.", "Claim-evidence-reasoning throughout."),
    ("3.6 Economic Reasoning", 1, "DBQ ‘progress for whom’ cost-benefit + US.04/05 content; a dedicated, systematic economic-reasoning strand is lighter.", "Present but not systematic (memo)."),
    ("3.7 Geographic Reasoning", 2, "Railroad + foreign-born maps analyzed for cause-effect; US.06 industrial centers.", "Integrated, not decorative."),
]
T4 = [  # Accessibility (5)
    ("4.1 ADA / WCAG", 1, "Print materials: adequate font/contrast/layout (verified). Digital WCAG 2.1 AA audit not yet run this cycle (accessibility-qc-agent gate).", "Print OK; formal digital audit pending (memo)."),
    ("4.2 NIMAS", 0, "No NIMAS-format file set produced yet.", "Genuine gap — must produce NIMAS files."),
    ("4.3 UDL Principles", 2, "UDL one-pager + embedded supports across all three principles in deck, workbook, DBQ, app.", "Comprehensive."),
    ("4.4 Multilingual Support", 2, "EN/ES throughout, DBQ EN/ES word bank, visual supports, scaffolded language.", "Robust EL support."),
    ("4.5 Assistive-Tech Compatibility", 1, "Read-aloud planned/first-party; not yet tested with screen readers / alt input this cycle.", "Testing pending (memo)."),
]


def score_table(title, rows, maxpts):
    got = sum(s for _, s, _, _ in rows)
    body = ""
    for ind, s, ev, just in rows:
        cls = {0: "s0", 1: "s1", 2: "s2"}[s]
        body += (f'<tr><td><b>{ind}</b></td><td style="text-align:center"><span class="chip {cls}">{s}</span></td>'
                 f'<td>{ev}</td><td>{just}</td></tr>')
    pct = got / maxpts * 100
    head = (f'<div class="sec" style="font-size:11.5pt"><span>{title}</span>'
            f'<span class="s">subtotal {got}/{maxpts} = {pct:.1f}%</span></div>')
    table = (f'<table><colgroup><col style="width:23%"><col style="width:7%"><col style="width:44%"><col style="width:26%"></colgroup>'
             f'<thead><tr><th>Indicator</th><th>Score</th><th>Evidence / proof</th><th>Justification</th></tr></thead><tbody>{body}</tbody></table>')
    return head + table, got, maxpts


def scheduleF_html():
    sections = ""
    total = 0; mx = 0
    for title, rows, m in [("Table 1 — Alignment of Content", T1, 10), ("Table 2 — Instructional Focus", T2, 18),
                            ("Table 3 — Social Studies Practices (SSPs)", T3, 14), ("Table 4 — Accessibility Features", T4, 10)]:
        html_, g, mm = score_table(title, rows, m); sections += html_; total += g; mx += mm
    overall = total / mx * 100
    verdict = "RECOMMENDED" if overall >= 80 else ("REVISE AND RESUBMIT" if overall >= 60 else "NOT RECOMMENDED")

    gateways = tbl(["Gateway", "Result", "Evidence"],
                   [("Standards coverage (all Met/Partial)", ("d", "PASS"), "7/7 standards Met — coverage crosswalk"),
                    ("Factual accuracy (Policy 2.600)", ("d", "PASS"), "Sourced content; no known error (full historian pass scheduled)"),
                    ("Values / bias (Policy 2.600)", ("d", "PASS"), "Balanced; sensitive documents framed historian-grade, no conclusion handed to students"),
                    ("No prohibited concepts (TCA §49-6-1019)", ("d", "PASS"), "Analytical, evidence-based; students weigh documented intent + consequences")],
                   widths=["40%", "12%", "48%"])

    memo = """
    <div class="gap"><b>4.2 NIMAS (score 0 → +2 possible, +3.8 pts overall).</b> Produce a NIMAS-format file set. Largest single lever.</div>
    <div class="gap"><b>2.9 Digital / 4.1 WCAG / 4.5 Assistive tech (three 1s).</b> Run the accessibility-qc-agent WCAG 2.2 AA gate, test read-aloud with screen readers, and capture functional-digital proof. (+ up to 3 pts.)</div>
    <div class="gap"><b>1.2 Depth / 2.8 Teacher support (two 1s).</b> Bring US.02–07 workbook prose to US.01 depth; build the printable teacher answer-key PDF + pedagogy notes. (+ up to 2 pts.)</div>
    <div class="gap"><b>2.7 Pacing / 3.6 Economic reasoning (two 1s).</b> Add a full 180-day pacing guide with review/assessment windows; add a dedicated cost-benefit economic-reasoning task. (+ up to 2 pts.)</div>
    """

    body = f"""
    <div class="cover"><div class="kick">U.S. HISTORY HACK™ · TDOE ADOPTION SELF-AUDIT</div>
    <h1>Schedule F — Social Studies Rubric Self-Score with Proof</h1>
    <div class="sub">Unit 1 (US.01–US.07) · TN Textbook &amp; Instructional Materials Quality Commission · TCA Title 49-6-22 · Policy 2.600</div>
    <div class="meta">Simulated TDOE panel self-audit — 0-1-2 scale across the four rubric tables (26 indicators). Scored HONESTLY: every 1 and 0 is a real, named gap. Generated {ISO}.</div></div>

    <div class="verdict"><b>OVERALL: {overall:.1f}%</b> &nbsp;→&nbsp; <b>{verdict}</b> &nbsp;·&nbsp; total {total}/{mx} points &nbsp;·&nbsp;
    standards coverage <b>100%</b> &nbsp;·&nbsp; gateways <b>PASS</b> &nbsp;·&nbsp; values <b>PASS</b>.
    <div class="note" style="margin-top:4px">Threshold: ≥80% + gateways passed → RECOMMENDED · 60–79.9% → revise · &lt;60% → not recommended. A values violation is a standalone FAIL regardless of score.</div></div>

    <div class="sec" style="font-size:11.5pt"><span>Gateway &amp; Values Checks</span><span class="s">must pass before rubric counts</span></div>
    {gateways}

    {sections}

    <div class="page"></div>
    <div class="sec"><span>Deficiency Memo — path to a higher score</span><span class="s">honest gaps, ranked by score impact</span></div>
    {memo}
    <div class="lead"><b>Bottom line.</b> Unit 1 self-scores <b>{overall:.1f}% → {verdict}</b> with 100% standards coverage and all gateways/values clear.
    The strengths (primary sources, differentiation, SSPs, UDL, multilingual, argumentation) are adoption-grade. The honest gaps are concentrated in
    accessibility artifacts (NIMAS, formal WCAG/assistive-tech testing) and a few production items (workbook-prose depth, teacher answer key, pacing guide,
    functional-digital proof) — none is a values or accuracy problem, and each has a clear fix above.</div>
    <div class="note" style="margin-top:6px">This is a self-audit, not a TDOE determination. It is deliberately conservative — where evidence is partial, the indicator is scored 1, not 2.
    Owner skill: tn-textbook-adoption-agent. Generated {ISO}.</div>
    """
    css = CSS.replace('content:"© 2026', 'content:"Schedule F Self-Score · © 2026')
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


def main():
    (ROOT / "out").mkdir(exist_ok=True)
    HTML(string=udl_html()).write_pdf(str(ROOT / "out/Unit1_UDL_in_Action_Teacher_Student_Journey.pdf"))
    HTML(string=scheduleF_html()).write_pdf(str(ROOT / f"out/Unit1_Schedule_F_SelfScore_{STAMP}.pdf"))
    print("wrote UDL-in-Action + Schedule-F self-score | ts", ISO)


if __name__ == "__main__":
    main()
