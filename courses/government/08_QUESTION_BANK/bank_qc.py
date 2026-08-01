# -*- coding: utf-8 -*-
"""QC / rigor report for the consolidated Government question bank.
Checks: per-standard coverage, DOK & type & Bloom's distributions, MC key-letter balance,
IRT-b difficulty spread, duplicate/near-duplicate stems, required-field completeness,
and a forbidden-string leak scan. Prints a report and exits non-zero if hard checks fail.

Usage: python3 08_QUESTION_BANK/bank_qc.py
"""
import os, json, re, sys, statistics
from collections import Counter, defaultdict
HERE=os.path.dirname(os.path.abspath(__file__))
BANK=os.path.join(HERE,"government_question_bank.json")
items=json.load(open(BANK,encoding="utf-8"))
FORBIDDEN=["History Hack","Williamson","George Jordan","Homestead","Transcontinental","Gilded",
           "industrializ","U.S. history","flight log","WCS"]
US_CODE=re.compile(r"\bUS\.\d")
REQ=["id","standard","unit","question_number","type","dok","level","question","correct_answer",
     "blooms","hess_crm_cell","irt_a","irt_b","irt_c","c3_dimension","distractor_tags","bias_flag"]
MCREQ=["options"]
hard_fail=0; soft=0

by_std=defaultdict(list)
for it in items: by_std[it.get("standard")].append(it)

print(f"# Government Question Bank — QC Report")
print(f"Total items: {len(items)}   ·   Standards covered: {len(by_std)}\n")

# 1. coverage
print("## Per-standard coverage")
thin=[]
for s in sorted(by_std,key=lambda x:(int(re.match(r'GC\.(\d+)',x).group(1)) if re.match(r'GC\.(\d+)',x) else 999)):
    g=by_std[s]; dok=Counter(i.get("dok") for i in g); typ=Counter(i.get("type") for i in g)
    mc=[i for i in g if i.get("type")=="multiple_choice"]
    keys=Counter(i.get("correct_answer") for i in mc)
    print(f"  {s}: {len(g)} items · DOK {dict(sorted(dok.items()))} · MC {len(mc)} keys {dict(keys)}")
    if len(g)<8: thin.append(s)
if thin: print(f"  THIN (<8): {', '.join(thin)}"); soft+=len(thin)

# 2. distributions
dok=Counter(i.get("dok") for i in items); n=len(items)
print("\n## DOK distribution (target ~ 20/40/40)")
for k in [1,2,3]:
    print(f"  DOK {k}: {dok.get(k,0)} ({100*dok.get(k,0)//max(n,1)}%)")
print("## Type distribution")
for t,c in Counter(i.get("type") for i in items).most_common(): print(f"  {t}: {c}")
print("## Bloom's distribution")
for b,c in Counter(i.get("blooms") for i in items).most_common(): print(f"  {b}: {c}")

# 3. global MC key balance
mc=[i for i in items if i.get("type")=="multiple_choice"]
kb=Counter(i.get("correct_answer") for i in mc)
print(f"\n## MC key-letter balance (n={len(mc)}): {dict(sorted(kb.items()))}")
if mc:
    mx=max(kb.values())/len(mc)
    if mx>0.35: print(f"  WARN key '{kb.most_common(1)[0][0]}' = {100*mx:.0f}% (>35%)"); soft+=1

# 4. IRT-b spread
bs=[i.get("irt_b") for i in items if isinstance(i.get("irt_b"),(int,float))]
if bs: print(f"\n## IRT difficulty b: n={len(bs)} mean={statistics.mean(bs):.2f} min={min(bs):.2f} max={max(bs):.2f}")

# 5. required fields
missing=defaultdict(int)
for it in items:
    for f in REQ:
        if f not in it or it.get(f) in (None,"") and f!="bias_flag": missing[f]+=1
    if it.get("type")=="multiple_choice":
        if not it.get("options") or len(it.get("options",{}))!=4: missing["options(4)"]+=1
        if it.get("correct_answer") not in (it.get("options") or {}): missing["key_in_options"]+=1
if missing:
    print("\n## MISSING/INVALID required fields"); [print(f"  {k}: {v}") for k,v in missing.items()]; hard_fail+=sum(missing.values())
else: print("\n## Required fields: all present ✓")

# 6. duplicate stems
seen=defaultdict(list)
for it in items: seen[re.sub(r'\s+',' ',str(it.get("question","")).strip().lower())].append(it.get("id"))
dups={k:v for k,v in seen.items() if len(v)>1}
if dups:
    print(f"\n## DUPLICATE stems: {len(dups)}"); [print(f"  {v}") for v in list(dups.values())[:10]]; hard_fail+=len(dups)
else: print("## Duplicate stems: none ✓")

# 7. leak scan
blob=json.dumps(items,ensure_ascii=False)
hits=[t for t in FORBIDDEN if t.lower() in blob.lower()]+(["US.xx code"] if US_CODE.search(blob) else [])
print(f"\n## Leak scan: {'CLEAN ✓' if not hits else 'HITS: '+', '.join(hits)}")
if hits: hard_fail+=len(hits)

print(f"\n=== {'PASS' if hard_fail==0 else 'FAIL'} · hard issues={hard_fail} · soft warnings={soft} ===")
sys.exit(1 if hard_fail else 0)
