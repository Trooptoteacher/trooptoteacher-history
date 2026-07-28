# -*- coding: utf-8 -*-
"""Unit 4 labeled -- US.32 Henry Ford, the Automobile & Mass Production (cause & effect).
Three INNOVATIONS feed the center EVENT (the mass-produced automobile); four EFFECTS
flow out to the right. Every writable field is a LIGHT well with a faded italic hint.
Neutral framing: effects named as facts (mobility, spillover industries, changed
work) -- both benefits and costs shown; students judge overall. HAS a Tennessee
Connection (gold chip + gold callout). Content approved for US.32.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .ce-grid{ flex:1 1 auto; display:flex; align-items:stretch; gap:5px; min-height:0; }
  .ce-col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .ce-colhead{ font-size:8.6pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase;
               text-align:center; margin-bottom:5px; flex:0 0 auto; }
  .ce-stack{ flex:1 1 auto; display:flex; flex-direction:column; gap:9px; min-height:0; }
  .cebox{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .cebox .band{ border-radius:6px 6px 0 0; font-size:8.4pt; padding:5px 8px; line-height:1.16; }
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
    "Model T &ldquo;Tin Lizzie&rdquo; <span class=\"yr\">(1908&ndash;1927)</span> &mdash; a car for average Americans",
    "The moving <b>assembly line</b> <span class=\"yr\">(1913)</span> &mdash; 12 hours &rarr; 93 minutes per car",
    "The <b>$5 Day</b> <span class=\"yr\">(1914)</span> &amp; the 8&#8209;hour workday",
]
_effects = [
    "Price $825 (1908) &rarr; $290 (1925); 15&nbsp;million built by 1927",
    "Personal mobility &mdash; ended rural isolation, enabled suburbs",
    "Boom in steel, rubber, glass, oil &amp; road&#8209;building",
    "Turnover cut 370%&rarr;16%; but repetitive work &amp; resistance to unions",
]

_causes_html = "\n            ".join(_cause_box(c) for c in _causes)
_effects_html = "\n            ".join(_effect_box(e) for e in _effects)

BODY = f"""
    <div class="prompt">Three <b>innovations</b> sit on the <b>left</b>; four <b>effects</b> on the economy and society flow out on the <b>right</b>. Arrows show the chain: <b>innovation &rarr; the car &rarr; effects</b>.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Innovations &middot; how Ford built it</div>
          <div class="ce-stack">
            {_causes_html}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The event</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">THE MASS&#8209;PRODUCED AUTOMOBILE</div>
            <div class="well lines cream"><span class="cue" style="position:absolute;top:7px;left:11px;right:11px;">By 1927 Ford controlled ~50% of the U.S. auto market &mdash; describe what mass production made possible</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Effects &middot; on economy &amp; society</div>
          <div class="ce-stack">
            {_effects_html}
          </div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> The automobile transformed Tennessee: 1920s <b>road&#8209;building</b>
        connected the state&rsquo;s cities, the <b>Dixie Highway</b> linked Tennessee to Florida tourism, and
        <b>Nashville and Memphis</b> became automobile distribution centers as rural Tennesseans reached urban markets.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="24_us32_causeeffect",
    title="How the Assembly Line Remade America",
    kicker="Unit 4 &middot; US.32 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Causation", "skill")],
    why=("Laying the chain out as <b>innovation &rarr; the car &rarr; effect</b> makes visible how a single manufacturing "
         "idea reshaped work, cities, and daily life &mdash; for better and worse. "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Word bank of the three innovations: <b>Model&nbsp;T &middot; assembly line &middot; $5&nbsp;Day</b>. Fill the center box first.",
        extend="Weigh it: were Ford&rsquo;s effects <b>more positive or negative</b> overall? Defend your call with evidence from the chain.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>diagram</b> how one car connected many industries."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 4 &middot; US.32 (labeled)",
)]
