#!/usr/bin/env python3
"""
Geography review audit — the SME sign-off ledger.

Scans every unit's content JSON and reports, per standard that carries geography:
  - how many places are authored
  - how many sources back them
  - the geo_review status (drafted / sme_approved / needs_fix / n/a)

An SME signs off by editing the standard's `geo_review` in the content JSON:
    "geo_review": {"status": "sme_approved", "by": "<name>", "date": "<YYYY-MM-DD>", "note": ""}

Exit code is non-zero if `--require-approved` is set and any geo standard is not
sme_approved (wire this into the build/admin review to gate on human sign-off).

Usage:
  python3 geo_review_audit.py [/path/to/HistoryHack_Platinum] [--require-approved]
"""
import json, os, sys, glob

root = None
require_approved = False
for a in sys.argv[1:]:
    if a == "--require-approved": require_approved = True
    else: root = a
root = root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

files = sorted(glob.glob(os.path.join(root, "build_unit*", "unit*_content.json")))
rows, pending = [], 0
for f in files:
    try:
        d = json.load(open(f, encoding="utf8"))
    except Exception as e:
        print(f"!! could not read {f}: {e}"); continue
    unit = os.path.basename(os.path.dirname(f))
    std = d.get("standards", {})
    for code in d.get("order", list(std.keys())):
        s = std.get(code, {})
        geo = s.get("geo")
        if not (geo and str(geo).strip()):
            continue  # no geography dimension for this standard
        places = s.get("geo_places") or []
        sources = s.get("geo_sources") or []
        review = s.get("geo_review") or {}
        status = review.get("status", "MISSING")
        rows.append((unit, code, len(places), len(sources), status, review.get("by", "")))
        if status not in ("sme_approved", "n/a"):
            pending += 1

print(f"{'Unit':10} {'Std':7} {'Places':>6} {'Src':>4}  {'Review':16} By")
print("-" * 60)
for unit, code, np, ns, status, by in rows:
    flag = "" if status in ("sme_approved", "n/a") else "  <-- pending"
    print(f"{unit:10} {code:7} {np:6} {ns:4}  {status:16} {by}{flag}")
print("-" * 60)
print(f"{len(rows)} geo standards | {pending} pending SME sign-off "
      f"| {sum(1 for r in rows if r[4]=='sme_approved')} approved")

if require_approved and pending:
    print(f"\nFAIL: {pending} geography standard(s) not SME-approved.")
    sys.exit(1)
