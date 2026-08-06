# -*- coding: utf-8 -*-
"""COURSE-PARAMETERIZED unit STUDENT WORKBOOK generator (print-first, no docx).

One generator, seven courses. Reads:
  - courses/<id>/course.json          (displayName, standardsPrefix, eocTestable, brand)
  - <course standardsFile>            (verbatim TDOE standard text + strands -> Lenses)
  - content/<id>/unit-NN.source.json  (authored content packs + unit meta)

...and emits content/<id>/unit-NN.json to the STUDENT_WORKBOOK_PLATINUM_STANDARD
7-activity anatomy, then hard-fails on verify_workbook_platinum.py. Renders via
render.py (WeasyPrint). U.S. History uses the dedicated gen_unit01.py; this is the
neutral path proven on World History and reused for Government / TN History / grades 6-8.

Course-binding walls honored (references/course-binding-and-walls.md): reads ONLY the
resolved course's standardsFile + content root; emits ONLY its prefix; no EOC framing
unless course.json eocTestable is true (W6).

Usage:
    python3 gen_unit.py world-history 1
"""
import base64
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent

LENS_NAME = {"C": "Culture", "E": "Economics", "G": "Geography",
             "H": "History", "P": "Politics/Government", "T": "Tennessee", "TCA": "Tennessee Code"}
SSP_TEXT = {
    "SSP.01": "Collect from sources (primary + secondary)",
    "SSP.02": "Examine a source (POV, purpose, bias; evidence vs. assertion)",
    "SSP.03": "Synthesize / compare sources (corroborate; find disparities)",
    "SSP.04": "Construct arguments (claim + evidence; cause/effect — CER)",
    "SSP.05": "Historical awareness (continuity & change; context; empathy)",
    "SSP.06": "Geographic awareness (place, region, spatial pattern, maps)",
}


def load_course(cid):
    return json.loads((REPO / "courses" / cid / "course.json").read_text())


def load_standards(course):
    sf = course.get("standardsFile")
    data = json.loads((REPO / sf).read_text())
    st = data["standards"] if isinstance(data, dict) else data
    return {s["code"]: s for s in st}


# ---------- per-standard activity builders (mirror the proven US anatomy) ----------

def opener(code, pack, std):
    lens = " · ".join(f"{c} {LENS_NAME.get(c, c)}" for c in std.get("strand", []))
    hook = pack["sections"][0]["content"].split(". ")[0] + "."
    return [
        {"type": "head", "text": "Opener", "sub": "before you learn"},
        {"type": "box", "label": "Learning target (I can…)", "paras": [pack["iCan"]]},
        {"type": "box", "label": "Lenses (this standard’s dimensions)", "paras": [lens]},
        {"type": "box", "label": "SET YOUR SMART GOAL — my short-term goal for this standard",
         "paras": ["Write a goal that is Specific · Measurable · Achievable · Relevant · Time-bound. "
                   "Example: “By Friday I can explain " + pack["title"].lower() + " using two pieces of evidence.”"]},
        {"type": "lines", "n": 2},
        {"type": "box", "label": "Hook — read this", "paras": [hook + " <em>What surprises you? What do you want to know?</em>"]},
        {"type": "box", "label": "Preview & Predict", "paras": ["Skim the standard. Predict who gained power and who lost it."]},
        {"type": "lines", "n": 2},
    ]


def act1_vocab(pack):
    rows = [[f"<strong>{t['term']}</strong>", t.get("def", ""), t.get("es", ""), ""] for t in pack["vocab"]]
    return [
        {"type": "head", "text": "Activity 1 · Vocabulary", "sub": "word bank + language support"},
        {"type": "table", "head": ["Term", "What it means", "Español", "Know it? (✓ / ? / new)"], "rows": rows},
        {"type": "box", "label": "Knowledge self-check", "paras": [
            "For each term mark ✓ (I can use it), ? (I’ve seen it), or new. Come back and re-mark after the lesson."]},
    ]


def act2_frayer(pack):
    term = pack["vocab"][0]["term"]
    return [
        {"type": "head", "text": "Activity 2 · Vocabulary Studio (Frayer)", "sub": "response choice"},
        {"type": "box", "label": f"Build a Frayer model for: {term}", "paras": [
            "Fill each quadrant. Then CONNECT THE TERMS: use two vocabulary words in one sentence (here or in your notebook)."]},
        {"type": "table", "class": "write", "head": ["Definition (your words)", "Characteristics"], "rows": [["", ""]]},
        {"type": "table", "class": "write", "head": ["Example", "Non-example"], "rows": [["", ""]]},
    ]


def act3_cornell(pack):
    secs = pack["sections"]
    rows = []
    for i, s in enumerate(secs, 1):
        cue = (f"<strong>{s['heading']}</strong><br>"
               f"<span style='color:#C9A227;font-weight:700;font-size:8pt'>▶ Deck · DI {i} of {len(secs)}</span><br>"
               f"<em style='font-size:8.5pt'>Guiding Q: What is the main idea, and what is the evidence?</em>")
        rows.append([cue, ""])
    return [
        {"type": "head", "text": "Activity 3 · Cornell Notes — Guided (Direct Teaching) · THE SPINE",
         "sub": "take notes as the teacher advances the deck, in order"},
        {"type": "cornell", "heading": "Cue column is pre-seeded with the lecture segments — write your notes on the right",
         "rows": rows},
        {"type": "box", "label": "Doodle Zone", "paras": ["Sketch one image, symbol, or timeline that captures this standard (dual-coding)."]},
        {"type": "lines", "n": 2},
        {"type": "box", "label": "Progress Check → Check Yourself", "paras": [
            "In one sentence (12–15 words), summarize the standard. Rate yourself 1–4 on each cue: 1 emerging · 2 developing · 3 proficient · 4 advanced."]},
        {"type": "lines", "n": 1},
        {"type": "tag", "color": "#1B5E20", "text": "Future Ready · Organization — keeping ordered, findable notes is a hireability skill."},
    ]


def act4_close_read(pack):
    secs = pack["sections"]
    core = [f"<strong>{s['heading']}.</strong> {s['content']}" for s in secs]
    tdq = [[f"Main idea of “{s['heading']}” + the evidence that supports it", "", ""] for s in secs]
    return [
        {"type": "head", "text": "Activity 4 · Close Read", "sub": "key terms first, then evidence"},
        {"type": "box", "label": "CORE PATH — read one chunk at a time", "paras": core},
        {"type": "box", "label": "Thesis mini-lesson — how to write a thesis", "paras": [
            "A thesis takes a position and previews your reasons: “Although ___, the bigger effect was ___ because ___.” "
            "You’ll carry this thesis into Activity 7 (CER)."]},
        {"type": "table", "class": "write",
         "head": ["Text-dependent question", "Evidence from the passage", "What it shows"], "rows": tdq},
        {"type": "tag", "color": "#B22234", "text": "ACT Connection · Reading — main idea + evidence is exactly the ACT Reading skill."},
    ]


def act5_hippo(pack):
    s = pack["sourceItFirst"]
    excerpt = s.get("excerpt", "")
    cite = s.get("citation", "")
    return [
        {"type": "head", "text": "Activity 5 · Primary Source / HIPPO", "sub": "source it first"},
        {"type": "box", "label": f"The document — {s.get('who','')} ({s.get('when','')})",
         "paras": [f"“{excerpt}”", f"<em style='font-size:8.5pt'>{cite}</em>"]},
        {"type": "box", "label": "Source it first", "paras": [
            "Before analyzing, source the document: who made it, when, and why. Then work the HIPPO frame and answer in a complete CER."]},
        {"type": "table", "class": "write", "head": ["HIPPO move", "What I notice"], "rows": [
            ["Historical context — what was happening when this was made?", ""],
            ["Intended audience — who was meant to see it?", ""],
            ["Point of view — whose perspective, and what is left out?", ""],
            ["Purpose — why was it created?", ""],
            ["Outside evidence — what do I already know that connects?", ""]]},
        {"type": "box", "label": "Confidence check-in", "paras": ["Rate your sourcing 1–4. What would move you up one level?"]},
        {"type": "lines", "n": 1},
        {"type": "tag", "color": "#1B5E20", "text": "Future Ready · Civic responsibility — weighing evidence fairly is a citizen’s skill."},
    ]


def act6_quiz(pack, eoc):
    items = pack["quiz"]
    check = "TCAP EOC" if eoc else "Standard-Mastery"
    blocks = [{"type": "head", "text": "Activity 6 · Practice Quiz", "sub": f"commit first, then check · {check}"}]
    q = []
    for n, it in enumerate(items, 1):
        opts = "<br>".join(f"{L}. {it['choices'][L]}" for L in ["A", "B", "C", "D"] if L in it["choices"])
        q.append(f"<strong>{n}.</strong> {it['stem']}<br>{opts}")
    blocks.append({"type": "box", "label": "Choose the best answer (circle a letter)", "paras": q})
    key = []
    for n, it in enumerate(items, 1):
        L = it["key"]
        why = it.get("why") or (it["choices"].get(L, ""))
        key.append(f'<span style="display:block;padding-left:26pt;text-indent:-26pt;margin-bottom:3pt">'
                   f'<strong style="color:#1B5E20;font-size:10.5pt">{n}.&nbsp;&nbsp;{L}</strong>'
                   f'&nbsp;&mdash;&nbsp;{why}</span>')
    blocks.append({"type": "box", "label": "Self-Check Key (commit your answers first!)", "paras": key})
    blocks.append({"type": "tag", "color": "#1B5E20",
                   "text": "Future Ready · Integrity / Lifelong learning — self-scoring honestly, then acting on the miss."})
    blocks.append({"type": "tag", "color": "#B22234",
                   "text": "ACT Connection · Test format — timed multiple-choice with tempting distractors mirrors the ACT."})
    return blocks


def act7_cer(pack):
    diff = pack.get("differentiation", "")
    entry = diff.split("Honors:")[0].replace("Entry:", "").strip(" .") if "Entry:" in diff else "Sentence stems + a word bank are provided; use the CER frame."
    honors = diff.split("Honors:")[1].strip(" .") if "Honors:" in diff else "Argue the opposite position, then decide which case is stronger."
    return [
        {"type": "head", "text": "Activity 7 · Constructed Response (CER)", "sub": "claim · evidence · reasoning"},
        {"type": "box", "label": "Big question", "paras": [pack["eq"] + " Use evidence from the reading (Act 4) and the source (Act 5)."]},
        {"type": "table", "head": ["★ Entry (more support)", "● On-Level (core)", "▲ Extension (challenge)"],
         "rows": [[entry,
                   "Write the full CER (claim + 2 evidence + reasoning) using the organizer below.",
                   honors]]},
        {"type": "table", "class": "write", "head": ["Claim", "Evidence", "Reasoning"], "rows": [["", "", ""]]},
        {"type": "box", "label": "Self-grade rubric (/12) — score yourself, then a peer", "paras": [
            "Claim answers the question (0–4) · Evidence is accurate + specific (0–4) · Reasoning links evidence to claim (0–4). "
            "Peer review: one glow, one grow, one revision."]},
        {"type": "lines", "n": 1},
        {"type": "box", "label": "SPEAK IT · 60-second Mission Brief — stand up and say it", "paras": [
            "Present your CER out loud: state your <strong>claim</strong>, give <strong>one</strong> piece of evidence, and say <strong>why it matters</strong> — 60 seconds. "
            "Score the delivery 1–4 (clear voice · eye contact · evidence). Speaking your argument is a Ready-Graduate + interview skill."]},
        {"type": "tag", "color": "#1B5E20", "text": "Future Ready · Communication (spoken) — the Mission Brief builds interview-ready voice."},
        {"type": "tag", "color": "#B22234", "text": "ACT Connection · English / Writing — building a claim with evidence is the ACT Writing task."},
    ]


def fr_question(code, fr):
    if not fr or fr.get("code") != code:
        return []
    return [
        {"type": "tag", "color": "#1F3A5F", "text": fr.get("label", "FUTURE READY QUESTION")},
        {"type": "box", "label": fr.get("title", "Your path after high school"), "paras": [fr.get("body", "")]},
        {"type": "lines", "n": 1},
    ]


def exit_ticket():
    return [
        {"type": "head", "text": "Exit Ticket", "sub": "close the standard"},
        {"type": "box", "label": "3–2–1", "paras": [
            "3 things you learned · 2 pieces of evidence you could use · 1 question you still have."]},
        {"type": "lines", "n": 3},
    ]


def gen_standard(code, pack, std, eoc, fr):
    blocks = []
    blocks += opener(code, pack, std)
    blocks += act1_vocab(pack)
    blocks += act2_frayer(pack)
    blocks += act3_cornell(pack)
    blocks += act4_close_read(pack)
    blocks += act5_hippo(pack)
    blocks += act6_quiz(pack, eoc)
    blocks += act7_cer(pack)
    blocks += fr_question(code, fr)
    blocks += exit_ticket()
    return {"code": code, "title": pack["title"], "blocks": blocks}


# ---------- front / back matter (parameterized) ----------

def cover_svg(title, era, brand_short):
    NAVY, RED, GOLD, CREAM = "#1F3A5F", "#B22234", "#C9A227", "#F8F5EF"
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="720" height="300" viewBox="0 0 720 300">
      <rect width="720" height="300" fill="{CREAM}"/>
      <rect width="720" height="300" fill="none" stroke="{GOLD}" stroke-width="6"/>
      <rect x="0" y="0" width="720" height="70" fill="{NAVY}"/>
      <rect x="0" y="70" width="720" height="8" fill="{RED}"/>
      <text x="360" y="46" font-family="Georgia,serif" font-size="30" fill="#fff" text-anchor="middle" font-weight="bold">{title}</text>
      <text x="360" y="150" font-family="Georgia,serif" font-size="52" fill="{NAVY}" text-anchor="middle" font-weight="bold">{era}</text>
      <text x="360" y="200" font-family="Arial,sans-serif" font-size="20" fill="{RED}" text-anchor="middle" letter-spacing="2">{brand_short}</text>
      <line x1="200" y1="230" x2="520" y2="230" stroke="{GOLD}" stroke-width="3"/>
      <text x="360" y="262" font-family="Arial,sans-serif" font-size="15" fill="#5C6470" text-anchor="middle">Student Workbook · Course Standard Edition</text>
    </svg>'''
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode("utf-8")).decode()


def cover(course, meta, order, packs):
    c = meta["cover"]
    stds = [f"<strong>{code}</strong> — {packs[code]['title']}" for code in order]
    return [{
        "type": "cover",
        "eyebrow": meta["brandLine"],
        "title": f"Unit {meta['unit']} — {meta['title']}",
        "subtitle": f"Student Workbook · Course Standard Edition · {meta['grade']}",
        "image": cover_svg(meta["title"], meta["era"], meta["brandLine"].split("™")[0].strip()),
        "standards": stds,
        "summary": c["summary"],
        "tn": c["tn"],
        "expect": c["expect"],
        "copyright": (f"{meta['brandLine'].split(' · ')[0]} · Unit {meta['unit']} (Course Standard Edition). "
                      f"&copy; 2026 TroopToTeacher Technologies LLC. All rights reserved. "
                      f"Author/producer: TroopToTeacher Technologies LLC. Single-classroom reproduction license. "
                      f"ISBN [to be assigned]. {c.get('copyright_extra','')} "
                      f"Cover: TroopToTeacher vector title panel (America 250 brand)."),
    }]


def front_matter(course, meta, order, packs):
    dn = course["displayName"]
    legend = ("<strong>Lenses/Dimensions pills:</strong> C Culture · E Economics · G Geography · H History · "
              "P Politics/Government. "
              "<strong>Self-check keys</strong> let you commit an answer, then check. "
              "<strong>▶ Deck · DI N of M</strong> keys your Cornell cues to the teacher’s slides. "
              "<strong>Future Ready</strong> tags mark where you build a hireability skill; "
              "<strong>ACT Connection</strong> tags mark where an activity builds an ACT skill.")
    seven = ("Every standard runs the same flow: Opener → 1 Vocabulary → 2 Vocabulary Studio → "
             "3 Cornell Notes (the spine) → 4 Close Read → 5 Primary Source/HIPPO → "
             "6 Practice Quiz → 7 CER → Exit Ticket.")
    std_line = " · ".join(f"{code} {packs[code]['title']}" for code in order)
    return [
        {"type": "head", "text": f"{dn} Hack™ · Unit {meta['unit']} — Student Workbook", "sub": meta["title"]},
        {"type": "head", "text": "My SMART Goals", "sub": "goal-setting — your Future Ready ladder"},
        {"type": "box", "label": "Short-term goal (this unit)", "paras": [
            "Exemplar (a real student’s voice): “By the end of this unit I will earn 80%+ on the unit test by finishing "
            "every Cornell note and self-checking each Practice Quiz.” Now write yours:"]},
        {"type": "lines", "n": 2},
        {"type": "box", "label": "Mid-term goal (this quarter)", "paras": ["Write a SMART goal for the quarter:"]},
        {"type": "lines", "n": 2},
        {"type": "box", "label": "Long-term goal (this year / after high school)", "paras": [
            "Write a SMART goal that ladders toward Ready Graduate (ACT ≥ 21 or an EPSO/credential):"]},
        {"type": "lines", "n": 2},
        {"type": "box", "label": "Reflect & Commit", "paras": [
            "How does the short-term goal ladder to the long-term one? Name one obstacle + your plan, "
            "an accountability partner, and your first step."]},
        {"type": "lines", "n": 2},
        {"type": "head", "text": "Unit at a Glance", "sub": "the seven-activity cycle"},
        {"type": "box", "label": "How this unit flows", "paras": [seven, "Standards: " + std_line + "."]},
        {"type": "head", "text": "How to Use This Workbook", "sub": "the legend"},
        {"type": "box", "label": "Read the symbols", "paras": [legend]},
    ]


def adoption_crosswalk(course, order, packs, standards):
    eoc = course.get("eocTestable")
    rows = []
    for code in order:
        pack = packs[code]
        tdoe = standards[code]["text"]
        ssps = ", ".join(f"{s} {SSP_TEXT.get(s, '').split('(')[0].strip()}" for s in pack.get("ssps", []))
        lenses = " · ".join(standards[code].get("strand", []))
        rows.append([f"<strong>{code}</strong>", tdoe, ssps, "DOK 1–3", lenses])
    frame = ("The 7-activity spine exercises these SSPs (source read → SSP.01/02 · compare → SSP.03 · "
             "CER → SSP.04 · sequence/context → SSP.05 · map/region → SSP.06).")
    eoc_line = ("Assessment framing: benchmark / Standard-Mastery (identical rigor; this course has no TCAP EOC). "
                if not eoc else "Assessment framing: TCAP EOC-aligned. ")
    return [
        {"type": "head", "text": "Standards Alignment / Adoption Crosswalk", "sub": "TDOE Schedule F · Policy 2.600 — reviewer-facing"},
        {"type": "box", "label": "How to read this", "paras": [
            "Per standard: the verbatim TDOE standard, the Social Studies Practices (SSP.01–06) it exercises, "
            "DOK coverage, and the disciplinary Lenses. " + frame]},
        {"type": "table", "head": ["Std", "Verbatim TDOE standard", "Social Studies Practices", "DOK", "Lenses"], "rows": rows},
        {"type": "box", "label": "Reviewer assurances", "paras": [
            eoc_line +
            "Standards alignment 100% · Content accuracy (Policy 2.600 — no known factual error ships) · "
            "Bias/sensitivity reviewed · Copyright: public-domain sources with citations · "
            "Accessibility: WCAG 2.2 AA / tagged PDF-UA (Rubric F) · Assessment items content-verified "
            "(classroom-formative · pre-field-test until calibrated)."]},
    ]


def udl_back_page():
    rows = [
        ["<strong>Engagement</strong><br>(the “why”)", "Essential Questions + hooks · SET YOUR SMART GOAL · confidence check-ins · CER stance choice · Future Ready relevance"],
        ["<strong>Representation</strong><br>(the “what”)", "EN/ES vocabulary + plain-language defs · primary-source excerpts · Cornell chunking · dual-coding Doodle Zone · deck read-aloud (app)"],
        ["<strong>Action &amp; Expression</strong><br>(the “how”)", "Guided Cornell + graphic organizers · CER + HIPPO frames · Practice-Quiz self-check · SPEAK IT Mission Brief · notebook-lined write space throughout"],
    ]
    return [
        {"type": "head", "text": "UDL 3.0 Supports (CAST, 2024)", "sub": "the access design built into this workbook"},
        {"type": "box", "label": "Universal Design for Learning — three principles", "paras": [
            "Supports add paths; they never lower the goal. This page names the real affordances this book delivers, "
            "in addition to each activity’s per-standard NOTES SUPPORTS."]},
        {"type": "table", "head": ["UDL 3.0 principle", "How this workbook delivers it"], "rows": rows},
        {"type": "box", "label": "Citation", "paras": [
            "CAST (2024). <em>Universal Design for Learning Guidelines version 3.0.</em> Supports work alongside — never in place of — a student’s IEP/504 accommodations."]},
    ]


def main():
    cid = sys.argv[1] if len(sys.argv) > 1 else "world-history"
    unit = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    course = load_course(cid)
    standards = load_standards(course)
    prefix = course["standardsPrefix"]
    src = ROOT / f"content/{cid}/unit-{unit:02d}.source.json"
    meta = json.loads(src.read_text())
    packs = meta["standards"]
    order = sorted(packs.keys(), key=lambda c: (len(c), c))

    # WALL W2: emit ONLY this course's prefix
    bad = [c for c in order if not c.startswith(prefix + ".")]
    if bad:
        sys.exit(f"WALL W2 VIOLATION: non-{prefix} codes in source: {bad}")
    missing = [c for c in order if c not in standards]
    if missing:
        sys.exit(f"codes not in standardsFile {course['standardsFile']}: {missing}")

    eoc = course.get("eocTestable")
    fr = meta.get("frQuestion")
    data = {
        "unit": unit, "title": meta["title"], "edition": "Course Standard Edition",
        "runhead": f"{course['displayName']} Hack™ · Unit {unit} · Course Standard Edition",
        "runfoot": f"{course['displayName']} Hack™ · Unit {unit} (Course Standard)   ·   © 2026 TroopToTeacher Technologies LLC",
        "front": cover(course, meta, order, packs) + front_matter(course, meta, order, packs)
                 + adoption_crosswalk(course, order, packs, standards),
        "standards": [gen_standard(c, packs[c], standards[c], eoc, fr) for c in order],
        "back": udl_back_page(),
    }
    out = ROOT / f"content/{cid}/unit-{unit:02d}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    tot = sum(len(s["blocks"]) for s in data["standards"])
    print(f"wrote {out} | course={cid} ({prefix}) | 7-activity × {len(order)} standards | {tot} std blocks + {len(data['front'])} front")
    if subprocess.run([sys.executable, str(ROOT / "verify_workbook_platinum.py"), str(out)]).returncode:
        sys.exit("platinum guardrail FAILED — see blockers above")


if __name__ == "__main__":
    main()
