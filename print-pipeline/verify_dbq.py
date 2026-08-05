#!/usr/bin/env python3
"""DBQ GUARDRAIL — prevents the two Unit 1 DBQ failures from recurring:
  (1) image-only document set (OPTIC images, no HIPPO text excerpts), and
  (2) a referenced-but-missing excerpt corpus file (assets/unit-N-sources.json).

Checks, for a given unit N:
  A. The canonical excerpt corpus `history-hack-dbq-workbook/assets/unit-<N>-sources.json`
     EXISTS (the file build_workbook_template.py loads). Missing = BLOCKER.
  B. If a DBQ docs manifest JSON is given, the document set has BOTH >=1 text/HIPPO
     document AND >=1 visual/OPTIC document, and every doc carries honest provenance
     (author/source + date). Image-only = BLOCKER.

Usage:
  python3 verify_dbq.py <unit-number> [dbq_docs_manifest.json]
Manifest shape: {"documents":[{"id","kind":"text"|"visual","title","source","date"}...]}
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILL_ASSETS = ROOT.parent / ".claude/skills/history-hack-dbq-workbook/assets"


def check(unit, manifest_path=None):
    fails = []

    # A. corpus file must exist
    corpus = SKILL_ASSETS / f"unit-{unit}-sources.json"
    if not corpus.exists():
        fails.append(f"MISSING CORPUS: {corpus.relative_to(ROOT.parent)} is referenced by "
                     f"build_workbook_template.py but absent — reconstruct + commit it before building.")

    # B. document-set balance (text + visual) if a manifest is provided
    if manifest_path:
        docs = json.loads(Path(manifest_path).read_text()).get("documents", [])
        text = [d for d in docs if d.get("kind") == "text"]
        visual = [d for d in docs if d.get("kind") == "visual"]
        if not text:
            fails.append("IMAGE-ONLY: no text/HIPPO documents — a DBQ must pair text excerpts with visual sources.")
        if not visual:
            fails.append("NO VISUAL SOURCES: add OPTIC-analyzed cartoon/photo/map documents.")
        if len(docs) < 5:
            fails.append(f"THIN SET: only {len(docs)} documents (a DBQ wants >=5-8).")
        for d in docs:
            if not (d.get("source") and d.get("date")):
                fails.append(f"PROVENANCE: document '{d.get('id', d.get('title','?'))}' lacks source/date.")

    return fails


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: verify_dbq.py <unit-number> [manifest.json]")
    unit = sys.argv[1]
    manifest = sys.argv[2] if len(sys.argv) > 2 else None
    fails = check(unit, manifest)
    print("=" * 60)
    print(f"DBQ GUARDRAIL — Unit {unit}")
    print("=" * 60)
    if fails:
        for f in fails:
            print("  ✗ BLOCKER:", f)
        print(f"\n  {len(fails)} blocker(s) — DBQ not ready.")
        sys.exit(1)
    print("  ✓ PASS — corpus present" + ("; document set balanced (text + visual) with provenance." if manifest else "."))
    sys.exit(0)


if __name__ == "__main__":
    main()
