# -*- coding: utf-8 -*-
"""Unit 6 labeled -- US.52 Women in World War II (cause & effect).
A wartime labor shortage feeds the center EVENT (women entering the workforce &
armed forces); four EFFECTS -- gains and limits -- flow out to the right. LIGHT
wells with faded italic hints. Neutral framing: gains and limits both shown. HAS a
Tennessee Connection (Oak Ridge). Content approved for US.52.
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
  .ce-center .band{ font-size:10.2pt; padding:8px; border-radius:7px 7px 0 0; line-height:1.12; }
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
    "16 million men in the armed forces &rarr; a massive labor shortage",
    "War production had to <b>double</b> the manufacturing workforce",
    "&ldquo;Rosie the Riveter&rdquo; campaigns + economic necessity recruited women",
]
_effects = [
    "Built bombers, Liberty ships &amp; ammunition &mdash; record production",
    "Gained independence, technical skills &amp; military roles (WAC, WAVES)",
    "But faced lower pay (~65% of men&rsquo;s), scarce childcare &amp; criticism",
    "Shifted expectations &mdash; setting the stage for later change",
]

_causes_html = "\n            ".join(_cause_box(c) for c in _causes)
_effects_html = "\n            ".join(_effect_box(e) for e in _effects)

BODY = f"""
    <div class="prompt">The wartime <b>labor shortage</b> sits on the <b>left</b>; four <b>effects</b> &mdash; gains and limits &mdash; flow out on the <b>right</b>. Arrows show the chain: <b>need &rarr; women step in &rarr; impact</b>.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Causes &middot; why women were needed</div>
          <div class="ce-stack">
            {_causes_html}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The change</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">WOMEN ENTER THE WORKFORCE &amp; ARMED FORCES</div>
            <div class="well lines cream"><span class="cue" style="position:absolute;top:7px;left:11px;right:11px;">12M (1940) &rarr; 20M (1945); 36% of civilian workers; 65% of aircraft workers. Describe the shift</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Effects &middot; gains &amp; limits</div>
          <div class="ce-stack">
            {_effects_html}
          </div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee women entered the workforce in unprecedented numbers. At
        <b>Oak Ridge</b>, women made up a large share of the workforce &mdash; many operating <b>calutrons to enrich uranium</b>
        without knowing the full nature of their work &mdash; while others served in the WAC, WAVES, and as nurses overseas.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="27_us52_causeeffect",
    title="When the Nation Needed Them: Women in WWII",
    kicker="Unit 6 &middot; US.52 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Causation", "skill")],
    why=("Reading it as <b>need &rarr; women step in &rarr; impact</b> shows how a labor shortage opened doors &mdash; and how "
         "the gains came alongside real limits that outlasted the war. "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the center change box first. Then sort the right&#8209;side boxes into <b>gains</b> and <b>limits</b>.",
        extend="Did WWII <b>permanently</b> change women&rsquo;s place in the workforce, or was it temporary? Use the effects to argue.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>diagram</b> how wartime need reshaped women&rsquo;s work."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 6 &middot; US.52 (labeled)",
)]
