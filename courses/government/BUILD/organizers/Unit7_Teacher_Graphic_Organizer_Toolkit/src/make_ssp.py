# -*- coding: utf-8 -*-
"""Page 2: SSP Crosswalk (TN Social Studies Practice -> organizers -> where in Unit 7).
Bespoke branded page. Writes pages/01_ssp_crosswalk.html. SSP wording is drawn from
the verbatim TN Social Studies Practices in government_standards_source.json.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from toolkit_lib import SHARED_CSS, FOOTER_BRAND  # noqa

# (code, short practice (from verbatim SSP), organizers that build it, where in Unit 7, color)
ROWS = [
    ("SSP.01", "Collect data &amp; information from a variety of primary and secondary sources.",
     "Comparison Matrix &middot; 5 Ws &middot; K-W-L",
     "GC.28 Tennessee&rsquo;s three branches (Matrix, branch &times; function).", "navy"),
    ("SSP.02", "Critically examine a source: purpose, point of view, evidence vs. assertion, bias.",
     "HIPPO &middot; Comparison Matrix",
     "GC.29 local-government types (Matrix, type &times; trait); HIPPO on a constitution clause.", "red"),
    ("SSP.03", "Synthesize data from several sources; compare accounts; frame new questions.",
     "Comparison Matrix &middot; Concept Web &middot; Venn",
     "GC.28 &amp; GC.29 compare branches, courts, and local-government types.", "navy"),
    ("SSP.04", "Construct &amp; communicate arguments citing supporting evidence.",
     "C-E-R &middot; T-Chart &middot; Problem&ndash;Solution",
     "GC.29 opinion piece on civic participation (C-E-R).", "navy"),
    ("SSP.05", "Develop historical awareness: cause, context, continuity &amp; change over time.",
     "Timeline &middot; Cause &amp; Effect &middot; Sequence",
     "How Tennessee&rsquo;s Grand Divisions and consolidated metro governments took shape over time.", "red"),
    ("SSP.06", "Develop geographic awareness: patterns and scale from local to national.",
     "&#9733; Tennessee Connection &middot; Lookup &middot; Matrix",
     "GC.30 identify your own governor, senator, and representative by district (Lookup); GC.29 your county on the map.", "gold"),
]

def dot(color):
    c = {"navy": "var(--navy)", "red": "var(--red)", "gold": "var(--gold)"}[color]
    return f'<span class="dot" style="background:{c}"></span>'

rows_html = []
for code, practice, orgs, where, color in ROWS:
    rows_html.append(f"""      <div class="qr">
        <div class="c-code">{dot(color)}<span>{code}</span></div>
        <div class="c-prac">{practice}</div>
        <div class="c-org">{orgs}</div>
        <div class="c-where">{where}</div>
      </div>""")

CSS = r"""
  .cover{ flex:0 0 auto; background:var(--navy); color:#fff; border-radius:9px; padding:15px 20px;
          display:flex; justify-content:space-between; align-items:center; border-bottom:4px solid var(--red); }
  .cover .ttl{ font-family:Georgia,serif; font-size:24pt; font-weight:700; line-height:1.02; }
  .cover .ttl .thin{ display:block; font-family:"Helvetica Neue",Arial,sans-serif; font-size:10.5pt;
                     font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--gold); margin-bottom:4px; }
  .cover .sub{ font-size:10pt; color:#cdd4e2; margin-top:5px; }
  .cover .r{ text-align:right; display:flex; flex-direction:column; align-items:flex-end; gap:7px; }
  .cover .repro2{ border:1.5px solid var(--gold); color:var(--gold); font-size:8pt; font-weight:800;
                  letter-spacing:.08em; text-transform:uppercase; padding:4px 10px; border-radius:4px; }
  .cover .seal{ font-family:Georgia,serif; font-style:italic; font-size:10pt; color:#e6d3a3; max-width:210px; text-align:right; line-height:1.25; }
  .lede{ flex:0 0 auto; margin:11px 2px 8px; font-size:10.5pt; color:#2c3446; line-height:1.35; }
  .lede b{ color:var(--navy); }
  .qtbl{ flex:1 1 auto; display:flex; flex-direction:column; border:2px solid var(--navy); border-radius:8px; overflow:hidden; min-height:0; }
  .qh{ flex:0 0 auto; display:grid; grid-template-columns:0.5fr 1.5fr 1.15fr 1.5fr; background:var(--navy); color:#fff; }
  .qh div{ padding:7px 12px; font-size:8.4pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase; }
  .qh div+div{ border-left:1px solid #3a4b68; }
  .qr{ flex:1 1 0; display:grid; grid-template-columns:0.5fr 1.5fr 1.15fr 1.5fr; align-items:center; border-top:1px solid var(--rule); min-height:0; }
  .qr:nth-child(even){ background:#fafbfc; }
  .qr>div{ padding:6px 12px; } .qr>div+div{ border-left:1px solid var(--rule); }
  .c-code{ display:flex; align-items:center; gap:8px; font-family:Georgia,serif; font-weight:700; font-size:11pt; color:var(--navy); }
  .c-code .dot{ width:12px; height:12px; border-radius:50%; flex:0 0 auto; }
  .c-prac{ font-size:8.7pt; color:#2c3446; line-height:1.25; }
  .c-org{ font-size:8.7pt; font-weight:800; color:var(--navy); line-height:1.25; }
  .c-where{ font-size:8.5pt; color:#3a4455; line-height:1.22; }
  .foot{ flex:0 0 auto; display:flex; justify-content:space-between; align-items:center;
         margin-top:8px; padding-top:6px; border-top:1px solid var(--rule); font-size:7.7pt; color:var(--muted); }
  .foot .brand{ font-weight:700; color:var(--navy); }
"""

HTML = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>SSP Crosswalk &mdash; Unit 7</title>
<style>{SHARED_CSS}
{CSS}</style></head>
<body>
<div class="page">
  <div class="cover">
    <div class="l">
      <div class="ttl"><span class="thin">Government Hack &middot; Teacher Graphic Organizer Toolkit</span>Social Studies Practices Crosswalk</div>
      <div class="sub">Unit 7 &middot; Tennessee State &amp; Local Government &nbsp;(SSP.01&ndash;SSP.06)</div>
    </div>
    <div class="r">
      <div class="repro2">&#10003; Reproducible</div>
      <div class="seal">Every organizer doubles as a <b>skills</b> tool.</div>
    </div>
  </div>

  <div class="lede">The Tennessee <b>Social Studies Practices (SSP.01&ndash;06)</b> are the skills every unit must build.
  This crosswalk maps each practice to the organizers that develop it &mdash; and shows <b>where</b> it lives in Unit 7 &mdash;
  so a graphic organizer is never busywork: it is deliberate practice toward a standard.</div>

  <div class="qtbl">
    <div class="qh"><div>Practice</div><div>What students do (TN SSP)</div><div>Organizers that build it</div><div>Where in Unit 7</div></div>
{chr(10).join(rows_html)}
  </div>

  <div class="foot">
    <span class="brand">{FOOTER_BRAND}</span>
    <span>Teacher Graphic Organizer Toolkit &middot; SSP Crosswalk</span>
  </div>
</div></body></html>
"""

out = os.path.join(os.path.dirname(HERE), "pages", "01_ssp_crosswalk.html")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    f.write(HTML)
print("wrote", out)
