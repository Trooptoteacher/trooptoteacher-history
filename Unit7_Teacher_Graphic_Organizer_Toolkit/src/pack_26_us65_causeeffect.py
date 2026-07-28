# -*- coding: utf-8 -*-
"""Unit 7 labeled -- US.65 U.S.-Cuba Relations (cause & effect).
The roots of conflict feed the center EVENT (Cuba as a Cold War flashpoint 90 miles
away); four CONSEQUENCES -- Bay of Pigs, the Missile Crisis, the quarantine, the
nuclear brink -- flow out to the right. LIGHT wells with faded hints. Neutral
framing. No TN tie in source. Content approved for US.65.
"""

CSS = r"""
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
  .synth{ flex:0 0 auto; margin-top:8px; background:var(--cream); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          font-size:9pt; color:var(--navy); } .synth b{ color:var(--navy); }
"""

def _cause_box(label):
    return (f'<div class="cebox"><div class="band navy sm">{label}</div>'
            f'<div class="well navy lines"></div></div>')

def _effect_box(label):
    return (f'<div class="cebox red"><div class="band red sm">{label}</div>'
            f'<div class="well red lines"></div></div>')

_causes = [
    "The U.S. had dominated Cuba since 1898 &amp; backed dictator Batista",
    "<b>Castro&rsquo;s 1959 revolution</b> &mdash; then communism &amp; nationalization",
    "Castro allies with the <b>USSR</b> &mdash; a communist state 90 miles from Florida",
]
_effects = [
    "<b>Bay of Pigs</b> <span class=\"yr\">(1961)</span>: CIA&#8209;backed exile invasion fails",
    "Failure pushes Castro closer to Moscow for protection",
    "<b>Cuban Missile Crisis</b> <span class=\"yr\">(Oct. 1962)</span>: Soviet missiles &mdash; 13 days on the brink",
    "Kennedy&rsquo;s naval quarantine &rarr; Soviet withdrawal (a secret Turkey deal)",
]

_causes_html = "\n            ".join(_cause_box(c) for c in _causes)
_effects_html = "\n            ".join(_effect_box(e) for e in _effects)

BODY = f"""
    <div class="prompt">The <b>roots</b> of conflict sit on the <b>left</b>; four <b>consequences</b> flow out on the <b>right</b>. Arrows show the chain: <b>roots &rarr; flashpoint &rarr; crises</b> &mdash; ending at the closest brush with nuclear war.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Causes &middot; roots of conflict</div>
          <div class="ce-stack">
            {_causes_html}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The flashpoint</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">CUBA: A COLD WAR FLASHPOINT<br><span class="yr">90 miles from Florida</span></div>
            <div class="well lines cream"><span class="cue" style="position:absolute;top:7px;left:11px;right:11px;">A communist ally of the USSR on America&rsquo;s doorstep &mdash; describe why that alarmed the U.S.</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Consequences &middot; two crises</div>
          <div class="ce-stack">
            {_effects_html}
          </div>
        </div>
      </div>
      <div class="synth"><b>Your call &mdash;</b> The world came closer to nuclear war in October 1962 than ever before or since. What made it end <b>peacefully</b>? ____________________________</div>
    </div>
"""

ORGANIZERS = [dict(
    slug="26_us65_causeeffect",
    title="Ninety Miles from War: The U.S. &amp; Cuba",
    kicker="Unit 7 &middot; US.65 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("DOK 2&#8211;3 &middot; Causation", "skill")],
    why=("Reading it as <b>roots &rarr; flashpoint &rarr; crises</b> shows how a revolution 90 miles away led, step by step, "
         "to the most dangerous standoff of the Cold War. "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the center flashpoint box first. Then order the right side: which crisis came first, and how did it lead to the next?",
        extend="Both leaders <b>and</b> luck helped avoid nuclear war. Argue which mattered more, using the chain.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>map</b> Cuba, Florida, and the Soviet missile threat."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 7 &middot; US.65 (labeled)",
)]
