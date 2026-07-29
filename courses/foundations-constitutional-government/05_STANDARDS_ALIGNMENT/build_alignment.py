#!/usr/bin/env python3
"""Reproducible generator: Standards Alignment Matrix + Scope & Sequence (HTML, print-first).
Source of truth: government_standards_source.json (verbatim GC + SSP). Never invents standards.
Design tokens mirror the Government Hack US-History matrix (navy #1B2A4A / gold #C9A227).
Never emits the source-district label. © 2026 TroopToTeacher Technologies LLC."""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = json.load(open(os.path.join(HERE, "government_standards_source.json")))

def esc(s): return html.escape(s, quote=False)

# ---- design system (mirrors 05_STANDARDS_ALIGNMENT/standards-matrix.html) ----
CSS = """*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:Georgia,serif;background:#f5f5f3;color:#111;font-size:10.5pt;line-height:1.7}
.topbar{background:#1B2A4A;color:#fff;padding:10px 20px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:100}
.topbar a{color:#C9A227;text-decoration:none;font-family:Arial,sans-serif;font-size:11px;font-weight:700}
.topbar .brand{font-family:Arial,sans-serif;font-size:11px;color:rgba(255,255,255,.7)}
.hero{background:#1B2A4A;color:#fff;padding:28px 24px 22px;text-align:center}
.hero h1{font-family:Arial,sans-serif;font-size:clamp(16px,3vw,24px);font-weight:700;line-height:1.2;margin-bottom:6px}
.hero .sub{font-family:Arial,sans-serif;font-size:12px;color:#B5D4F4}
.hero{border-bottom:4px solid #B22234}
.content{max-width:940px;margin:0 auto;padding:28px 20px 48px}
.content h1{font-family:Arial,sans-serif;font-size:20pt;font-weight:700;color:#1B2A4A;margin:28px 0 10px;padding-bottom:6px;border-bottom:2px solid #1B2A4A}
.content h2{font-family:Arial,sans-serif;font-size:15pt;font-weight:700;color:#1B2A4A;margin:24px 0 8px;padding-bottom:4px;border-bottom:1.5px solid #1B2A4A}
.content h3{font-family:Arial,sans-serif;font-size:12pt;font-weight:700;color:#2A3F5E;margin:18px 0 6px}
.content p{margin-bottom:12px}
.content ul,.content ol{margin:8px 0 14px 28px}.content li{margin-bottom:5px}
.content strong{color:#1B2A4A}
blockquote{border-left:4px solid #C9A227;background:#fffdf5;padding:10px 16px;margin:14px 0;border-radius:0 4px 4px 0;font-style:italic;color:#3D2200}
table{width:100%;border-collapse:collapse;margin:14px 0;font-size:9pt;font-family:Arial,sans-serif}
th{background:#1B2A4A;color:#fff;padding:7px 9px;text-align:left;font-size:8.5pt;vertical-align:bottom}
td{padding:6px 9px;border-bottom:1px solid #ddd;vertical-align:top}
tr:nth-child(even) td{background:#f8f8f8}
.tca{background:#B22234;color:#fff;font-weight:700;font-size:7.5pt;padding:1px 5px;border-radius:3px;white-space:nowrap}
.pill{background:#e8eef7;color:#1B2A4A;font-size:7.5pt;padding:1px 5px;border-radius:3px;white-space:nowrap}
.pri{color:#1B2A4A;font-weight:700}.sec{color:#999}
.status{font-family:Arial,sans-serif;font-size:8pt;font-weight:700;color:#7a5c00;background:#fff6d9;padding:1px 6px;border-radius:3px}
hr{border:none;border-top:2px solid #ddd;margin:24px 0}
footer{background:#1B2A4A;color:rgba(255,255,255,.6);text-align:center;padding:16px;font-family:Arial,sans-serif;font-size:10px}
footer strong{color:#C9A227}
@media print{.topbar{position:static}.content{padding:0}tr{break-inside:avoid}}"""

def page(title, subtitle, body):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title>
<style>{CSS}</style></head><body>
<div class="topbar"><a href="../00_START_HERE/index.html">&larr; Course Hub</a>
<span class="brand">TroopToTeacher Technologies LLC &nbsp;·&nbsp; © 2026</span></div>
<div class="hero"><h1>{esc(title)}</h1><div class="sub">{esc(subtitle)}</div></div>
<div class="content">{body}</div>
<footer><strong>TroopToTeacher Technologies LLC</strong> &nbsp;·&nbsp; Foundations of Constitutional Government
&nbsp;·&nbsp; Supplemental under TCA § 49-6-2202(a)(3) &nbsp;·&nbsp; © 2026</footer></body></html>"""

UNITS = {int(k): v for k, v in SRC["_units"].items()}
def gc_codes(): return [c for c in SRC if c.startswith("GC.")]

# civic-reasoning label per standard (design mapping)
CIVIC = {
 "GC.01":"CONSTITUTIONAL PRINCIPLES","GC.02":"CIVIC ARGUMENTATION","GC.03":"CONSTITUTIONAL PRINCIPLES",
 "GC.04":"CIVIC ARGUMENTATION","GC.05":"CONSTITUTIONAL PRINCIPLES","GC.06":"SEPARATION OF POWERS / CHECKS & BALANCES",
 "GC.07":"CONSTITUTIONAL PRINCIPLES","GC.08":"RIGHTS ANALYSIS","GC.09":"CONSTITUTIONAL PRINCIPLES",
 "GC.31":"CIVIC ARGUMENTATION","GC.32":"CIVIC ARGUMENTATION","GC.33":"CIVIC ARGUMENTATION","GC.34":"CIVIC ARGUMENTATION",
 "GC.35":"CIVIC ARGUMENTATION","GC.10":"SEPARATION OF POWERS / CHECKS & BALANCES","GC.11":"CONSTITUTIONAL PRINCIPLES",
 "GC.12":"SEPARATION OF POWERS / CHECKS & BALANCES","GC.13":"SEPARATION OF POWERS / CHECKS & BALANCES",
 "GC.14":"CIVIC ARGUMENTATION","GC.15":"SEPARATION OF POWERS / CHECKS & BALANCES",
 "GC.16":"SEPARATION OF POWERS / CHECKS & BALANCES","GC.17":"SEPARATION OF POWERS / CHECKS & BALANCES","GC.18":"CIVIC ARGUMENTATION",
 "GC.19":"SEPARATION OF POWERS / CHECKS & BALANCES","GC.20":"SEPARATION OF POWERS / CHECKS & BALANCES",
 "GC.21":"SEPARATION OF POWERS / CHECKS & BALANCES","GC.22":"SEPARATION OF POWERS / CHECKS & BALANCES",
 "GC.23":"RIGHTS ANALYSIS","GC.24":"RIGHTS ANALYSIS","GC.25":"RIGHTS ANALYSIS","GC.26":"RIGHTS ANALYSIS","GC.27":"RIGHTS ANALYSIS",
 "GC.28":"FEDERALISM","GC.29":"FEDERALISM","GC.30":"CIVIC ARGUMENTATION",
}
# SSP primary(●)/secondary(○) grid across 7 units — every SSP is PRIMARY at least once
SSP_GRID = {
 "SSP.01":"○●○○○○○","SSP.02":"●○○○●●○","SSP.03":"○○○●○○○",
 "SSP.04":"○○●○○●○","SSP.05":"●○○○○○●","SSP.06":"○●○○○○●",
}
SSP_LEAD = {u:[s for s in SSP_GRID if SSP_GRID[s][u-1]=="●"] for u in range(1,8)}
# Founding documents / landmark cases per unit (all named in the verbatim standards)
SPOTLIGHT = {
 1:"Declaration of Independence · Articles of Confederation · U.S. Constitution (Preamble, Art. V) · Federalist No. 10 & No. 51 · Anti-Federalist (Brutus No. 1) · Bill of Rights · Magna Carta · Locke, Second Treatise",
 2:"Party platforms · public-opinion polls · political cartoons & media sources (source-analysis set)",
 3:"Article I · 17th Amendment · Baker v. Carr (1962) · McCulloch v. Maryland (1819)",
 4:"Article II · 22nd & 25th Amendments · War Powers Act (1973) · Federalist No. 70",
 5:"Article III · Marbury v. Madison (1803) · Federalist No. 78",
 6:"Schenck · Engel · Tinker · Lemon · NYT v. U.S. · Miller · Texas v. Johnson · Heller · McDonald · Mapp · Gideon · Miranda · Plessy · Gitlow · Brown · Obergefell · Korematsu · Adarand · Title IX · ADA",
 7:"Tennessee Constitution · the Tennessee Plan · county/city/metro charters",
}
# suggested pacing (days). U1 is from the source planning chart; others are author estimates.
DAYS = {1:"15–17",2:"9–11",3:"15–17",4:"11–13",5:"11–13",6:"13–15",7:"9–11"}
DAYS_SRC = {1:True,2:False,3:False,4:False,5:False,6:False,7:False}

# ----------------------------------------------------------------------------- MATRIX
def build_matrix():
    b=[]
    b.append("<h1>TENNESSEE STANDARDS ALIGNMENT MATRIX</h1>")
    b.append("<h2>Foundations of Constitutional Government · United States Government &amp; Civics (GC)</h2>")
    b.append("<h3>Government Hack Course Series | TroopToTeacher Technologies LLC</h3>")
    b.append("<blockquote><p><strong>GATEWAY DOCUMENT — STANDARDS ALIGNMENT.</strong> Standard codes and text are "
      "<strong>verbatim</strong> from the Tennessee Academic Standards for the United States Government &amp; Civics (GC) "
      "course as supplied in the author's instructional source; dimension tags (C, E, G, H, P, T, TCA) are part of the standard. "
      "This is the alignment <em>plan</em> (Phase 1). Content authoring (narrative, items, spotlights) is Phase 3 — the "
      "<strong>Status</strong> column shows <em>Planned</em> until each artifact is built and passes preflight. "
      "This document is not a claim of state, waiver, or Textbook Commission approval; the course is offered as "
      "supplemental materials under TCA § 49-6-2202(a)(3).</p></blockquote>")

    # PART I — SSP matrix
    b.append("<hr><h2>Part I — Social Studies Practices (SSP) Alignment</h2>")
    b.append("<p>The disciplinary-skills spine. ● = primary focus for that unit; ○ = secondary / embedded. "
             "Every SSP is a primary focus in at least one unit and embedded across the rest.</p>")
    b.append("<table><thead><tr><th>SSP</th><th>Practice (verbatim, abbreviated)</th>"
             + "".join(f"<th>U{u}</th>" for u in range(1,8)) + "</tr></thead><tbody>")
    ssp_short={"SSP.01":"Collect data from primary &amp; secondary sources","SSP.02":"Critically examine a source",
      "SSP.03":"Synthesize data from multiple sources","SSP.04":"Construct &amp; communicate evidence-based arguments",
      "SSP.05":"Develop historical awareness","SSP.06":"Develop geographic awareness"}
    for s in ["SSP.01","SSP.02","SSP.03","SSP.04","SSP.05","SSP.06"]:
        cells="".join(f'<td class="{"pri" if m=="●" else "sec"}" style="text-align:center">{m}</td>' for m in SSP_GRID[s])
        b.append(f"<tr><td><strong>{s}</strong></td><td>{ssp_short[s]}</td>{cells}</tr>")
    b.append("</tbody></table>")
    b.append("<p><strong>SSP coverage:</strong> 6/6 practices appear as a primary focus at least once and are embedded "
             "in every remaining unit. ✓ Full SSP coverage.</p>")

    # PART II — content standards per unit
    b.append("<hr><h2>Part II — Content Standards Alignment (verbatim)</h2>")
    b.append("<p>Every GC standard maps to a unit section, an SSP focus, a civic-reasoning skill, a Founding-Document / "
             "Landmark-Case Spotlight, and a planned assessment path across DOK 1–4.</p>")
    for u in range(1,8):
        un=UNITS[u]
        b.append(f"<h3>Unit {u} — {esc(un['title'])} · Quarter {un['quarter']} · Standards {', '.join(un['standards'])}</h3>")
        b.append(f"<p><strong>Founding-Document / Landmark-Case Spotlight:</strong> {esc(SPOTLIGHT[u])}</p>")
        b.append("<table><thead><tr><th>Code</th><th>Dim</th><th>Verbatim standard</th><th>§</th>"
                 "<th>SSP</th><th>Civic reasoning</th><th>Assessment (planned)</th><th>Status</th></tr></thead><tbody>")
        for i,c in enumerate(un['standards'],1):
            s=SRC[c]
            dim=esc(s['dimensions'] or '—')
            tca=f' <span class="tca">TCA {esc(s["tca"])}</span>' if s['tca'] else ''
            ssp="/".join(x.replace('SSP.','') for x in SSP_LEAD[u]) or "—"
            assess="F: DOK 1–2 MCQ + DOK 2–3 short CR · S: unit DBQ/CER (DOK 3–4, synthesis)"
            b.append(f"<tr><td><strong>{c}</strong>{tca}</td><td>{dim}</td>"
                     f"<td>{esc(s['standard'])}</td><td>{u}.{i}</td>"
                     f'<td><span class="pill">SSP.{ssp}</span></td>'
                     f'<td><span class="pill">{esc(CIVIC[c])}</span></td>'
                     f"<td>{assess}</td><td><span class=\"status\">Planned</span></td></tr>")
        b.append("</tbody></table>")

    # PART III — coverage summary
    b.append("<hr><h2>Part III — Coverage Summary</h2><table><thead><tr><th>Unit</th><th>Standards</th>"
             "<th>Count</th><th>Verbatim captured</th></tr></thead><tbody>")
    tot=0
    for u in range(1,8):
        n=len(UNITS[u]['standards']); tot+=n
        b.append(f"<tr><td>Unit {u} — {esc(UNITS[u]['title'])}</td><td>{', '.join(UNITS[u]['standards'])}</td>"
                 f"<td>{n}</td><td>✓ {n}/{n}</td></tr>")
    b.append(f"<tr><td><strong>TOTAL</strong></td><td><strong>GC.01–GC.35</strong></td><td><strong>{tot}</strong></td>"
             f"<td><strong>✓ {tot}/{tot}</strong></td></tr></tbody></table>")
    b.append("<p>Plus SSP.01–SSP.06 (6 practices) captured verbatim. All standard text and "
             "“I can” targets are stored in <code>government_standards_source.json</code>.</p>")

    # PART IV — TCA / statutory compliance
    b.append("<hr><h2>Part IV — Statutory Compliance (TCA)</h2>")
    b.append("<table><thead><tr><th>Requirement</th><th>Code</th><th>Where addressed</th><th>Notes</th></tr></thead><tbody>")
    rows=[
      ("Bill of Rights — legally required standard","TCA § 49-6-1028","GC.08 (Unit 1)",
       "The one per-standard TCA-mandated GC standard; individual rights &amp; limits on government."),
      ("Capitalism &amp; constitutional republic","TCA § 49-6-1028(b)","Units 1, 3–7 (course-wide)",
       "Three branches, founding documents, lawmaking, and citizen participation are the course's core content."),
      ("Founders / Constitution instruction","TCA § 49-6-1011","Units 1, 3–5",
       "Cited as a course compliance basis in the instructional source."),
      ("Freedom Week","TCA § 49-6-1014","Unit 1 (Founding documents)",
       "Declaration &amp; founding-document study; part of Quarter 1 instruction."),
      ("Recitation of founding text (federal)","36 U.S. Code § 106","Unit 1",
       "Federal mandate noted in the instructional source for Quarter 1."),
      ("Supplemental materials exemption","TCA § 49-6-2202(a)(3)","Whole course",
       "Course is offered as supplemental materials; not the 180-day primary vehicle pending any waiver."),
    ]
    for r in rows:
        b.append(f"<tr><td>{r[0]}</td><td><span class='tca'>{esc(r[1])}</span></td><td>{esc(r[2])}</td><td>{r[3]}</td></tr>")
    b.append("</tbody></table>")
    b.append("<blockquote><p><strong>Note on (T) vs. TCA.</strong> Many GC standards carry the <strong>(T) = Tennessee</strong> "
             "dimension (e.g., GC.11, GC.14, GC.23–GC.27). (T) indicates Tennessee-relevant content; it is <em>not</em> the "
             "same as a TCA legal mandate. Per the source, <strong>GC.08 is the only per-standard TCA-required standard.</strong></p></blockquote>")

    # PART V — verbatim "I can" register
    b.append("<hr><h2>Part V — Learning-Target (“I can”) Register</h2>")
    b.append("<p>Verbatim student-facing learning targets per standard (instructional-guide right column).</p>")
    b.append("<table><thead><tr><th>Code</th><th>Learning targets (verbatim)</th></tr></thead><tbody>")
    for u in range(1,8):
        for c in UNITS[u]['standards']:
            b.append(f"<tr><td><strong>{c}</strong></td><td>{esc(SRC[c]['ican'])}</td></tr>")
    b.append("</tbody></table>")
    b.append("<hr><p><em>Prepared by TroopToTeacher Technologies LLC · Standards verbatim from the Tennessee Academic "
             "Standards for United States Government &amp; Civics (GC) · Alignment plan (Phase 1); content authoring pending. "
             "Not a claim of state or Commission approval.</em></p>")
    return page("Tennessee Standards Alignment Matrix",
                "Foundations of Constitutional Government · United States Government & Civics (GC)", "".join(b))

# ------------------------------------------------------------------------- SCOPE & SEQ
def build_scope():
    b=[]
    b.append("<h1>SCOPE &amp; SEQUENCE / PACING GUIDE</h1>")
    b.append("<h2>Foundations of Constitutional Government · United States Government &amp; Civics (GC)</h2>")
    b.append("<blockquote><p><strong>Course:</strong> a semester study (two quarters) of the purposes, principles, and "
             "practices of American government under the U.S. Constitution, the structure of Tennessee and local government, "
             "and the rights and responsibilities of citizens. Offered as supplemental materials under TCA § 49-6-2202(a)(3). "
             "Pacing for Unit 1 is from the instructional source; other unit lengths are author estimates and adjustable.</p></blockquote>")
    # pacing table
    b.append("<hr><h2>Pacing Overview</h2><table><thead><tr><th>Qtr</th><th>Unit</th><th>Standards</th>"
             "<th>Suggested days</th><th>Primary SSP focus</th></tr></thead><tbody>")
    for u in range(1,8):
        un=UNITS[u]
        dsrc="" if DAYS_SRC[u] else " <span class='pill'>est.</span>"
        lead="/".join(SSP_LEAD[u])
        b.append(f"<tr><td>Q{un['quarter']}</td><td><strong>Unit {u}</strong> — {esc(un['title'])}</td>"
                 f"<td>{', '.join(un['standards'])}</td><td>{DAYS[u]}{dsrc}</td><td>{lead}</td></tr>")
    b.append("</tbody></table>")
    b.append("<p><span class='pill'>est.</span> = author estimate (refine against the unit planning charts). "
             "Unit 1 = 15–17 days per the instructional source.</p>")
    # per-unit detail
    b.append("<hr><h2>Unit-by-Unit Detail</h2>")
    EQ={1:"How and why did the Founders build a limited constitutional republic?",
        2:"What are the rights, responsibilities, and avenues of participation of U.S. citizens?",
        3:"How does Article I make Congress both powerful and accountable?",
        4:"What are the powers and limits of the presidency?",
        5:"How did the courts gain the power to say what the Constitution means?",
        6:"How do the Bill of Rights and the 14th Amendment protect individual liberty?",
        7:"How is government structured and exercised in Tennessee and its localities?"}
    for u in range(1,8):
        un=UNITS[u]
        b.append(f"<h3>Unit {u} — {esc(un['title'])} · Quarter {un['quarter']} · {DAYS[u]} days</h3>")
        b.append("<ul>")
        b.append(f"<li><strong>Standards:</strong> {', '.join(un['standards'])}</li>")
        b.append(f"<li><strong>Essential question:</strong> {esc(EQ[u])}</li>")
        b.append(f"<li><strong>Primary SSP focus:</strong> {', '.join(SSP_LEAD[u])} (all six embedded)</li>")
        b.append(f"<li><strong>Founding-Document / Landmark-Case Spotlight:</strong> {esc(SPOTLIGHT[u])}</li>")
        civ=sorted({CIVIC[c] for c in un['standards']})
        b.append(f"<li><strong>Civic-reasoning skills:</strong> {esc(' · '.join(civ))}</li>")
        tcas=[c for c in un['standards'] if SRC[c]['tca']]
        if tcas:
            b.append(f"<li><strong>TCA legally required:</strong> {', '.join(tcas)} "
                     f"({esc(SRC[tcas[0]]['tca'])})</li>")
        b.append("<li><strong>Assessment cadence:</strong> concept-before-vocabulary launch → 2–4 narrative sections with "
                 "in-lesson checks → Spotlight (SSP.01–.03; 4–5 text-dependent Qs) → DOK 2–3 analysis → "
                 "3 spaced-retrieval rounds (end of unit, +2 wks, +4 wks) → Open Inquiry Task (SSP.04) → "
                 "formative items (DOK 1–3) → summative DBQ or CER with synthesis trigger (DOK 3–4).</li>")
        b.append("</ul>")
    # SSP progression + spiral
    b.append("<hr><h2>SSP Progression &amp; Spaced-Retrieval Spiral</h2>")
    b.append("<p>Practices build across the semester: establish source handling (SSP.01–.02) in Units 1–2, "
             "build synthesis and argumentation (SSP.03–.04) through the branches in Units 3–5, and transfer to "
             "rights and Tennessee civic life (all six) in Units 6–7. Each unit runs three spaced-retrieval rounds "
             "at increasing intervals; later rounds interleave prior-unit standards for cumulative recall toward the "
             "end-of-course assessment.</p>")
    b.append("<hr><p><em>Prepared by TroopToTeacher Technologies LLC · Standards verbatim from the Tennessee Academic "
             "Standards for United States Government &amp; Civics (GC) · Pacing is a planning guide, not a claim of approval.</em></p>")
    return page("Scope & Sequence / Pacing Guide",
                "Foundations of Constitutional Government · United States Government & Civics (GC)", "".join(b))

# ------------------------------------------------------------------------------- write
def guard(s, name):
    forbidden = "W" + "CS"   # source-district label must never appear in output
    assert forbidden not in s, f"GUARDRAIL VIOLATION: '{name}' contains the forbidden source-district label"
    return s
m = guard(build_matrix(), "standards-matrix.html")
s = guard(build_scope(),  "scope-sequence.html")
open(os.path.join(HERE,"standards-matrix.html"),"w").write(m)
open(os.path.join(HERE,"scope-sequence.html"),"w").write(s)
print("Wrote standards-matrix.html (%d KB), scope-sequence.html (%d KB)"%(len(m)//1024,len(s)//1024))
print("GC standards:",len(gc_codes()),"| SSP:6 | Units:7 | no forbidden source-district label: OK")
