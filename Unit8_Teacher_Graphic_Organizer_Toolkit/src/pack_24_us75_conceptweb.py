# -*- coding: utf-8 -*-
"""Unit 8 labeled -- US.75 Television & Mass Media (concept web).
Center hub = "TELEVISION" as a faint watermark. Four spokes = family life, politics,
advertising & economy, and a shared national culture -- each a LIGHT bubble with a
bold label and a FADED italic hint. A bottom LIGHT box asks what TV gained and cost
Americans. HAS a Tennessee Connection. Content approved for US.75.
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
    (21, 20, "Family Life", "the center of home entertainment; families plan around shows; living rooms face the set"),
    (79, 20, "Politics", "the 1960 Kennedy&ndash;Nixon debates &mdash; TV viewers favored the telegenic Kennedy"),
    (21, 82, "Advertising &amp; Economy", "reaches millions at once; shapes desires; the dominant ad medium"),
    (79, 82, "A National Culture", "everyone watches the same shows &rarr; shared values &amp; tastes"),
]
_outer_html = "\n        ".join(_node(x, y, 214, 96, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is the new medium. On each bubble, write how television changed that part of American life &mdash; the faint notes are starters. Then answer the box below: what did TV give Americans, and what did it cost?</div>
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
          <div class="hcue">Tele&#8209;<br/>vision</div>
          <div class="hguides"><div class="nline"></div><div class="nline"></div></div>
        </div>
      </div>
      <div class="synthbox">
        <div class="band navy sm">What did television <b>give</b> Americans &mdash; and what did it <b>cost</b>?</div>
        <div class="well lines" style="position:relative;">
          <span class="fh">a shared national experience &amp; instant news &nbsp;&middot;&nbsp; but also more time indoors, more advertising, and pressure to look &amp; buy the same</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Television reshaped Tennessee too: <b>WSM&#8209;TV in Nashville</b> broadcast
        the <b>Grand Ole Opry</b>, helping country music reach a national TV audience, while Senator <b>Estes Kefauver&rsquo;s</b>
        televised crime hearings (1950&ndash;51) showed the nation TV&rsquo;s political power.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="24_us75_conceptweb",
    title="The Box That Changed Everything",
    kicker="Unit 8 &middot; US.75 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Analyze", "skill")],
    why=("A web shows how one invention reached into the home, politics, and the economy at once &mdash; and tied them "
         "together into a shared national culture. "
         "<span class='cite'>Connecting one cause to many effects builds SSP.03 (synthesize).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the four bubble labels; fill one together. Ask: which change would a 1950s family notice first?",
        extend="Did TV bring Americans <b>together</b> or push them <b>apart</b>? Use two bubbles to argue each side.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>storyboard</b> a 1950s TV ad."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 8 &middot; US.75 (labeled)",
)]
