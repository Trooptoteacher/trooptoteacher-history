#!/usr/bin/env python3
"""Item-rigor linter — enforces the objective item-writing rules the product standard requires:
 (1) answer variance / de-biased keys (even A/B/C/D), (2) option-length parity (the correct answer must
 NOT be the giveaway longest/shortest option), (3) no absolute-word clueing, (4) no all/none-of-the-above,
 (5) stem length sanity, (6) parallel option structure. Reports PASS/FLAG per rule and lists offending ids.
Does not judge historical distractor plausibility — that needs the human/item-writer rubric."""
import json, os, glob, re
from collections import Counter
HERE=os.path.dirname(os.path.abspath(__file__))
QDIR=os.path.abspath(os.path.join(HERE,"..","..","WEB_EDITION","public","data","government","questions","unit-1"))
items=[]
for f in sorted(glob.glob(os.path.join(QDIR,"dok-*.json"))):
    items+=json.load(open(f))["items"]
mcq=[q for q in items if q["type"]=="multiple_choice"]
ABS=re.compile(r'\b(always|never|all|none|only|every|no one|everyone)\b',re.I)
def wc(s): return len(s.split())
flags={}
def flag(qid,rule): flags.setdefault(qid,[]).append(rule)

# 1. answer variance
dist=Counter(q["correct_answer"] for q in mcq)
spread=max(dist.values())-min(dist.get(k,0) for k in "ABCD")
key_ok = spread<=max(1,round(len(mcq)*0.15))
# per-item checks
for q in mcq:
    opts=[q["options"][k] for k in "ABCD"]; lens=[wc(o) for o in opts]
    correct=q["options"][q["correct_answer"]]; cl=wc(correct)
    # 2. option-length parity: correct must not be uniquely longest or shortest, and spread must be modest
    if cl==max(lens) and lens.count(max(lens))==1: flag(q["id"],"correct-is-longest")
    if cl==min(lens) and lens.count(min(lens))==1 and max(lens)-min(lens)>=3: flag(q["id"],"correct-is-shortest")
    if max(lens)>0 and max(lens)/max(1,min(lens))>2.2: flag(q["id"],"option-length-imbalance(%d–%d words)"%(min(lens),max(lens)))
    # 3. absolute-word clueing in distractors
    for k in "ABCD":
        if k!=q["correct_answer"] and ABS.search(q["options"][k]): flag(q["id"],f"absolute-word-in-distractor-{k}")
    # 4. all/none of the above
    if any(re.search(r'(all|none) of the above',o,re.I) for o in opts): flag(q["id"],"all/none-of-the-above")
    # 5. stem length
    sl=wc(q["question"])
    if sl<5: flag(q["id"],"stem-too-short")
    if sl>60: flag(q["id"],"stem-too-long")
    # 6. parallel structure — options should start with same case (all cap or all lower)
    caps=[o[:1].isupper() for o in opts if o]
    if len(set(caps))>1: flag(q["id"],"non-parallel-capitalization")

print("=== ITEM-RIGOR REPORT (Unit 1) ===")
print(f"MCQ items: {len(mcq)} | CR: {sum(1 for q in items if q['type']=='constructed_response')} | DBQ: {sum(1 for q in items if q['type']=='dbq')}")
print(f"1. Answer variance / de-bias: keys={dict(dist)}  spread={spread}  -> {'PASS' if key_ok else 'FLAG'}")
print(f"2-6. Per-item rigor flags: {len(flags)} of {len(mcq)} MCQ flagged")
for qid,fs in sorted(flags.items()):
    print(f"   {qid}: {', '.join(fs)}")
if not flags: print("   (none — all MCQ pass length-parity, clueing, parallel-structure checks)")
# option-length stats
allratios=[]
for q in mcq:
    lens=[wc(q["options"][k]) for k in "ABCD"]; allratios.append(max(lens)/max(1,min(lens)))
print(f"Avg max/min option-length ratio: {sum(allratios)/len(allratios):.2f} (closer to 1.0 = better parity)")
