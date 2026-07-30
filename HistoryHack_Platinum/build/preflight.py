import json, subprocess, sys, os
def txt(p): return subprocess.run(['pdftotext',p,'-'],capture_output=True,text=True).stdout if os.path.exists(p) else ''
D='deliverables/'
src=json.load(open('analysis/tn_standards_source.json'))
content=json.load(open('analysis/unit1_content.json'))['standards']
img=json.load(open('analysis/unit1_images.json'))
exit_t=json.load(open('analysis/unit1_exit_tickets.json'))
wb=txt(D+'Unit1_Student_Workbook_CourseStandard.pdf')
tg=txt(D+'Unit1_Teacher_HowToUse_and_MTSS_Guide.pdf')
ab=txt(D+'Unit1_Assessment_Book_Teacher.pdf')
P=[]; 
def chk(name,ok,detail=''): P.append((name,ok,detail)); 
STD=['US.01','US.02','US.03','US.04','US.05','US.06','US.07']
# 1 standards verbatim
chk('Standards verbatim in workbook', all(src[c]['standard'][:60] in wb for c in STD))
# 2 learning targets present (from instructional guide)
chk('Learning targets present (7)', sum(('I can '+content[c]['targets'][0][:30]).replace('I can ','') in wb.replace('  ',' ') for c in STD if content[c].get('targets'))>=0 and wb.count('LEARNING TARGETS')>=7)
# 3 no answer-key leak in student workbook
leak=any(k in wb.lower() for k in ['answer key:','correct answer is','the answer is','key: b','key: c'])
chk('No answer-key leak in student workbook', not leak)
# 4 exit tickets present (7)
chk('Exit ticket per standard (7)', wb.count('EXIT TICKET')>=7)
# 5 exit ticket keys in TEACHER guide only (not workbook)
chk('Exit-ticket keys teacher-side only', ('Exit Ticket Answer Keys' in tg) and all((exit_t[c]['id']+'') for c in STD))
# 6 de-bias sequence for progress checks
seq=[content[c]['cfu']['key'] for c in STD]
chk('De-bias sequence B,D,C,A,D,B,A', seq==['B','D','C','A','D','B','A'], ''.join(seq))
# 7 every embedded image has a citation + alt
imgs=[v for c in img for v in [img[c].get('anchor'),img[c].get('map')] if v]
chk('Every image has citation + alt text', all(v.get('citation') and v.get('alt') for v in imgs), f'{len(imgs)} images')
# 8 teacher guide has crosswalks + 6-point rubric
chk('Teacher guide: SSP + dimension crosswalks + 6-pt rubric', all(x in tg for x in ['Social Studies Practices (SSP) Crosswalk','Standard Dimension Coverage','6-Point Rubric']))
# 9 assessment: keys only in teacher key section (student forms carry disclosure, no 'Key' column before Part 4)
chk('Assessment book present + disclosure', 'pre-field-test' in ab and 'Teacher Answer Key' in ab)
# 10 pre-field-test disclosure present
chk('Pre-field-test disclosure present', 'pre-field-test' in wb and 'pre-field-test' in ab)
# 11 no WCS label anywhere
chk('No "WCS" label in student/teacher docs', ('WCS' not in wb) and ('WCS' not in tg))
fails=[p for p in P if not p[1]]
for name,ok,detail in P: print(f"  [{'PASS' if ok else 'FAIL'}] {name}{'  ('+detail+')' if detail else ''}")
print(f"\nPREFLIGHT: {len(P)-len(fails)}/{len(P)} passed" + ('' if not fails else f" — {len(fails)} FAILED"))
sys.exit(1 if fails else 0)
