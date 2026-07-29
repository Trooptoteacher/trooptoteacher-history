#!/usr/bin/env python3
"""Government Hack — Unit 1 Graphic Organizer Library. Uses the EXACT US-History Hack organizer
structures (frayer-grid, venn-wrap, cause-grid, ccot-grid, arg-grid/CER, hipp-grid, soaps-grid),
reproduced byte-for-byte from graphic-organizers.html, with Government content. Reuses the US CSS
verbatim. Print-first, B&W-safe, bilingual EN/ES. Rendered to PDF via Chromium. © 2026 TroopToTeacher."""
import os, re, html
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.abspath(os.path.join(HERE,"..","..","01_STUDENT_PACKETS"))
os.makedirs(OUT,exist_ok=True)
def e(s): return html.escape(str(s),quote=False)
CSS=re.sub(r"</?style>","",open(os.path.join(HERE,"us_organizer_style.html"),encoding="utf-8").read()).strip()

def header(title,meta,std,dok,skill):
    return (f'<div class="org-header"><div><div class="org-title">{e(title)}</div>'
            f'<div class="org-meta">{e(meta)}</div></div><div class="org-badges">'
            f'<span class="badge badge-std">{e(std)}</span><span class="badge badge-dok">DOK {dok}</span>'
            f'<span class="badge badge-skill">{e(skill)}</span></div></div>')
def page(title,meta,std,dok,skill,body):
    return f'<div class="organizer-page">{header(title,meta,std,dok,skill)}<div class="ver-panel active" style="padding:16px">{body}</div></div>'

# ---------- EXACT Frayer card (from US structure) ----------
def frayer_card(term,es):
    return (f'<div class="frayer-card">\n  <div class="frayer-term">{e(term)}<div class="es">{e(es)}</div></div>\n'
      '  <div class="frayer-inner">\n'
      '    <div class="frayer-cell" style="border-bottom:1.5px solid #1B2A4A;border-right:1.5px solid #1B2A4A">\n'
      '      <span class="frayer-cell-lbl">📖 My Definition / Mi Definición</span>\n'
      '      <span class="write-line"></span><span class="write-line"></span><span class="write-line"></span>\n'
      '      <div class="stem" style="font-size:8pt">This means... / Esto significa...</div>\n    </div>\n'
      '    <div class="frayer-cell" style="border-bottom:1.5px solid #1B2A4A">\n'
      '      <span class="frayer-cell-lbl">🖼 Picture / Imagen</span>\n'
      '      <div style="border:1px dashed #ccc;min-height:55px;border-radius:3px;display:flex;align-items:center;justify-content:center;color:#bbb;font-size:8.5pt">Draw here / Dibuja aquí</div>\n    </div>\n'
      '    <div class="frayer-cell" style="border-right:1.5px solid #1B2A4A">\n'
      '      <span class="frayer-cell-lbl">✅ Example / Ejemplo</span>\n'
      '      <span class="write-line"></span><span class="write-line"></span>\n'
      '      <div class="stem" style="font-size:8pt">For example... / Por ejemplo...</div>\n    </div>\n'
      '    <div class="frayer-cell">\n'
      '      <span class="frayer-cell-lbl">❌ Non-Example / No-Ejemplo</span>\n'
      '      <span class="write-line"></span><span class="write-line"></span>\n'
      '      <div class="stem" style="font-size:8pt">This is NOT like... / Esto NO es como...</div>\n    </div>\n  </div>\n</div>')
def frayer_grid(cards): return '<div class="frayer-grid">\n'+"".join(cards)+'\n</div>'

# ---------- EXACT Venn (svg) ----------
def venn(leftT,rightT):
    return (f'<div class="venn-wrap">\n  <svg class="venn-svg" viewBox="0 0 500 220" xmlns="http://www.w3.org/2000/svg">\n'
      f'    <circle cx="175" cy="110" r="95" fill="rgba(27,42,74,.07)" stroke="#1B2A4A" stroke-width="2.5"/>\n'
      f'    <circle cx="325" cy="110" r="95" fill="rgba(201,162,39,.1)" stroke="#C9A227" stroke-width="2.5"/>\n'
      f'    <text x="105" y="70" text-anchor="middle" font-size="10" font-weight="bold" fill="#1B2A4A">{e(leftT)}</text>\n'
      f'    <text x="395" y="70" text-anchor="middle" font-size="10" font-weight="bold" fill="#633806">{e(rightT)}</text>\n'
      f'    <text x="250" y="50" text-anchor="middle" font-size="9" font-weight="bold" fill="#333">BOTH / AMBOS</text>\n  </svg>\n</div>'
      '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:6px">'
      f'<div class="venn-col"><div class="venn-lbl" style="color:#1B2A4A">ONLY {e(leftT)}</div><span class="write-line"></span><span class="write-line"></span><span class="write-line"></span></div>'
      '<div class="venn-col"><div class="venn-lbl" style="color:#333">BOTH / AMBOS</div><span class="write-line"></span><span class="write-line"></span><span class="write-line"></span></div>'
      f'<div class="venn-col"><div class="venn-lbl" style="color:#633806">ONLY {e(rightT)}</div><span class="write-line"></span><span class="write-line"></span><span class="write-line"></span></div></div>')

# ---------- EXACT Cause & Effect (4 boxes pol/eco/soc/ide) ----------
def cause_grid(rows):
    cls=["pol","eco","soc","ide"]
    body="".join(f'<div class="cause-box"><div class="cause-hdr {cls[i]}">{e(h)}</div><div class="cause-body">'
                 f'<div style="font-size:8.5pt;color:#666;margin-bottom:4px">{e(hint)}</div>'
                 '<span class="write-line"></span><span class="write-line"></span><span class="write-line"></span></div></div>'
                 for i,(h,hint) in enumerate(rows))
    return f'<div class="cause-grid">{body}</div>'

# ---------- EXACT CCOT (before / change / after) ----------
def ccot(before,change,after):
    def col(hdr,sub,stem):
        return (f'<div class="ccot-col"><div class="ccot-hdr">{e(hdr)}<br><small>{e(sub)}</small></div>'
                f'<div class="ccot-body"><div class="stem">{e(stem)}</div>'
                '<span class="write-line"></span><span class="write-line"></span><span class="write-line"></span><span class="write-line"></span><span class="write-line"></span></div></div>')
    return ('<div class="ccot-grid">'+col("BEFORE / ANTES",before[0],before[1])+'<div class="ccot-arrow">→</div>'
            +col("CHANGE / CAMBIO",change[0],change[1])+'<div class="ccot-arrow">→</div>'
            +col("AFTER / DESPUÉS",after[0],after[1])+'</div>')

# ---------- EXACT CER (arg-grid) ----------
def cer():
    return ('<div class="arg-grid">'
      '<div class="arg-box"><div class="arg-hdr claim-hdr">📌 CLAIM / AFIRMACIÓN<br><small>What do you argue? / ¿Qué argumentas?</small></div>'
      '<div class="arg-body"><div class="stem">I argue that... / Yo argumento que...</div><span class="write-line"></span><span class="write-line"></span><span class="write-line"></span><span class="write-line"></span></div></div>'
      '<div class="arg-box"><div class="arg-hdr evidence-hdr">📚 EVIDENCE / EVIDENCIA<br><small>What proof do you have? / ¿Qué prueba tienes?</small></div>'
      '<div class="arg-body"><div class="stem">One piece of evidence is... / Una evidencia es...</div><span class="write-line"></span><span class="write-line"></span><span class="write-line"></span><div class="stem">Another piece of evidence is... / Otra evidencia es...</div><span class="write-line"></span><span class="write-line"></span></div></div>'
      '<div class="arg-box"><div class="arg-hdr reasoning-hdr">🔗 REASONING / RAZONAMIENTO<br><small>Why does evidence prove your claim?</small></div>'
      '<div class="arg-body"><div class="stem">This evidence proves my claim because... / Esto prueba mi afirmación porque...</div><span class="write-line"></span><span class="write-line"></span><span class="write-line"></span><span class="write-line"></span></div></div>'
      '</div>')

# ---------- EXACT HIPP (argumentative connection table) ----------
def hipp():
    def row(el,stem):
        return (f'<div class="hipp-row"><div class="hipp-cell" style="font-weight:700">{el}</div>'
                '<div class="hipp-cell"><span class="write-line"></span><span class="write-line"></span></div>'
                f'<div class="hipp-cell"><div class="stem" style="font-size:8pt">{stem}</div><span class="write-line"></span></div></div>')
    return ('<div class="hipp-grid" style="margin-top:10px"><div class="hipp-hdr">HIPP Analysis — Argumentative Connection / Conexión con el Argumento</div>'
            '<div class="hipp-row hdr-row"><div class="hipp-cell">HIPP Element</div><div class="hipp-cell">I identified... / Identifiqué...</div><div class="hipp-cell">This means for my argument... / Para mi argumento...</div></div>'
            +row("Historical Context","Because of the context...")+row("Intended Audience","Because the audience was...")
            +row("Purpose","Because the purpose was...")+row("Point of View","Because of the author's view...")+'</div>')

# ---------- EXACT SOAPS (S/O/A/P/S rows) ----------
def soaps():
    rows=[("S","Speaker / Autor","Who created this? / ¿Quién creó esto?"),
          ("O","Occasion / Ocasión","When and why was this created? / ¿Cuándo y por qué?"),
          ("A","Audience / Audiencia","Who was this for? / ¿Para quién fue?"),
          ("P","Purpose / Propósito","Why was it written? / ¿Por qué se escribió?"),
          ("S","Subject / Tema","What is it about? / ¿De qué trata?")]
    inner="".join(f'<div class="soaps-row"><div class="soaps-letter">{L}</div><div class="soaps-body"><span class="lbl">{e(lbl)}</span>'
                  f'<div class="stem" style="font-size:8pt">{e(q)}</div><span class="write-line"></span></div></div>' for L,lbl,q in rows)
    return f'<div class="soaps-grid"><div>{inner}</div></div>'

ORG=[
 page("Frayer — Foundations Key Terms","Deep vocabulary. Best for a term students must own.","GC.01/GC.06/GC.08",1,"VOCABULARY",
   frayer_grid([frayer_card("Natural Rights","Derechos naturales"),frayer_card("Federalism","Federalismo"),
                frayer_card("Separation of Powers","Separación de poderes"),frayer_card("Bill of Rights","Carta de Derechos")])),
 page("SOAPS — Founding-Document Source Analysis","First-encounter tool for a founding document (e.g., the Declaration).","GC.02",2,"SSP.02 · SOURCING",soaps()),
 page("HIPP — Argumentative Source Analysis","Connect a source's features to your argument (e.g., Federalist No. 51).","GC.06",3,"SSP.02–.03 · SOURCING",hipp()),
 page("Venn — Articles of Confederation vs. U.S. Constitution","Compare the two frameworks; find what changed and what both shared.","GC.03/GC.04",3,"COMPARISON",
   venn("ARTICLES","CONSTITUTION")),
 page("Cause & Effect — Why the Articles Failed","Sort the causes that led to the Constitutional Convention.","GC.03",2,"CAUSATION",
   cause_grid([("Political / Político","No executive or courts; nine of thirteen states needed to act; all thirteen to amend."),
               ("Economic / Económico","Congress could not tax or regulate trade; unpaid war debt; states taxed each other."),
               ("Social / Social","Shays's Rebellion (1786) frightened leaders; farmers in debt; no way to keep order."),
               ("Ideological / Ideológico","Fear of a too-strong central power vs. the need for a workable national union.")])),
 page("CCOT — Government Before &amp; After the Constitution","Track what changed from the Articles to the new republic.","GC.03–GC.08",3,"CONTINUITY &amp; CHANGE",
   ccot(("Articles of Confederation (1781–1789)","Under the Articles, the national government..."),
        ("New Constitution (1787–1788)","What changed was..."),
        ("Bill of Rights added (1791)","After ratification..."))),
 page("CER — Make and Defend a Claim","Claim + Evidence + Reasoning on the founding.","GC.01–GC.09",3,"SSP.04 · ARGUMENTATION",cer()),
]

doc=(f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
     f'<meta name="viewport" content="width=device-width,initial-scale=1">'
     f'<title>Government Hack — Unit 1 Graphic Organizer Library</title><style>{CSS}</style></head><body>'
     f'<div class="site-header"><div><h1>Graphic Organizer Library</h1>'
     f'<div class="sub">Government Hack™ · Unit 1: Foundations of Constitutional Government · Reproducible · EN/ES</div></div></div>'
     f'<div class="gold-bar"><span>Print-first · B&amp;W-safe · bilingual · UDL response choice</span><span>Supplemental · TCA § 49-6-2202(a)(3)</span></div>'
     f'<div class="unit-content active" style="padding:20px 30px"><div class="unit-hdr"><h2>Unit 1 — Foundations of Constitutional Government (GC.01–GC.09)</h2>'
     f'<div class="meta">Best-fit organizers per standard, in the Government Hack organizer structure. Each is a reproducible blank.</div></div>'
     + "".join(ORG) +
     f'<div class="org-footer" style="padding:10px 0;color:#555;font-size:8pt">Government Hack™ · TroopToTeacher Technologies LLC · © 2026 · Organizers: Frayer · SOAPS · HIPP · Venn · Cause &amp; Effect · CCOT · CER.</div>'
     f'</div></body></html>')
assert "W"+"CS" not in doc and "History Hack" not in doc, "Leakage: WCS or History Hack found in output"
open(os.path.join(OUT,"unit-1-graphic-organizers.html"),"w",encoding="utf-8").write(doc)
print("Wrote unit-1-graphic-organizers.html:",len(doc)//1024,"KB ·",len(ORG),"organizers (EXACT US structures)")
