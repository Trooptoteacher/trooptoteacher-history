# -*- coding: utf-8 -*-
"""Unit 10 labeled -- US.83 Johnson's Great Society (concept web).
Center hub = "THE GREAT SOCIETY" as a faint watermark. Four spokes = Medicare &
Medicaid, the War on Poverty, education, and urban renewal (with its costs). A
bottom LIGHT box asks what it promised and where it fell short. HAS a Tennessee
Connection. Content approved for US.83.
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
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:12pt; color:#97a2ba;
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
    (21, 20, "Medicare &amp; Medicaid", "health insurance for those 65+ and for low&#8209;income families &mdash; ended age discrimination in coverage"),
    (79, 20, "War on Poverty", "Head Start, VISTA &amp; job programs to fight poverty at its roots"),
    (21, 82, "Education", "the Elementary &amp; Secondary Education Act &mdash; federal funding for schools"),
    (79, 82, "Urban Renewal", "rebuilt inner cities &mdash; but often displaced minority neighborhoods"),
]
_outer_html = "\n        ".join(_node(x, y, 214, 98, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is Johnson&rsquo;s domestic vision. On each bubble, write what that program <b>did</b> &mdash; the faint notes are starters. Then answer the box below: what did the Great Society promise, and where did it fall short?</div>
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
          <div class="hcue">The Great<br/>Society</div>
          <div class="hguides"><div class="nline"></div><div class="nline"></div></div>
        </div>
      </div>
      <div class="synthbox">
        <div class="band navy sm">What did the Great Society <b>promise</b> &mdash; and where did it <b>fall short</b>?</div>
        <div class="well lines">
          <span class="fh">a promise to end poverty &amp; expand healthcare &nbsp;&middot;&nbsp; Medicare endured, but urban renewal displaced communities and costs rose faster than projected</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> The Great Society reached deep into Tennessee: the <b>Appalachian
        Regional Commission</b> invested in East Tennessee&rsquo;s roads and schools, <b>Medicare</b> transformed care for the
        state&rsquo;s elderly, and <b>Head Start</b> spread across rural communities.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="20_us83_conceptweb",
    title="The Great Society: A War on Poverty",
    kicker="Unit 10 &middot; US.83 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Analyze", "skill")],
    why=("A web shows the Great Society&rsquo;s many programs as one ambitious agenda &mdash; and lets students weigh which "
         "delivered and which caused harm. "
         "<span class='cite'>Connecting parts to one hub builds SSP.03 (synthesize).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the four bubble labels; fill Medicare together. Ask: who did this program help?",
        extend="Which program did the most good, and which did the most harm? Use the urban&#8209;renewal bubble to argue.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>draw</b> an icon for each program."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 10 &middot; US.83 (labeled)",
)]
