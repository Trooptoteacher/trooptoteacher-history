# -*- coding: utf-8 -*-
"""Unit 7 labeled -- US.60 Containment & Early Cold War Policies (concept web).
Center hub = "CONTAINMENT" as a faint watermark. Four spokes = the Long Telegram,
the Truman Doctrine, the Marshall Plan, and the Berlin Airlift -- each a LIGHT
bubble with a bold label and a FADED italic hint. A bottom LIGHT box captures the
shared goal. HAS a Tennessee Connection. Content approved for US.60.
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
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:13pt; color:#97a2ba;
              letter-spacing:.02em; text-align:center; line-height:1.02; text-transform:uppercase; }
  .hub .hguides{ position:absolute; left:15%; right:15%; bottom:22%; }
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
    (21, 20, "The Long Telegram", "Kennan, 1946: the USSR is expansionist &mdash; contain it firmly"),
    (79, 20, "Truman Doctrine", "1947: support &ldquo;free peoples&rdquo; (Greece &amp; Turkey); end of isolationism"),
    (21, 82, "Marshall Plan", "$13B to rebuild Western Europe &amp; block communism"),
    (79, 82, "Berlin Airlift", "1948&ndash;49: supply West Berlin by air past the Soviet blockade"),
]
_outer_html = "\n        ".join(_node(x, y, 214, 96, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is the strategy. On each bubble, write how that policy carried out <b>containment</b> &mdash; the faint notes are starters. Then answer the box below: what was the shared <b>goal</b>?</div>
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
          <div class="hcue">Contain&#8209;<br/>ment</div>
          <div class="hguides"><div class="nline"></div><div class="nline"></div></div>
        </div>
      </div>
      <div class="synthbox">
        <div class="band navy sm">What was the shared <b>goal</b> of all four policies?</div>
        <div class="well lines" style="position:relative;">
          <span class="fh">stop Soviet expansion without direct war &nbsp;&middot;&nbsp; help nations resist communism &nbsp;&middot;&nbsp; commit the U.S. to global engagement</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee&rsquo;s <b>Senator Estes Kefauver</b> was a prominent Cold
        War&#8209;era figure &mdash; he ran for president in <b>1952 and 1956</b> and, through nationally televised hearings,
        showed how <b>television</b> was reshaping American politics in the containment era.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="21_us60_conceptweb",
    title="How America Tried to Contain Communism",
    kicker="Unit 7 &middot; US.60 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2 &middot; Cause &amp; Purpose", "skill")],
    why=("A web shows four early Cold War policies as one strategy radiating from a single idea &mdash; containment &mdash; "
         "so students see how each piece served the same goal. "
         "<span class='cite'>Connecting policies to one purpose builds SSP.03 (synthesize).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Define <b>containment</b> first, then match each policy to how it contained the USSR.",
        extend="Which policy did the most to stop Soviet expansion? Defend your pick with evidence from the bubbles.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>map</b> where each policy was applied (Greece, Berlin, &hellip;)."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 7 &middot; US.60 (labeled)",
)]
