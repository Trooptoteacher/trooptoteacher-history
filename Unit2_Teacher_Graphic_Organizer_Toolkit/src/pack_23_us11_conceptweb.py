# -*- coding: utf-8 -*-
"""Unit 2 labeled -- US.11 The Rise of the Labor Movement (concept web).
Center hub = "THE LABOR MOVEMENT" as a faint watermark over writing lines (leave
room to write, per the concept-web guardrail). Five outer LIGHT bubbles are
pre-labeled; students fill them in. Content approved for US.11 (labor movement:
why workers organized, tactics, leaders, unions, obstacles).
"""

CSS = r"""
  .web-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .web-wrap > svg{ position:absolute; inset:0; width:100%; height:100%; }
  .node{ position:absolute; transform:translate(-50%,-50%);
         display:flex; flex-direction:column; align-items:stretch; justify-content:flex-start;
         background:var(--paper); border:2px solid var(--navy); border-radius:16px; padding:6px 11px 8px; }
  .node .nlab{ font-family:Georgia,serif; font-weight:700; font-size:10.2pt; color:var(--navy); line-height:1.04; text-align:center; }
  .node .nsub{ font-size:7.4pt; font-style:italic; color:#8792a4; text-align:center; line-height:1.12; margin-top:2px; }
  .node .nline{ border-bottom:1.4px dashed #C4CCDA; height:0; margin-top:9px; }
  .node .nline+.nline{ margin-top:11px; }
  .hub{ background:var(--navy-tint); border:3px solid var(--navy); border-radius:50%;
        align-items:center; justify-content:center; padding:0; }
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:12.5pt; color:#97a2ba;
              letter-spacing:.02em; text-align:center; line-height:1.02; text-transform:uppercase; }
  .hub .hguides{ position:absolute; left:14%; right:14%; bottom:20%; }
  .hub .hguides .nline{ border-bottom-color:#9aa6bd; margin-top:12px; }
  .tnbox{ flex:0 0 auto; margin-top:6px; background:var(--gold-tint); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:7px 12px; display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.8pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

def _node(x, y, w, h, lab, sub="", lines=1):
    subhtml = f'<div class="nsub">{sub}</div>' if sub else ""
    guides = "".join('<div class="nline"></div>' for _ in range(lines))
    return (f'<div class="node" style="left:{x}%; top:{y}%; width:{w}px; height:{h}px;">'
            f'<div class="nlab">{lab}</div>{subhtml}{guides}</div>')

# five outer bubbles: (x%, y%, label, faded sub-hint)
_outer = [
    (50, 12, "Why workers organized", ""),
    (85, 39, "Union tactics", "strikes &middot; collective bargaining &middot; boycotts"),
    (74, 86, "Key leaders", "Eugene Debs &middot; Samuel Gompers / AFL"),
    (26, 86, "Major unions", ""),
    (15, 39, "What blocked them", "court injunctions &middot; convict lease"),
]

_outer_html = "\n      ".join(
    _node(x, y, 196, (92 if sub else 78), lab, sub, lines=(1 if sub else 2))
    for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is the big idea. On each outer bubble, fill in what you know about that part of the movement &mdash; then draw links that <b>connect</b> them.</div>
    <div class="canvas">
      <div class="web-wrap">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none">
          <g stroke="#C4CCDA" stroke-width="0.7">
            <line x1="50" y1="50" x2="50" y2="12"/>
            <line x1="50" y1="50" x2="85" y2="39"/>
            <line x1="50" y1="50" x2="74" y2="86"/>
            <line x1="50" y1="50" x2="26" y2="86"/>
            <line x1="50" y1="50" x2="15" y2="39"/>
          </g>
        </svg>
        {_outer_html}
        <div class="node hub" style="left:50%; top:50%; width:210px; height:158px;">
          <div class="hcue">The Labor<br/>Movement</div>
          <div class="hguides"><div class="nline"></div><div class="nline"></div></div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> The <b>Coal Creek War (1891&ndash;1892, Anderson County)</b> &mdash;
        Tennessee miners rose up against the <b>convict-lease system</b> that undercut their wages.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="23_us11_conceptweb",
    title="The Rise of the Labor Movement",
    kicker="Unit 2 &middot; US.11 &middot; Best-Fit Organizer",
    chips=[("Concept Web &middot; Connect", "navy"), ("DOK 2 &middot; Relationships", "skill")],
    tn=True,
    why=("Use to <b>brainstorm and connect</b> the leaders, tactics, and obstacles of the labor movement "
         "around one hub &mdash; the spokes make the relationships visible at a glance. "
         "<span class='cite'>Organizing ideas into a nonlinear web supports schema-building (UDL 3.0).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Seed one bubble together and give a linking stem: &ldquo;This connects to the movement because ___.&rdquo;",
        extend="Draw new lines <b>between</b> outer bubbles (e.g., how did the obstacles shape the tactics?) and label each link.",
        show="Students may <b>write</b>, <b>say</b> (record), <b>draw</b> icons in bubbles, or <b>build</b> it with sticky notes."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 2 &middot; US.11 (labeled)",
)]
