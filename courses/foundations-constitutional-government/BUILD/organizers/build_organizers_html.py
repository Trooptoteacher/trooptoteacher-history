#!/usr/bin/env python3
"""Government Hack — Unit 1 Graphic Organizer Library (HTML), matching the US-History
graphic-organizers.html look (Source Sans 3 + Merriweather, navy #1B2A4A / gold #C9A227,
print-first, B&W-safe, bilingual EN/ES, .organizer-page / .frayer / .venn-svg / .cause-grid /
.write-line components). Reuses the US CSS verbatim. © 2026 TroopToTeacher Technologies LLC."""
import os, re, html
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.abspath(os.path.join(HERE,"..","..","01_STUDENT_PACKETS"))
os.makedirs(OUT,exist_ok=True)
def e(s): return html.escape(str(s),quote=False)
# reuse the US organizer CSS verbatim (the <style> block saved from graphic-organizers.html)
css=open(os.path.join(HERE,"us_organizer_style.html"),encoding="utf-8").read()
CSS=re.sub(r"</?style>","",css).strip()

def header(title,meta,std,dok,skill):
    return (f'<div class="org-header"><div><div class="org-title">{e(title)}</div>'
            f'<div class="org-meta">{e(meta)}</div></div><div class="org-badges">'
            f'<span class="badge badge-std">{e(std)}</span><span class="badge badge-dok">DOK {dok}</span>'
            f'<span class="badge badge-skill">{e(skill)}</span></div></div>')
def page(title,meta,std,dok,skill,body):
    return f'<div class="organizer-page">{header(title,meta,std,dok,skill)}<div class="ver-panel active">{body}</div></div>'
def wl(n=3): return '<span class="write-line"></span>'*n

# ---- FRAYER (bilingual) ----
def frayer_card(term,es,hint):
    cellA=('<div class="frayer-cell" style="border-bottom:1.5px solid #1B2A4A;border-right:1.5px solid #1B2A4A">'
           '<span class="frayer-cell-lbl">📖 My Definition / Mi Definición</span>'+wl(3)+
           f'<div class="stem" style="font-size:8pt">{e(hint)}</div></div>')
    cellB=('<div class="frayer-cell" style="border-bottom:1.5px solid #1B2A4A">'
           '<span class="frayer-cell-lbl">🖼 Picture / Imagen</span>'
           '<div style="border:1px dashed #ccc;min-height:55px;border-radius:3px;display:flex;'
           'align-items:center;justify-content:center;color:#bbb;font-size:8.5pt">Draw here / Dibuja aquí</div></div>')
    cellC=('<div class="frayer-cell" style="border-right:1.5px solid #1B2A4A">'
           '<span class="frayer-cell-lbl">✅ Examples / Ejemplos</span>'+wl(3)+'</div>')
    cellD=('<div class="frayer-cell"><span class="frayer-cell-lbl">🚫 Non-Examples / No-Ejemplos</span>'+wl(3)+'</div>')
    return (f'<div class="frayer-card"><div class="frayer-term">{e(term)}<div class="es">{e(es)}</div></div>'
            f'<div class="frayer-inner">{cellA}{cellB}{cellC}{cellD}</div></div>')

# ---- VENN (SVG, 2-circle) ----
def venn(leftT,rightT,leftES,rightES):
    svg=(f'<div class="venn-wrap"><svg class="venn-svg" viewBox="0 0 500 220" xmlns="http://www.w3.org/2000/svg">'
         f'<circle cx="175" cy="110" r="95" fill="rgba(27,42,74,.07)" stroke="#1B2A4A" stroke-width="2.5"/>'
         f'<circle cx="325" cy="110" r="95" fill="rgba(201,162,39,.1)" stroke="#C9A227" stroke-width="2.5"/>'
         f'<text x="105" y="66" text-anchor="middle" font-size="10" font-weight="bold" fill="#1B2A4A">{e(leftT)}</text>'
         f'<text x="395" y="66" text-anchor="middle" font-size="10" font-weight="bold" fill="#633806">{e(rightT)}</text>'
         f'<text x="250" y="50" text-anchor="middle" font-size="9" font-weight="bold" fill="#333">BOTH / AMBOS</text></svg></div>')
    cols=('<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:4px">'
          f'<div class="venn-col"><div class="venn-lbl" style="color:#1B2A4A">ONLY {e(leftT)} / SOLO</div>{wl(4)}</div>'
          f'<div class="venn-col"><div class="venn-lbl" style="color:#333">BOTH / AMBOS</div>{wl(4)}</div>'
          f'<div class="venn-col"><div class="venn-lbl" style="color:#633806">ONLY {e(rightT)} / SOLO</div>{wl(4)}</div></div>')
    return svg+cols

# ---- CAUSE & EFFECT ----
def cause_effect(rows):
    boxes=""
    cls=["pol","eco","soc"]
    for i,(hdr,hint) in enumerate(rows):
        boxes+=(f'<div class="cause-box"><div class="cause-hdr {cls[i%3]}">{e(hdr)}</div>'
                f'<div class="cause-body"><div style="font-size:8.5pt;color:#666;margin-bottom:4px">{e(hint)}</div>{wl(3)}</div></div>')
    return f'<div class="cause-grid">{boxes}</div>'

# ---- T-CHART (two-column) ----
def tchart(leftT,rightT,leftHint,rightHint):
    return ('<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">'
            f'<div class="venn-col"><div class="venn-lbl" style="color:#1B2A4A">{e(leftT)}</div>'
            f'<div style="font-size:8.5pt;color:#666;margin-bottom:4px">{e(leftHint)}</div>{wl(5)}</div>'
            f'<div class="venn-col"><div class="venn-lbl" style="color:#633806">{e(rightT)}</div>'
            f'<div style="font-size:8.5pt;color:#666;margin-bottom:4px">{e(rightHint)}</div>{wl(5)}</div></div>')

# ---- TIMELINE ----
def timeline(events):
    cells="".join(f'<div class="venn-col" style="text-align:center"><div class="venn-lbl" style="color:#1B2A4A">{e(y)}</div>'
                  f'<div style="font-size:8.5pt;color:#333">{e(ev)}</div></div>' for y,ev in events)
    return (f'<div style="display:grid;grid-template-columns:repeat({len(events)},1fr);gap:6px">{cells}</div>'
            '<div style="border-top:3px solid #C9A227;margin:8px 0 6px"></div>'
            '<div class="field-label">Why did the ORDER matter? / ¿Por qué importó el orden?</div>'+wl(3))

# ---- CER ----
def cer(claim_prompt):
    def box(lbl,hint,n): return (f'<div class="arg-box"><div class="arg-hdr">{lbl}</div>'
            f'<div style="font-size:8.5pt;color:#666;margin:3px 0">{e(hint)}</div>{wl(n)}</div>')
    return ('<div class="org-topic">'+e(claim_prompt)+'</div><div class="arg-grid">'
            +box("CLAIM / Afirmación","State your position in one sentence.",2)
            +box("EVIDENCE / Evidencia","Two specific details from the sources.",3)
            +box("REASONING / Razonamiento","Explain how the evidence supports your claim.",3)+'</div>')

# ---- CONCEPT WEB ----
def concept_web(center,spokes):
    items="".join(f'<div class="venn-col"><div class="venn-lbl" style="color:#1B2A4A">{e(s)}</div>{wl(2)}</div>' for s in spokes)
    return (f'<div style="text-align:center;margin-bottom:8px"><span style="display:inline-block;background:#1B2A4A;color:#fff;'
            f'font-weight:700;padding:8px 18px;border-radius:6px">{e(center)}</span></div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px">{items}</div>')

ORG=[]
ORG.append(page("Frayer Vocabulary — Foundations Key Terms","Best for deep vocabulary (Bill of Rights, federalism).","GC.01/GC.08",1,"VOCABULARY · SSP.02",
  '<div class="frayer-grid">'
  +frayer_card("Natural Rights","Derechos naturales","God-given rights to life, liberty, property.")
  +frayer_card("Federalism","Federalismo","Power divided between nation and states.")
  +frayer_card("Separation of Powers","Separación de poderes","Three branches, no one holds all power.")
  +frayer_card("Bill of Rights","Carta de Derechos","The first ten amendments; limits on government.")+'</div>'))
ORG.append(page("Venn — Articles of Confederation vs. U.S. Constitution","Compare the two frameworks; find what changed and what both shared.","GC.03/GC.04",3,"COMPARISON · SSP.03",
  venn("ARTICLES","CONSTITUTION","","")))
ORG.append(page("Cause & Effect — Weaknesses of the Articles","How each weakness of the Articles led to a problem.","GC.03",2,"CAUSATION · SSP.05",
  cause_effect([("No power to tax / Sin poder de gravar","Congress could only request money → unpaid debts."),
                ("No national army / Sin ejército","Shays’s Rebellion (1786) went unchecked."),
                ("No trade regulation / Sin regular el comercio","States taxed each other → economic chaos.")])))
ORG.append(page("T-Chart — Federalists vs. Anti-Federalists","Weigh the two sides of the ratification debate.","GC.04",3,"ARGUMENTATION · SSP.04",
  tchart("FEDERALISTS","ANTI-FEDERALISTS","For a stronger national union; wrote the Federalist Papers.","Feared central power; demanded a Bill of Rights.")))
ORG.append(page("Timeline — Founding Documents (1776–1791)","Sequence the documents that built the republic.","GC.02–GC.08",2,"CHRONOLOGY · SSP.05",
  timeline([("1776","Declaration of Independence"),("1781","Articles of Confederation"),("1787","Constitutional Convention"),("1788","Constitution ratified"),("1791","Bill of Rights")])))
ORG.append(page("Concept Web — Principles of Limited Government","Connect the principles that keep government limited.","GC.06",2,"CONSTITUTIONAL PRINCIPLES",
  concept_web("LIMITED GOVERNMENT",["Separation of Powers","Checks & Balances","Federalism","Judicial Review","Popular Sovereignty","Rule of Law"])))
ORG.append(page("CER — Claim, Evidence, Reasoning","Make and defend a claim about the founding.","GC.01–GC.09",3,"CIVIC ARGUMENTATION · SSP.04",
  cer("Did the Founders build a government that trusts the people, or one that guards against them? Defend your claim with two sources.")))

doc=(f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
     f'<meta name="viewport" content="width=device-width,initial-scale=1">'
     f'<title>Government Hack — Unit 1 Graphic Organizer Library</title><style>{CSS}</style></head><body>'
     f'<div class="site-header"><div><h1>Graphic Organizer Library</h1>'
     f'<div class="sub">Government Hack™ · Unit 1: Foundations of Constitutional Government · Reproducible · EN/ES</div></div></div>'
     f'<div class="gold-bar"><span>Print-first · B&amp;W-safe · bilingual · UDL response choice</span>'
     f'<span>Supplemental · TCA § 49-6-2202(a)(3)</span></div>'
     f'<div class="unit-content active"><div class="unit-hdr"><h2>Unit 1 — Foundations of Constitutional Government '
     f'(GC.01–GC.09)</h2><div class="meta">Best-fit organizers per standard. Each is a reproducible blank; teachers pick by learner need.</div></div>'
     + "".join(ORG) +
     f'<div class="org-footer" style="padding:10px 0;color:#555;font-size:8pt">Government Hack™ · TroopToTeacher Technologies LLC · © 2026 · '
     f'Assessment/teaching frameworks: Frayer, Venn, Cause &amp; Effect, T-Chart, Timeline, Concept Web, CER · SSP.01–.06.</div>'
     f'</div></body></html>')
assert "W"+"CS" not in doc and "History Hack" not in doc
open(os.path.join(OUT,"unit-1-graphic-organizers.html"),"w",encoding="utf-8").write(doc)
print("Wrote unit-1-graphic-organizers.html:",len(doc)//1024,"KB ·",len(ORG),"organizers · style matched to US library")
