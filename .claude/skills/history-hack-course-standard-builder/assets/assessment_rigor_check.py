#!/usr/bin/env python3
"""Item-rigor linter — enforces tn-assessment-specialist / tcap-item-writer-v2 objective rules:
(1) answer variance / de-biased keys, (2) option-length parity (no correct-is-longest; max/min word
ratio ≤ ~1.6 ≈ within 20% band), (3) Option D not the weakest, (4) every distractor tagged (PK/MC/PE/NE/
CA/AN/OG) + has a rationale, (5) no AOTA/NOTA, (6) no absolute-word clueing, (7) complete-question stems,
(8) parallel capitalization. Reports PASS/FLAG. Human/skill rubric still judges historical distractor quality."""
import json, os, re, sys
from collections import Counter
HERE=os.path.dirname(os.path.abspath(__file__))
# Usage: assessment_rigor_check.py [path/to/mcq-bank.json]  (default: Unit 1)
BANK=sys.argv[1] if len(sys.argv)>1 else os.path.abspath(os.path.join(
    HERE,"..","..","WEB_EDITION","public","data","government","questions","unit-1","mcq-bank.json"))
data=json.load(open(BANK))
mcq=[q for q in data["items"] if q["type"]=="multiple-choice"]
ABS=re.compile(r'\b(always|never)\b',re.I)  # ASC-prohibited absolute qualifiers (AOTA/NOTA checked separately)
TAGS={"PK","MC","PE","NE","CA","AN","OG"}
def wc(s): return len(s.split())
flags={}
def flag(qid,r): flags.setdefault(qid,[]).append(r)
dist=Counter(q["correctAnswer"] for q in mcq)
spread=max(dist.values())-min(dist.get(k,0) for k in "ABCD")
for q in mcq:
    o=q["options"]; opts=[o[k] for k in "ABCD"]; lens=[wc(x) for x in opts]
    key=q["correctAnswer"]; cl=wc(o[key])
    if cl==max(lens) and lens.count(max(lens))==1: flag(q["id"],"correct-is-longest")
    if max(lens)/max(1,min(lens))>1.6: flag(q["id"],"length-ratio>%0.1f(%d–%d w)"%(max(lens)/max(1,min(lens)),min(lens),max(lens)))
    if wc(o["D"])<max(1,min(wc(o["A"]),wc(o["B"]),wc(o["C"]))-1): flag(q["id"],"option-D-weakest")
    for k in "ABCD":
        if k!=key and ABS.search(o[k]): flag(q["id"],f"absolute-word-{k}")
    if any(re.search(r'(all|none) of the above',x,re.I) for x in opts): flag(q["id"],"AOTA/NOTA")
    # distractor tags + rationales
    for k in "ABCD":
        if k!=key and q["distractorTags"].get(k) not in TAGS: flag(q["id"],f"untagged-distractor-{k}")
        if not q["distractorRationales"].get(k): flag(q["id"],f"no-rationale-{k}")
    if not q["question"].strip().endswith(("?",":")): flag(q["id"],"stem-not-question-or-completion")
    caps=[x[:1].isupper() for x in opts if x]
    if len(set(caps))>1: flag(q["id"],"non-parallel-caps")
    # metacognitive: dok/blooms consistency
    if (q["blooms"]=="Remember" and q["dok"]>=3) or (q["blooms"] in("Evaluate","Create") and q["dok"]==1):
        flag(q["id"],"dok-blooms-mismatch")

print("=== ITEM-RIGOR REPORT v2 (Unit 1, tn-assessment-specialist schema) ===")
print(f"MCQ: {len(mcq)}")
print(f"Answer variance: keys={dict(dist)} spread={spread} -> {'PASS' if spread<=1 else 'FLAG'}")
ratios=[max(wc(q['options'][k]) for k in 'ABCD')/max(1,min(wc(q['options'][k]) for k in 'ABCD')) for q in mcq]
print(f"Avg option max/min length ratio: {sum(ratios)/len(ratios):.2f} (target ≤1.6)")
print(f"Per-item flags: {len(flags)}/{len(mcq)} flagged")
for qid,fs in sorted(flags.items()): print(f"   {qid}: {', '.join(fs)}")
if not flags: print("   ✓ ALL MCQ PASS objective rigor checks (length parity, D-strength, tags, rationales, stems, de-bias)")
