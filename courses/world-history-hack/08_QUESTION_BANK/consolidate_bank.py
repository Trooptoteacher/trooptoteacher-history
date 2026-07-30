# -*- coding: utf-8 -*-
"""Merge every per-unit item bank (BUILD/unitN/analysis/unitN_item_bank.json) into one
consolidated World History question bank, mirroring the U.S. History flagship all_questions.json
(flat array) but as a superset carrying full psychometrics. Sorts by standard then question_number.

Usage: python3 08_QUESTION_BANK/consolidate_bank.py
"""
import os, json, glob, re
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
OUT=os.path.join(HERE,"world_history_question_bank.json")
items=[]
for p in sorted(glob.glob(os.path.join(ROOT,"BUILD","unit*","analysis","unit*_item_bank*.json"))):
    try:
        d=json.load(open(p,encoding="utf-8"))
    except Exception as e:
        print(f"SKIP {p}: {e}"); continue
    if isinstance(d,list): items.extend(d)
    elif isinstance(d,dict) and isinstance(d.get("items"),list): items.extend(d["items"])
    print(f"  + {os.path.relpath(p,ROOT)}: {len(d if isinstance(d,list) else d.get('items',[]))} items")

def sk(it):
    m=re.match(r"W\.(\d+)",str(it.get("standard",""))); n=int(m.group(1)) if m else 999
    return (n, it.get("question_number",0))
items.sort(key=sk)
json.dump(items, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"\nWROTE {os.path.relpath(OUT,ROOT)}: {len(items)} items")
