# -*- coding: utf-8 -*-
"""Unit 6 labeled -- US.58 Founding of the UN & Cordell Hull (concept web).
Center hub = "THE UNITED NATIONS" as a faint watermark. Three spokes = lessons
from the League's failure, Cordell Hull's role, and the UN's goals & structure --
each a LIGHT bubble with a bold label and a FADED italic hint. HAS a strong
Tennessee Connection (Cordell Hull, a Tennessean and Nobel laureate). Approved US.58.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .web-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .web-wrap > svg{ position:absolute; inset:0; width:100%; height:100%; }
  .node{ position:absolute; transform:translate(-50%,-50%);
         display:flex; flex-direction:column; align-items:stretch; justify-content:flex-start;
         background:var(--paper); border:2px solid var(--navy); border-radius:16px; padding:6px 12px 8px; }
  .node .nlab{ font-family:Georgia,serif; font-weight:700; font-size:10pt; color:var(--navy);
         line-height:1.04; text-align:center; }
  .node .nsub{ font-size:7.4pt; font-style:italic; color:#9aa6bd; text-align:center; line-height:1.2; margin-top:3px; }
  .node .nline{ border-bottom:1.4px dashed #C4CCDA; height:0; margin-top:8px; }
  .hub{ background:var(--navy-tint); border:3px solid var(--navy); border-radius:50%;
        align-items:center; justify-content:center; padding:0; }
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:11.5pt; color:#97a2ba;
              letter-spacing:.02em; text-align:center; line-height:1.04; text-transform:uppercase; }
  .hub .hguides{ position:absolute; left:15%; right:15%; bottom:22%; }
  .hub .hguides .nline{ border-bottom-color:#9aa6bd; margin-top:12px; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.6pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""


def _node(x, y, w, h, lab, sub):
    return (f'<div class="node" style="left:{x}%; top:{y}%; width:{w}px; height:{h}px;">'
            f'<div class="nlab">{lab}</div><div class="nsub">{sub}</div>'
            f'<div class="nline"></div><div class="nline"></div></div>')


_outer = [
    (50, 17, "Lessons from the League", "the U.S. never joined; no enforcement; it couldn&rsquo;t stop aggression"),
    (21, 80, "Cordell Hull&rsquo;s Role", "FDR&rsquo;s Secretary of State; planned the UN; Nobel Peace Prize, 1945"),
    (79, 80, "UN Goals &amp; Structure", "keep peace by collective action; a Security Council with real power"),
]
_outer_html = "\n        ".join(_node(x, y, 236, 104, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is the new organization. On each bubble, write how it shaped the UN &mdash; the faint notes are starters. The League <b>failed</b>; planners built the UN to <b>fix</b> those weaknesses.</div>
    <div class="canvas">
      <div class="web-wrap">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none">
          <g stroke="#C4CCDA" stroke-width="0.7">
            <line x1="50" y1="50" x2="50" y2="17"/>
            <line x1="50" y1="50" x2="21" y2="80"/>
            <line x1="50" y1="50" x2="79" y2="80"/>
          </g>
        </svg>
        {_outer_html}
        <div class="node hub" style="left:50%; top:50%; width:200px; height:142px;">
          <div class="hcue">The United<br/>Nations</div>
          <div class="hguides"><div class="nline"></div></div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> <b>Cordell Hull</b> of <b>Pickett County, Tennessee</b>, served as
        Secretary of State (1933&ndash;1944) and was instrumental in founding the United Nations &mdash; earning the
        <b>Nobel Peace Prize in 1945</b> and the title &ldquo;Father of the United Nations,&rdquo; one of Tennessee&rsquo;s greatest
        contributions to world history.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="33_us58_conceptweb",
    title="Building a Body to Keep the Peace",
    kicker="Unit 6 &middot; US.58 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2 &middot; Cause &amp; Purpose", "skill")],
    why=("A web connects <b>why</b> the UN was founded &mdash; the League&rsquo;s failure, a Tennessean&rsquo;s leadership, and the "
         "goals it was built to serve &mdash; around one hub. "
         "<span class='cite'>Connecting causes and purpose into one picture builds SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Start with the League bubble: list why it failed, then show how each UN feature answers a failure.",
        extend="Which weakness of the League was most important to fix? Defend your pick using the UN&rsquo;s structure.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>match</b> each League failure to its UN fix."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 6 &middot; US.58 (labeled)",
)]
