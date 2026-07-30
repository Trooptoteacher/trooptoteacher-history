#!/usr/bin/env python3
"""Slide-deck generator for World History Hack (course-agnostic; reads the unit content JSON).
AUDIENCE=teacher (default) includes CFU answer reveal + teacher notes; AUDIENCE=student drops all
keys/notes and adds an opening "supports for everyone" UDL slide. Emits print-first 16:9 HTML;
render to tagged PDF with Chromium (see render note at bottom). Leak-guarded: no forbidden strings.
Usage: AUDIENCE=teacher python3 ../engine/build_deck.py   (run from BUILD/unitN)
"""
import json, os, html, sys
C=json.load(open('analysis/unit1_content.json'))
U=C['unit']; STD=C['standards']; ORDER=C['order']
AUD=os.environ.get('AUDIENCE','teacher').lower()
IS_T = AUD=='teacher'
BRAND=U.get('brand','Course'); COURSE=U.get('course_name','')
NAVY='#1B2A4A'; GOLD='#C89B3C'; RED='#B22234'; CREAM='#F7F5EF'; INK='#1A1A1A'
def e(s): return html.escape(str(s),quote=False)

UDL='UDL 3.0 (CAST, 2024): read-aloud on request · key terms glossed (EN/ES) · respond in writing, speech, or a labeled diagram · large-print & screen-reader friendly. Same target for everyone; supports vary the means, not the ceiling.'
MTSS='MTSS: Tier 1 core lesson for all · Tier 2 small-group reteach of this standard (Cornell cues + organizer), then re-check · Tier 3 intensive 1:1 with concrete→representational→abstract scaffolding, progress-monitored to the same standard.'

slides=[]
def slide(inner, cls=''):
    slides.append(f'<section class="slide {cls}">{inner}</section>')

# --- title slide ---
slide(f'''<div class="eye">{e(BRAND)} · {e(COURSE)}</div>
 <h1>{e(U['code'])} — {e(U['title'])}</h1>
 <div class="sub">{e(U.get('cover_era',''))} · {e(U['standards_range'])} · {e(U['quarter'])}</div>
 <div class="eq"><b>Essential Question:</b> {e(U['essential_question'])}</div>
 <div class="foot">{"TEACHER DECK — includes answer reveals + teaching notes (do not display to students)" if IS_T else "STUDENT DECK"}</div>''','title')

# --- student-only universal-supports slide ---
if not IS_T:
    slide(f'''<h2>Supports for everyone</h2>
     <p class="big">{e(UDL)}</p>
     <p class="chip">You can show what you know by writing, speaking, or drawing a labeled diagram.</p>''','support')

for code in ORDER:
    s=STD[code]; a=s['auth']
    # standard opener
    slide(f'''<div class="code">{e(code)}</div><h2>{e(s['title'])}</h2>
     <div class="stext">{e(s['tn'])}</div>
     <div class="targets"><b>I can…</b><ul>{''.join(f'<li>{e(t)}</li>' for t in s.get('targets',[]))}</ul></div>''','std')
    # hook + vocab
    slide(f'''<div class="code">{e(code)}</div><h3>Hook</h3><p class="big">{e(s['hook'])}</p>
     <h3>Key terms</h3><table class="vocab">{''.join(f"<tr><td><b>{e(v['term'])}</b> <span class=say>/{e(v['say'])}/</span><br><i>ES: {e(v['es'])}</i></td><td>{e(v['def'])}</td></tr>" for v in s['vocab'])}</table>''','vocab')
    # primary source (cited)
    src=(s.get('sources') or [{}])[0]
    if src:
        slide(f'''<div class="code">{e(code)}</div><h3>Primary source — analyze with HIPPO</h3>
         <div class="srcbox">“{e(src.get('quote',''))}”</div>
         <div class="cite">{e(src.get('title',''))}. {e(src.get('who',''))}, {e(src.get('date',''))}. {e(src.get('repo',''))}. Public domain. {e(src.get('url',''))}</div>
         <p class="note">Image drops in from the primary-source bank at build; citation shown above.</p>''','source')
    # cornell cues
    slide(f'''<div class="code">{e(code)}</div><h3>Cornell cues — capture these</h3>
     <ul class="cues">{''.join(f'<li>{e(q)}</li>' for q in s.get('cues',[]))}</ul>''','cues')
    # Make It Stick (CFU) — teacher sees the key
    cfu=s['cfu']
    opts=''.join(f"<li{' class=key' if (IS_T and k==cfu['key']) else ''}>{k}. {e(cfu['options'][k])}{' ✓' if (IS_T and k==cfu['key']) else ''}</li>" for k in ['A','B','C','D'])
    slide(f'''<div class="code">{e(code)}</div><h3>Make It Stick — check for understanding</h3>
     <p class="big">{e(cfu['stem'])}</p><ul class="mc">{opts}</ul>
     {f'<div class="teacher">Answer: {cfu["key"]} · DOK {cfu["dok"]}. Reveal after students commit (mark it, say it, or explain it).</div>' if IS_T else '<p class="chip">Commit before the reveal: mark it, say it, or explain it aloud.</p>'}''','stick')
    # UDL / MTSS strip
    slide(f'''<div class="code">{e(code)}</div><h3>Access for every learner</h3>
     <div class="strip udl"><b>UDL 3.0</b> — {e(UDL)}</div>
     <div class="strip mtss"><b>MTSS</b> — {e(MTSS)}</div>
     <div class="cite">CAST (2024). Universal Design for Learning Guidelines version 3.0.</div>''','udl')

CSS=f'''*{{margin:0;padding:0;box-sizing:border-box}}
@page{{size:13.333in 7.5in;margin:0}}
body{{font-family:'Segoe UI',Arial,sans-serif;color:{INK}}}
.slide{{width:13.333in;height:7.5in;padding:.6in .8in;page-break-after:always;position:relative;overflow:hidden;border-bottom:1px solid #eee}}
.slide.title,.slide.support{{background:{NAVY};color:#fff}}
.eye{{color:{GOLD};font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:13pt}}
h1{{font-size:40pt;line-height:1.1;margin:.15in 0}}
h2{{font-size:30pt;color:{NAVY};margin-bottom:.12in}} .title h2,h1{{color:#fff}}
h3{{font-size:20pt;color:{RED};margin:.12in 0 .06in}}
.sub{{font-size:16pt;color:#dbe6f5}} .eq{{margin-top:.3in;font-size:17pt;font-style:italic;border-left:5px solid {GOLD};padding-left:.2in}}
.foot{{position:absolute;bottom:.4in;left:.8in;font-size:11pt;color:{GOLD};font-weight:700}}
.code{{position:absolute;top:.35in;right:.8in;font-weight:800;color:{GOLD};font-size:15pt}}
.stext{{font-size:14pt;color:#333;background:{CREAM};padding:.15in;border-radius:6px;margin-bottom:.1in}}
.targets ul,.cues,.mc,.vocab{{font-size:15pt;margin-left:.3in;line-height:1.5}}
.big{{font-size:19pt;line-height:1.4;margin:.15in 0}}
.vocab{{border-collapse:collapse;width:100%;list-style:none;margin:0}}.vocab td{{border:1px solid #ccc;padding:.08in .12in;font-size:13pt;vertical-align:top}}.say{{color:#777;font-size:11pt}}
.srcbox{{background:{CREAM};border-left:5px solid {NAVY};padding:.2in;font-size:17pt;font-style:italic;margin:.1in 0}}
.cite{{font-size:10pt;color:#666;margin-top:.08in}} .note{{font-size:11pt;color:#999;font-style:italic}}
.mc li.key{{background:#e7f3e7;font-weight:700}} .mc{{list-style:none}}
.teacher{{background:#fff3d6;border:1px dashed {GOLD};padding:.12in;margin-top:.15in;font-size:13pt;font-weight:600}}
.chip{{display:inline-block;background:{GOLD};color:{NAVY};padding:.06in .2in;border-radius:20px;font-weight:700;font-size:12pt;margin-top:.1in}}
.strip{{padding:.12in;border-radius:6px;margin:.08in 0;font-size:12.5pt}}.strip.udl{{background:#eef4ec;border-left:5px solid #4a7c59}}.strip.mtss{{background:#f0f5fb;border-left:5px solid {NAVY}}}
.support .big{{color:#fff}}'''
doc=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>{e(BRAND)} — {e(U['code'])} {e(U['title'])} — {"Teacher" if IS_T else "Student"} Deck</title><style>{CSS}</style></head><body>{''.join(slides)}</body></html>'''
os.makedirs('deliverables',exist_ok=True)
name=f"Unit1_{'Teacher' if IS_T else 'Student'}_Deck"
open(f'deliverables/{name}.html','w').write(doc)
# leak guard
import re
FORB=r'Government Hack|Government & Civics|U\.S\. History|Foundations of Constitutional|Williamson|WCS|US\.[0-9]{2}|GC\.[0-9]|flight log|civic'
hits=re.findall(FORB, doc)
print(f"WROTE deliverables/{name}.html · {len(slides)} slides · AUDIENCE={AUD} · leak {'HITS:'+str(set(hits)) if hits else 'clean'}")
if hits: sys.exit(2)
