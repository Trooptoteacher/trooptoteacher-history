# -*- coding: utf-8 -*-
"""Unit 6 labeled -- US.49 WWII Leaders & Key Figures (concept web).
Center hub = "WWII LEADERS" as a faint watermark. Three spokes group the named
figures into families (Allied political, Allied military, Axis) -- each a LIGHT
bubble with a bold category label and a FADED italic list of figures students
write roles over. HAS a Tennessee Connection. Content approved for US.49.
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
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:12pt; color:#97a2ba;
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


# three spokes in a triangle: (x%, y%, label, faded figures)
_outer = [
    (50, 17, "Allied Political Leaders", "Churchill (UK) &middot; FDR (US) &middot; Truman (US) &middot; Stalin (USSR)"),
    (21, 80, "Allied Military Leaders", "Eisenhower (D&#8209;Day) &middot; MacArthur (Pacific) &middot; Marshall &middot; Patton"),
    (79, 80, "Axis Leaders", "Hitler (Germany) &middot; Mussolini (Italy) &middot; Tojo (Japan)"),
]
_outer_html = "\n        ".join(_node(x, y, 236, 104, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is the war&rsquo;s leadership. Sort each figure into the right bubble, then write each one&rsquo;s <b>role or key action</b> over the faint names &mdash; who led, and what they did.</div>
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
        <div class="node hub" style="left:50%; top:50%; width:196px; height:140px;">
          <div class="hcue">WWII<br/>Leaders</div>
          <div class="hguides"><div class="nline"></div></div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee helped supply the war&rsquo;s leadership: Lt. Alexander
        &ldquo;Sandy&rdquo; Ninninger trained at <b>Fort Oglethorpe near Chattanooga</b> and was the <b>first Medal of Honor
        recipient of WWII</b>, and thousands of officers trained at Tennessee installations before deploying to both theaters.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="24_us49_conceptweb",
    title="Who Led World War II?",
    kicker="Unit 6 &middot; US.49 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 1&#8211;2 &middot; Identify", "skill")],
    why=("A web sorts the war&rsquo;s many leaders into three families around one hub &mdash; so students see at a glance "
         "who fought on which side, and can attach each one&rsquo;s role. "
         "<span class='cite'>Organizing people and roles into one picture builds SSP.01 (collect information).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the figures on cards; sort them into the three bubbles together before writing roles.",
        extend="Which leader&rsquo;s decisions mattered most to the war&rsquo;s outcome? Defend your pick with a key action.",
        show="Students may <b>write</b> roles, <b>say</b> them aloud, or <b>match</b> figure cards to actions."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 6 &middot; US.49 (labeled)",
)]
