# -*- coding: utf-8 -*-
"""Unit 5 labeled -- US.40 The Dust Bowl (cause & effect).
Three CAUSES (over-plowing, farming practices, drought) feed the center EVENT
(the Dust Bowl); three IMPACTS -- social, geographic, economic -- flow out to the
right, matching the standard's three impact dimensions. LIGHT wells with faded
italic hints. Neutral framing: human choices + nature, stated as facts. HAS a
Tennessee Connection (TVA). Content approved for US.40.
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
  .ce-center .band{ font-size:11pt; padding:8px; border-radius:7px 7px 0 0; line-height:1.12; }
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
    "Plowing up native prairie grasses that held the soil",
    "WWI wheat boom + tractors &rarr; monoculture, no crop rotation",
    "Severe <b>drought</b> <span class=\"yr\">(1931&ndash;1939)</span> &mdash; 40% below normal rain",
]
_effects = [
    "<b>Social:</b> 3.5M leave; &ldquo;Okies&rdquo; take Route 66 to California; families split",
    "<b>Geographic:</b> 75% of topsoil blown away; &ldquo;black blizzards&rdquo; across 100M acres",
    "<b>Economic:</b> wheat down 40%; cattle die; banks foreclose on farms",
]

_causes_html = "\n            ".join(_cause_box(c) for c in _causes)
_effects_html = "\n            ".join(_effect_box(e) for e in _effects)

BODY = f"""
    <div class="prompt">Human choices <b>and</b> nature sit on the <b>left</b>; three kinds of <b>impact</b> flow out on the <b>right</b>. Arrows show the chain: <b>causes &rarr; the Dust Bowl &rarr; impacts</b>.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Causes &middot; choices &amp; nature</div>
          <div class="ce-stack">
            {_causes_html}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The event</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">THE DUST BOWL, <span class="yr">1931&ndash;1939</span></div>
            <div class="well lines cream"><span class="cue" style="position:absolute;top:7px;left:11px;right:11px;">Dust storms ruined the Southern Great Plains &mdash; TX, OK, KS, CO &amp; NM. Describe it in your words</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Impacts &middot; social &middot; geographic &middot; economic</div>
          <div class="ce-stack">
            {_effects_html}
          </div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee lay outside the Dust Bowl&rsquo;s core, but the state
        faced severe <b>soil erosion</b> in the 1930s. The <b>Tennessee Valley Authority (TVA)</b>, created in
        1933, answered with <b>reforestation, soil conservation, and flood control</b> across the Tennessee River
        watershed.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="21_us40_causeeffect",
    title="The Dust Bowl: Choices, Drought &amp; Consequences",
    kicker="Unit 5 &middot; US.40 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Causation", "skill")],
    why=("Laying it out as <b>causes &rarr; event &rarr; impacts</b> shows how farming choices and a natural drought "
         "together turned the Plains to dust &mdash; and sorts the fallout into social, geographic, and economic. "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the center event box first. Then ask of each cause: was it a <b>human choice</b> or <b>nature</b>?",
        extend="Could the Dust Bowl have been prevented? Use the causes to argue which choices mattered most.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>map</b> the Dust Bowl states and the Route 66 migration."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 5 &middot; US.40 (labeled)",
)]
