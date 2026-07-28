# -*- coding: utf-8 -*-
"""Reference page: TN Social Studies Practices (SSP) Crosswalk.
Maps each SSP -> the organizers that build it -> when/where to use it in Unit 5.
SSP names sourced from the course docs (SSP.01 Collect Information; SSP.02
Critically Examine Sources; SSP.03 Synthesize Data; SSP.04 Construct &
Communicate with Evidence; SSP.05 Historical Awareness; SSP.06 Geographic
Awareness). Writes pages/01_ssp_crosswalk.html.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from toolkit_lib import SHARED_CSS, FOOTER_BRAND  # noqa

# (code, name, what-it-is, [organizer chips], use-when / Unit-1 anchor)
SSP = [
    ("SSP.01", "Collect Information", "navy",
     "Gather facts from primary &amp; secondary sources.",
     ["5 Ws", "Main Idea &amp; Details", "K&#8209;W&#8209;L"],
     "Intake: pulling the who/what/when and key ideas out of a reading, image, or lecture."),
    ("SSP.02", "Critically Examine Sources", "red",
     "Interrogate a source: author, audience, point of view, purpose, reliability.",
     ["HIPPO", "C&#8209;E&#8209;R"],
     "Any primary source in US.39&ndash;US.44 &mdash; a Dust Bowl photograph, a Hooverville account, or an FDR Fireside Chat."),
    ("SSP.03", "Synthesize Data", "gold",
     "Organize &amp; combine data from several sources into one picture.",
     ["Comparison matrix", "Concept web", "Main Idea"],
     "US.43 (New Deal 3 R&rsquo;s &mdash; Relief, Recovery, Reform) &mdash; holding many programs against one yardstick."),
    ("SSP.04", "Construct &amp; Communicate with Evidence", "navy",
     "Build and defend an argument or explanation with evidence.",
     ["C&#8209;E&#8209;R", "T&#8209;chart", "Problem&ndash;Solution"],
     "US.44 (New Deal achievements vs. criticisms &mdash; socialism &amp; court&#8209;packing) &mdash; take a stance."),
    ("SSP.05", "Develop Historical Awareness", "red",
     "Sequence in time, trace cause &amp; effect, and see change over time.",
     ["Timeline", "Cause &amp; Effect", "Concept web"],
     "US.39 (the many causes &rarr; the Crash) &amp; US.40 (over&#8209;farming + drought &rarr; the Dust Bowl)."),
    ("SSP.06", "Develop Geographic Awareness", "gold",
     "Read place, region &amp; spatial patterns; connect geography to events.",
     ["Dust Bowl map", "&#9733; Tennessee Connection"],
     "US.40 (Dust Bowl states &amp; the Route 66 migration) &mdash; and every Tennessee Connection (TVA, Norris Dam)."),
]

def dot(color):
    c = {"navy": "var(--navy)", "red": "var(--red)", "gold": "var(--gold)"}[color]
    return c

rows = []
for code, name, color, what, orgs, use in SSP:
    chips = "".join(f'<span class="ochip">{o}</span>' for o in orgs)
    rows.append(f"""      <div class="sr">
        <div class="c-code"><span class="badge" style="background:{dot(color)}{'; color:var(--navy)' if color=='gold' else ''}">{code}</span><span class="nm">{name}</span></div>
        <div class="c-what">{what}</div>
        <div class="c-org">{chips}</div>
        <div class="c-use">{use}</div>
      </div>""")

CSS = r"""
  .cover{ flex:0 0 auto; background:var(--navy); color:#fff; border-radius:9px; padding:14px 20px;
          display:flex; justify-content:space-between; align-items:center; }
  .cover .ttl{ font-family:Georgia,serif; font-size:23pt; font-weight:700; line-height:1.03; }
  .cover .ttl .thin{ display:block; font-family:"Helvetica Neue",Arial,sans-serif; font-size:10pt;
                     font-weight:700; letter-spacing:.15em; text-transform:uppercase; color:var(--gold); margin-bottom:4px; }
  .cover .sub{ font-size:9.6pt; color:#cdd4e2; margin-top:5px; }
  .cover .repro2{ border:1.5px solid var(--gold); color:var(--gold); font-size:8pt; font-weight:800;
                  letter-spacing:.08em; text-transform:uppercase; padding:4px 10px; border-radius:4px; }
  .lede{ flex:0 0 auto; margin:11px 2px 8px; font-size:10.3pt; color:#2c3446; line-height:1.35; }
  .lede b{ color:var(--navy); }
  .stbl{ flex:1 1 auto; display:flex; flex-direction:column; border:2px solid var(--navy); border-radius:8px; overflow:hidden; min-height:0; }
  .sh{ flex:0 0 auto; display:grid; grid-template-columns:1.15fr 1.35fr 1.15fr 1.5fr; background:var(--navy); color:#fff; }
  .sh div{ padding:7px 12px; font-size:8.4pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase; }
  .sh div+div{ border-left:1px solid #3a4b68; }
  .sr{ flex:1 1 0; display:grid; grid-template-columns:1.15fr 1.35fr 1.15fr 1.5fr; align-items:center; border-top:1px solid var(--rule); min-height:0; }
  .sr:nth-child(even){ background:#fafbfc; }
  .sr>div{ padding:7px 12px; } .sr>div+div{ border-left:1px solid var(--rule); }
  .c-code{ display:flex; flex-direction:column; gap:4px; }
  .c-code .badge{ align-self:flex-start; color:#fff; font-weight:800; font-size:9pt; letter-spacing:.03em; padding:3px 9px; border-radius:5px; }
  .c-code .nm{ font-size:9.3pt; font-weight:800; color:var(--navy); line-height:1.1; }
  .c-what{ font-size:8.8pt; color:#3a4455; line-height:1.26; }
  .c-org{ display:flex; flex-wrap:wrap; gap:4px; }
  .ochip{ background:var(--navy-tint); border:1px solid #c3ccdc; color:var(--navy); font-size:8pt; font-weight:700; padding:2px 7px; border-radius:9px; }
  .c-use{ font-size:8.6pt; color:#3a4455; line-height:1.26; } .c-use i{ font-family:Georgia,serif; }
  .foot{ flex:0 0 auto; display:flex; justify-content:space-between; align-items:center;
         margin-top:8px; padding-top:6px; border-top:1px solid var(--rule); font-size:7.7pt; color:var(--muted); }
  .foot .brand{ font-weight:700; color:var(--navy); }
"""

HTML = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>SSP Crosswalk</title>
<style>{SHARED_CSS}
{CSS}</style></head>
<body>
<div class="page">
  <div class="cover">
    <div class="l">
      <div class="ttl"><span class="thin">TN Social Studies Practices</span>SSP Crosswalk</div>
      <div class="sub">Which organizer builds which practice &mdash; and where it lives in Unit 5</div>
    </div>
    <div class="repro2">&#10003; Reproducible</div>
  </div>

  <div class="lede">Every organizer in this toolkit is also a <b>skills tool</b>. Use this crosswalk to name the
  Tennessee Social Studies Practice you&rsquo;re building &mdash; and to pick the organizer that builds it best.</div>

  <div class="stbl">
    <div class="sh"><div>Practice</div><div>What students do</div><div>Build it with</div><div>Use it when &middot; where in Unit 5</div></div>
{chr(10).join(rows)}
  </div>

  <div class="foot">
    <span class="brand">{FOOTER_BRAND}</span>
    <span>Teacher Graphic Organizer Toolkit &middot; SSP Crosswalk</span>
  </div>
</div></body></html>
"""

out = os.path.join(os.path.dirname(HERE), "pages", "01_ssp_crosswalk.html")
with open(out, "w") as f:
    f.write(HTML)
print("wrote", out)
