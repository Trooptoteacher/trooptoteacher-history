# -*- coding: utf-8 -*-
"""Unit 4 labeled -- US.33 The Harlem Renaissance (concept web).
Center hub = "HARLEM RENAISSANCE" as a faint watermark over writing lines. Four
spokes = music/jazz, literature, visual art & theater, the "New Negro" movement --
each a LIGHT bubble with a bold anchor label and a FADED italic content hint
students write over. A bottom LIGHT box captures its lasting impact.
HAS a Tennessee Connection (gold chip + gold callout). Content approved for US.33.
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
  .node .nlab b{ color:var(--red); }
  .node .nsub{ font-size:7.3pt; font-style:italic; color:#9aa6bd; text-align:center; line-height:1.16; margin-top:3px; }
  .node .nline{ border-bottom:1.4px dashed #C4CCDA; height:0; margin-top:9px; }
  .hub{ background:var(--navy-tint); border:3px solid var(--navy); border-radius:50%;
        align-items:center; justify-content:center; padding:0; }
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:11.5pt; color:#97a2ba;
              letter-spacing:.02em; text-align:center; line-height:1.04; text-transform:uppercase; }
  .hub .hguides{ position:absolute; left:14%; right:14%; bottom:19%; }
  .hub .hguides .nline{ border-bottom-color:#9aa6bd; margin-top:12px; }
  .synthbox{ flex:0 0 auto; margin-top:7px; display:flex; flex-direction:column; }
  .synthbox .band{ border-radius:6px 6px 0 0; }
  .synthbox .well{ min-height:64px; }
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


# four spokes: (x%, y%, anchor label, faded content hint)
_outer = [
    (21, 20, "Music &amp; Jazz", "Louis Armstrong (trumpet, scat); Duke Ellington (&ldquo;Mood Indigo&rdquo;)"),
    (79, 20, "Literature", "Langston Hughes; Zora Neale Hurston; James Weldon Johnson"),
    (21, 82, "Art &amp; Theater", "Aaron Douglas&rsquo;s art; &ldquo;Shuffle Along&rdquo; on Broadway; the Apollo &amp; Cotton Club"),
    (79, 82, "&ldquo;New Negro&rdquo; Movement", "racial pride; challenging stereotypes; <i>Crisis</i> &amp; <i>Opportunity</i>"),
]
_outer_html = "\n        ".join(_node(x, y, 210, 96, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is the movement. On each bubble, write how that art form or idea carried the Harlem Renaissance &mdash; the faint notes name key figures. Then answer the box below: what was its lasting <b>impact</b>?</div>
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
        <div class="node hub" style="left:50%; top:51%; width:212px; height:150px;">
          <div class="hcue">Harlem<br/>Renaissance</div>
          <div class="hguides"><div class="nline"></div><div class="nline"></div></div>
        </div>
      </div>
      <div class="synthbox">
        <div class="band navy sm">How did the Harlem Renaissance change American culture &mdash; and challenge stereotypes?</div>
        <div class="well lines" style="position:relative;">
          <span class="fh">it put Black artists &amp; writers at the center of American culture &nbsp;&middot;&nbsp; jazz reached mainstream audiences &nbsp;&middot;&nbsp; its influence lasted long past the 1920s</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Though centered in New York, the movement had deep Tennessee roots:
        <b>Fisk University</b> in <b>Nashville</b> was a major center of African American intellectual life &mdash; its
        <b>Jubilee Singers</b> had pioneered spirituals, and writer <b>Arna Bontemps</b> (a Fisk graduate) kept ties to
        Nashville&rsquo;s Black community.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="25_us33_conceptweb",
    title="A Cultural Flowering: The Harlem Renaissance",
    kicker="Unit 4 &middot; US.33 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Analyze", "skill")],
    why=("A web shows music, literature, art, and the &ldquo;New Negro&rdquo; idea as one movement radiating from a single hub &mdash; "
         "and how its figures connect. "
         "<span class='cite'>Organizing figures and ideas into one picture builds SSP.03 (synthesize).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the four bubble labels as a word bank; place one figure in each bubble together first.",
        extend="Which figure&rsquo;s work reached the widest audience? Draw links between bubbles to show how the arts fed each other.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>share</b> a song, poem, or artwork from the movement."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 4 &middot; US.33 (labeled)",
)]
