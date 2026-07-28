# -*- coding: utf-8 -*-
"""Unit 3 labeled -- US.19 Causes of American Imperialism (concept web).
Center hub = "AMERICAN IMPERIALISM" as a faint watermark (per the concept-web
guardrail: hub word and any pre-loaded bubble words are a soft watermark, never
bold prominent text, so students can write over/around them). Four outer LIGHT
bubbles name a driver in faded text with a faded italic hint + writing lines;
students add their own evidence. Neutral framing: the "moral ideals" driver is
labeled the STATED goal / a claimed mission -- no value judgment is asserted.
Content approved for US.19 (economic drive, stated democratic/moral ideals,
yellow journalism, naval power / Mahan 1890).
"""

CSS = r"""
  .web-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .web-wrap > svg{ position:absolute; inset:0; width:100%; height:100%; }
  .node{ position:absolute; transform:translate(-50%,-50%);
         display:flex; flex-direction:column; align-items:stretch; justify-content:flex-start;
         background:var(--paper); border:2px dashed #B7C0D2; border-radius:16px; padding:7px 12px 9px; }
  .node .nlab{ font-family:Georgia,serif; font-weight:700; font-style:italic; font-size:10.4pt;
               color:#9aa6bd; line-height:1.04; text-align:center; }
  .node .nsub{ font-size:7.3pt; font-style:italic; color:#aab3c4; text-align:center; line-height:1.14; margin-top:2px; }
  .node .nline{ border-bottom:1.4px dashed #C4CCDA; height:0; margin-top:10px; }
  .node .nline+.nline{ margin-top:12px; }
  .hub{ background:var(--navy-tint); border:3px solid #9aa6bd; border-radius:50%;
        align-items:center; justify-content:center; padding:0; }
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-style:italic; font-size:12pt; color:#97a2ba;
              letter-spacing:.01em; text-align:center; line-height:1.04; text-transform:uppercase; }
  .hub .hguides{ position:absolute; left:15%; right:15%; bottom:19%; }
  .hub .hguides .nline{ border-bottom:1.4px dashed #9aa6bd; height:0; margin-top:12px; }
"""

def _node(x, y, w, h, lab, sub):
    subhtml = f'<div class="nsub">{sub}</div>' if sub else ""
    return (f'<div class="node" style="left:{x}%; top:{y}%; width:{w}px; height:{h}px;">'
            f'<div class="nlab">{lab}</div>{subhtml}'
            f'<div class="nline"></div><div class="nline"></div></div>')

# four outer bubbles: (x%, y%, faded driver label, faded italic hint)
_outer = [
    (20, 19, "New Markets &amp; Raw Materials",
     "sell factory goods abroad &middot; secure rubber, oil &amp; sugar"),
    (80, 19, "Spreading Democratic &amp; Moral Ideals",
     "the <b>stated</b> goal &mdash; missionaries &amp; a claimed &lsquo;civilizing&rsquo; mission"),
    (20, 81, "Yellow Journalism &amp; Public Opinion",
     "Hearst &amp; Pulitzer&rsquo;s sensational stories stirred support"),
    (80, 81, "Naval Power",
     "Mahan, <i>The Influence of Sea Power upon History</i> (1890) &middot; bases &amp; coaling stations"),
]

_outer_html = "\n      ".join(_node(x, y, 232, 150, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub names the <b>outcome</b>. On each spoke, add <b>evidence</b> for a driver that pushed the U.S. to look outward &mdash; then draw links between drivers that reinforced each other.</div>
    <div class="canvas">
      <div class="web-wrap">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none">
          <g stroke="#C4CCDA" stroke-width="0.7">
            <line x1="50" y1="50" x2="20" y2="19"/>
            <line x1="50" y1="50" x2="80" y2="19"/>
            <line x1="50" y1="50" x2="20" y2="81"/>
            <line x1="50" y1="50" x2="80" y2="81"/>
          </g>
        </svg>
        {_outer_html}
        <div class="node hub" style="left:50%; top:50%; width:210px; height:158px;">
          <div class="hcue">American<br/>Imperialism</div>
          <div class="hguides"><div class="nline"></div><div class="nline"></div></div>
        </div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="20_us19_conceptweb",
    title="Why the U.S. Looked Outward",
    kicker="Unit 3 &middot; US.19 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("DOK 2 &middot; Causation", "skill")],
    why=("A concept web surfaces the several <b>drivers</b> that converged on one outcome &mdash; American "
         "imperialism &mdash; and makes their relationships visible at a glance. "
         "<span class='cite'>Mapping multiple causes onto a single effect is core causal reasoning "
         "(TN Social Studies Practice SSP.05).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Word bank on the board: <b>markets &amp; raw materials &middot; stated democratic/moral ideals &middot; yellow journalism &middot; naval power</b>. Fill one spoke together with a linking stem: &ldquo;This drove expansion because ___.&rdquo;",
        extend="<b>Rank</b> the four drivers &mdash; which mattered most in pushing the U.S. outward, and why? Defend it with one piece of evidence.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>draw</b> an icon in each bubble."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 3 &middot; US.19 (labeled)",
)]
