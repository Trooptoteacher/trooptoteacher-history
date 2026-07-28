# -*- coding: utf-8 -*-
"""Unit 8 labeled -- US.74 The Automobile's Growing Influence (cause & effect).
What made the car central feeds the center EVENT (the car reshapes American life);
four EFFECTS -- suburbs, fast food, motels, and a car-centered daily life -- flow
out to the right. LIGHT wells with faded hints. HAS a Tennessee Connection.
Content approved for US.74.
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
    "Personal <b>mobility</b> &mdash; live, work, shop &amp; travel across wider areas",
    "Interstate highways make long <b>commutes</b> practical",
    "Owning a car becomes a symbol of freedom &amp; prosperity",
]
_effects = [
    "The <b>suburban boom</b> &mdash; Levittown built around cars; driveways &amp; garages",
    "<b>Fast food</b> is born &mdash; drive&#8209;ins; McDonald&rsquo;s franchised <span class=\"yr\">1955</span>",
    "<b>Motels</b> replace hotels along highways; travel industries grow",
    "Drive&#8209;ins, shopping centers &amp; car&#8209;dependent suburbs reshape daily life",
]

_causes_html = "\n            ".join(_cause_box(c) for c in _causes)
_effects_html = "\n            ".join(_effect_box(e) for e in _effects)

BODY = f"""
    <div class="prompt">What made the car <b>central</b> sits on the <b>left</b>; four <b>effects</b> flow out on the <b>right</b>. Arrows show the chain: <b>mobility &rarr; the car &rarr; a new way of life</b>.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Causes &middot; why cars took over</div>
          <div class="ce-stack">
            {_causes_html}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The event</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">THE CAR RESHAPES AMERICAN LIFE</div>
            <div class="well lines cream"><span class="cue" style="position:absolute;top:7px;left:11px;right:11px;">The automobile moved from luxury to necessity &mdash; describe how it changed where and how Americans lived</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Effects &middot; a car&#8209;built America</div>
          <div class="ce-stack">
            {_effects_html}
          </div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> The car transformed Tennessee: <b>Interstate 40</b> (east&ndash;west across
        the whole state) and <b>Interstate 65</b> through Nashville reshaped the state&rsquo;s geography &mdash; enabling suburban
        sprawl and roadside businesses even as downtown commercial districts declined.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="23_us74_causeeffect",
    title="How the Car Rebuilt America",
    kicker="Unit 8 &middot; US.74 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Causation", "skill")],
    why=("Reading it as <b>mobility &rarr; the car &rarr; effects</b> shows how one machine reshaped where Americans lived, "
         "how they ate, and how they traveled. "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the center event box first. Then connect each effect to the car: &ldquo;Because everyone drove, ___.&rdquo;",
        extend="Which effect of the car most changed America &mdash; and did it help or hurt communities? Defend your answer.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>design</b> a 1950s roadside sign (drive&#8209;in, motel, or diner)."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 8 &middot; US.74 (labeled)",
)]
