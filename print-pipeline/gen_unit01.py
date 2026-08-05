#!/usr/bin/env python3
"""Generate the Unit 1 Course-Standard student workbook content JSON (US.01-US.07)
from the deck's own build data, so the workbook and teacher/student decks share one
source of truth and match by construction. US.01 keeps its hand-authored blocks;
US.02-US.07 are generated in the identical proven structure. No .docx anywhere —
this JSON renders through render.py (WeasyPrint) to a print-ready PDF.

Run:  python3 gen_unit01.py
Then: python3 render.py content/us-history/unit-01.json out/Unit1_Student_Workbook.pdf
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DECK = ROOT.parent / ".claude/skills/history-hack-tcap-deck-builder/assets/unit1-example"
BUILD = json.loads((DECK / "_build.json").read_text())
ACTS = json.loads((DECK / "_activities.json").read_text())
UNIT_JSON = ROOT / "content/us-history/unit-01.json"

# Short essential questions per standard (interpretive, "at whose expense?" framing).
EQ = {
    "US.02": "How did federal policy try to erase Native nations — and how did they resist?",
    "US.03": "How did the end of Reconstruction harden into Jim Crow — and who fought back?",
    "US.04": "Who really held power in the Gilded Age — voters, party machines, or money?",
    "US.05": "Did industrial innovation lift everyone, or concentrate wealth and power?",
    "US.06": "Why did people leave the countryside for the city — and what did they find there?",
    "US.07": "What pulled “new” immigrants to America, and what did nativism push back with?",
}

def ssp_lead(ssps):
    return ("Reading type: History Hack-authored instructional synthesis. Not a primary "
            "source. Builds " + ", ".join(ssps[:3]) + " — collect, examine, and "
            "synthesize evidence with historical awareness.")

def gen_standard(code):
    v = BUILD[code]
    secs = v["sections"]
    vocab = v.get("vocab", [])
    act = ACTS.get(code, {})
    vocab_terms = " · ".join(t["term"] for t in vocab[:5])

    # Cornell universal front
    front = {
        "type": "cornell", "heading": "Cornell Universal Front",
        "rows": [
            ["Essential Question", EQ.get(code, "")],
            ["Deck slides", f"Teacher & Student decks — {code} section (advance in order)"],
            ["Vocabulary", vocab_terms],
            ["Success criteria", v["iCan"]],
        ],
    }

    # Vocabulary table (term / definition / Espanol) — word-wall match to the deck
    vocab_tbl = {
        "type": "table",
        "head": ["Term", "What it means", "Español"],
        "rows": [[f"<strong>{t['term']}</strong>", t.get("simple") or t["def"], t.get("es", "")]
                 for t in vocab],
    }

    # Close Read — one box paragraph per section + language support + TDQ write table
    core_paras = [f"<strong>{s['heading']}.</strong> {s['content']}" for s in secs]
    tdq_rows = [[f"What is the main idea of “{s['heading']}”, and what evidence supports it?", "", ""]
                for s in secs]
    close_read = {
        "type": "activity", "num": 4, "name": "Close Read", "time": "~15 min",
        "lead": ssp_lead(v.get("ssps", ["SSP.03", "SSP.05"])),
        "blocks": [
            {"type": "box", "label": "Core Path — read one chunk at a time", "paras": core_paras},
            {"type": "box", "label": "Language support", "paras": [
                "Key terms to know first: " + ", ".join(t["term"] for t in vocab[:2]) +
                ". Read once for the gist, then again for evidence."]},
            {"type": "table", "class": "write",
             "head": ["Text-dependent question", "Evidence from the passage", "Your answer (what it shows)"],
             "rows": tdq_rows},
        ],
    }

    # Primary Source (HIPPO)
    hippo = {
        "type": "activity", "num": 5, "name": "Primary Source (HIPPO)", "time": "~15 min",
        "lead": ("Analyze a verified primary source with HIPPO: Historical context, "
                 "Intended audience, Point of view, Purpose, Outside evidence. Builds SSP.01–SSP.02."),
        "blocks": [
            {"type": "box", "label": "Source it first", "paras": [
                "Every source gets sourced before it gets analyzed. Fill the HIPPO frame, "
                "then answer the guiding question in a complete CER (Claim – Evidence – Reasoning)."]},
            {"type": "table", "class": "write",
             "head": ["HIPPO move", "What I notice in this source"],
             "rows": [
                 ["Historical context — what was happening when this was made?", ""],
                 ["Intended audience — who was meant to see it?", ""],
                 ["Point of view — whose perspective, and what is left out?", ""],
                 ["Purpose — why was it created?", ""],
                 ["Outside evidence — what do I already know that connects?", ""],
             ]},
        ],
    }

    # Apply activity (from the shared activities file) + CER write space
    apply_blocks = [{"type": "box", "label": f"Task — {act.get('grouping','Pairs')} · {act.get('minutes','~12 min')}",
                     "paras": [act.get("prompt", ""),
                               f"<strong>Deliverable:</strong> {act.get('deliverable','')}"]}]
    if act.get("differentiation"):
        apply_blocks.append({"type": "box", "label": "Differentiation", "paras": [act["differentiation"]]})
    apply_blocks.append({"type": "table", "class": "write",
                         "head": ["Claim", "Evidence", "Reasoning"], "rows": [["", "", ""]]})
    apply = {"type": "activity", "num": 6, "name": act.get("title", "Apply"),
             "time": act.get("minutes", "~12 min"),
             "lead": "Use evidence from the reading and the source to build your answer.",
             "blocks": apply_blocks}

    # Guided Cornell notes
    cues = [t["term"] for t in vocab[:3]] + ["Who benefited? Who bore the cost?"]
    notes = {"type": "cornellnotes", "heading": "Cornell Notes (25 / 75)", "cues": cues}

    return {"code": code, "title": v["title"],
            "blocks": [front, vocab_tbl, close_read, hippo, apply, notes]}


def main():
    data = json.loads(UNIT_JSON.read_text())
    existing = {s["code"]: s for s in data["standards"]}
    order = ["US.01", "US.02", "US.03", "US.04", "US.05", "US.06", "US.07"]
    out = []
    for code in order:
        if code == "US.01":
            # keep hand-authored US.01, but add the vocab table + Apply activity for parity
            std = existing["US.01"]
            has_vocab_tbl = any(b.get("type") == "table" and b.get("head", [None])[0] == "Term"
                                for b in std["blocks"])
            if not has_vocab_tbl:
                v = BUILD["US.01"]; vocab = v.get("vocab", [])
                vt = {"type": "table", "head": ["Term", "What it means", "Español"],
                      "rows": [[f"<strong>{t['term']}</strong>", t.get("simple") or t["def"], t.get("es", "")]
                               for t in vocab]}
                # insert vocab table right after the cornell front (index 1)
                std["blocks"].insert(1, vt)
            out.append(std)
        else:
            out.append(gen_standard(code))
    data["standards"] = out
    UNIT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"wrote {UNIT_JSON}  |  standards: {[s['code'] for s in out]}")
    for s in out:
        print(f"  {s['code']}: {len(s['blocks'])} blocks")


if __name__ == "__main__":
    main()
