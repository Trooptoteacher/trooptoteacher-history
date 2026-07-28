# -*- coding: utf-8 -*-
"""Unit 6 labeled -- US.55 Home Front Mobilization (concept web).
Center hub = "THE HOME FRONT" as a faint watermark. Four spokes = rationing &
conservation, war bonds & propaganda, factory conversion, migration & the Bracero
program -- each a LIGHT bubble with a bold label and a FADED italic hint. A bottom
LIGHT box captures how the home front made victory possible. HAS a Tennessee
Connection. Content approved for US.55.
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
    (21, 20, "Rationing &amp; Conservation", "ration books (gas, sugar, meat); victory gardens; scrap drives"),
    (79, 20, "Bonds &amp; Propaganda", "Liberty &amp; Victory bonds; the Office of War Information; posters &amp; film"),
    (21, 82, "Factory Conversion", "auto plants retool for tanks &amp; aircraft &rarr; record production"),
    (79, 82, "Migration &amp; Bracero", "millions move to defense centers; the Bracero Program (1942)"),
]
_outer_html = "\n        ".join(_node(x, y, 216, 96, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is the war at home. On each bubble, write how that effort supported the war &mdash; the faint notes are starters. Then answer the box below: how did the home front make victory possible?</div>
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
          <div class="hcue">The Home<br/>Front</div>
          <div class="hguides"><div class="nline"></div><div class="nline"></div></div>
        </div>
      </div>
      <div class="synthbox">
        <div class="band navy sm">How did civilians far from the fighting help <b>win</b> the war?</div>
        <div class="well lines" style="position:relative;">
          <span class="fh">shared sacrifice built national unity &nbsp;&middot;&nbsp; factories out&#8209;produced the enemy &nbsp;&middot;&nbsp; bonds &amp; labor kept the war supplied</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee was a major center for war production: <b>Alcoa, Tennessee,</b>
        produced <b>aluminum for military aircraft</b>, and <b>Camp Forrest</b> near Tullahoma was a major Army training
        base, as women across the state joined the workforce in unprecedented numbers.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="30_us55_conceptweb",
    title="Winning the War at Home",
    kicker="Unit 6 &middot; US.55 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2 &middot; Describe", "skill")],
    why=("A web shows rationing, bonds, factory conversion, and labor as one home&#8209;front system feeding the war effort &mdash; "
         "and how each part connects to victory. "
         "<span class='cite'>Connecting ideas around one hub builds SSP.01 (collect information).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the four bubble labels as a word bank; fill one together. Ask: which effort touched the most families?",
        extend="Draw links <b>between</b> bubbles &mdash; e.g., how did propaganda connect to bond drives and to factory work?",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>design</b> a home&#8209;front poster for one bubble."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 6 &middot; US.55 (labeled)",
)]
