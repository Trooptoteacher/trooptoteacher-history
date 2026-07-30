#!/usr/bin/env python3
"""Author analysis/unit1_assessment.json for the Assessment Book builder from the rigor-compliant
MCQ bank. formative + Form A come from mcq-bank.json (9 items, 1/standard); Form B is a parallel
set (distinct stems) so the two summative forms don't overlap. Schema: disclosure, formative{std:[]},
formA[], formB[]; item = {stem, std, dok, choices:[{id,text}], key, rc, reteach}. No district label."""
import json, os
HERE=os.path.dirname(os.path.abspath(__file__))
BANK=json.load(open(os.path.abspath(os.path.join(HERE,"..","..","..","WEB_EDITION","public","data","government","questions","unit-1","mcq-bank.json"))))
RC="RC-GOV1: Foundations of Constitutional Government"
RETEACH={
 "GC.01":"Re-anchor on Locke's Second Treatise; re-teach natural rights + social contract.",
 "GC.02":"Re-read the Declaration's preamble; connect grievances to the argument for separation.",
 "GC.03":"Review the Articles' lack of taxing power and Shays's Rebellion.",
 "GC.04":"Compare the Virginia and New Jersey Plans; re-teach the Great Compromise.",
 "GC.05":"Re-read the Preamble; list its six purposes and 'We the People'.",
 "GC.06":"Re-teach separation of powers + checks and balances with Federalist 51.",
 "GC.07":"Walk through Article V's two-step amendment process.",
 "GC.08":"Re-teach the Bill of Rights as limits on government; 1st and 10th Amendments.",
 "GC.09":"Contrast a republic and a direct democracy using Federalist 10.",
}
def from_bank(q):
    return {"stem":q["question"],"std":q["standard"],"dok":q["dok"],
            "choices":[{"id":k,"text":q["options"][k]} for k in ["A","B","C","D"]],
            "key":q["correctAnswer"],"rc":RC,"reteach":RETEACH.get(q["standard"],"")}
formA=[from_bank(q) for q in BANK["items"]]
formative={}
for q in BANK["items"]: formative.setdefault(q["standard"],[]).append(from_bank(q))

# Form B — parallel items (distinct stems), keys rotated for de-bias by the same convention
FB=[
 ("GC.01",1,"Locke's idea that people are born with rights to life, liberty, and property is called:",
  ["natural rights","the divine right of kings","popular sovereignty","judicial review"],0),
 ("GC.02",2,"The Declaration of Independence was written mainly to:",
  ["justify the colonies' separation from Britain","create the U.S. Congress","end slavery in the colonies","declare war on France"],0),
 ("GC.03",2,"A key weakness of the Articles of Confederation was that the national government could not:",
  ["tax the states or citizens","declare war on enemies","sign treaties abroad","operate a post office"],0),
 ("GC.04",3,"The Virginia and New Jersey Plans disagreed most about:",
  ["how states would be represented in Congress","whether to add a Bill of Rights","the date slavery would end","the president's term length"],0),
 ("GC.05",2,"The Preamble's phrase 'promote the general Welfare' names a:",
  ["purpose of the government","branch of the government","constitutional amendment","power of the courts"],0),
 ("GC.06",1,"Separation of powers divides the federal government into:",
  ["three branches","two houses","fifty states","nine courts"],0),
 ("GC.07",2,"A new amendment is formally added to the Constitution through:",
  ["the Article V process","a single presidential order","one Supreme Court ruling","a single state's vote"],0),
 ("GC.08",2,"The Tenth Amendment reserves undelegated powers to the:",
  ["states and the people","president alone","federal courts","Congress only"],0),
 ("GC.09",2,"In a representative democracy, laws are made by:",
  ["elected representatives","the people voting on each law","a single monarch","the military"],0),
]
def mk(std,dok,stem,opts,keyi):
    ids=["A","B","C","D"]
    return {"stem":stem,"std":std,"dok":dok,"choices":[{"id":ids[i],"text":opts[i]} for i in range(4)],
            "key":ids[keyi],"rc":RC,"reteach":RETEACH.get(std,"")}
formB=[mk(*x) for x in FB]
# de-bias Form B keys across items (rotate A/B/C/D)
L=["A","B","C","D"]
for i,q in enumerate(formB):
    tgt=L[i%4]; cur=q["key"]
    if cur!=tgt:
        ci={c["id"]:c["text"] for c in q["choices"]}
        ci[cur],ci[tgt]=ci[tgt],ci[cur]
        q["choices"]=[{"id":k,"text":ci[k]} for k in L]; q["key"]=tgt

out={"disclosure":"Assessment items are classroom-formative · pre-field-test.",
     "formative":formative,"formA":formA,"formB":formB}
s=json.dumps(out,indent=2,ensure_ascii=False); assert "W"+"CS" not in s
open(os.path.join(HERE,"unit1_assessment.json"),"w").write(s)
from collections import Counter
print("unit1_assessment.json: formative %d stds, Form A %d, Form B %d"%(len(formative),len(formA),len(formB)))
print("Form B key dist:",dict(Counter(q["key"] for q in formB)))
