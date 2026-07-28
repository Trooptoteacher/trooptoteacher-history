# -*- coding: utf-8 -*-
"""Unit 5 labeled -- US.42 Herbert Hoover's Response (cause & effect).
Hoover's philosophy and the steps it allowed feed the center EVENT (his limited
response); four RESULTS -- including the Bonus Army fallout -- flow out to the
right. LIGHT wells with faded italic hints. Neutral framing: philosophy and steps
described factually; students judge whether it was enough. HAS a Tennessee
Connection (TN swings to FDR, 1932). Content approved for US.42.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .ce-grid{ flex:1 1 auto; display:flex; align-items:stretch; gap:5px; min-height:0; }
  .ce-col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .ce-colhead{ font-size:8.6pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase;
               text-align:center; margin-bottom:5px; flex:0 0 auto; }
  .ce-stack{ flex:1 1 auto; display:flex; flex-direction:column; gap:9px; min-height:0; }
  .cebox{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .cebox .band{ border-radius:6px 6px 0 0; font-size:8.3pt; padding:5px 8px; line-height:1.15; }
  .cebox .band .yr{ color:var(--gold); font-weight:800; }
  .cebox.red .band .yr{ color:#f6d9a6; }
  .cebox .well{ flex:1 1 0; }
  .ce-arrs{ flex:0 0 24px; display:flex; flex-direction:column; justify-content:space-around;
            align-items:center; padding:22px 0; }
  .ce-arrs .arr-r{ border-left-width:16px; border-top-width:11px; border-bottom-width:11px; }
  .ce-arrs.out .arr-r{ border-left-color:var(--red); }
  .ce-center{ flex:1.24 1 0; display:flex; flex-direction:column; justify-content:center; min-height:0; }
  .ce-center .band{ font-size:10.6pt; padding:8px; border-radius:7px 7px 0 0; line-height:1.12; }
  .ce-center .band .yr{ color:var(--gold); font-weight:800; }
  .ce-center .well{ flex:1 1 0; }
  .ce-center .cue{ color:#aab3c4; font-style:italic; text-transform:none; letter-spacing:0;
                   font-weight:600; font-size:8pt; }
  .tnbox{ flex:0 0 auto; margin-top:8px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.7pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

def _cause_box(label):
    return (f'<div class="cebox"><div class="band navy sm">{label}</div>'
            f'<div class="well navy lines"></div></div>')

def _effect_box(label):
    return (f'<div class="cebox red"><div class="band red sm">{label}</div>'
            f'<div class="well red lines"></div></div>')

_causes = [
    "<b>Rugged Individualism</b> &mdash; people solve their own problems; direct federal relief seen as unconstitutional",
    "<b>Public works</b> &mdash; Boulder (Hoover) Dam; Emergency Relief &amp; Construction Act <span class=\"yr\">(1932)</span>",
    "<b>RFC</b> <span class=\"yr\">(1932)</span> &mdash; $2B in loans to banks &amp; businesses (&ldquo;trickle&#8209;down&rdquo;)",
]
_effects = [
    "Too small &amp; too slow to dent 25% unemployment",
    "RFC criticized as helping the wealthy, not common people",
    "<b>Bonus Army</b> (1932): 17,000 WWI vets evicted by the Army &rarr; outrage",
    "Voters turn to <b>Franklin D. Roosevelt</b> in the 1932 election",
]

_causes_html = "\n            ".join(_cause_box(c) for c in _causes)
_effects_html = "\n            ".join(_effect_box(e) for e in _effects)

BODY = f"""
    <div class="prompt">Hoover&rsquo;s <b>philosophy &amp; steps</b> sit on the <b>left</b>; the <b>results</b> flow out on the <b>right</b>. Arrows show the chain: <b>belief &rarr; response &rarr; results</b>. Then judge: was it enough?</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">His philosophy &amp; steps</div>
          <div class="ce-stack">
            {_causes_html}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">His response</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">HOOVER&rsquo;S RESPONSE, <span class="yr">1929&ndash;1933</span></div>
            <div class="well lines cream"><span class="cue" style="position:absolute;top:7px;left:11px;right:11px;">Limited, voluntary federal action &mdash; describe how Hoover chose to respond to the Depression</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Results &middot; was it enough?</div>
          <div class="ce-stack">
            {_effects_html}
          </div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Hoover&rsquo;s limited response was felt acutely in Tennessee, where
        the collapse of Nashville&rsquo;s largest bank had already devastated the state&rsquo;s finances. Tennesseans
        <b>overwhelmingly supported Franklin Roosevelt in the 1932 election</b>, seeking more aggressive federal help.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="23_us42_causeeffect",
    title="Hoover&rsquo;s Response: Belief, Action &amp; Backlash",
    kicker="Unit 5 &middot; US.42 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Causation", "skill")],
    why=("Reading it as <b>belief &rarr; response &rarr; results</b> shows how Hoover&rsquo;s philosophy shaped a limited "
         "response &mdash; and how the Bonus Army episode helped end his presidency. "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Define <b>Rugged Individualism</b> together first, then trace how that belief shaped each step and result.",
        extend="Evaluate: how did the <b>Bonus Army</b> response damage Hoover? Use the chain to defend your answer.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>diagram</b> how one belief led to the 1932 result."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 5 &middot; US.42 (labeled)",
)]
