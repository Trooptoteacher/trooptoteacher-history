#!/usr/bin/env python3
"""Unit 1 assessment bank — psychometric metadata mirrors US-History all_questions.json
(id·standard·unit·type·dok·level·options·correct_answer·tennessee_specific·topics) PLUS the
platinum guardrail fields the mission requires: bloom, reporting_category, difficulty,
per-distractor rationale, answer_explanation, bilingual stem (ES), de-biased key positions,
pre-field-test disclosure. Built to the TN GC standards (verbatim) + assessment guardrails.
Output → WEB_EDITION/public/data/government/questions/unit-1/dok-<1..4>.json (canonical web path,
mirrors public/data/us-history/questions/). © 2026 TroopToTeacher Technologies LLC. No district label."""
import json, os
HERE=os.path.dirname(os.path.abspath(__file__))
GOV=json.load(open(os.path.join(HERE,"analysis","government_standards_source.json"))) if os.path.exists(os.path.join(HERE,"analysis","government_standards_source.json")) else None
OUT=os.path.abspath(os.path.join(HERE,"..","..","WEB_EDITION","public","data","government","questions","unit-1"))
os.makedirs(OUT,exist_ok=True)
BLOOM={1:"Remember",2:"Understand",3:"Analyze",4:"Evaluate"}
LEVEL={1:"Developing",2:"Proficient",3:"Advanced",4:"Advanced"}
DIFF={1:"easy",2:"medium",3:"hard",4:"hard"}
RC="Foundations of Constitutional Government"

def mc(std,dok,stem,stem_es,opts,key,rat,expl,ts=False,topics=None):
    return dict(type="multiple_choice",standard=std,unit=1,dok=dok,bloom=BLOOM[dok],level=LEVEL[dok],
        reporting_category=RC,difficulty=DIFF[dok],question=stem,question_es=stem_es,options=opts,
        correct_answer=key,distractor_rationale=rat,answer_explanation=expl,tennessee_specific=ts,
        topics=topics or [],calibration="pre-field-test",pre_field_test=True)
def cr(std,dok,prompt,prompt_es,rubric,topics=None):
    return dict(type="constructed_response",standard=std,unit=1,dok=dok,bloom=BLOOM[dok],level=LEVEL[dok],
        reporting_category=RC,difficulty=DIFF[dok],question=prompt,question_es=prompt_es,rubric=rubric,
        tennessee_specific=False,topics=topics or [],calibration="pre-field-test",pre_field_test=True)

ITEMS=[]
# ---- GC.01 ----
ITEMS+=[
 mc("GC.01",1,"Which Enlightenment thinker is most associated with the idea of natural rights and the social contract?",
    "¿Qué pensador de la Ilustración se asocia más con la idea de los derechos naturales y el contrato social?",
    {"A":"Thomas Hobbes","B":"John Locke","C":"King John","D":"Julius Caesar"},"B",
    {"A":"Hobbes stressed order and the need for a strong sovereign, not natural rights as Locke framed them.",
     "B":"Correct — Locke argued people are born with natural rights to life, liberty, and property.",
     "C":"King John signed Magna Carta but did not develop natural-rights theory.",
     "D":"A Roman leader, not an Enlightenment natural-rights theorist."},
    "Locke's natural-rights and social-contract ideas directly shaped the Declaration's 'consent of the governed.'",
    topics=["Enlightenment","natural rights","Locke"]),
 mc("GC.01",3,"A student argues that American independence used 'old ideas, not new ones.' Which piece of evidence BEST supports this claim?",
    "Un estudiante sostiene que la independencia usó 'ideas viejas, no nuevas'. ¿Qué evidencia apoya MEJOR esta afirmación?",
    {"A":"Magna Carta (1215) already limited the king's power and protected life, liberty, and property.",
     "B":"The colonists invented the idea of natural rights in 1776.",
     "C":"The Constitution was written before the Declaration.",
     "D":"Greek democracy had no influence on American government."},"A",
    {"A":"Correct — Magna Carta predates 1776 by centuries and already limited royal power, showing the roots were old.",
     "B":"Opposite of the claim; natural rights were inherited from Locke and earlier traditions.",
     "C":"False chronology — the Declaration (1776) came before the Constitution (1787).",
     "D":"Incorrect — Greek democracy and the Roman republic were cited influences."},
    "The colonists drew on Magna Carta, Locke, and classical models — evidence the ideas were inherited and reshaped, not invented.",
    topics=["Magna Carta","roots","continuity"]),
]
# ---- GC.02 ----
ITEMS+=[
 mc("GC.02",1,"According to the Declaration of Independence, governments derive their just powers from:",
    "Según la Declaración de Independencia, los gobiernos obtienen sus poderes justos de:",
    {"A":"the wealthiest citizens","B":"the army","C":"the consent of the governed","D":"the king"},"C",
    {"A":"The Declaration rejects rule by a privileged few.","B":"Military force is not the source of just power in the text.",
     "C":"Correct — 'deriving their just powers from the consent of the governed.'","D":"The Declaration is a break FROM the king's authority."},
    "Consent of the governed is the Declaration's core principle of legitimate government.",topics=["Declaration","consent"]),
 mc("GC.02",3,"The Declaration lists natural rights and then a long list of grievances against King George III. Why place them together?",
    "La Declaración enumera derechos naturales y luego agravios contra el rey. ¿Por qué juntarlos?",
    {"A":"To make the document longer","B":"To build an argument: rights + the king's violations justify separation",
     "C":"To request an apology from the king","D":"To describe how to run state governments"},"B",
    {"A":"Length was not the purpose; the structure is an argument.","B":"Correct — universal rights (premise) + specific violations (evidence) → justified separation (conclusion).",
     "C":"The Declaration announces separation, not a request for apology.","D":"It does not outline state-government procedures."},
    "Grievances turn principle into justification — the logic of a government that may be altered when it violates rights.",
    topics=["Declaration","grievances","argument"]),
]
# ---- GC.03 ----
ITEMS+=[
 mc("GC.03",2,"Which power did the national government LACK under the Articles of Confederation, causing serious problems?",
    "¿Qué poder le FALTABA al gobierno nacional bajo los Artículos de la Confederación?",
    {"A":"The power to tax the states and citizens directly","B":"The power to declare war",
     "C":"The power to run a post office","D":"The power to make treaties"},"A",
    {"A":"Correct — Congress could only request money from states, leaving it unable to pay debts.",
     "B":"Congress could declare war under the Articles.","C":"Congress operated a post office.","D":"Congress could make treaties."},
    "No taxing power left the national government too weak to pay debts or respond to crises like Shays's Rebellion.",
    topics=["Articles","taxation","weakness"]),
 mc("GC.03",2,"Shays's Rebellion (1786–1787) is significant because it:",
    "La Rebelión de Shays (1786–1787) es importante porque:",
    {"A":"proved the Articles created a strong military","B":"exposed the national government's weakness and pushed leaders toward a new constitution",
     "C":"ended the Revolutionary War","D":"was led by King George III"},"B",
    {"A":"The opposite — the government could not raise forces to stop it.","B":"Correct — its failure to respond convinced leaders to replace the Articles.",
     "C":"The war had already ended in 1783.","D":"It was a farmers' uprising in Massachusetts, unrelated to the king."},
    "The rebellion revealed the Articles' fatal weakness and helped trigger the 1787 Convention.",topics=["Shays","Articles"]),
]
# ---- GC.04 ----
ITEMS+=[
 mc("GC.04",3,"The Great Compromise settled which major disagreement at the Constitutional Convention?",
    "El Gran Compromiso resolvió ¿cuál desacuerdo importante en la Convención Constitucional?",
    {"A":"Whether to keep the Articles of Confederation","B":"Whether to have a president or a king",
     "C":"How states would be represented in Congress — by population or equally","D":"Whether to allow political parties"},"C",
    {"A":"That debate was settled by writing a new constitution, not by the Great Compromise.","B":"The Convention rejected monarchy from the start.",
     "C":"Correct — a population-based House plus an equal-representation Senate reconciled large and small states.","D":"Parties are not addressed by the compromise."},
    "The Virginia Plan (population) and New Jersey Plan (equal) were merged into a bicameral Congress.",topics=["Great Compromise","representation"]),
 mc("GC.04",2,"The Anti-Federalists agreed to support the Constitution mainly on the condition that:",
    "Los antifederalistas apoyaron la Constitución principalmente con la condición de que:",
    {"A":"a bill of rights be added to protect individual liberties","B":"the president serve for life",
     "C":"states lose all their powers","D":"the Articles be kept unchanged"},"A",
    {"A":"Correct — their central demand was a bill of rights against a too-powerful central government.",
     "B":"They feared concentrated power; a life term is the opposite of their aim.","C":"They wanted to PROTECT state power.","D":"They accepted a new constitution, not the old Articles."},
    "The promise of a Bill of Rights secured ratification.",topics=["Anti-Federalists","ratification","Bill of Rights"]),
]
# ---- GC.05 ----
ITEMS+=[
 mc("GC.05",2,"The Preamble begins 'We the People.' Which principle does this phrase express?",
    "El Preámbulo comienza 'Nosotros el Pueblo'. ¿Qué principio expresa esta frase?",
    {"A":"Judicial review","B":"Popular sovereignty — government power comes from the people",
     "C":"Separation of powers","D":"Federalism"},"B",
    {"A":"Judicial review comes from Article III / Marbury, not the Preamble's opening.","B":"Correct — authority flows from the people themselves.",
     "C":"Separation of powers is a structural principle, not the meaning of 'We the People.'","D":"Federalism concerns nation-state power division."},
    "'We the People' declares popular sovereignty — the source of the Constitution's authority.",topics=["Preamble","popular sovereignty"]),
]
# ---- GC.06 ----
ITEMS+=[
 mc("GC.06",3,"Madison wrote that 'ambition must be made to counteract ambition.' Which design does this describe?",
    "Madison escribió que 'la ambición debe contrarrestar la ambición'. ¿Qué diseño describe esto?",
    {"A":"Popular sovereignty","B":"The amendment process","C":"Federalism between nation and states",
     "D":"Checks and balances that let each branch limit the others"},"D",
    {"A":"Popular sovereignty concerns the source of power, not inter-branch checks.","B":"Article V is unrelated to Madison's point here.",
     "C":"Federalism divides nation/state power, a different limit.","D":"Correct — branches are set against each other so each checks the others' ambition."},
    "Federalist No. 51's logic is structural: pit power against power through checks and balances.",topics=["checks and balances","Federalist 51"]),
 mc("GC.06",2,"The power of courts to declare a law unconstitutional is called:",
    "El poder de los tribunales para declarar inconstitucional una ley se llama:",
    {"A":"the veto","B":"judicial review","C":"impeachment","D":"popular sovereignty"},"B",
    {"A":"The veto is an executive power over legislation.","B":"Correct — judicial review, established in Marbury v. Madison (1803).",
     "C":"Impeachment removes officials; it does not void laws.","D":"Popular sovereignty is the source of authority, not a court power."},
    "Judicial review lets courts void unconstitutional acts — a key check.",topics=["judicial review","Marbury"]),
]
# ---- GC.07 ----
ITEMS+=[
 mc("GC.07",2,"To ratify a constitutional amendment under Article V requires approval by:",
    "Ratificar una enmienda constitucional bajo el Artículo V requiere la aprobación de:",
    {"A":"the president","B":"a simple majority of voters","C":"three-fourths of the states","D":"the Supreme Court"},"C",
    {"A":"The president has no formal role in amending the Constitution.","B":"A simple national majority is not the standard.",
     "C":"Correct — three-fourths of the states must ratify.","D":"Courts interpret, they do not ratify amendments."},
    "Article V requires a 2/3 proposal and 3/4 state ratification — a high, federalism-protecting bar.",topics=["Article V","amendment"]),
]
# ---- GC.08 (TCA) ----
ITEMS+=[
 mc("GC.08",3,"The First Amendment begins 'Congress shall make no law…'. Why phrase protections as limits on government?",
    "La Primera Enmienda comienza 'El Congreso no hará ley…'. ¿Por qué expresar protecciones como límites al gobierno?",
    {"A":"To show the government created these rights and may remove them","B":"Because rights pre-exist government; the Constitution's job is to stop government from violating them",
     "C":"To give Congress more power over speech","D":"Because only Congress has rights"},"B",
    {"A":"The framing implies the opposite — rights are not government gifts.","B":"Correct — natural-rights thinking: rights belong to people already; limits restrain government.",
     "C":"The clause restricts Congress, it does not expand its power.","D":"Rights belong to persons, not to Congress."},
    "Phrasing rights as prohibitions limits government power rather than granting rights it could revoke.",ts=True,
    topics=["Bill of Rights","First Amendment","limits"]),
 mc("GC.08",1,"According to the Tenth Amendment, powers not given to the national government are:",
    "Según la Décima Enmienda, los poderes no otorgados al gobierno nacional están:",
    {"A":"reserved to the states or the people","B":"given to the president","C":"held only by the courts","D":"eliminated entirely"},"A",
    {"A":"Correct — reserved powers are a cornerstone of federalism.","B":"The amendment does not assign them to the president.",
     "C":"Courts are not the default holder of reserved powers.","D":"They are retained, not eliminated."},
    "The Tenth Amendment reserves undelegated powers to the states or the people — federalism in the Bill of Rights.",ts=True,
    topics=["Tenth Amendment","federalism","reserved powers"]),
]
# ---- GC.09 ----
ITEMS+=[
 mc("GC.09",1,"The United States is best described as a:",
    "Estados Unidos se describe mejor como:",
    {"A":"direct democracy","B":"constitutional republic / representative democracy","C":"monarchy","D":"confederation"},"B",
    {"A":"Citizens elect representatives rather than voting on every law.","B":"Correct — a constitutional republic in which the people elect representatives.",
     "C":"There is no monarch.","D":"The confederation model was abandoned with the Articles."},
    "A constitutional republic combines majority rule through elections with protection of minority rights.",topics=["republic","democracy"]),
 mc("GC.09",2,"In Federalist No. 10, Madison argues a large republic is better than a pure democracy because it:",
    "En El Federalista No. 10, Madison sostiene que una república grande es mejor que una democracia pura porque:",
    {"A":"eliminates all disagreement","B":"better controls the dangers of faction","C":"has no elections","D":"gives all power to one leader"},"B",
    {"A":"Madison expects factions to persist; the aim is to control, not eliminate them.","B":"Correct — a large republic dilutes and checks factions.",
     "C":"Republics rely on elections.","D":"Concentrating power is the opposite of Madison's design."},
    "Madison's large-republic argument is that scale and representation control faction.",topics=["Federalist 10","faction","republic"]),
]
# ---- Constructed response (one per standard, DOK 3) ----
for code in GOV["_units"]["1"]["standards"] if GOV else []:
    pass
CR_PROMPTS={
 "GC.01":("Explain how ONE European or classical root (Locke, Montesquieu, Greek democracy, Roman republic, or Magna Carta) shaped American government. Use one piece of evidence.",
          "Explica cómo UNA raíz europea o clásica moldeó el gobierno estadounidense. Usa una evidencia."),
 "GC.02":("Choose one grievance in the Declaration of Independence and explain how it violated the colonists' rights and helped justify independence.",
          "Elige un agravio de la Declaración y explica cómo violó los derechos de los colonos."),
 "GC.03":("Identify two weaknesses of the Articles of Confederation and explain one problem each caused.",
          "Identifica dos debilidades de los Artículos de la Confederación y explica un problema de cada una."),
 "GC.04":("Explain how the Great Compromise resolved the conflict between large and small states.",
          "Explica cómo el Gran Compromiso resolvió el conflicto entre estados grandes y pequeños."),
 "GC.05":("Choose two purposes of government from the Preamble and explain why each matters for a free society.",
          "Elige dos propósitos del gobierno del Preámbulo y explica por qué importa cada uno."),
 "GC.06":("Explain how checks and balances prevent any one branch from becoming too powerful. Use one example.",
          "Explica cómo los controles y equilibrios evitan que una rama sea demasiado poderosa. Usa un ejemplo."),
 "GC.07":("Explain the two-step process for amending the Constitution and why the Framers made it difficult.",
          "Explica el proceso de dos pasos para enmendar la Constitución y por qué los Redactores lo hicieron difícil."),
 "GC.08":("Explain how the Bill of Rights limits government power. Use one amendment as evidence.",
          "Explica cómo la Carta de Derechos limita el poder del gobierno. Usa una enmienda como evidencia."),
 "GC.09":("Explain the difference between a republic and a direct democracy, and why the Framers chose a republic.",
          "Explica la diferencia entre una república y una democracia directa, y por qué los Redactores eligieron una república."),
}
RUBRIC="6-pt CER: Claim (0–2) clear/defensible · Evidence (0–2) two accurate cited details · Reasoning (0–2) links evidence to claim + addresses a counterpoint."
for code,(p,pes) in CR_PROMPTS.items():
    ITEMS.append(cr(code,3,p,pes,RUBRIC,topics=["CER","argumentation"]))
# ---- Unit DBQ (DOK 4) ----
ITEMS.append(dict(type="dbq",standard="GC.01–GC.09",unit=1,dok=4,bloom="Evaluate",level="Advanced",
  reporting_category=RC,difficulty="hard",
  question=("Document-Based Question — Using at least THREE documents from the Unit 1 primary-source set "
   "(Locke's Second Treatise, the Declaration of Independence, Federalist No. 10, Federalist No. 51, Brutus No. 1, "
   "the Preamble, and the Bill of Rights), construct an argument: Did the Founders build a government that trusts the "
   "people, or one that guards against them? Support your claim with evidence from the documents and explain how the "
   "documents corroborate or complicate one another (synthesis)."),
  question_es=("Pregunta basada en documentos — Usando al menos TRES documentos del conjunto de la Unidad 1, "
   "argumenta: ¿Los Fundadores construyeron un gobierno que confía en el pueblo o que se protege de él?"),
  synthesis_required=True,
  source_bank="WEB_EDITION/public/data/government/primary-sources/unit-1.json",
  rubric="Tennessee EOC-style DBQ rubric: thesis, use of ≥3 documents, sourcing, outside evidence, synthesis.",
  tennessee_specific=False,topics=["DBQ","synthesis","founding"],calibration="pre-field-test",pre_field_test=True))

# ---- ANALYTICS / MASTERY / REMEDIATION layer (the product differentiator) ----
# Every item carries a remediation route: a missed item points a student back to the exact
# reteach assets for that standard so the dashboard can turn "not mastered" into an action.
STD_TITLE={c:GOV[c]["title"] for c in GOV if c.startswith("GC.")} if GOV else {}
def remediation_for(std):
    return {
      "standard":std,
      "reteach_narrative":f"03_TEXTBOOK_UNITS/unit-1/unit-1.html#{std}",     # the standard's close-read section
      "reteach_teacher":f"03_TEXTBOOK_UNITS/unit-1/unit-1-teacher-guide.html#{std}",  # "What's Next" reteach
      "vocabulary":"Frayer terms for "+std,
      "primary_source":"WEB_EDITION/public/data/government/primary-sources/unit-1.json",
      "next_step":"Re-anchor on the primary source, re-teach the 3 vocabulary terms (EN/ES), then re-attempt a parallel item."
    }
for q in ITEMS:
    base=q["standard"].split("–")[0].split("-")[0] if q["standard"].startswith("GC") else "GC.01"
    q["remediation"]=remediation_for(base)
    q["mastery_weight"]=1
    # per-distractor misconception signal for the analytics engine (which wrong idea a pick reveals)
    if q["type"]=="multiple_choice":
        q["misconception_by_option"]={k:("(correct)" if k==q["correct_answer"] else v)
                                      for k,v in q["distractor_rationale"].items()}

# mastery config — how the dashboard rolls items up to per-standard mastery + triggers remediation
mastery={
 "_doc":"Standards-mastery + remediation model (the analytics selling point). Mirrors US-History analytics.",
 "subject":"government","unit":1,
 "mastery_rule":{"scale":"per GC standard","evidence":"all items tagged to the standard across DOK 1–4",
   "thresholds":{"not_started":0,"developing":"<50% correct","approaching":"50–74%","proficient":"75–89%","mastered":"90%+"},
   "dok_weighting":"DOK 3–4 items weighted x1.5 toward mastery (depth over recall)",
   "min_items_for_mastery":3},
 "remediation_trigger":"Any standard below 'proficient' surfaces its reteach route (narrative section + teacher reteach + vocab + primary source) on the teacher dashboard and the student's practice queue.",
 "spiral":"Missed standards re-enter the 3 spaced-retrieval rounds automatically (interleaving).",
 "reporting_categories":sorted({q["reporting_category"] for q in ITEMS}),
 "standards_covered":sorted({q["standard"] for q in ITEMS}),
 "disclosure":"Items are classroom-formative · pre-field-test; mastery estimates are formative, not a state score."
}
os.makedirs(OUT,exist_ok=True)
open(os.path.join(OUT,"mastery-config.json"),"w").write(json.dumps(mastery,indent=2,ensure_ascii=False))

# ---- de-bias MCQ answer positions (rotate correct key to an even A/B/C/D cycle) ----
LETTERS=["A","B","C","D"]
mcq=[q for q in ITEMS if q["type"]=="multiple_choice"]
for i,q in enumerate(mcq):
    target=LETTERS[i%4]; cur=q["correct_answer"]
    if cur!=target:
        for field in ("options","distractor_rationale"):
            d=q[field]; d[cur],d[target]=d[target],d[cur]
        q["correct_answer"]=target
    # rebuild misconception map so the (new) correct position is marked correct
    q["misconception_by_option"]={k:("(correct)" if k==q["correct_answer"] else q["distractor_rationale"][k]) for k in ["A","B","C","D"]}
from collections import Counter
dist=Counter(q["correct_answer"] for q in mcq)
# assign ids + stamp unit/standard-based numbering
counts={}
for q in ITEMS:
    std=q["standard"]; counts[std]=counts.get(std,0)+1
    q["id"]=f"{std}-U1Q{counts[std]:02d}"
# split MCQ into dok files; CR/DBQ go to their DOK file too
byd={1:[],2:[],3:[],4:[]}
for q in ITEMS: byd[q["dok"]].append(q)
for dok in (1,2,3,4):
    payload={"_schema":"History Hack canonical question bank (mirrors public/data/us-history/questions/). "
             "Psychometric metadata: dok, bloom, level, reporting_category, difficulty, per-distractor rationale, "
             "answer_explanation, bilingual question_es, de-biased keys. Items are classroom-formative · pre-field-test.",
             "subject":"government","unit":1,"dok":dok,"count":len(byd[dok]),"items":byd[dok]}
    s=json.dumps(payload,indent=2,ensure_ascii=False)
    assert "W"+"CS" not in s
    open(os.path.join(OUT,f"dok-{dok}.json"),"w").write(s)
print("Unit 1 assessment bank written to",OUT)
print("Totals — MCQ %d · CR %d · DBQ %d · ALL items %d"%(len(mcq),
    sum(1 for q in ITEMS if q['type']=='constructed_response'),
    sum(1 for q in ITEMS if q['type']=='dbq'),len(ITEMS)))
print("MCQ key distribution (de-bias target = even):",dict(dist))
for dok in (1,2,3,4): print(f"  dok-{dok}.json: {len(byd[dok])} items")
