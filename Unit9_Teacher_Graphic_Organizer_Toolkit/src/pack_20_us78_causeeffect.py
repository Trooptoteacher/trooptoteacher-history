# -*- coding: utf-8 -*-
"""Unit 9 labeled -- US.78 Brown v. Board of Education (cause & effect).
The context that produced the case (left) feeds the center EVENT (the 1954 ruling);
its effects on desegregation (right) flow out. LIGHT wells with faded hints.
Factual, dignified framing. HAS a Tennessee Connection. Content approved for US.78.
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
  .tnbox .t{ font-size:8.7pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

def _cause_box(label):
    return (f'<div class="cebox"><div class="band navy sm">{label}</div>'
            f'<div class="well navy lines"></div></div>')

def _effect_box(label):
    return (f'<div class="cebox red"><div class="band red sm">{label}</div>'
            f'<div class="well red lines"></div></div>')

_causes = [
    "&ldquo;Separate but equal&rdquo; set by <b>Plessy v. Ferguson</b> <span class=\"yr\">1896</span>",
    "The <b>NAACP</b>&rsquo;s legal strategy (Thurgood Marshall); <b>Sweatt v. Painter</b> (1950) weakens the doctrine",
    "Kenneth Clark&rsquo;s <b>doll tests</b> show segregation&rsquo;s harm to Black children",
]
_effects = [
    "Legally <b>ends school segregation</b> &mdash; a foundation for the whole movement",
    "<b>Brown II</b> (1955): &ldquo;all deliberate speed&rdquo; &rarr; slow, uneven change",
    "<b>Massive resistance</b> &mdash; private academies, closed schools; by 1964 only <b>2%</b> of Black Southern students in integrated schools",
]

_causes_html = "\n            ".join(_cause_box(c) for c in _causes)
_effects_html = "\n            ".join(_effect_box(e) for e in _effects)

BODY = f"""
    <div class="prompt">The context that produced the case sits on the <b>left</b>; its <b>effects</b> on desegregation flow out on the <b>right</b>. Arrows show the chain: <b>context &rarr; the ruling &rarr; impact</b>.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Context &middot; what led to the case</div>
          <div class="ce-stack">
            {_causes_html}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The decision</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">BROWN v. BOARD OF EDUCATION, <span class="yr">1954</span></div>
            <div class="well lines cream"><span class="cue" style="position:absolute;top:7px;left:11px;right:11px;">Chief Justice Warren&rsquo;s unanimous ruling: &ldquo;separate&hellip; inherently unequal,&rdquo; violating the 14th Amendment &mdash; describe what it overturned</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Impact &middot; on desegregation</div>
          <div class="ce-stack">
            {_effects_html}
          </div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee schools desegregated after <i>Brown</i> &mdash; slowly and with
        conflict. <b>Clinton High School</b> in Anderson County was one of the <b>first public high schools in the South
        to desegregate</b>, in 1956.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="20_us78_causeeffect",
    title="Brown v. Board: The Ruling That Started It",
    kicker="Unit 9 &middot; US.78 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Examine", "skill")],
    why=("Reading it as <b>context &rarr; ruling &rarr; impact</b> shows both why the case succeeded and why change came "
         "so slowly afterward. "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the center ruling box first. Then trace one effect at a time: &ldquo;Because the Court ruled ___, ___.&rdquo;",
        extend="Brown ended segregation in law but not at once in fact. Use the effects to explain that gap.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>diagram</b> the court&rsquo;s reasoning."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 9 &middot; US.78 (labeled)",
)]
