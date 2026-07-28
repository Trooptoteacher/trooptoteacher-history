# -*- coding: utf-8 -*-
"""Unit 10 labeled -- US.87 The Emergence of Environmentalism (cause & effect).
The factors that sparked awareness (left) feed the center EVENT (the environmental
movement); its effects (right) -- the EPA, new laws, Superfund -- flow out. LIGHT
wells with faded hints. HAS a Tennessee Connection. Content approved for US.87.
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
  .ce-center .band{ font-size:10pt; padding:8px; border-radius:7px 7px 0 0; line-height:1.1; }
  .ce-center .band .yr{ color:var(--gold); font-weight:800; }
  .ce-center .well{ flex:1 1 0; }
  .ce-center .cue{ color:#aab3c4; font-style:italic; text-transform:none; letter-spacing:0;
                   font-weight:600; font-size:8pt; }
  .tnbox{ flex:0 0 auto; margin-top:8px; background:var(--gold-tint); border:1.6px solid var(--gold);
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
    "Rachel Carson&rsquo;s <b>Silent Spring</b> <span class=\"yr\">1962</span> exposes pesticide dangers",
    "Visible pollution &mdash; smog, contaminated rivers, oil spills",
    "<b>Earth Day 1970</b> &amp; a growing science of ecology raise public alarm",
]
_effects = [
    "The <b>EPA</b> is created <span class=\"yr\">1970</span> &mdash; sets &amp; enforces pollution standards",
    "New federal laws regulate air, water &amp; toxic substances",
    "<b>Love Canal</b> &mdash; a toxic&#8209;waste neighborhood &mdash; leads to the <b>Superfund</b> cleanup program",
    "<b>Three Mile Island</b> (1979) raises fears about nuclear safety",
]

_causes_html = "\n            ".join(_cause_box(c) for c in _causes)
_effects_html = "\n            ".join(_effect_box(e) for e in _effects)

BODY = f"""
    <div class="prompt">The factors that sparked awareness sit on the <b>left</b>; the movement&rsquo;s <b>effects</b> flow out on the <b>right</b>. Arrows show the chain: <b>warning signs &rarr; a movement &rarr; new protections</b>.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Causes &middot; what sparked it</div>
          <div class="ce-stack">
            {_causes_html}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The movement</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">THE ENVIRONMENTAL MOVEMENT</div>
            <div class="well lines cream"><span class="cue" style="position:absolute;top:7px;left:11px;right:11px;">Americans demand that the government protect air, water &amp; land &mdash; describe how public concern became national policy</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Effects &middot; new protections</div>
          <div class="ce-stack">
            {_effects_html}
          </div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee sat at the center of the debate: the <b>Tellico Dam</b>
        controversy pitted the TVA against efforts to protect the endangered <b>snail darter</b>, producing the landmark
        Supreme Court case <b><i>TVA v. Hill</i></b> (1978) &mdash; a defining moment for the Endangered Species Act.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="24_us87_causeeffect",
    title="The Birth of the Environmental Movement",
    kicker="Unit 10 &middot; US.87 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Causation", "skill")],
    why=("Reading it as <b>warning signs &rarr; movement &rarr; new laws</b> shows how public alarm turned into a permanent "
         "federal role in protecting the environment. "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the center box first. Then connect one cause at a time: &ldquo;Because people saw ___, they demanded ___.&rdquo;",
        extend="Was the EPA an overreach or a necessary protection? Use the causes and effects to argue.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>design</b> an Earth Day 1970 poster."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 10 &middot; US.87 (labeled)",
)]
