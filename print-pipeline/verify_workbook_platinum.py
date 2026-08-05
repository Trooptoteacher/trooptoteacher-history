#!/usr/bin/env python3
"""PLATINUM WORKBOOK GUARDRAIL — fails the build if a unit workbook JSON is not built to
the STUDENT_WORKBOOK_PLATINUM_STANDARD 7-activity anatomy. Wire this into every workbook
build so a thin/partial workbook can NEVER ship again (this is the guardrail Sean asked
for after a partial Unit 1 shipped).

Checks, per unit-NN.json:
  - front matter carries "My SMART Goals"
  - EVERY standard has: an Opener, all SEVEN activities in order, an Exit Ticket
  - EVERY standard embeds Future Ready (>=1 FR tag) and ACT (>=1 ACT-Connection tag)
  - EVERY standard has a guided Cornell block AND ruled writing space (lines/cornell/write)
Exit code 0 = pass; 1 = one or more BLOCKERS (printed).

Usage: python3 verify_workbook_platinum.py content/us-history/unit-01.json
"""
import json
import sys
from pathlib import Path

REQUIRED_HEADS = [
    "Opener",
    "Activity 1 · Vocabulary",
    "Activity 2 · Vocabulary Studio",
    "Activity 3 · Cornell Notes",
    "Activity 4 · Close Read",
    "Activity 5 · Primary Source",
    "Activity 6 · Practice Quiz",
    "Activity 7 · Constructed Response",
    "Exit Ticket",
]


def heads(blocks):
    return [b.get("text", "") for b in blocks if b.get("type") == "head"]


def types(blocks):
    return [b.get("type") for b in blocks]


def texts(blocks):
    return " ".join(json.dumps(b, ensure_ascii=False) for b in blocks)


def check(path):
    data = json.loads(Path(path).read_text())
    fails = []

    front = texts(data.get("front", []))
    if "My SMART Goals" not in front:
        fails.append("FRONT MATTER: missing 'My SMART Goals' page")

    stds = data.get("standards", [])
    if not stds:
        fails.append("no standards found")

    for s in stds:
        code = s.get("code", "?")
        h = heads(s["blocks"])
        hjoined = " | ".join(h)
        # required heads present and in order
        last = -1
        for req in REQUIRED_HEADS:
            idx = next((i for i, x in enumerate(h) if x.startswith(req) or req in x), -1)
            if idx == -1:
                fails.append(f"{code}: MISSING '{req}'")
            elif idx < last:
                fails.append(f"{code}: '{req}' is OUT OF ORDER")
            else:
                last = idx
        body = texts(s["blocks"])
        if "Future Ready" not in body:
            fails.append(f"{code}: no Future Ready tag embedded")
        if "ACT Connection" not in body:
            fails.append(f"{code}: no ACT-Connection tag embedded")
        t = types(s["blocks"])
        if "cornell" not in t:
            fails.append(f"{code}: no guided Cornell block (the spine)")
        if "lines" not in t and "cornell" not in t and not any(
                b.get("class") == "write" for b in s["blocks"] if b.get("type") == "table"):
            fails.append(f"{code}: no ruled writing space (lines / cornell / write table)")

    return fails


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "content/us-history/unit-01.json"
    fails = check(path)
    print("=" * 64)
    print(f"PLATINUM WORKBOOK GUARDRAIL — {path}")
    print("=" * 64)
    if fails:
        for f in fails:
            print("  ✗ BLOCKER:", f)
        print(f"\n  {len(fails)} blocker(s) — NOT platinum. Build must not ship.")
        sys.exit(1)
    print("  ✓ PASS — full 7-activity anatomy, Future Ready + ACT embedded, ruled writing space, all standards.")
    sys.exit(0)


if __name__ == "__main__":
    main()
