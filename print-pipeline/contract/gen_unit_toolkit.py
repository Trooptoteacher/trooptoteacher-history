#!/usr/bin/env python3
"""Generate the COMPLETE Unit 1 Teacher Graphic Organizer Toolkit content JSON,
matching the Unit 6 toolkit structure, pulling real US.01-07 content."""
import json
from pathlib import Path

SRC = Path("/home/user/trooptoteacher-history/HistoryHack_Platinum/build_unit1/unit1_content.json")
OUT = Path("/home/user/trooptoteacher-history/print-pipeline/contract/fixtures/unit1-toolkit-full.json")

data = json.loads(SRC.read_text())
STD = data["standards"]
ORDER = data["order"]

def pb():
    return {"type": "html", "html": "<div class='page-break'></div>"}

blocks = []

# ---- Cover ----
blocks += [
    {"type": "heading", "level": 1, "text": "Teacher Graphic Organizer Toolkit"},
    {"type": "para", "text": "<strong>U.S. History Hack&trade; &middot; Unit 1 &mdash; The Rise of Industrialization (1877&ndash;1900) &middot; US.01&ndash;US.07.</strong> Reproducible &mdash; you may copy these pages for classroom use."},
    {"type": "box", "label": "Why this toolkit", "paras": [
        "Knowing WHICH organizer to use, and WHEN, is half the battle. This toolkit tells you &mdash; with a brief why for each &mdash; then gives you reproducible blanks (Part 1) and per-standard Cornell support backs (Part 2). Tennessee connections are highlighted throughout; the local-to-national move is a History Hack signature and a point of difference for our classrooms."]},
]

# ---- Quick Guide ----
blocks += [
    pb(),
    {"type": "heading", "level": 2, "text": "Which Organizer, When — Quick Guide"},
    {"type": "para", "text": "Scan the left column for what the activity asks students to do; reach for the organizer on the right. Every organizer in Part 1 also carries its own “when to use · why it works” note."},
    {"type": "table", "head": ["When the task asks students to…", "Reach for…", "Why it works"], "rows": [
        ["compare / contrast TWO things", "Venn (2) or T-Chart", "Marzano's highest-yield strategy; the overlap names shared traits"],
        ["compare 3+ things on set criteria", "Compare &amp; Contrast Matrix", "systematic; lowers cognitive load"],
        ["explain causes / effects", "Cause &amp; Effect", "makes causal chains visible (SSP.05)"],
        ["put events in order / show change", "Timeline / Sequence", "builds chronological reasoning (SSP.05)"],
        ["brainstorm or connect ideas", "Concept Web", "activates prior knowledge; shows relationships"],
        ["summarize a text or source", "Main Idea &amp; Details", "separates the central idea from support"],
        ["activate prior knowledge &amp; track learning", "KWL", "metacognition; frames inquiry"],
        ["learn a key term deeply", "Frayer", "deep vocabulary processing"],
        ["analyze a primary source", "HIPPO", "disciplinary sourcing (SSP.01–SSP.02)"],
        ["make and defend a claim", "CER", "claim + evidence + reasoning (SSP.04)"],
        ["weigh two sides / a decision", "T-Chart or Problem–Solution", "structures evaluation"],
        ["capture the basics of an event", "5 Ws", "ensures full coverage"],
        ["connect a national event to Tennessee", "★ Tennessee Connection", "our signature local-to-national move"],
    ]},
]

# ---- SSP Crosswalk ----
blocks += [
    pb(),
    {"type": "heading", "level": 2, "text": "SSP Crosswalk — Tennessee Social Studies Practices"},
    {"type": "para", "text": "Every organizer doubles as a skills tool. This maps each TN Social Studies Practice (SSP.01–SSP.06) to the organizers that build it and where it lives in Unit 1."},
    {"type": "table", "head": ["TN Social Studies Practice", "Organizers that build it", "Where in Unit 1"], "rows": [
        ["SSP.01 — Gather information from primary &amp; secondary sources", "HIPPO · Main Idea &amp; Details", "US.01, US.03, US.07 source work"],
        ["SSP.02 — Critically examine a source (context, point of view)", "HIPPO · T-Chart", "US.03 Plessy; US.05 industry perspectives"],
        ["SSP.03 — Synthesize evidence from multiple sources", "CER · Compare &amp; Contrast Matrix", "US.04–US.05 Gilded Age analysis"],
        ["SSP.04 — Construct &amp; defend an argument with evidence", "CER · Problem–Solution", "US.02 policy evaluation; US.07 assimilation"],
        ["SSP.05 — Develop historical awareness (change over time)", "Timeline · Cause &amp; Effect", "US.01 expansion; US.06 urbanization"],
        ["SSP.06 — Connect past to present / local to national", "★ Tennessee Connection", "every standard's TN tie"],
    ]},
]

# ---- Part 1 blanks ----
blocks += [pb(), {"type": "heading", "level": 1, "text": "Part 1 — Reusable Blank Organizers"},
           {"type": "para", "text": "Content-agnostic blanks. Print as many as you need; use across any standard or subject."}]

def org(title, tag, when, cite, body_blocks, udl_over=None):
    out = [pb(), {"type": "orgtitle", "text": title, "tag": tag},
           {"type": "whenwhy2", "text": when, "cite": cite}]
    out += body_blocks
    out += [{"type": "udl", **(udl_over or {})}]
    return out

blocks += org("Venn Diagram (2)", "Compare &amp; Contrast",
    "Task says “compare,” “contrast,” “how are they alike/different?” for TWO things.",
    "Marzano's #1 strategy (identifying similarities &amp; differences); the shared zone forces students to name what overlaps.",
    [{"type": "venn", "left": "Only ______ (A)", "right": "Only ______ (B)", "both": "Both / shared"}])

blocks += org("Venn (3) / Triple Compare", "Compare THREE",
    "Comparing three people, groups, or ideas across the same traits.",
    "Extends comparison to three items without losing structure.",
    [{"type": "table", "class": "gwrite", "head": ["Trait / criterion", "Item A", "Item B", "Item C"],
      "rows": [["Trait 1", "", "", ""], ["Trait 2", "", "", ""], ["Trait 3", "", "", ""], ["Trait 4", "", "", ""]]}])

blocks += org("T-Chart", "Two Sides / Pros &amp; Cons / Before–After",
    "Two categories to sort or weigh: benefits vs costs, pros vs cons, before vs after, cause vs effect.",
    "Fast, low-floor entry point for comparison.",
    [{"type": "tchart", "left": "______", "right": "______", "lines": 8}])

blocks += org("Compare &amp; Contrast Matrix", "Items × Criteria",
    "Comparing several items across the SAME set of criteria.",
    "Reduces cognitive load by making the comparison systematic.",
    [{"type": "table", "class": "gwrite", "head": ["Criterion", "Item 1", "Item 2", "Item 3"],
      "rows": [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]}])

blocks += org("Cause &amp; Effect", "Causal Chains",
    "Task asks “what caused…?”, “what were the effects/consequences of…?”",
    "Makes causal reasoning visible (builds SSP.05).",
    [{"type": "chain", "nodes": ["Cause", "Effect", "Effect"]}])

blocks += org("Timeline / Sequence", "Chronology",
    "Ordering events or tracing change over time.",
    "Builds chronological reasoning (SSP.05).",
    [{"type": "table", "class": "gwrite", "head": ["Date / order", "Event", "Why it mattered"],
      "rows": [["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]}])

blocks += org("Concept Web", "Connect &amp; Brainstorm",
    "Activating prior knowledge or showing how ideas relate to a central concept.",
    "Great as a pre-reading or review move.",
    [{"type": "table", "class": "gwrite", "head": ["Central idea", "Connected idea", "How it connects"],
      "rows": [["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]}])

blocks += org("Main Idea &amp; Details", "Summarize",
    "Pulling the central idea and its support from a text or source.",
    "Separates the big idea from the evidence.",
    [{"type": "frame", "title": "MAIN IDEA", "lines": 2},
     {"type": "table", "class": "gwrite", "head": ["Detail", "Detail", "Detail"], "rows": [["", "", ""]]}])

blocks += org("KWL", "Activate &amp; Track Learning",
    "Start of a standard: what students Know / Want to know; end: what they Learned.",
    "Builds metacognition and frames inquiry.",
    [{"type": "table", "class": "gwrite", "head": ["K — what I Know", "W — what I Want to know", "L — what I Learned"],
      "rows": [["", "", ""], ["", "", ""], ["", "", ""]]}])

blocks += org("5 Ws", "Cover the Basics of an Event",
    "Making sure students capture who/what/when/where/why of an event before analysis.",
    "Ensures full coverage.",
    [{"type": "table", "class": "write", "head": ["Question", "Answer"],
      "rows": [["Who?", ""], ["What?", ""], ["When?", ""], ["Where?", ""], ["Why?", ""]]}])

blocks += org("Problem &amp; Solution", "Evaluate Responses",
    "Analyzing a problem and the responses to it (e.g., a policy or reform).",
    "Structures evaluation.",
    [{"type": "table", "class": "gwrite", "head": ["Problem", "Proposed solution", "Result / evaluation"],
      "rows": [["", "", ""], ["", "", ""], ["", "", ""]]}])

blocks += org("Frayer Model", "Deep Vocabulary",
    "Learning a key term deeply (definition, characteristics, examples, non-examples).",
    "Deep vocabulary processing; durable retention.",
    [{"type": "frayer", "term": "Key Term", "quads": ["Definition (own words)", "Characteristics", "Examples", "Non-examples"]}],
    udl_over={"extend": "push higher-DOK — “Give a non-example that is easy to confuse with this term, and explain the difference.”"})

blocks += org("CER", "Build an Argument",
    "Any “make a claim / defend / argue” task. Claim + two pieces of evidence + reasoning.",
    "Builds SSP.04.",
    [{"type": "frame", "title": "Claim", "lines": 2},
     {"type": "frame", "title": "Evidence (two specifics)", "lines": 3},
     {"type": "frame", "title": "Reasoning", "lines": 3}])

blocks += org("HIPPO", "Analyze a Primary Source",
    "Analyzing a photo, cartoon, map, or document. Pair with OPTIC for visuals.",
    "Disciplinary sourcing (builds SSP.01–SSP.02).",
    [{"type": "table", "class": "write", "head": ["H-I-P-P-O", "Prompt / notes"],
      "rows": [["H — Historical context", ""], ["I — Intended audience", ""],
               ["P — Purpose", ""], ["P — Point of view", ""], ["O — Outside connection", ""]]}])

blocks += org("Tennessee Connection", "★ Local ↔ National",
    "Whenever a standard has a Tennessee tie: link the national event to our state/community and say why the local story matters.",
    "The local-to-national move — a History Hack signature.",
    [{"type": "table", "class": "gwrite", "head": ["The national event / idea", "Our Tennessee (or local) connection", "Why the local story matters"],
      "rows": [["", "", ""], ["", "", ""], ["", "", ""]]}])

# ---- Part 2 Cornell Support Backs ----
blocks += [pb(), {"type": "heading", "level": 1, "text": "Part 2 — Cornell Support Backs (per standard)"},
           {"type": "para", "text": "Guided and Light scaffolds for each standard's Cornell notes — copy only as needed (MTSS). Fade Guided → Light → independent as evidence grows. <em>Not a track, not a separate grade.</em>"}]

for code in ORDER:
    s = STD[code]
    vocab = s.get("vocab", [])[:3]
    title = s["title"]
    vrows = [[v["term"], v["def"]] for v in vocab]
    lrows = [[v["term"], ""] for v in vocab]
    modeled = ""
    if vocab:
        modeled = f"A key idea of {title.lower()} was {vocab[0]['term']}: {vocab[0]['def']}"
    blocks += [
        pb(),
        {"type": "orgtitle", "text": f"{code} — {title}", "tag": "Cornell Support Backs"},
        {"type": "para", "text": "<em>Reproducible — scaffolds ONLY the Cornell notes for this standard. Copy for students who need them; fade as evidence grows. Not a track, not a separate grade.</em>"},
        {"type": "supband", "text": "Guided Support"},
        {"type": "table", "head": ["Key vocabulary", "What it means"], "rows": vrows},
        {"type": "modeled", "label": "Modeled example (one worked note — yours will differ)", "text": modeled},
        {"type": "table", "class": "write", "head": ["Step", "Rehearse it here, then transfer to the Cornell front"],
         "rows": [["Name it", ""], ["Evidence", ""], ["Explain", ""], ["Headline", ""]]},
        {"type": "supband", "light": True, "text": "Light Support"},
        {"type": "table", "class": "write", "head": ["Key vocabulary", "Finish the idea — “This term means …”"], "rows": lrows},
        {"type": "box", "label": "Guiding questions — answer on the lines below or in your front notes", "paras": [
            f"• What is the main idea of “{s.get('criteria',[''])[0]}”, and what evidence supports it?" if s.get('criteria') else "• What is the main idea of this standard, and what evidence supports it?",
            "• Whose perspective benefits in this passage, and whose is harmed or left out?"]},
        {"type": "writelines", "lines": 3},
    ]
    if s.get("tn_connection"):
        blocks.append({"type": "tnconn", "tie": s["tn_connection"][:220],
                       "prompt": "Which Cornell cue still needs work? Circle it and tell your teacher.", "lines": 2})

doc = {"runhead": "U.S. History Hack · Unit 1 · Graphic Organizer Toolkit",
       "runfoot": "Unit 1 · Rise of Industrialization (US.01–US.07)",
       "blocks": blocks}
OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1))
print("wrote", OUT, "with", len(blocks), "blocks")
