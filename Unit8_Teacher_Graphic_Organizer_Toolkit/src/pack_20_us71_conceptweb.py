# -*- coding: utf-8 -*-
"""Unit 8 labeled -- US.71 1950s Prosperity & Consumerism (concept web).
Center hub = "1950s PROSPERITY" as a faint watermark. Four spokes = white-collar
jobs, the suburban ideal, the G.I. Bill, and consumerism -- each a LIGHT bubble
with a bold label and a FADED italic hint. A bottom LIGHT box asks what made it
possible and who shared it. HAS a Tennessee Connection. Content approved for US.71.
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
  .node .nsub{ font-size:7.3pt; font-style:italic; color:#9aa6bd; text-align:center; line-height:1.16; margin-top:3px; }
  .node .nline{ border-bottom:1.4px dashed #C4CCDA; height:0; margin-top:9px; }
  .hub{ background:var(--navy-tint); border:3px solid var(--navy); border-radius:50%;
        align-items:center; justify-content:center; padding:0; }
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:12.5pt; color:#97a2ba;
              letter-spacing:.02em; text-align:center; line-height:1.02; text-transform:uppercase; }
  .hub .hguides{ position:absolute; left:14%; right:14%; bottom:20%; }
  .hub .hguides .nline{ border-bottom-color:#9aa6bd; margin-top:12px; }
  .synthbox{ flex:0 0 auto; margin-top:7px; display:flex; flex-direction:column; }
  .synthbox .band{ border-radius:6px 6px 0 0; }
  .synthbox .well{ min-height:62px; }
  .synthbox .fh{ position:absolute; top:7px; left:12px; right:12px; font-size:8pt; font-style:italic;
             color:#9aa6bd; line-height:1.4; }
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
    (21, 20, "White&#8209;Collar Jobs", "office &amp; management work outnumbers factory work by 1956; the &ldquo;organization man&rdquo;"),
    (79, 20, "The Suburban Ideal", "Levittown (1947): affordable mass&#8209;produced homes; space, safety, schools"),
    (21, 82, "The G.I. Bill", "helped veterans buy homes &amp; attend college &mdash; fuel for the middle class"),
    (79, 82, "Consumerism", "pent&#8209;up demand; the highest standard of living; half the world&rsquo;s goods"),
]
_outer_html = "\n        ".join(_node(x, y, 214, 96, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is the boom. On each bubble, write how that force fed 1950s prosperity &mdash; the faint notes are starters. Then answer the box below: what made it possible, and who shared in it?</div>
    <div class="canvas">
      <div class="web-wrap">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none">
          <g stroke="#C4CCDA" stroke-width="0.7">
            <line x1="50" y1="50" x2="21" y2="20"/>
            <line x1="50" y1="50" x2="79" y2="20"/>
            <line x1="50" y1="50" x2="21" y2="82"/>
            <line x1="50" y1="50" x2="79" y2="82"/>
          </g>
        </svg>
        {_outer_html}
        <div class="node hub" style="left:50%; top:51%; width:210px; height:150px;">
          <div class="hcue">1950s<br/>Prosperity</div>
          <div class="hguides"><div class="nline"></div><div class="nline"></div></div>
        </div>
      </div>
      <div class="synthbox">
        <div class="band navy sm">What made the boom possible &mdash; and who benefited most from it?</div>
        <div class="well lines" style="position:relative;">
          <span class="fh">wartime savings &amp; demand &nbsp;&middot;&nbsp; government support (G.I. Bill) &nbsp;&middot;&nbsp; new jobs &amp; homes &mdash; though not everyone could buy into the suburbs</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee shared in the boom through <b>suburban growth around
        Nashville, Memphis, and Knoxville</b>. Completing the interstate highway system through the state connected
        Tennessee to national markets and sped up suburban development and consumer culture.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="20_us71_conceptweb",
    title="The Boom Years: Prosperity in the 1950s",
    kicker="Unit 8 &middot; US.71 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Analyze", "skill")],
    why=("A web shows white&#8209;collar work, suburbs, the G.I. Bill, and consumerism as one system driving postwar "
         "prosperity &mdash; and how the pieces connect. "
         "<span class='cite'>Connecting causes around one hub builds SSP.03 (synthesize).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the four bubble labels as a word bank; fill one together. Ask: which change touched the most families?",
        extend="Draw links <b>between</b> bubbles &mdash; e.g., how did the G.I. Bill connect to suburbs and to white&#8209;collar jobs?",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>draw</b> an icon for each part of the boom."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 8 &middot; US.71 (labeled)",
)]
