#!/usr/bin/env python3
"""Fit Activity 1 (Vocabulary) to one full page after adopting the deck's ~6 Word Wall terms.

Applies the no-white-space edits to a pristine build_workbook_u<N>.js (all HH workbook
builders share this Activity 1 / vocabSelfCheck code verbatim):
  1. Word Bank term/def/es -> 9pt (size 18)
  2. vocabSelfCheck: drop leading gap(40); self-check term -> 8pt (size 16);
     take a `fillLines` arg and end with `...ruled(fillLines)`
  3. drop the redundant trailing Quick Write
  4. ADAPTIVE fill: the caller computes fill from the standard's definition lengths
     (`23 - estimatedWordBankLines`, clamped 0..4) so short-definition standards fill the
     page to the margin and long-definition standards never overflow to a second page.

Idempotent: refuses to double-apply. Aborts if the builder diverged from the shared template.

Usage:
  python3 fit_activity1.py build_workbook_u<N>.js
"""
import sys

SRC = sys.argv[1]
s = open(SRC).read()

if "fillLines" in s and "23-_wl" in s:
    print("already fitted — no change"); sys.exit(0)

EDITS = [
    # 1. Word Bank 9pt
    ("""    new TextRun({text:v.term,bold:true,size:20,font:FONT,color:INK}), v.def, v.es]),[2683,4282,2683]));""",
     """    new TextRun({text:v.term,bold:true,size:18,font:FONT,color:INK}),
    new TextRun({text:v.def,size:18,font:FONT,color:INK}),
    new TextRun({text:v.es,size:18,font:FONT,color:INK})]),[2683,4282,2683]));"""),
    # 2. self-check takes a fill count
    ("""function vocabSelfCheck(code){const s=C.standards[code];""",
     """function vocabSelfCheck(code,fillLines=2){const s=C.standards[code];"""),
    # 3. self-check term 8pt
    ("""const rows=s.vocab.map(v=>new TableRow({children:[cell(P(R(v.term,{s:18,b:true}),{spacing:{after:0}}),{w:W[0]})""",
     """const rows=s.vocab.map(v=>new TableRow({children:[cell(P(R(v.term,{s:16,b:true}),{spacing:{after:0}}),{w:W[0]})"""),
    # 4. drop leading gap(40)
    ("""  return [gap(40),
    callout('VOCABULARY SELF-CHECK · Knowledge Rating',""",
     """  return [
    callout('VOCABULARY SELF-CHECK · Knowledge Rating',"""),
    # 5. trailing ruled(2) -> adaptive fill
    ("""give a real-world example.',{s:20})],{spacing:{before:60,after:40}}),
    ...ruled(2)];}""",
     """give a real-world example.',{s:20})],{spacing:{before:60,after:40}}),
    ...ruled(fillLines)];}"""),
    # 6. caller: compute adaptive fill; drop the redundant Quick Write
    ("""  out.push(...vocabSelfCheck(code));
  out.push(...FILL_LIB.quickwrite('Which of these terms do you think will matter MOST for this standard, and why? You’ll revisit this at the end.'));""",
     """  {const _wl=s.vocab.reduce((a,v)=>a+Math.max(1,Math.ceil((v.def||'').length/52)),0);
   const _sparse=s.vocab.length<=3;   // deck Word Wall thin on terms -> fill the page with real work, not blanks
   out.push(...vocabSelfCheck(code,_sparse?1:Math.max(0,Math.min(4,23-_wl))));
   if(_sparse){
     out.push(callout('APPLY THE VOCABULARY — show you own each term',['Use each term below in your own words, connected to this standard. Write, say, or diagram your answer.']));
     const prompts=s.vocab.length===1
       ? ['use it in a sentence about this standard','where do you see its effects today? explain or draw','why did it matter for this era?']
       : ['use it in a sentence about this standard, then give a real example or a quick sketch'];
     const per=s.vocab.length===1?5:s.vocab.length===2?6:3;
     s.vocab.forEach(v=>{ prompts.forEach(pr=>{
       out.push(P([R(v.term+':  ',{s:21,b:true,c:NAVY}),R(pr+'.',{s:20})],{spacing:{before:70,after:30}}));
       out.push(...ruled(per)); }); });
   }}"""),
    # 7. LANGUAGE SUPPORT: no empty "Pronunciations: ." when the deck's terms carry no
    #    pronunciation (e.g. proper nouns) — fall back to a Spanish-column note.
    ("""  out.push(callout('LANGUAGE SUPPORT',['Pronunciations: '+s.vocab.filter(v=>v.say).map(v=>`${v.term} (${v.say})`).join('; ')+'.']));""",
     """  {const _pron=s.vocab.filter(v=>v.say);
   out.push(callout('LANGUAGE SUPPORT',[_pron.length
     ? 'Pronunciations: '+_pron.map(v=>`${v.term} (${v.say})`).join('; ')+'.'
     : 'Use the Spanish column in the Word Bank above to access these terms — cognates and translations support understanding, not translation of assessment.']));}"""),
]

for old, new in EDITS:
    if old not in s:
        print("ABORT: expected code not found (builder diverged from the shared template):\n  " + old[:80])
        sys.exit(2)
    s = s.replace(old, new, 1)

open(SRC, "w").write(s)
print("fitted Activity 1 (adaptive) in", SRC)
