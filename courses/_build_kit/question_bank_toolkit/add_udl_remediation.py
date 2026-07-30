# -*- coding: utf-8 -*-
"""Attach UDL grounding + remediation to every item in the consolidated bank.

UDL is grounded in CAST UDL Guidelines 3.0 (Representation / Action & Expression / Engagement),
tailored by item type and whether the item carries a stimulus. Firm goal, flexible means:
supports vary access/expression, never the mastery target (UDL design, not IEP modification).

Remediation is distractor-based (derived from each item's own distractor_tags: the misconception
each wrong choice targets -> a targeted reteach), plus a standard-level reteach and MTSS Tier 2/3
routing. Open-response items route to the rubric criteria instead of distractors.

Idempotent: adds/overwrites `udl_supports` and `remediation` on every item. Run after
consolidate_bank.py.  Usage: python3 08_QUESTION_BANK/add_udl_remediation.py
"""
import os, json
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
BANK=os.path.join(HERE,"government_question_bank.json")
# per-standard titles for the reteach reference
STD_TITLE={}
import glob
for cf in glob.glob(os.path.join(ROOT,"BUILD","unit*","analysis","unit*_content.json")):
    try:
        c=json.load(open(cf,encoding="utf-8"))
        for code,rec in c.get("standards",{}).items():
            STD_TITLE[code]=rec.get("title",code)
    except Exception: pass

CODE_MOVE={
 "PK":"clarify the boundary between this concept and the related idea the student confused it with",
 "MC":"directly confront and correct the misconception with a worked counter-example",
 "PE":"model how to carry partial evidence through to the fully correct conclusion",
 "NE":"contrast the near-miss with the precise correct answer, side by side",
 "CA":"re-teach the cause-and-effect chain so the student attributes it correctly",
 "AN":"place the events on a timeline so the anachronism becomes visible",
 "OG":"test the overgeneralization against a specific case where it breaks down",
}

def udl_for(it):
    t=it.get("type"); has_stim=bool(it.get("stimulus")) or t=="document_based"
    rep=("2.1 key vocabulary and civic terms are glossed on request; 1.1 available in large-print and "
         "screen-reader-compatible formats; 2.2 the stem may be read aloud")
    if has_stim: rep+="; 1.2/2.5 the source is provided as accessible text with a plain-language description and may be enlarged"
    rep+=" (CAST 3.0, Representation)."
    if t=="multiple_choice":
        ae=("4.1 respond by selecting, pointing, or via assistive technology; 4.2 compatible with AT / "
            "TestNav accessibility tools (CAST 3.0, Action & Expression).")
    else:
        ae=("5.1 demonstrate mastery in writing, as a recorded spoken response, or as a labeled diagram/"
            "graphic organizer; 5.2 word processor, speech-to-text, and a planning organizer are available; "
            "5.3 graduated sentence/argument frames on request (CAST 3.0, Action & Expression).")
    eng=("8.5 action-oriented feedback via the remediation routing below; 8.2 challenge is DOK-tiered so every "
         "learner has an entry point and a ceiling; 7.2 items use authentic civic contexts (CAST 3.0, Engagement).")
    return {"representation":rep,"action_expression":ae,"engagement":eng,
            "firm_goal_note":("Supports vary the means of access and expression only; the standard mastery target "
                              "is identical for every student. These are UDL design options, not modifications — "
                              "the ceiling is not lowered."),
            "udl_citation":"CAST (2024). Universal Design for Learning Guidelines version 3.0."}

def remediation_for(it):
    title=STD_TITLE.get(it.get("standard"),it.get("standard"))
    if_missed=(f"Revisit “{title}” using the unit's Cornell notes and the standard's best-fit graphic "
               f"organizer; re-check with the Exit Ticket, then re-assess with a parallel-form item.")
    by=[]
    if it.get("type")=="multiple_choice":
        for d in it.get("distractor_tags",[]) or []:
            code=d.get("code");
            by.append({"choice":d.get("label"),
                       "signals_misconception":d.get("rationale",""),
                       "reteach":f"If chosen: {CODE_MOVE.get(code,'reteach the underlying concept')}."})
        tier2=("Small-group (Tier 2) reteach targeting the specific misconception the student's wrong choice "
               "signals: 10–15 min with the graphic organizer and a worked example, then re-assess with a "
               "parallel item.")
    else:
        by=[]
        if_missed=(f"Score against the rubric ({it.get('rubric_name','rubric')}); identify the lowest-scoring "
                   f"criterion and reteach it. " + if_missed)
        tier2=("Small-group (Tier 2) reteach of the rubric criterion not yet met, using a model response and a "
               "claim–evidence–reasoning frame; re-collect the response in the student's chosen mode.")
    tier3=("If the gap persists across parallel forms (Tier 3): intensive 1:1 using concrete–representational–"
           "abstract scaffolding and a think-aloud; progress-monitor weekly toward the same standard.")
    return {"if_missed":if_missed,"by_distractor":by,"mtss":{"tier2":tier2,"tier3":tier3}}

items=json.load(open(BANK,encoding="utf-8"))
for it in items:
    it["udl_supports"]=udl_for(it)
    it["remediation"]=remediation_for(it)
json.dump(items,open(BANK,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
mc=sum(1 for i in items if i.get("type")=="multiple_choice")
print(f"Added udl_supports + remediation to {len(items)} items ({mc} MC with distractor-based routing, {len(items)-mc} open-response with rubric routing).")
