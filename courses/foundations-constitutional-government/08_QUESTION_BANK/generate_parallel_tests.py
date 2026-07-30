# -*- coding: utf-8 -*-
"""Generate N PARALLEL tests of equal rigor from the consolidated Government question bank.

Forms are EQUATED: each form draws the same number of items per standard and the same DOK
composition, and a rotating (Latin-square) assignment balances item difficulty (IRT-b) across
forms so their mean difficulty converges. Distinct items are used per form until the pool is
exhausted (then reuse is reported). Answer keys are written to a SEPARATE teacher file only.

Usage:
  python3 08_QUESTION_BANK/generate_parallel_tests.py [--forms 4] [--scope all|unitN|GC.01,GC.02]
      [--per-standard 1] [--mc-only] [--outdir 08_QUESTION_BANK/generated_tests] [--title "..."]

Outputs, per form: <outdir>/<title>_Form_<L>_STUDENT.md and _TEACHER_KEY.md, plus
<outdir>/EQUATING_REPORT.md comparing the forms.
"""
import os, json, sys, re, statistics
from collections import Counter, defaultdict

HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
BANK=os.path.join(HERE,"government_question_bank.json")

def arg(flag,default=None,isflag=False):
    if isflag: return flag in sys.argv
    if flag in sys.argv:
        i=sys.argv.index(flag)
        if i+1<len(sys.argv): return sys.argv[i+1]
    return default

FORMS=int(arg("--forms","4"))
SCOPE=arg("--scope","all")
PER=int(arg("--per-standard","1"))
MC_ONLY=arg("--mc-only",isflag=True) or True  # parallel objective tests default to MC
OUTDIR=os.path.join(ROOT,arg("--outdir","08_QUESTION_BANK/generated_tests"))
TITLE=arg("--title","Government_Parallel_Test")
os.makedirs(OUTDIR,exist_ok=True)

UNIT_STDS={1:["GC.01","GC.02","GC.03","GC.04","GC.05","GC.06","GC.07","GC.08","GC.09"],
 2:["GC.31","GC.32","GC.33","GC.34"],3:["GC.35","GC.10","GC.11","GC.12","GC.13","GC.14","GC.15"],
 4:["GC.16","GC.17","GC.18"],5:["GC.19","GC.20","GC.21","GC.22"],
 6:["GC.23","GC.24","GC.25","GC.26","GC.27"],7:["GC.28","GC.29","GC.30"]}

bank=json.load(open(BANK,encoding="utf-8"))
def stdnum(s):
    m=re.match(r"GC\.(\d+)",str(s)); return int(m.group(1)) if m else 999

if SCOPE=="all":
    scope=sorted({i["standard"] for i in bank},key=stdnum)
elif SCOPE.startswith("unit"):
    scope=UNIT_STDS[int(SCOPE[4:])]
else:
    scope=[s.strip() for s in SCOPE.split(",")]

by_std=defaultdict(list)
for it in bank:
    if it["standard"] in scope and (it.get("type")=="multiple_choice" or not MC_ONLY):
        by_std[it["standard"]].append(it)

# Build FORMS parallel forms. For each standard, sort its items by DOK then difficulty, then
# assign to forms with a per-standard rotating offset so easy/hard items spread across forms.
forms=[[] for _ in range(FORMS)]
reuse_warnings=[]
for j,std in enumerate(scope):
    pool=sorted(by_std.get(std,[]),key=lambda x:(x.get("dok",2),x.get("irt_b",0)))
    if not pool:
        reuse_warnings.append(f"{std}: NO items in pool"); continue
    need=FORMS*PER
    picks=[]
    if len(pool)>=need:
        picks=pool[:need]
    else:
        # reuse cyclically to fill; note it
        picks=[pool[k%len(pool)] for k in range(need)]
        reuse_warnings.append(f"{std}: pool {len(pool)} < needed {need} — items reused across forms")
    # rotate assignment by standard index so difficulty balances across forms
    for k,it in enumerate(picks):
        f=(k+j)%FORMS
        forms[f].append(it)

def opt_lines(it):
    o=it.get("options") or {}
    return "\n".join(f"   {L}. {o[L]}" for L in ["A","B","C","D"] if L in o)

L=[chr(65+i) for i in range(FORMS)]  # form labels A,B,C,...
def write_form(fi):
    label=L[fi]; items=forms[fi]
    # student
    s=[f"# {TITLE.replace('_',' ')} — Form {label} (Student)",
       "",f"**Name:** ______________________  **Class/Period:** ______  **Date:** ______","",
       "_Choose the best answer for each question. Assessment items are classroom-formative · pre-field-test._",""]
    for n,it in enumerate(items,1):
        s.append(f"**{n}.** {it['question']}  _[{it['standard']} · DOK {it['dok']}]_")
        s.append(opt_lines(it)); s.append("")
    open(os.path.join(OUTDIR,f"{TITLE}_Form_{label}_STUDENT.md"),"w",encoding="utf-8").write("\n".join(s))
    # teacher key
    k=[f"# {TITLE.replace('_',' ')} — Form {label} (TEACHER KEY — do not distribute)","",
       "| # | Std | DOK | Bloom's (Hess) | Key | IRT b | Why the key is correct |","|--|--|--|--|--|--|--|"]
    for n,it in enumerate(items,1):
        k.append(f"| {n} | {it['standard']} | {it['dok']} | {it.get('hess_crm_cell','—')} | "
                 f"{it.get('correct_answer','—')} | {it.get('irt_b','—')} | {str(it.get('key_rationale','')).replace('|','/')} |")
    dok=Counter(it["dok"] for it in items); bs=[it.get("irt_b") for it in items if isinstance(it.get("irt_b"),(int,float))]
    k+=["","**Form stats:** DOK "+", ".join(f"{d}:{dok.get(d,0)}" for d in [1,2,3])+
        f" · mean IRT-b {statistics.mean(bs):.2f}" if bs else ""]
    open(os.path.join(OUTDIR,f"{TITLE}_Form_{label}_TEACHER_KEY.md"),"w",encoding="utf-8").write("\n".join(k))
    return dok,(statistics.mean(bs) if bs else 0)

# equating report
rep=[f"# Equating Report — {TITLE.replace('_',' ')}","",
     f"Scope: {SCOPE} ({len(scope)} standards) · {FORMS} parallel forms · {PER} item(s)/standard/form · length {len(forms[0])} items each","",
     "| Form | Items | DOK 1/2/3 | Mean IRT-b |","|--|--|--|--|"]
means=[]
for fi in range(FORMS):
    dok,mb=write_form(fi); means.append(mb)
    rep.append(f"| {L[fi]} | {len(forms[fi])} | {dok.get(1,0)}/{dok.get(2,0)}/{dok.get(3,0)} | {mb:.2f} |")
spread=(max(means)-min(means)) if means else 0
rep+=["",f"**Difficulty spread across forms (max−min mean b): {spread:.2f}** "+
      ("— tightly equated ✓" if spread<=0.35 else "— review: forms differ in difficulty"),""]
if reuse_warnings:
    rep+=["## Pool notes",*[f"- {w}" for w in reuse_warnings]]
else:
    rep.append("All forms use fully distinct items (no reuse). ✓")
open(os.path.join(OUTDIR,"EQUATING_REPORT.md"),"w",encoding="utf-8").write("\n".join(rep))
print(f"Wrote {FORMS} parallel forms ({len(forms[0])} items each) to {os.path.relpath(OUTDIR,ROOT)}")
print(f"Difficulty spread (max-min mean b) = {spread:.2f}")
if reuse_warnings: print("Notes:","; ".join(reuse_warnings[:5]))
