# -*- coding: utf-8 -*-
"""Full inventory + standards crosswalk for the Government question bank.

Emits:
  - item_inventory.csv        every item, flat (id, standard, unit, type, dok, level, blooms,
                              hess, C3, SSP, key, IRT a/b/c, TN-specific, tcap_format, topics)
  - standards_crosswalk.csv   one row per standard: coverage + DOK/type mix + verbatim standard
  - QUESTION_BANK_INVENTORY.md narrative rollups + the full crosswalk table

Usage: python3 08_QUESTION_BANK/build_inventory.py
"""
import os, json, csv, re
from collections import Counter, defaultdict
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
BANK=os.path.join(HERE,"government_question_bank.json")
items=json.load(open(BANK,encoding="utf-8"))

# standard metadata (verbatim text, dimensions, TCA, unit title)
STD={}
def findkey(o,code):
    if isinstance(o,dict):
        if code in o and isinstance(o[code],dict) and "standard" in o[code]: return o[code]
        for v in o.values():
            r=findkey(v,code)
            if r: return r
    elif isinstance(o,list):
        for x in o:
            r=findkey(x,code)
            if r: return r
src=json.load(open(os.path.join(ROOT,"05_STANDARDS_ALIGNMENT","government_standards_source.json"),encoding="utf-8"))
CODES=sorted({i["standard"] for i in items},key=lambda s:int(re.match(r"GC\.(\d+)",s).group(1)))
for c in CODES:
    r=findkey(src,c) or {}
    STD[c]=dict(title=r.get("title",c),std=r.get("standard",""),dim=r.get("dimensions",""),
                tca=("Yes" if r.get("legally_required") else ""),unit=r.get("unit",""),
                unit_title=r.get("unit_title",""))

by=defaultdict(list)
for it in items: by[it["standard"]].append(it)

# ---- item_inventory.csv ----
with open(os.path.join(HERE,"item_inventory.csv"),"w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(["id","standard","unit","reporting_category","type","dok","level","blooms","hess_crm_cell",
                "c3_dimension","ssp","correct_answer","irt_a","irt_b","irt_c","tennessee_specific",
                "tcap_format","field_test_ready","topics"])
    for it in items:
        w.writerow([it.get("id"),it.get("standard"),it.get("unit"),it.get("reporting_category"),it.get("type"),
                    it.get("dok"),it.get("level"),it.get("blooms"),it.get("hess_crm_cell"),it.get("c3_dimension"),
                    it.get("ssp"),it.get("correct_answer"),it.get("irt_a"),it.get("irt_b"),it.get("irt_c"),
                    it.get("tennessee_specific"),it.get("tcap_format"),it.get("field_test_ready"),
                    "; ".join(it.get("topics",[]) if isinstance(it.get("topics"),list) else [])])

# ---- standards_crosswalk.csv ----
def row_for(c):
    g=by[c]; dok=Counter(i.get("dok") for i in g); typ=Counter(i.get("type") for i in g)
    ssp=sorted({i.get("ssp") for i in g if i.get("ssp")}); c3=sorted({i.get("c3_dimension") for i in g if i.get("c3_dimension")})
    tn=sum(1 for i in g if i.get("tennessee_specific"))
    ids=sorted(i.get("id") for i in g)
    return dict(standard=c,unit=STD[c]["unit"],title=STD[c]["title"],dimensions=STD[c]["dim"],tca=STD[c]["tca"],
        items=len(g),dok1=dok.get(1,0),dok2=dok.get(2,0),dok3=dok.get(3,0),
        mc=typ.get("multiple_choice",0),sa=typ.get("short_answer",0),cr=typ.get("constructed_response",0),
        er=typ.get("extended_response",0),dbq=typ.get("document_based",0),tn_specific=tn,
        ssp="/".join(ssp),c3="/".join(c3),id_range=f"{ids[0]}–{ids[-1]}",
        reporting_category=g[0].get("reporting_category",""),verbatim=STD[c]["std"])
rows=[row_for(c) for c in CODES]
with open(os.path.join(HERE,"standards_crosswalk.csv"),"w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); [w.writerow(r) for r in rows]

# ---- QUESTION_BANK_INVENTORY.md ----
L=["# Government Question Bank — Full Inventory & Standards Crosswalk","",
   f"**Foundations of Constitutional Government** (Government Hack edition) · Tennessee U.S. Government & Civics (GC).",
   f"Total items: **{len(items)}** across **{len(CODES)} standards** (GC.01–GC.35).",
   "Each item carries full psychometrics (DOK, Bloom's, Hess CRM cell, IRT 3PL, C3, SSP, coded distractors),",
   "CAST UDL 3.0 supports, and distractor-based MTSS remediation. Answer keys are teacher-side only.",""]
# rollups
L+=["## Rollups","",
    "| Dimension | Breakdown |","|---|---|"]
L.append(f"| Items per unit | "+", ".join(f"U{u}: {sum(1 for i in items if i.get('unit')==u)}" for u in range(1,8))+" |")
L.append(f"| DOK | "+", ".join(f"DOK{k}: {sum(1 for i in items if i.get('dok')==k)}" for k in [1,2,3])+" |")
L.append(f"| Item type | "+", ".join(f"{t}: {c}" for t,c in Counter(i.get('type') for i in items).most_common())+" |")
L.append(f"| Bloom's | "+", ".join(f"{b}: {c}" for b,c in Counter(i.get('blooms') for i in items).most_common())+" |")
mc=[i for i in items if i.get('type')=='multiple_choice']
L.append(f"| MC answer-key balance | "+", ".join(f"{k}: {v}" for k,v in sorted(Counter(i.get('correct_answer') for i in mc).items()))+f" (n={len(mc)}) |")
L.append(f"| TN-specific items | {sum(1 for i in items if i.get('tennessee_specific'))} |")
bs=[i.get('irt_b') for i in items if isinstance(i.get('irt_b'),(int,float))]
L.append(f"| IRT difficulty b | mean {sum(bs)/len(bs):.2f}, range {min(bs):.2f}…{max(bs):.2f} |")
L.append(f"| TCAP-format MC/MS | {sum(1 for i in items if i.get('tcap_format'))} · field-test-ready {sum(1 for i in items if i.get('field_test_ready'))} |")
# crosswalk table
L+=["","## Standards crosswalk","",
    "| Std | U | Title | Dim | TCA | Items | DOK 1/2/3 | MC | SA | CR | ER | DBQ | TN | SSP | C3 | Item IDs |",
    "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    L.append(f"| {r['standard']} | {r['unit']} | {r['title']} | {r['dimensions']} | {r['tca']} | {r['items']} | "
             f"{r['dok1']}/{r['dok2']}/{r['dok3']} | {r['mc']} | {r['sa']} | {r['cr']} | {r['er']} | {r['dbq']} | "
             f"{r['tn_specific']} | {r['ssp']} | {r['c3']} | {r['id_range']} |")
L+=["","## Verbatim standards (source of truth)",""]
for r in rows:
    L.append(f"- **{r['standard']}** ({r['reporting_category']}): {r['verbatim']}")
L+=["","---","_Generated by build_inventory.py from government_question_bank.json. "
    "IRT parameters are pre-field-test design-time estimates._"]
open(os.path.join(HERE,"QUESTION_BANK_INVENTORY.md"),"w",encoding="utf-8").write("\n".join(L))
print(f"Wrote item_inventory.csv ({len(items)} rows), standards_crosswalk.csv ({len(rows)} standards), QUESTION_BANK_INVENTORY.md")
