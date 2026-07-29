#!/usr/bin/env python3
"""Render Unit 1 from unit1_content.json into print-first, B&W-safe HTML:
 - unit-1.html                (student textbook chapter — NO answer keys)
 - unit-1-teacher-guide.html  (teacher guide — answer keys + reteach, teacher-side only)
Design tokens mirror 00_START_HERE/playbook.html (navy #1B2A4A / gold #C9A227, Merriweather + Source Sans 3).
Bilingual EN/ES vocab · WCAG-minded · never emits the source-district label. © 2026 TroopToTeacher Technologies LLC."""
import json, os, html
HERE=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(os.path.join(HERE,"analysis","unit1_content.json")))
OUT=os.path.abspath(os.path.join(HERE,"..","..","03_TEXTBOOK_UNITS","unit-1"))
os.makedirs(OUT,exist_ok=True)
def e(s): return html.escape(str(s),quote=False)

CSS="""@import url('https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&family=Merriweather:ital,wght@0,400;0,700&display=swap');
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{background:#ddd}
body{font-family:'Source Sans 3',Arial,sans-serif;background:#fff;color:#111;width:8.5in;margin:.18in auto;
 box-shadow:0 3px 24px rgba(0,0,0,.26);font-size:10.5pt;line-height:1.6}
@page{size:letter portrait;margin:.6in .65in}
@media print{html{background:#fff}body{margin:0;box-shadow:none;width:auto}.no-print{display:none!important}
 .std{break-inside:avoid-page}.pss,.frayer,.cfu,.card{break-inside:avoid}}
.no-print{position:fixed;top:10px;right:10px;background:#1B2A4A;color:#fff;border:none;border-radius:5px;
 padding:7px 14px;font-size:11px;font-weight:700;cursor:pointer;z-index:99}
.hero{background:#1B2A4A;padding:26px .6in 20px;color:#fff}
.hero .eye{font-size:8pt;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:#C9A227}
.hero h1{font-family:'Merriweather',Georgia,serif;font-size:19pt;line-height:1.2;margin:6px 0 4px}
.hero .sub{font-size:10pt;color:#B5D4F4;font-style:italic}
.gold-bar{background:#C9A227;color:#3D2200;padding:5px .6in;font-size:8.5pt;font-weight:700;
 display:flex;justify-content:space-between;flex-wrap:wrap;gap:6px;border-bottom:3px solid #B22234}
.eq{background:#f0f5fb;border-left:4px solid #1B2A4A;padding:11px 16px;margin:14px .6in;border-radius:0 5px 5px 0;font-style:italic;font-size:11pt}
.pg{padding:6px .6in .3in}
.std{margin:22px 0;border:1px solid #d8dee8;border-radius:6px;overflow:hidden}
.std>.band{background:#1B2A4A;color:#fff;padding:10px 16px}
.std .code{font-family:'Merriweather',serif;font-size:13pt;font-weight:700}
.std .stext{font-size:9.5pt;color:#dbe6f5;margin-top:3px;line-height:1.5}
.tags{margin-top:7px;display:flex;flex-wrap:wrap;gap:5px}
.tag{font-size:7.5pt;font-weight:700;padding:2px 7px;border-radius:3px;background:#2A3F5E;color:#cfe0f5}
.tag.tca{background:#B22234;color:#fff}.tag.dim{background:#33507a;color:#dbe6f5}
.body{padding:13px 16px}
.ican{background:#eef4ec;border-left:4px solid #4a7c59;padding:8px 12px;border-radius:0 4px 4px 0;font-size:9.5pt;margin-bottom:11px}
.ican b{color:#2f5233}
.hook{font-family:'Merriweather',serif;font-style:italic;color:#1B2A4A;font-size:11pt;margin:2px 0 12px;padding-left:10px;border-left:3px solid #C9A227}
h3{font-family:'Merriweather',serif;font-size:11pt;color:#1B2A4A;margin:14px 0 6px}
h4{font-size:9.5pt;font-weight:700;color:#2A3F5E;margin:11px 0 4px;text-transform:uppercase;letter-spacing:.04em}
p{margin-bottom:9px}
.pss{background:#f7f4ea;border:1px solid #d9cfa8;border-left:4px solid #C9A227;border-radius:0 5px 5px 0;padding:12px 15px;margin:12px 0}
.pss .lbl{font-size:8pt;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8a6d1f}
.pss .src-t{font-weight:700;color:#1B2A4A;margin-top:3px}
.pss blockquote{font-family:'Merriweather',serif;font-style:italic;font-size:10pt;line-height:1.55;margin:7px 0;padding:7px 12px;background:#fffdf6;border-left:3px solid #1B2A4A}
.pss cite{display:block;font-size:8pt;color:#555;font-style:normal;margin-top:3px}
.soaps{font-size:8.5pt;color:#3D2200;background:#fbf7ec;border:1px dashed #cbb978;border-radius:4px;padding:6px 10px;margin:8px 0}
ol.tdq{margin:6px 0 4px 20px}ol.tdq li{margin-bottom:5px;font-size:9.5pt}
.write{border-bottom:1px solid #bbb;height:.34in}
.frayer{border:1.5px solid #1B2A4A;border-radius:5px;margin:9px 0;overflow:hidden}
.frayer .ft{background:#1B2A4A;color:#fff;padding:5px 11px;font-weight:700;font-size:10pt;display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px}
.frayer .ft .say{font-weight:400;font-style:italic;color:#B5D4F4;font-size:8.5pt}
.frayer .ft .es{color:#C9A227;font-size:8.5pt}
.frayer .fd{padding:8px 11px;font-size:9.5pt}
.frayer .grid{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid #d8dee8}
.frayer .grid div{padding:7px 11px;min-height:.55in;font-size:8pt;color:#666}
.frayer .grid div:first-child{border-right:1px solid #d8dee8}
.frayer .grid .row2{border-top:1px solid #d8dee8}
.cfu{background:#eef2f8;border:1px solid #c3d0e6;border-radius:5px;padding:11px 14px;margin:11px 0}
.cfu .q{font-weight:600;margin-bottom:6px}
.cfu ol{margin-left:22px}.cfu li{margin-bottom:3px;font-size:9.5pt}
.dok{display:inline-block;background:#1B2A4A;color:#fff;font-size:7.5pt;font-weight:700;padding:1px 6px;border-radius:3px;margin-left:6px}
.card{background:#f8f8f6;border:1px solid #ddd;border-radius:5px;padding:10px 14px;margin:11px 0}
.retrieval{background:#1B2A4A;color:#fff;padding:14px .6in;margin-top:18px}
.retrieval h2{font-family:'Merriweather',serif;color:#C9A227;font-size:13pt;margin-bottom:6px}
.retrieval li{margin:4px 0 4px 20px;font-size:9.5pt}
.disc{font-size:8pt;color:#777;font-style:italic;margin-top:6px}
.foot{background:#1B2A4A;color:rgba(255,255,255,.55);padding:8px .6in;font-size:7.5pt;display:flex;justify-content:space-between;flex-wrap:wrap;gap:6px}
.foot b{color:#C9A227}
.tnote{background:#FBEEEF;border:1px solid #e3b7bb;border-left:4px solid #B22234;border-radius:0 5px 5px 0;padding:10px 14px;margin:11px 0}
.tnote .k{font-weight:700;color:#B22234;font-size:8.5pt;text-transform:uppercase;letter-spacing:.05em}
.key{font-weight:700;color:#2f5233}
.udl{border:1.5px solid #4a7c59;border-radius:5px;margin:11px 0;overflow:hidden}
.udl-h{background:#4a7c59;color:#fff;padding:5px 12px;font-weight:700;font-size:9.5pt}
.udl-grid{display:grid;grid-template-columns:1fr 1fr;gap:0}
.udl-grid div{padding:7px 12px;font-size:9pt;border-top:1px solid #dbe7de}
.udl-grid div:nth-child(odd){border-right:1px solid #dbe7de}
.udl-acc{padding:7px 12px;font-size:8.5pt;color:#2f5233;background:#eef4ec;border-top:1px solid #dbe7de}
.refs{padding:12px .6in 4px}
.refs h2{font-family:'Merriweather',serif;font-size:12pt;color:#1B2A4A;margin-bottom:8px;border-bottom:2px solid #C9A227;padding-bottom:4px}
.refs ol{margin-left:22px;font-size:8.5pt;line-height:1.5}.refs li{margin-bottom:5px}
"""

def head(title,sub):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title><style>{CSS}</style></head>
<body><button class="no-print" onclick="window.print()">⎙ Print</button>
<div class="hero"><div class="eye">Government Hack Course Series · Foundations of Constitutional Government</div>
<h1>{e(title)}</h1><div class="sub">{e(sub)}</div></div>
<div class="gold-bar"><span>Unit 1 · {e(C['unit']['standards_range'])} · Quarter 1 · Suggested {e(C['unit']['suggested_days'])} days</span>
<span>Supplemental · TCA § 49-6-2202(a)(3) · Not a claim of state approval</span></div>
<div class="eq"><b>Essential Question:</b> {e(C['unit']['essential_question'])}</div>"""

def foot():
    return f"""<div class="foot"><span><b>TroopToTeacher Technologies LLC</b> · {e(C['unit']['footer'])}</span><span>© 2026</span></div></body></html>"""

def std_band(code,s,teacher=False):
    dims=[x.strip() for x in s['tn'].split('(')[-1].rstrip(')').split(',')] if '(' in s['tn'] else []
    tags=f'<span class="tag">SSP {s["ssp_focus"].replace("SSP.","")}</span><span class="tag">{e(s["civic_label"])}</span>'
    if dims and dims!=['']:
        tags+='<span class="tag dim">'+e(' · '.join(dims))+'</span>'
    if 'tca' in s: tags+=f'<span class="tag tca">TCA {e(s["tca"])} — legally required</span>'
    return (f'<div class="band"><span class="code">{e(code)} — {e(s["title"])}</span>'
            f'<div class="stext">{e(s["tn"])}</div><div class="tags">{tags}</div></div>')

def frayer(v):
    return (f'<div class="frayer"><div class="ft"><span>{e(v["term"])} '
            f'<span class="say">/{e(v["say"])}/</span></span><span class="es">ES: {e(v["es"])}</span></div>'
            f'<div class="fd">{e(v["def"])}</div>'
            f'<div class="grid"><div><b>Draw it / Dibújalo</b></div><div><b>Use it in a sentence</b></div></div></div>')

def spotlight(src):
    return (f'<div class="pss"><div class="lbl">Founding-Document / Landmark-Case Spotlight</div>'
            f'<div class="src-t">{e(src["title"])} &mdash; <span style="font-weight:400">{e(src["who"])}, {e(src["date"])}</span></div>'
            f'<blockquote>&ldquo;{e(src["quote"])}&rdquo;</blockquote>'
            f'<cite><b>Source:</b> {e(src["who"])}, &ldquo;{e(src["title"])},&rdquo; {e(src["date"])}. {e(src["repo"])}. '
            f'<span style="word-break:break-all">{e(src["url"])}</span> &middot; Public domain.</cite></div>')

def udl(s):
    """UDL — multiple means of engagement, representation, and action/expression."""
    return ('<div class="udl"><div class="udl-h">Show What You Know &mdash; Your Choice (UDL)</div>'
            '<div class="udl-grid">'
            '<div><b>✍ Write</b> a short paragraph answering the standard\'s question.</div>'
            '<div><b>🎨 Draw</b> a labeled diagram or one-page sketch-note.</div>'
            '<div><b>🎙 Record</b> a 30-second spoken explanation.</div>'
            '<div><b>🗣 Discuss</b> with a partner, then summarize your best idea.</div>'
            '</div><div class="udl-acc"><b>Access supports:</b> read-aloud friendly · vocabulary in English &amp; Spanish (above) · '
            'use the matching graphic organizer · sentence starter: &ldquo;One key idea of this standard is ___ because ___.&rdquo;</div></div>')

# ---------------- STUDENT CHAPTER ----------------
def student():
    b=[head("Foundations of Constitutional Government","Student Textbook Chapter · Print-first · Bilingual vocabulary (EN/ES)")]
    b.append('<div class="pg">')
    b.append('<p style="margin-top:10px"><b>How to use this chapter.</b> Each standard opens with a question to think about, '
             'a short reading, a Founding-Document or Landmark-Case Spotlight to analyze, key vocabulary, and a check for '
             'understanding. Work through them in order, or use the standard you need. Teachers hold the answer keys.</p>')
    for code in C['order']:
        s=C['standards'][code]
        b.append('<div class="std">'+std_band(code,s))
        b.append('<div class="body">')
        b.append(f'<div class="ican"><b>I can</b> {e(s["ican"].replace("I can ",""))}</div>')
        b.append(f'<p class="hook">{e(s["hook"])}</p>')
        b.append('<h3>Read: The Big Idea</h3>')
        b.append(f'<p>{e(s["auth"]["close"])}</p>')
        # spotlight (first source) + SOAPS frame + TDQs
        b.append(spotlight(s['sources'][0]))
        b.append('<div class="soaps"><b>Analyze it (SSP.02):</b> Speaker/author? Occasion (when &amp; why)? '
                 'Audience? Purpose? Subject/main idea? Then answer:</div>')
        b.append('<ol class="tdq">'+''.join(f'<li>{e(q)}<div class="write"></div></li>' for q in s['auth']['tdq'])+'</ol>')
        # second source as corroboration
        b.append('<h4>Corroborating source (SSP.03)</h4>'+spotlight(s['sources'][1]))
        # vocabulary
        b.append('<h4>Key Vocabulary — Frayer (EN/ES)</h4>')
        for v in s['vocab']: b.append(frayer(v))
        # CFU (no key on student side)
        c=s['cfu']
        b.append(f'<div class="cfu"><div class="q">Check for Understanding <span class="dok">DOK {c["dok"]}</span></div>'
                 f'<p>{e(c["stem"])}</p><ol type="A">'+''.join(f'<li>{e(c["options"][k])}</li>' for k in ["A","B","C","D"])+'</ol></div>')
        # CER
        b.append(f'<div class="card"><b>Claim–Evidence–Reasoning.</b> {e(s["auth"]["cer"])}<div class="write"></div><div class="write"></div></div>')
        # UDL response choice + access supports
        b.append(udl(s))
        b.append('</div></div>')  # body, std
    # Sources & Attributions (from the canonical primary-source bank)
    bankp=os.path.abspath(os.path.join(HERE,"..","..","WEB_EDITION","public","data","government","primary-sources","unit-1.json"))
    if os.path.exists(bankp):
        bank=json.load(open(bankp))["sources"]
        b.append('<div class="refs"><h2>Sources &amp; Attributions</h2>'
                 '<p style="font-size:8.5pt;color:#555">All primary-source excerpts in this chapter are public domain, quoted verbatim from the cited repository.</p><ol>')
        for r in bank:
            b.append(f'<li>{e(r["citation_chicago"])} <i>(Rights: {e(r["rights"])} · Standards: {e(", ".join(r["standards"]))})</i></li>')
        b.append('</ol></div>')
    # spaced retrieval
    b.append('</div><div class="retrieval"><h2>Spaced Retrieval — 3 Rounds</h2>'
             '<p>Close your notes. Answer from memory. Your teacher will run these at increasing intervals.</p>'
             '<ol><li><b>Round 1 (end of unit):</b> Name the three branches and one job of each. What are natural rights?</li>'
             '<li><b>Round 2 (+2 weeks):</b> Explain the Great Compromise and why the Bill of Rights was added.</li>'
             '<li><b>Round 3 (+4 weeks):</b> Contrast a republic and a direct democracy, and explain how Article V changes the Constitution.</li></ol>'
             '<p class="disc">Assessment items in this course are classroom-formative · pre-field-test.</p></div>')
    b.append(foot())
    return "".join(b)

# ---------------- TEACHER GUIDE ----------------
def teacher():
    b=[head("Foundations of Constitutional Government — Teacher Guide","How-to-Use &amp; MTSS · Answer Keys &amp; Reteach · TEACHER-SIDE ONLY")]
    b.append('<div class="pg">')
    b.append('<div class="tnote"><span class="k">Teacher-side only</span><p style="margin:5px 0 0">This guide contains answer keys, '
             'rationale, and reteach ("What\'s Next"). Do not distribute to students or place in student-accessible folders. '
             'Standards and learning targets are verbatim from the Tennessee GC standards and the instructional guide.</p></div>')
    b.append(f'<p><b>Essential question:</b> {e(C["unit"]["essential_question"])} &nbsp;·&nbsp; <b>Pacing:</b> {e(C["unit"]["suggested_days"])} days (Quarter 1).</p>')
    for code in C['order']:
        s=C['standards'][code]; c=s['cfu']; q=s['auth']['quiz'][0]
        b.append('<div class="std">'+std_band(code,s,teacher=True)+'<div class="body">')
        b.append(f'<h4>Verbatim learning targets (source of truth)</h4><p style="font-size:9.5pt">{e(s["learning_targets"])}</p>')
        b.append(f'<h4>Success criteria</h4><ul style="margin-left:20px;font-size:9.5pt">'+''.join(f'<li>{e(x)}</li>' for x in s['criteria'])+'</ul>')
        # CFU key
        b.append(f'<div class="cfu"><div class="q">CFU key <span class="dok">DOK {c["dok"]}</span></div>'
                 f'<p>{e(c["stem"])}</p><p><span class="key">Correct: {c["key"]}</span> — {e(c["options"][c["key"]])}</p>'
                 f'<p style="font-size:9pt"><b>Why:</b> {e(c["why"])}</p></div>')
        # quiz key
        b.append(f'<div class="card"><b>Retrieval item key</b> <span class="dok">DOK {q["dok"]}</span><br>{e(q["stem"])} '
                 f'<span class="key">→ {q["key"]}</span> ({e(q["opts"][q["key"]])})</div>')
        # dimension crosswalk
        if s['dim_map']:
            b.append('<h4>Dimension crosswalk</h4><ul style="margin-left:20px;font-size:9pt">'
                     +''.join(f'<li><b>{k}:</b> {e(v)}</li>' for k,v in s['dim_map'].items())+'</ul>')
        # reteach
        b.append('<div class="tnote"><span class="k">What\'s Next — reteach if &lt;70%</span>'
                 f'<p style="margin:5px 0 0;font-size:9.5pt">Re-anchor on the primary source: have students mark the exact words in '
                 f'&ldquo;{e(s["sources"][0]["title"])}&rdquo; that answer the CFU stem, then re-attempt in pairs (think-pair-share). '
                 f'ELL/MTSS: pre-teach the three vocabulary terms with the Spanish glosses and a picture cue before re-reading.</p></div>')
        b.append('</div></div>')
    b.append('<div class="tnote"><span class="k">CER rubric (6-pt)</span><p style="margin:5px 0 0;font-size:9.5pt">'
             'Claim (0–2): clear, defensible position. Evidence (0–2): two accurate, cited details from the sources. '
             'Reasoning (0–2): explains how the evidence supports the claim and addresses a counterpoint.</p></div>')
    b.append('<p class="disc">Assessment items are classroom-formative · pre-field-test. De-bias answer positions across surfaces before printing class sets.</p>')
    b.append(foot())
    return "".join(b)

for name,fn in [("unit-1.html",student),("unit-1-teacher-guide.html",teacher)]:
    doc=fn()
    assert "W"+"CS" not in doc, f"GUARDRAIL: source-district label in {name}"
    open(os.path.join(OUT,name),"w").write(doc)
    print(f"Wrote {name}: {len(doc)//1024} KB")
print("Output dir:",OUT)
