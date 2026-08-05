# -*- coding: utf-8 -*-
"""Unit 1 Course-Standard STUDENT WORKBOOK — FULL 7-activity cycle (print-first, no docx).
Rebuilt to the STUDENT_WORKBOOK_PLATINUM_STANDARD anatomy: front matter (My SMART Goals,
Unit at a Glance, How-to-Use legend) + per standard an OPENER (Learning Targets · Lenses ·
SET YOUR SMART GOAL · Hook · Preview) + the SEVEN activities in order —
  1 Vocabulary · 2 Vocabulary Studio (Frayer) · 3 Cornell Notes (Guided/Direct-Teaching = spine)
  · 4 Close Read · 5 Primary Source/HIPPO · 6 Practice Quiz (bank-sourced + self-check key)
  · 7 Constructed Response (CER + rubric) — + an Exit Ticket.
Future Ready is embedded (never forced): SMART goal ladder, employability micro-moments,
a standard-tied Future Ready Question (US.05), and ACT-Connection tags where the skill lives.
Content SoT: deck _build.json (vocab/sections/SSPs), _activities.json, standard_to_dimensions.json,
and 21 verified Form-A items (stem+choices+key) extracted from the Unit 1 Assessment Book.
Renders via render.py (WeasyPrint). No .docx.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SK = ROOT.parent / ".claude/skills"
BUILD = json.loads((SK / "history-hack-tcap-deck-builder/assets/unit1-example/_build.json").read_text())
ACTS = json.loads((SK / "history-hack-tcap-deck-builder/assets/unit1-example/_activities.json").read_text())
DIMS = json.loads((SK / "history-hack-unit-content-build/assets/lenses-dimensions/standard_to_dimensions.json").read_text())
QUIZ = json.loads(Path("/tmp/u1_quiz.json").read_text())
UNIT_JSON = ROOT / "content/us-history/unit-01.json"

CATS = DIMS["_legend"]
EQ = {
    "US.01": "How did federal land and railroad policy reshape the West — and at whose expense?",
    "US.02": "How did federal policy try to erase Native nations — and how did they resist?",
    "US.03": "How did the end of Reconstruction harden into Jim Crow — and who fought back?",
    "US.04": "Who really held power in the Gilded Age — voters, party machines, or money?",
    "US.05": "Did industrial innovation lift everyone, or concentrate wealth and power?",
    "US.06": "Why did people leave the countryside for the city — and what did they find there?",
    "US.07": "What pulled “new” immigrants to America, and what did nativism push back with?",
}
ORDER = [f"US.0{i}" for i in range(1, 8)]


def opener(code, v):
    dm = DIMS["standards"][code]["dimensions"]
    lens = " · ".join(f"{c} {CATS[c]}" for c in dm)
    hook = v["sections"][0]["content"].split(". ")[0] + "."
    return [
        {"type": "head", "text": "Opener", "sub": "before you learn"},
        {"type": "box", "label": "Learning target (I can…)", "paras": [v["iCan"]]},
        {"type": "box", "label": "Lenses (this standard’s dimensions)", "paras": [lens]},
        {"type": "box", "label": "SET YOUR SMART GOAL — my short-term goal for this standard",
         "paras": ["Write a goal that is Specific · Measurable · Achievable · Relevant · Time-bound. "
                   "Example: “By Friday I can explain " + v["title"].lower() + " using two pieces of evidence.”"]},
        {"type": "lines", "n": 2},
        {"type": "box", "label": "Hook — read this", "paras": [hook + " <em>What surprises you? What do you want to know?</em>"]},
        {"type": "box", "label": "Preview & Predict", "paras": ["Skim the standard. Predict who benefited and who bore the cost."]},
        {"type": "lines", "n": 2},
    ]


def act1_vocab(v):
    vocab = v["vocab"]
    rows = [[f"<strong>{t['term']}</strong>", t.get("simple") or t["def"], t.get("es", ""), ""]
            for t in vocab]
    return [
        {"type": "head", "text": "Activity 1 · Vocabulary", "sub": "word bank + language support"},
        {"type": "table", "head": ["Term", "What it means", "Español", "Know it? (✓ / ? / new)"], "rows": rows},
        {"type": "box", "label": "Knowledge self-check", "paras": [
            "For each term mark ✓ (I can use it), ? (I’ve seen it), or new. Come back and re-mark after the lesson."]},
    ]


def act2_frayer(v):
    term = v["vocab"][0]["term"]
    return [
        {"type": "head", "text": "Activity 2 · Vocabulary Studio (Frayer)", "sub": "response choice"},
        {"type": "box", "label": f"Build a Frayer model for: {term}", "paras": [
            "Fill each quadrant. Then CONNECT THE TERMS: use two vocabulary words in one sentence (here or in your notebook)."]},
        {"type": "table", "class": "write",
         "head": ["Definition (your words)", "Characteristics"], "rows": [["", ""]]},
        {"type": "table", "class": "write",
         "head": ["Example", "Non-example"], "rows": [["", ""]]},
    ]


def act3_cornell(code, v):
    # cue column pre-seeded with DI segments in lecture order (deck-keyed placeholders)
    rows = []
    for i, s in enumerate(v["sections"], 1):
        cue = (f"<strong>{s['heading']}</strong><br>"
               f"<span style='color:#C9A227;font-weight:700;font-size:8pt'>▶ Deck · DI {i} of {len(v['sections'])}</span><br>"
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


def act4_close_read(v):
    secs = v["sections"]
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


def act5_hippo(v):
    who = (v.get("sourceItFirst") or {}).get("who", "the creator")
    return [
        {"type": "head", "text": "Activity 5 · Primary Source / HIPPO", "sub": "source it first"},
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


def act6_quiz(code):
    items = QUIZ.get(code, [])
    blocks = [{"type": "head", "text": "Activity 6 · Practice Quiz", "sub": "commit first, then check"}]
    q = []
    for n, it in enumerate(items, 1):
        opts = "<br>".join(f"{L}. {it['choices'][L]}" for L in ["A", "B", "C", "D"] if L in it["choices"])
        q.append(f"<strong>{n}.</strong> {it['stem']}<br>{opts}")
    blocks.append({"type": "box", "label": "Choose the best answer (circle a letter)", "paras": q})
    # self-check key: correct letter + one-line rationale (derived from the verified correct choice)
    key = []
    for n, it in enumerate(items, 1):
        L = it["key"]; correct = it["choices"].get(L, "")
        why = " ".join(correct.split()[:14]) + ("…" if len(correct.split()) > 14 else "")
        key.append(f"<strong>{n}. {L}</strong> — “{why}” is correct; the other options misstate a fact or overreach.")
    blocks.append({"type": "box", "label": "Self-Check Key (commit your answers first!)", "paras": key})
    blocks.append({"type": "tag", "color": "#1B5E20",
                   "text": "Future Ready · Integrity / Lifelong learning — self-scoring honestly, then acting on the miss."})
    blocks.append({"type": "tag", "color": "#B22234",
                   "text": "ACT Connection · Test format — timed multiple-choice with tempting distractors mirrors the ACT."})
    return blocks


def act7_cer(code, v):
    act = ACTS.get(code, {})
    return [
        {"type": "head", "text": "Activity 7 · Constructed Response (CER)", "sub": "claim · evidence · reasoning"},
        {"type": "box", "label": "Big question", "paras": [EQ[code] + " Use evidence from the reading (Act 4) and the source (Act 5)."]},
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


def exit_ticket(code, v):
    return [
        {"type": "head", "text": "Exit Ticket", "sub": "close the standard"},
        {"type": "box", "label": "3–2–1", "paras": [
            "3 things you learned · 2 pieces of evidence you could use · 1 question you still have."]},
        {"type": "lines", "n": 3},
    ]


def fr_question(code):
    # embedded ONLY where the content gives a natural hook — US.05 Gilded Age = wealth/opportunity
    if code != "US.05":
        return []
    return [
        {"type": "tag", "color": "#1F3A5F", "text": "FUTURE READY QUESTION (hung on US.05 — the age of self-made fortunes)"},
        {"type": "box", "label": "Your path after high school", "paras": [
            "Carnegie and Rockefeller built empires in this era. What’s <em>your</em> plan? "
            "Circle a path — trade / college / military / work — and name one step: a scholarship, "
            "FAFSA, an EPSO, or a credential. (Free-college and scholarship options exist — ask your counselor.) "
            "Add this to <em>My SMART Goals</em>."]},
        {"type": "lines", "n": 1},
    ]


def gen_standard(code):
    v = BUILD[code]
    blocks = []
    blocks += opener(code, v)
    blocks += act1_vocab(v)
    blocks += act2_frayer(v)
    blocks += act3_cornell(code, v)
    blocks += act4_close_read(v)
    blocks += act5_hippo(v)
    blocks += act6_quiz(code)
    blocks += act7_cer(code, v)
    blocks += fr_question(code)
    blocks += exit_ticket(code, v)
    return {"code": code, "title": v["title"], "blocks": blocks}


def front_matter():
    legend = ("<strong>Lenses/Dimensions pills:</strong> C Culture · E Economics · G Geography · H History · "
              "P Politics/Government · T Tennessee · TCA Tennessee Code Annotated. "
              "<strong>Self-check keys</strong> let you commit an answer, then check. "
              "<strong>▶ Deck · DI N of M</strong> keys your Cornell cues to the teacher’s slides. "
              "<strong>Future Ready</strong> tags mark where you build a hireability skill; "
              "<strong>ACT Connection</strong> tags mark where an activity builds an ACT skill.")
    seven = ("Every standard runs the same flow: Opener → 1 Vocabulary → 2 Vocabulary Studio → "
             "3 Cornell Notes (the spine) → 4 Close Read → 5 Primary Source/HIPPO → "
             "6 Practice Quiz → 7 CER → Exit Ticket.")
    return [
        {"type": "head", "text": "U.S. History Hack™ · Unit 1 — Student Workbook", "sub": "The Rise of Industrialization, 1877–1900"},
        {"type": "head", "text": "My SMART Goals", "sub": "goal-setting — your Future Ready ladder"},
        {"type": "box", "label": "Short-term goal (this unit)", "paras": [
            "Exemplar (a real student’s voice): “By the end of Unit 1 I will earn 80%+ on the unit test by finishing "
            "every Cornell note and self-checking each Practice Quiz.” Now write yours:"]},
        {"type": "lines", "n": 2},
        {"type": "box", "label": "Mid-term goal (this quarter)", "paras": ["Write a SMART goal for the quarter:"]},
        {"type": "lines", "n": 2},
        {"type": "box", "label": "Long-term goal (this year / after high school)", "paras": [
            "Write a SMART goal that ladders toward Ready Graduate (ACT ≥ 21 or an EPSO/credential):"]},
        {"type": "lines", "n": 2},
        {"type": "box", "label": "Reflect & Commit", "paras": [
            "How does the short-term goal ladder to the long-term one? Name one obstacle + your plan, "
            "an accountability partner, and your first step. (Your Launch/Debrief sheets and the app track the delta.)"]},
        {"type": "lines", "n": 2},
        {"type": "head", "text": "Unit at a Glance", "sub": "the seven-activity cycle"},
        {"type": "box", "label": "How this unit flows", "paras": [seven,
            "Standards: US.01 Homestead & Railroad · US.02 Federal Indian Policy · US.03 Compromise of 1877 & Jim Crow · "
            "US.04 Gilded Age · US.05 Inventions & Entrepreneurs · US.06 Industrial Centers · US.07 Immigration."]},
        {"type": "head", "text": "How to Use This Workbook", "sub": "the legend"},
        {"type": "box", "label": "Read the symbols", "paras": [legend]},
    ]


def main():
    data = {
        "unit": 1, "title": "The Rise of Industrialization, 1877–1900",
        "edition": "Course Standard Edition",
        "runhead": "U.S. History Hack™ · Unit 1 · Course Standard Edition",
        "runfoot": "U.S. History Hack™ · Unit 1 (Course Standard)   ·   © 2026 TroopToTeacher Technologies LLC",
        "front": front_matter(),
        "standards": [gen_standard(c) for c in ORDER],
    }
    UNIT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    tot = sum(len(s["blocks"]) for s in data["standards"])
    print(f"wrote {UNIT_JSON} | 7-activity cycle × {len(ORDER)} standards | {tot} standard blocks + {len(data['front'])} front")


if __name__ == "__main__":
    main()
