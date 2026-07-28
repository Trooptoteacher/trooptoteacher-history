# -*- coding: utf-8 -*-
"""Unit 6 labeled -- US.56 Manhattan Project & the Atomic Bomb (cause & effect).
The secret project (Oak Ridge and the other sites) feeds the center EVENT (the
atomic bomb); the effects include Japan's surrender and the stated rationale, with
a neutral note acknowledging the human cost and the ongoing debate. LIGHT wells
with faded hints. HAS a strong Tennessee Connection (Oak Ridge). Approved US.56.
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
  .ce-center .band{ font-size:10.4pt; padding:8px; border-radius:7px 7px 0 0; line-height:1.12; }
  .ce-center .band .yr{ color:var(--gold); font-weight:800; }
  .ce-center .well{ flex:1 1 0; }
  .ce-center .cue{ color:#aab3c4; font-style:italic; text-transform:none; letter-spacing:0;
                   font-weight:600; font-size:8pt; }
  .note{ flex:0 0 auto; margin-top:8px; background:var(--navy-tint); border:1.5px solid #b9c3d6;
         border-left:6px solid var(--navy); border-radius:0 6px 6px 0; padding:6px 11px;
         font-size:8.2pt; color:#2c3446; line-height:1.3; } .note b{ color:var(--navy); }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.6pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

def _cause_box(label):
    return (f'<div class="cebox"><div class="band navy sm">{label}</div>'
            f'<div class="well navy lines"></div></div>')

def _effect_box(label):
    return (f'<div class="cebox red"><div class="band red sm">{label}</div>'
            f'<div class="well red lines"></div></div>')

_causes = [
    "<b>Oak Ridge, TN</b> &mdash; the &ldquo;Secret City&rdquo;: TVA power &amp; secrecy enrich uranium",
    "A secret multi&#8209;site program: Los Alamos, Oak Ridge &amp; Hanford; Groves &amp; Oppenheimer",
    "The <b>Trinity test</b> <span class=\"yr\">(July 16, 1945)</span> proves the bomb works",
]
_effects = [
    "Japan surrenders &mdash; <b>World War II ends</b>",
    "<b>Rationale:</b> avoid a costly invasion (feared huge casualties)",
    "<b>Rationale:</b> force a rapid surrender; signal U.S. power to the USSR",
    "The <b>atomic age</b> begins &mdash; opening the Cold War",
]

_causes_html = "\n            ".join(_cause_box(c) for c in _causes)
_effects_html = "\n            ".join(_effect_box(e) for e in _effects)

BODY = f"""
    <div class="prompt">The secret <b>project</b> sits on the <b>left</b>; the <b>outcomes and the rationale</b> flow out on the <b>right</b>. Arrows show the chain: <b>project &rarr; the bomb &rarr; the war ends</b>. Then weigh the decision.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Causes &middot; the Manhattan Project</div>
          <div class="ce-stack">
            {_causes_html}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The event</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">THE ATOMIC BOMB<br>Hiroshima &amp; Nagasaki, <span class="yr">Aug. 1945</span></div>
            <div class="well lines cream"><span class="cue" style="position:absolute;top:7px;left:11px;right:11px;">Truman authorized the bomb to end the war quickly &mdash; describe the decision</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Effects &middot; outcome &amp; rationale</div>
          <div class="ce-stack">
            {_effects_html}
          </div>
        </div>
      </div>
      <div class="note"><b>The decision, then and now.</b> The bombings ended the war but caused enormous civilian loss of
      life, and historians still <b>debate</b> whether they were necessary. A good answer explains the rationale <i>and</i>
      weighs the cost.</div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> <b>Oak Ridge, Tennessee</b> &mdash; the &ldquo;Secret City&rdquo; &mdash; was a central
        Manhattan Project site. Built from scratch in 1942 and shown on <b>no maps</b>, it employed over <b>75,000 workers</b>
        enriching the uranium for the bomb, making Tennessee crucial to the atomic age.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="31_us56_causeeffect",
    title="The Secret City &amp; the Bomb That Ended the War",
    kicker="Unit 6 &middot; US.56 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 3 &middot; Causation", "skill")],
    why=("Reading it as <b>project &rarr; bomb &rarr; surrender</b> lets students explain the rationale for using the atomic "
         "bomb while weighing its cost &mdash; and see Tennessee&rsquo;s central role. "
         "<span class='cite'>Analyzing cause &amp; effect and weighing a decision are TN Social Studies Practices (SSP.05, SSP.04).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the center box first. Then sort the right side into <b>what happened</b> vs. the <b>reasons given</b>.",
        extend="Weigh it: explain the rationale for the bomb, then give the strongest reason someone might disagree.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>diagram</b> the project&#8209;to&#8209;surrender chain."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 6 &middot; US.56 (labeled)",
)]
