# -*- coding: utf-8 -*-
"""Unit 9 labeled -- US.82 American Indian, Chicano & Feminist Movements (concept web).
Center hub = "MOVEMENTS FOR EQUALITY" as a faint watermark. Three spokes = AIM, the
Chicano Movement, and the Feminist Movement; a fourth spoke names what all three
shared with the Civil Rights Movement. A bottom LIGHT box asks how they connect.
HAS a Tennessee Connection. Content approved for US.82.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .web-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .web-wrap > svg{ position:absolute; inset:0; width:100%; height:100%; }
  .node{ position:absolute; transform:translate(-50%,-50%);
         display:flex; flex-direction:column; align-items:stretch; justify-content:flex-start;
         background:var(--paper); border:2px solid var(--navy); border-radius:16px; padding:6px 12px 8px; }
  .node.share{ border-color:var(--gold); background:var(--gold-tint); }
  .node .nlab{ font-family:Georgia,serif; font-weight:700; font-size:9.6pt; color:var(--navy);
         line-height:1.03; text-align:center; }
  .node.share .nlab{ color:#7a5c15; }
  .node .nsub{ font-size:7.1pt; font-style:italic; color:#9aa6bd; text-align:center; line-height:1.14; margin-top:3px; }
  .node.share .nsub{ color:#a08a4e; }
  .node .nline{ border-bottom:1.4px dashed #C4CCDA; height:0; margin-top:8px; }
  .node.share .nline{ border-bottom-color:#d9c48a; }
  .hub{ background:var(--navy-tint); border:3px solid var(--navy); border-radius:50%;
        align-items:center; justify-content:center; padding:0; }
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:11pt; color:#97a2ba;
              letter-spacing:.02em; text-align:center; line-height:1.03; text-transform:uppercase; }
  .hub .hguides{ position:absolute; left:14%; right:14%; bottom:19%; }
  .hub .hguides .nline{ border-bottom-color:#9aa6bd; margin-top:11px; }
  .synthbox{ flex:0 0 auto; margin-top:7px; display:flex; flex-direction:column; }
  .synthbox .well{ min-height:56px; position:relative; }
  .synthbox .fh{ position:absolute; top:7px; left:12px; right:12px; font-size:8pt; font-style:italic;
             color:#9aa6bd; line-height:1.4; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.5pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""


def _node(x, y, w, h, lab, sub, cls=""):
    return (f'<div class="node {cls}" style="left:{x}%; top:{y}%; width:{w}px; height:{h}px;">'
            f'<div class="nlab">{lab}</div><div class="nsub">{sub}</div>'
            f'<div class="nline"></div><div class="nline"></div></div>')


_outer = [
    (21, 20, "American Indian Movement", "tribal sovereignty &amp; treaty rights; Alcatraz (1969&ndash;71), Wounded Knee (1973); Russell Means, &ldquo;Red Power&rdquo;", ""),
    (79, 20, "Chicano Movement", "educational equality &amp; labor rights; East L.A. walkouts, grape boycotts; Cesar Chavez, United Farm Workers", ""),
    (21, 82, "Feminist Movement", "equal pay &amp; an end to gender discrimination; NOW; Betty Friedan, <i>The Feminine Mystique</i> (1963)", ""),
    (79, 82, "Shared with the Movement", "legal challenges &middot; direct&#8209;action protest &middot; federal legislation &middot; group pride", "share"),
]
_outer_html = "\n        ".join(_node(x, y, 216, 100, lab, sub, cls) for x, y, lab, sub, cls in _outer)

BODY = f"""
    <div class="prompt">The hub is the model the Civil Rights Movement set. On each bubble, write that movement&rsquo;s <b>goals</b> and <b>key actions</b> &mdash; the faint notes are starters. The gold bubble names what all three <b>borrowed</b> from the movement.</div>
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
        <div class="node hub" style="left:50%; top:51%; width:206px; height:150px;">
          <div class="hcue">Movements<br/>for Equality</div>
          <div class="hguides"><div class="nline"></div><div class="nline"></div></div>
        </div>
      </div>
      <div class="synthbox">
        <div class="band navy sm">How are these three movements <b>related</b> to the Civil Rights Movement?</div>
        <div class="well lines">
          <span class="fh">Each adapted its strategies &mdash; the courts, protest, and the push for federal law &mdash; to advance equality for a different group</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> The <b>Highlander Folk School</b> in Monteagle trained activists across
        these movements. And <b>Wilma Mankiller</b> &mdash; the first female Principal Chief of the Cherokee Nation &mdash; was
        rooted in the Cherokee&rsquo;s Tennessee heritage before her family&rsquo;s relocation.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="24_us82_conceptweb",
    title="One Movement Inspires Many",
    kicker="Unit 9 &middot; US.82 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Analyze", "skill")],
    why=("A web puts three movements around the model the Civil Rights Movement built, so students see both what made "
         "each distinct and the strategies they shared. "
         "<span class='cite'>Connecting cases to a common idea builds SSP.03 (synthesize).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the four bubble labels; fill the AIM bubble together. Ask: what did this group want to change?",
        extend="Pick two movements and compare their <b>tactics</b>. Which borrowed most directly from the Civil Rights Movement?",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>draw</b> a symbol for each movement."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 9 &middot; US.82 (labeled)",
)]
