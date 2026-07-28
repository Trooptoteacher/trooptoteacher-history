# -*- coding: utf-8 -*-
"""Unit 10 labeled -- US.92 The Impact of September 11th (cause & effect).
Who attacked and why (left) feeds the center EVENT (9/11); America's responses
(right) flow out -- Homeland Security, the War on Terror, Afghanistan, Iraq.
LIGHT wells with faded hints. Factual, measured framing. HAS a Tennessee
Connection. Content approved for US.92.
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
    "<b>al&#8209;Qaeda</b>, led by Osama bin Laden, plans the attacks",
    "19 hijackers strike the World Trade Center &amp; the Pentagon &mdash; nearly 3,000 killed",
    "the <b>Taliban</b> government in Afghanistan shelters al&#8209;Qaeda",
]
_effects = [
    "<b>Homeland Security</b> &amp; the <b>PATRIOT Act</b> &mdash; new surveillance &amp; airport security",
    "a <b>&ldquo;War on Terror&rdquo;</b> is declared",
    "the <b>Afghanistan War</b> removes the Taliban &mdash; and becomes the <b>longest war</b> in U.S. history",
    "the <b>Iraq War</b> &mdash; launched on WMD claims that proved <b>false</b> &mdash; brings instability",
]

_causes_html = "\n            ".join(_cause_box(c) for c in _causes)
_effects_html = "\n            ".join(_effect_box(e) for e in _effects)

BODY = f"""
    <div class="prompt">Who attacked and why sits on the <b>left</b>; America&rsquo;s <b>responses</b> flow out on the <b>right</b>. Arrows show the chain: <b>the attack &rarr; the response &rarr; two long wars</b>.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Causes &middot; the attack</div>
          <div class="ce-stack">
            {_causes_html}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The event</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">SEPTEMBER 11, <span class="yr">2001</span></div>
            <div class="well lines cream"><span class="cue" style="position:absolute;top:7px;left:11px;right:11px;">The deadliest attack on U.S. soil reshapes American security &amp; foreign policy &mdash; describe how the nation responded</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Effects &middot; the response</div>
          <div class="ce-stack">
            {_effects_html}
          </div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee&rsquo;s <b>Fort Campbell 101st Airborne Division</b> was among the
        first conventional forces sent to Afghanistan in Operation Enduring Freedom, and the state tightened security
        at key sites including the <b>Oak Ridge</b> nuclear complex.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="29_us92_causeeffect",
    title="September 11th and America&rsquo;s Response",
    kicker="Unit 10 &middot; US.92 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Causation", "skill")],
    why=("Reading it as <b>attack &rarr; response &rarr; consequences</b> shows how one day reshaped security at home and "
         "led to two long wars abroad. "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the center box first. Then connect each response to the attack: &ldquo;After 9/11, the U.S. ___.&rdquo;",
        extend="The Iraq War&rsquo;s WMD claims proved false. Explain why that mattered for public trust.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>diagram</b> the domestic vs. international responses."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 10 &middot; US.92 (labeled)",
)]
