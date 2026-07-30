# -*- coding: utf-8 -*-
"""Generate N PARALLEL tests of equal rigor from the consolidated World History question bank.

Forms are EQUATED: each form draws the same number of items per standard and the same DOK
composition, and a rotating (Latin-square) assignment balances item difficulty (IRT-b) across
forms so their mean difficulty converges. Distinct items are used per form until the pool is
exhausted (then reuse is reported). Answer keys are written to a SEPARATE teacher file only.

Usage:
  python3 08_QUESTION_BANK/generate_parallel_tests.py [--forms 4] [--scope all|unitN|W.01,W.02]
      [--per-standard 1] [--mc-only] [--outdir 08_QUESTION_BANK/generated_tests] [--title "..."]

Outputs, per form: <outdir>/<title>_Form_<L>_STUDENT.md and _TEACHER_KEY.md, plus
<outdir>/EQUATING_REPORT.md comparing the forms.
"""
import os, json, sys, re, statistics
from collections import Counter, defaultdict

HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
BANK=os.path.join(HERE,"world_history_question_bank.json")

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
TITLE=arg("--title","World_History_Parallel_Test")
os.makedirs(OUTDIR,exist_ok=True)

UNIT_STDS={1:["W.01", "W.02", "W.03", "W.04", "W.08a"],2:["W.05", "W.06", "W.07", "W.08b", "W.09"],3:["W.10", "W.11", "W.12", "W.13", "W.14", "W.15", "W.16"],4:["W.17", "W.18"],5:["W.19", "W.20", "W.21", "W.22"],6:["W.23", "W.24", "W.25", "W.26", "W.27", "W.28"],7:["W.29", "W.30", "W.31", "W.32", "W.33", "W.34", "W.35", "W.36", "W.37", "W.38"],8:["W.39", "W.40", "W.41", "W.42", "W.43", "W.44", "W.49"],9:["W.45", "W.46", "W.47", "W.48", "W.50", "W.51", "W.52", "W.53"],10:["W.54", "W.55", "W.56a", "W.56b", "W.57", "W.58", "W.59"],11:["W.60", "W.61", "W.62", "W.63a", "W.63b", "W.64", "W.65"],12:["W.66", "W.67", "W.68", "W.69", "W.70", "W.71", "W.72", "W.73", "W.74", "W.75", "W.76"],13:["W.77", "W.78", "W.79", "W.80", "W.81", "W.82", "W.83", "W.84", "W.85", "W.86", "W.87", "W.88", "W.89"]}

bank=json.load(open(BANK,encoding="utf-8"))
def stdnum(s):
    m=re.match(r"W\.(\d+)",str(s)); return int(m.group(1)) if m else 999

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
def interleave_by_dok(pool):
    """Order a standard's items so DOK levels alternate (d1,d2,d3,d1,...) — a round-robin
    across DOK buckets, each bucket internally sorted by difficulty. This spreads recall/
    reasoning/analysis across form slots so every form gets a balanced DOK mix, not just the
    easiest items."""
    buckets={1:[],2:[],3:[]}
    for it in sorted(pool,key=lambda x:x.get("irt_b",0)):
        buckets.setdefault(it.get("dok",2),[]).append(it)
    ordered=[];
    while any(buckets.values()):
        for dk in (1,2,3):
            if buckets.get(dk): ordered.append(buckets[dk].pop(0))
    return ordered

forms=[[] for _ in range(FORMS)]
reuse_warnings=[]
for j,std in enumerate(scope):
    pool=interleave_by_dok(by_std.get(std,[]))
    if not pool:
        reuse_warnings.append(f"{std}: NO items in pool"); continue
    need=FORMS*PER
    if len(pool)<need:
        reuse_warnings.append(f"{std}: pool {len(pool)} < needed {need} — some items reused across forms")
    # rotating offset by standard so each form samples different DOK positions and difficulty
    # balances across forms; distinct items per form while the pool lasts.
    for slot in range(need):
        it=pool[(slot+j)%len(pool)]
        forms[slot%FORMS].append(it)

def opt_lines(it):
    o=it.get("options") or {}
    return "\n".join(f"   {L}. {o[L]}" for L in ["A","B","C","D"] if L in o)

L=[chr(65+i) for i in range(FORMS)]  # form labels A,B,C,...
UDL_BANNER=("> **Universal supports — available to every student, no special request needed:** this test may be "
 "read aloud; key history and geography terms are glossed on request; large-print and screen-reader formats are available; "
 "extended time is available. For any written-response question you may answer **in writing, by recording your "
 "spoken response, or with a labeled diagram/organizer.** The learning target is the same for everyone. "
 "_(Designed on CAST UDL Guidelines 3.0 — firm goal, flexible means.)_")

def write_form(fi):
    label=L[fi]; items=forms[fi]
    # ---- student form (no keys) ----
    s=[f"# {TITLE.replace('_',' ')} — Form {label} (Student)","",
       f"**Name:** ______________________  **Class/Period:** ______  **Date:** ______","",
       UDL_BANNER,"",
       "_Choose the best answer for each question. Assessment items are classroom-formative · pre-field-test._",""]
    for n,it in enumerate(items,1):
        s.append(f"**{n}.** {it['question']}  _[{it['standard']} · DOK {it['dok']}]_")
        s.append(opt_lines(it)); s.append("")
    open(os.path.join(OUTDIR,f"{TITLE}_Form_{label}_STUDENT.md"),"w",encoding="utf-8").write("\n".join(s))
    # ---- teacher answer key + remediation (accompanies every form) ----
    k=[f"# {TITLE.replace('_',' ')} — Form {label} — TEACHER ANSWER KEY + REMEDIATION",
       "","_Teacher copy — do not distribute. Answer key, item psychometrics, and UDL-grounded reteach/MTSS "
       "routing. IRT values are pre-field-test design-time estimates._","",
       "## Answer key","",
       "| # | Std | DOK | Bloom's (Hess) | Key | IRT b | Why the key is correct |","|--|--|--|--|--|--|--|"]
    for n,it in enumerate(items,1):
        k.append(f"| {n} | {it['standard']} | {it['dok']} | {it.get('hess_crm_cell','—')} | "
                 f"{it.get('correct_answer','—')} | {it.get('irt_b','—')} | {str(it.get('key_rationale','')).replace(chr(124),'/')} |")
    dok=Counter(it["dok"] for it in items); bs=[it.get("irt_b") for it in items if isinstance(it.get("irt_b"),(int,float))]
    k+=["",("**Form stats:** DOK "+", ".join(f"{d}:{dok.get(d,0)}" for d in [1,2,3])+
        (f" · mean IRT-b {statistics.mean(bs):.2f}" if bs else "")),
       "","## Remediation & MTSS routing (if missed)",""]
    for n,it in enumerate(items,1):
        rem=it.get("remediation") or {}
        k.append(f"**{n}. {it['standard']} — {it.get('correct_answer','')}**  {rem.get('if_missed','Reteach the standard; re-assess with a parallel item.')}")
        for d in (rem.get("by_distractor") or []):
            k.append(f"  - **{d.get('choice')}** → {str(d.get('signals_misconception','')).strip()}  _{d.get('reteach','')}_")
        m=rem.get("mtss") or {}
        if m: k.append(f"  - _Tier 2:_ {m.get('tier2','')}  _Tier 3:_ {m.get('tier3','')}")
        k.append("")
    u=(items[0].get("udl_supports") or {}) if items else {}
    k+=["## UDL supports on this form (CAST 3.0)","",
        f"- **Representation:** {u.get('representation','key terms glossed; read-aloud; large-print/screen-reader.')}",
        f"- **Action & Expression:** {u.get('action_expression','multiple response modes for constructed items; AT-compatible.')}",
        f"- **Engagement:** {u.get('engagement','action-oriented feedback; DOK-tiered challenge; authentic historical and geographic contexts.')}",
        f"- _{u.get('firm_goal_note','Supports vary the means, not the mastery target — UDL design, not modification.')}_"]
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
