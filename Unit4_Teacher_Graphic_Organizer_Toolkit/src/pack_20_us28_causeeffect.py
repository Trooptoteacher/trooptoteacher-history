# -*- coding: utf-8 -*-
"""Unit 4 labeled -- US.28 The Great Migration (cause & effect).
Push & pull forces feed the center EVENT (the Great Migration); four IMPACTS flow
out to the right. Every writable field is a LIGHT well with a faded italic hint.
Neutral framing: impacts named as facts (population shifts, new communities, new
tensions) -- none called a win/loss or progress; students judge significance.
HAS a Tennessee Connection (gold chip + gold callout). Content approved for US.28.
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
    "<b>Push</b> &middot; Jim Crow segregation, disenfranchisement &amp; racial violence",
    "<b>Push</b> &middot; sharecropping poverty &amp; the boll weevil&rsquo;s damage to cotton",
    "<b>Pull</b> &middot; WWI factory jobs at higher wages &mdash; ~$1,000/yr North vs. ~$300 South",
]
_effects = [
    "Chicago, Detroit &amp; New York grow; new Black neighborhoods &amp; businesses form",
    "New access to voting &amp; political participation in the North",
    "A flowering of culture &mdash; the Harlem Renaissance",
    "The South loses working&#8209;age population; new racial tensions rise in Northern cities",
]

_causes_html = "\n            ".join(_cause_box(c) for c in _causes)
_effects_html = "\n            ".join(_effect_box(e) for e in _effects)

BODY = f"""
    <div class="prompt">Forces that <b>pushed</b> people out of the South and <b>pulled</b> them North sit on the <b>left</b>; four <b>impacts</b> flow out on the <b>right</b>. Arrows show the chain: <b>causes &rarr; movement &rarr; effects</b>.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Causes &middot; push &amp; pull factors</div>
          <div class="ce-stack">
            {_causes_html}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The movement</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">THE GREAT MIGRATION, <span class="yr">1916&ndash;1970</span></div>
            <div class="well lines cream"><span class="cue" style="position:absolute;top:7px;left:11px;right:11px;">~6 million African Americans move from the rural South to Northern &amp; Midwestern cities &mdash; describe it in your words</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Impacts &middot; on North &amp; South</div>
          <div class="ce-stack">
            {_effects_html}
          </div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> <b>Memphis</b> and <b>Nashville</b> were key departure points for
        the Great Migration. Tennessee&rsquo;s Black communities &mdash; especially in <b>West Tennessee</b> &mdash; shifted
        in large numbers to cities like Chicago, Detroit, and St.&nbsp;Louis.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="20_us28_causeeffect",
    title="Why the Great Migration Reshaped America",
    kicker="Unit 4 &middot; US.28 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Causation", "skill")],
    why=("Laying it out as <b>push/pull &rarr; movement &rarr; impact</b> makes visible how millions of decisions to "
         "leave the South reshaped both the region people left and the cities they built. "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Sort a word bank into <b>push</b> (reasons to leave) vs. <b>pull</b> (reasons to go). Fill the center movement box first.",
        extend="Which impact mattered most &mdash; to the North, or to the South? Defend your choice with evidence from the chain.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>map</b> the routes people traveled north."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 4 &middot; US.28 (labeled)",
)]
