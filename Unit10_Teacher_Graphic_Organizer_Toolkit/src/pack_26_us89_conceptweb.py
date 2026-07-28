# -*- coding: utf-8 -*-
"""Unit 10 labeled -- US.89 The Reagan Administration (concept web).
Center hub = "THE REAGAN ERA" as a faint watermark. Four spokes = national pride,
Reaganomics, SDI, and the Iran-Contra affair. A bottom LIGHT box asks how Reagan
changed America's mood and economy. Balanced framing (growth AND deficits; a
scandal). HAS a Tennessee Connection. Content approved for US.89.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .web-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .web-wrap > svg{ position:absolute; inset:0; width:100%; height:100%; }
  .node{ position:absolute; transform:translate(-50%,-50%);
         display:flex; flex-direction:column; align-items:stretch; justify-content:flex-start;
         background:var(--paper); border:2px solid var(--navy); border-radius:16px; padding:6px 12px 8px; }
  .node .nlab{ font-family:Georgia,serif; font-weight:700; font-size:9.8pt; color:var(--navy);
         line-height:1.03; text-align:center; }
  .node .nsub{ font-size:7.2pt; font-style:italic; color:#9aa6bd; text-align:center; line-height:1.15; margin-top:3px; }
  .node .nline{ border-bottom:1.4px dashed #C4CCDA; height:0; margin-top:8px; }
  .hub{ background:var(--navy-tint); border:3px solid var(--navy); border-radius:50%;
        align-items:center; justify-content:center; padding:0; }
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:12.5pt; color:#97a2ba;
              letter-spacing:.02em; text-align:center; line-height:1.02; text-transform:uppercase; }
  .hub .hguides{ position:absolute; left:14%; right:14%; bottom:20%; }
  .hub .hguides .nline{ border-bottom-color:#9aa6bd; margin-top:11px; }
  .synthbox{ flex:0 0 auto; margin-top:7px; display:flex; flex-direction:column; }
  .synthbox .well{ min-height:60px; position:relative; }
  .synthbox .fh{ position:absolute; top:7px; left:12px; right:12px; font-size:8pt; font-style:italic;
             color:#9aa6bd; line-height:1.4; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.5pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""


def _node(x, y, w, h, lab, sub):
    return (f'<div class="node" style="left:{x}%; top:{y}%; width:{w}px; height:{h}px;">'
            f'<div class="nlab">{lab}</div><div class="nsub">{sub}</div>'
            f'<div class="nline"></div><div class="nline"></div></div>')


_outer = [
    (21, 20, "National Pride", "&ldquo;Morning in America&rdquo;; a military buildup &amp; Grenada &mdash; confidence after Vietnam &amp; Watergate"),
    (79, 20, "Reaganomics", "supply&#8209;side: tax cuts &amp; deregulation &mdash; growth &amp; lower inflation, but rising deficits &amp; inequality"),
    (21, 82, "SDI (&ldquo;Star Wars&rdquo;)", "a space&#8209;based missile defense; critics called it unfeasible &mdash; some credit it with pressuring the USSR"),
    (79, 82, "Iran&#8209;Contra Affair", "secret arms sales to Iran funded the Contras &mdash; in violation of Congress"),
]
_outer_html = "\n        ".join(_node(x, y, 216, 100, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is the Reagan era. On each bubble, write what that policy or moment <b>did</b> &mdash; the faint notes are starters. Then answer the box below: how did Reagan change America&rsquo;s mood and economy?</div>
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
        <div class="node hub" style="left:50%; top:51%; width:208px; height:150px;">
          <div class="hcue">The Reagan<br/>Era</div>
          <div class="hguides"><div class="nline"></div><div class="nline"></div></div>
        </div>
      </div>
      <div class="synthbox">
        <div class="band navy sm">How did Reagan change America&rsquo;s <b>mood</b> and its <b>economy</b>?</div>
        <div class="well lines">
          <span class="fh">optimism &amp; renewed pride &nbsp;&middot;&nbsp; a booming but more unequal economy &nbsp;&middot;&nbsp; a bigger military and bigger deficits</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee Senator <b>Howard Baker</b> served as Reagan&rsquo;s
        <b>White House Chief of Staff</b> (1987&ndash;88), and <b>Lamar Alexander</b> &mdash; later Tennessee governor &mdash; was
        Reagan&rsquo;s <b>Secretary of Education</b>, leading education reform.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="26_us89_conceptweb",
    title="The Reagan Era: Pride, Economics &amp; Power",
    kicker="Unit 10 &middot; US.89 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Analyze", "skill")],
    why=("A web holds Reagan&rsquo;s presidency together &mdash; national confidence, supply&#8209;side economics, missile "
         "defense, and a scandal &mdash; so students can weigh its promise and its costs. "
         "<span class='cite'>Connecting parts to one hub builds SSP.03 (synthesize).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the four bubble labels; fill &ldquo;National Pride&rdquo; together. Ask: who gained, and who lost, under Reaganomics?",
        extend="Reaganomics grew the economy but widened inequality. Use that bubble to argue whether it was worth it.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>draw</b> an icon for each part of the era."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 10 &middot; US.89 (labeled)",
)]
