#!/usr/bin/env python3
import json

BASE = "/home/user/workspace"
D = json.load(open(f"{BASE}/unit1-lean-full/_build.json"))
OUT = f"{BASE}/hh-web/public/data/us-history/tcap-decks/unit-1-lean/manifest.json"

# short title per slide
def title_for(s):
    k = s["kind"]
    std = s["standard"]
    foot = s.get("footer", "")
    # use the footer's descriptive tail after "·" when present
    if "·" in foot:
        tail = foot.split("·", 1)[1].strip()
    else:
        tail = s.get("title", "")
    if k == "Standard Divider":
        return f"{std} — {s.get('title','')}"
    if k == "Hook":
        return "Unit Hook: settling a continent — who pays?"
    if k == "Three Perspectives Synthesis":
        return f"{std} — Three Perspectives synthesis"
    if k == "Primary Source Analysis":
        return f"{std} — Source It First"
    if k == "We Do":
        return f"{std} — We Do: railroad → buffalo → people"
    if k == "Tennessee Connection":
        return f"{std} — Tennessee: George Jordan, Williamson County"
    return f"{std} — {tail}" if tail else f"{std} — {k}"

slides = []
for s in D["slides"]:
    n = s["n"]
    slides.append({
        "n": n,
        "image": f"/data/us-history/tcap-decks/unit-1-lean/slides/deckimg-{n:03d}.jpg",
        "title": title_for(s),
        "standard": s["standard"],
        "kind": s["kind"],
    })

manifest = {
    "unitId": "unit-1-lean",
    "unitLabel": "Unit 1 — The Rise of Industrialization · Lean Student Deck (US.01–US.07)",
    "standards": ["US.01", "US.02", "US.03", "US.04", "US.05", "US.06", "US.07"],
    "slideCount": len(slides),
    "aspectRatio": "16:9",
    "version": "2.0",
    "lastUpdated": "2026-07-01",
    "downloads": {
        "pptx": {
            "label": "Lean Student Deck (PowerPoint)",
            "path": "/downloads/tcap-decks/unit-1-lean/US_History_Hack_Unit1_Lean_Student_Deck.pptx",
            "filename": "US_History_Hack_Unit1_Lean_Student_Deck.pptx"
        },
        "answerKey": {
            "label": "Teacher Answer Key (PDF)",
            "path": "/downloads/tcap-decks/unit-1-lean/Unit1_Lean_Teacher_Answer_Key.pdf",
            "filename": "Unit1_Lean_Teacher_Answer_Key.pdf"
        },
        "usageGuide": {
            "label": "Teacher Usage Guide",
            "path": "/downloads/tcap-decks/unit-1-lean/Unit1_Lean_Deck_Usage_Guide.md",
            "filename": "Unit1_Lean_Deck_Usage_Guide.md"
        }
    },
    "slides": slides,
}

json.dump(manifest, open(OUT, "w"), ensure_ascii=False, indent=2)
print("Wrote", OUT, "with", len(slides), "slides")
