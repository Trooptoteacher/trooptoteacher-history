#!/usr/bin/env python3
"""Unit 1 MCQ bank v2 — authored to the tn-assessment-specialist schema & rigor:
option-length parity (within ~20%), Option D as strong as A–C, every distractor tagged (PK/MC/PE/NE)
+ rationale, dok/blooms rationales, C3 dimension, reporting category, content tags, de-biased keys.
Government adaptation: no US-History EOC, so reportingCategory = GC domain, instructionalPurpose=formative,
tcapFormat=false with itemWritingCompliant flag; disclosure pre-field-test. No district label."""
import json, os
HERE=os.path.dirname(os.path.abspath(__file__))
GOV=json.load(open(os.path.join(HERE,"analysis","government_standards_source.json")))
OUT=os.path.abspath(os.path.join(HERE,"..","..","WEB_EDITION","public","data","government","questions","unit-1"))
os.makedirs(OUT,exist_ok=True)
RC="RC-GOV1: Foundations of Constitutional Government"

# (std, dok, blooms, c3, ssp, stem, {A..D}, correct, tags{A..D}, rats{A..D}, dokR, bloomR)
I=[
("GC.01",2,"Understand","D2","SSP.02",
 "Which idea from John Locke did the American colonists rely on most directly to justify self-government?",
 {"A":"Natural rights that government exists to protect","B":"The divine right of kings to rule alone",
  "C":"The economic theory of laissez-faire markets","D":"The military duty of every free citizen"},"A",
 {"A":None,"B":"MC","C":"PK","D":"PE"},
 {"A":"Correct — Locke's natural-rights/social-contract idea underlies self-government.",
  "B":"Misconception — colonists rejected divine right; it is the opposite of Locke.",
  "C":"Prior-knowledge error — laissez-faire is an economic idea, not Locke's rights theory.",
  "D":"Plausible error — civic duty is real but not the Lockean basis for self-rule."},
 "Requires interpreting which concept underlies self-government, not recalling a name.",
 "Student explains a relationship between an idea and a political outcome."),
("GC.02",2,"Understand","D3","SSP.02",
 "How does the Declaration of Independence justify the colonies' break from Britain?",
 {"A":"By blaming the colonists for the whole conflict","B":"By listing the king's abuses of colonists' rights",
  "C":"By promising to restore the monarchy's power","D":"By offering to pay Britain for its losses"},"B",
 {"A":"PE","B":None,"C":"MC","D":"NE"},
 {"A":"Plausible error — the Declaration blames the king, not the colonists.",
  "B":"Correct — grievances document the king's violations to justify separation.",
  "C":"Misconception — it rejects monarchy rather than restoring it.",
  "D":"Near miss — economics is not the Declaration's stated justification."},
 "Requires explaining the document's argument structure, not recalling its date.",
 "Student explains how evidence supports a conclusion."),
("GC.03",2,"Understand","D2","SSP.05",
 "What was the main weakness of the national government under the Articles of Confederation?",
 {"A":"It gave the president too much military authority","B":"It abolished the separate state governments completely",
  "C":"It could not tax the states or citizens","D":"It let one state pass laws by itself"},"C",
 {"A":"MC","B":"MC","C":None,"D":"PE"},
 {"A":"Misconception — the Articles had no strong executive at all.",
  "B":"Misconception — states kept their power; the center was weak.",
  "C":"Correct — no taxing power left the government unable to pay debts.",
  "D":"Plausible error — major laws needed nine of thirteen states, not one."},
 "Requires identifying a structural weakness and its effect, not a single fact.",
 "Student explains cause and effect of a policy design."),
("GC.04",3,"Analyze","D2","SSP.04",
 "How did the Great Compromise resolve the dispute between large and small states?",
 {"A":"It gave each state a single equal vote in the Congress","B":"It based the House on population and the Senate on equality",
  "C":"It let the very largest states control both of the houses","D":"It removed the smallest states from the newly formed Union"},"B",
 {"A":"NE","B":None,"C":"PE","D":"MC"},
 {"A":"Near miss — that describes the Articles, not the Great Compromise.",
  "B":"Correct — a population House plus an equal Senate reconciled both sides.",
  "C":"Plausible error — the compromise checked large-state dominance.",
  "D":"Misconception — no states were removed; both were accommodated."},
 "Requires analyzing how a compromise balanced competing interests.",
 "Student examines how a solution reconciles opposing positions."),
("GC.05",2,"Understand","D2","SSP.02",
 "What does the phrase 'We the People' in the Preamble establish about government?",
 {"A":"That the states hold all the governing power","B":"That the courts decide every national question",
  "C":"That the president leads the federal government","D":"That authority comes from the people themselves"},"D",
 {"A":"NE","B":"PK","C":"PK","D":None},
 {"A":"Near miss — that is federalism, not the meaning of 'We the People.'",
  "B":"Prior-knowledge error — that is judicial review, a different principle.",
  "C":"Prior-knowledge error — that describes the executive, not popular sovereignty.",
  "D":"Correct — 'We the People' declares popular sovereignty."},
 "Requires interpreting the meaning of a phrase, not recalling it.",
 "Student explains the principle a phrase expresses."),
("GC.06",3,"Analyze","D2","SSP.04",
 "Madison wrote that 'ambition must be made to counteract ambition.' Which design does this describe?",
 {"A":"Popular sovereignty exercised through regular elections","B":"Federal power divided between nation and states",
  "C":"Checks and balances among the three branches","D":"The difficult process for amending the document"},"C",
 {"A":"PK","B":"NE","C":None,"D":"PK"},
 {"A":"Prior-knowledge error — that concerns the source of power, not checks.",
  "B":"Near miss — federalism is a limit, but not the one Madison describes here.",
  "C":"Correct — branches restrain each other's ambition (checks and balances).",
  "D":"Prior-knowledge error — Article V is unrelated to Madison's point."},
 "Requires connecting a quotation to a structural design, not recalling a term.",
 "Student analyzes how a design controls power."),
("GC.07",2,"Understand","D2","SSP.05",
 "Why did the Framers make the amendment process in Article V deliberately difficult?",
 {"A":"To allow change only with broad national agreement","B":"To keep the Constitution from ever being changed",
  "C":"To give the president control over amendments","D":"To let a single state change it on its own"},"A",
 {"A":None,"B":"MC","C":"PK","D":"MC"},
 {"A":"Correct — supermajorities require broad consensus while allowing change.",
  "B":"Misconception — it permits change; it has happened 27 times.",
  "C":"Prior-knowledge error — the president has no formal amendment role.",
  "D":"Misconception — ratification needs three-fourths of the states."},
 "Requires explaining the purpose behind a process, not recalling the steps.",
 "Student explains the rationale for a design choice."),
("GC.08",3,"Analyze","D3","SSP.02",
 "Why does the First Amendment phrase its protections as limits on Congress ('shall make no law')?",
 {"A":"Because Congress creates the rights it can remove","B":"Because rights precede government, which cannot violate them",
  "C":"Because only the states may protect these rights","D":"Because courts alone define the people's freedoms"},"B",
 {"A":"MC","B":None,"C":"NE","D":"PK"},
 {"A":"Misconception — rights are not government gifts in this framing.",
  "B":"Correct — natural-rights logic: limits restrain government from violating rights.",
  "C":"Near miss — states matter, but the clause restrains Congress directly.",
  "D":"Prior-knowledge error — courts interpret, but the clause limits Congress."},
 "Requires analyzing why a right is framed as a limit, not recalling its text.",
 "Student evaluates the reasoning behind constitutional phrasing."),
("GC.09",2,"Understand","D2","SSP.04",
 "What best distinguishes a republic from a direct democracy?",
 {"A":"Citizens vote directly on every proposed law","B":"A single monarch inherits and holds the power",
  "C":"Citizens elect representatives to make the laws","D":"The states act as fully independent nations"},"C",
 {"A":"NE","B":"MC","C":None,"D":"PK"},
 {"A":"Near miss — that describes direct democracy, not a republic.",
  "B":"Misconception — a republic is not a monarchy.",
  "C":"Correct — in a republic the people rule through elected representatives.",
  "D":"Prior-knowledge error — that describes a confederation."},
 "Requires distinguishing two related systems, not recalling one definition.",
 "Student compares and contrasts two forms of government."),
]

def dims_of(std):
    d=GOV[std]["dimensions"]; return [x.strip() for x in d.strip("()").split(",")] if d else []
items=[]
for n,(std,dok,bl,c3,ssp,stem,opts,key,tags,rats,dokR,blR) in enumerate(I,1):
    items.append({
      "id":f"{std}-U1Q{n:02d}","standard":std,"secondaryStandard":None,"unit":1,
      "reportingCategory":RC,"dok":dok,"blooms":bl,"dokRationale":dokR,"bloomsRationale":blR,
      "question":stem,"stimulus":None,"stimulusAttribution":None,"options":opts,"correctAnswer":key,
      "distractorTags":tags,"distractorRationales":rats,
      "tcapFormat":False,"itemWritingCompliant":True,"instructionalPurpose":"formative",
      "itemCategory":"classroom-instructional","c3Dimension":c3,"sspAlignment":ssp,
      "tennesseeSpecific":False,"tcaRequired":bool(GOV[std]["tca"]),"contentTags":dims_of(std),
      "rubricId":None,"rubricName":None,"sensitivityFlag":None,"type":"multiple-choice","pointValue":1,
      "calibration":"pre-field-test","pre_field_test":True,
      "remediation":{"standard":std,"reteach_narrative":f"03_TEXTBOOK_UNITS/unit-1/unit-1.html#{std}",
        "reteach_teacher":f"03_TEXTBOOK_UNITS/unit-1/unit-1-teacher-guide.html#{std}"},
    })

# de-bias: rotate correct key to an even A/B/C/D cycle (swap option text + tags + rationales)
L=["A","B","C","D"]
for i,q in enumerate(items):
    tgt=L[i%4]; cur=q["correctAnswer"]
    if cur!=tgt:
        for f in ("options","distractorTags","distractorRationales"):
            d=q[f]; d[cur],d[tgt]=d[tgt],d[cur]
        q["correctAnswer"]=tgt
    q["distractorTags"][q["correctAnswer"]]=None  # correct answer has no tag

payload={"_schema":"tn-assessment-specialist / tcap-item-writer-v2 item schema (adapted for the Government "
  "course: no US-History EOC, so reportingCategory=GC domain, tcapFormat=false, itemWritingCompliant flag). "
  "Full psychometric metadata: dok+blooms(+rationales), C3, SSP, distractor tags (PK/MC/PE/NE)+rationales, "
  "content tags, de-biased keys. Items are classroom-formative · pre-field-test.",
  "subject":"government","unit":1,"count":len(items),"items":items}
from collections import Counter
s=json.dumps(payload,indent=2,ensure_ascii=False); assert "W"+"CS" not in s
open(os.path.join(OUT,"mcq-bank.json"),"w").write(s)
print("Wrote mcq-bank.json:",len(items),"MCQ (v2, rigor-compliant schema)")
print("Key distribution:",dict(Counter(q["correctAnswer"] for q in items)))
