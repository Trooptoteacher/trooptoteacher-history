# -*- coding: utf-8 -*-
"""Unit 3 labeled -- US.21 Spanish-American War & Outcomes (cause & effect).
Three CAUSES feed a center EVENT (Spanish-American War, 1898); four OUTCOMES flow
out to the right. Every writable field is a LIGHT well with a faded italic hint.
Neutral framing: outcomes are named as facts (annexation, territories acquired,
Cuba & the Roosevelt Corollary, the Philippine Insurrection) -- none is called a
win/loss or progress; students judge significance on their own. HAS a Tennessee
Connection: rendered as a gold "Tennessee Connection" chip in the header (chips
list) plus a gold callout box in the body, matching the Unit 2 labeled packs.
Content approved for US.21.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .ce-grid{ flex:1 1 auto; display:flex; align-items:stretch; gap:5px; min-height:0; }
  .ce-col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .ce-colhead{ font-size:8.6pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase;
               text-align:center; margin-bottom:5px; flex:0 0 auto; }
  .ce-stack{ flex:1 1 auto; display:flex; flex-direction:column; gap:9px; min-height:0; }
  .cebox{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .cebox .band{ border-radius:6px 6px 0 0; font-size:8.6pt; padding:5px 8px; line-height:1.18; }
  .cebox .band .yr{ color:var(--gold); font-weight:800; }
  .cebox.red .band .yr{ color:#f6d9a6; }
  .cebox .well{ flex:1 1 0; }
  .ce-arrs{ flex:0 0 24px; display:flex; flex-direction:column; justify-content:space-around;
            align-items:center; padding:22px 0; }
  .ce-arrs .arr-r{ border-left-width:16px; border-top-width:11px; border-bottom-width:11px; }
  .ce-arrs.out .arr-r{ border-left-color:var(--red); }
  .ce-center{ flex:1.24 1 0; display:flex; flex-direction:column; justify-content:center; min-height:0; }
  .ce-center .band{ font-size:11.5pt; padding:8px; border-radius:7px 7px 0 0; line-height:1.12; }
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
    "Cuban struggle for independence from Spain",
    "Yellow journalism &mdash; Hearst &amp; Pulitzer",
    "Explosion of the USS <i>Maine</i> <span class=\"yr\">(1898)</span>",
]
_effects = [
    "U.S. annexes Hawaii <span class=\"yr\">(1898)</span>",
    "U.S. gains Puerto Rico, Guam &amp; the Philippines",
    "Cuba &amp; the Roosevelt Corollary",
    "Philippine Insurrection &mdash; Emilio Aguinaldo",
]

_causes_html = "\n            ".join(_cause_box(c) for c in _causes)
_effects_html = "\n            ".join(_effect_box(e) for e in _effects)

BODY = f"""
    <div class="prompt">Three <b>causes</b> pushed toward war on the <b>left</b>; four <b>outcomes</b> flowed out on the <b>right</b>. Arrows show the chain: <b>causes &rarr; event &rarr; effects</b>.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Causes &middot; what led to war</div>
          <div class="ce-stack">
            {_causes_html}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The event</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">SPANISH&#8209;AMERICAN WAR, <span class="yr">1898</span></div>
            <div class="well lines cream"><span class="cue" style="position:absolute;top:7px;left:11px;right:11px;">Describe the conflict between the U.S. and Spain</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Outcomes &middot; a new American empire</div>
          <div class="ce-stack">
            {_effects_html}
          </div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee &mdash; the <b>&ldquo;Volunteer State&rdquo;</b> &mdash; sent
        thousands of volunteers to the <b>Spanish-American War of 1898</b>. Tennessee regiments served, continuing
        the state&rsquo;s volunteer tradition.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="22_us21_causeeffect",
    title="The Spanish&#8209;American War &amp; a New American Empire",
    kicker="Unit 3 &middot; US.21 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Causation", "skill")],
    why=("Laying the chain out as <b>cause &rarr; event &rarr; effect</b> makes visible how the war of 1898 grew "
         "from Cuban independence, the press, and the <i>Maine</i> &mdash; and reshaped America&rsquo;s role in the world. "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Word bank of the three causes: <b>Cuban independence &middot; yellow journalism &middot; USS <i>Maine</i></b>. Ask: which cause was the <b>spark</b>? Fill the event box first.",
        extend="Which <b>outcome</b> most changed America&rsquo;s role in the world? Defend your choice with evidence from the chain.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>map</b> the new territories the U.S. acquired."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 3 &middot; US.21 (labeled)",
)]
