# -*- coding: utf-8 -*-
"""Unit 4 labeled -- US.37 Prohibition & Its Impact (cause & effect).
Three CAUSES (why Prohibition passed, including its intended goals) feed the center
EVENT (Prohibition); four ACTUAL RESULTS -- many unintended -- flow out to the
right, so the gap between intent and outcome is visible. LIGHT wells with faded
italic hints. Neutral framing: results named as facts; students judge "more harm
or good." HAS a Tennessee Connection. Approved US.37.
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
    "Temperance movement, religious groups &amp; progressive reformers",
    "<b>Intended goals:</b> less crime, better health, stronger families, more productivity",
    "The <b>18th Amendment</b> <span class=\"yr\">(1919)</span> &amp; the Volstead Act",
]
_effects = [
    "Only 1,500 federal agents; ~5% of illegal alcohol intercepted",
    "Organized crime boomed &mdash; Al Capone; St.&nbsp;Valentine&rsquo;s Day Massacre (1929)",
    "Bootlegging &amp; &ldquo;bathtub gin&rdquo;; smuggling from Canada &amp; the Caribbean",
    "Speakeasies spread; widespread disregard for the law",
]

_causes_html = "\n            ".join(_cause_box(c) for c in _causes)
_effects_html = "\n            ".join(_effect_box(e) for e in _effects)

BODY = f"""
    <div class="prompt">Why Prohibition passed &mdash; and its <b>intended goals</b> &mdash; sit on the <b>left</b>. What <b>actually</b> happened flows out on the <b>right</b>. Compare the two: where did outcome match intent, and where did it not?</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Causes &middot; goals &amp; the law</div>
          <div class="ce-stack">
            {_causes_html}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The policy</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">PROHIBITION, <span class="yr">1920&ndash;1933</span></div>
            <div class="well lines cream"><span class="cue" style="position:absolute;top:7px;left:11px;right:11px;">A national ban on making, selling &amp; transporting alcohol &mdash; describe what it tried to do</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">What actually happened</div>
          <div class="ce-stack">
            {_effects_html}
          </div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee went <b>dry in 1909</b> &mdash; a full decade before the
        18th Amendment. During national Prohibition, the state&rsquo;s mountainous terrain became a haven for
        <b>moonshiners</b>, and <b>Memphis</b>, with its river access, was a hub for illegal alcohol.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="29_us37_causeeffect",
    title="Prohibition: Intended Goals vs. Actual Results",
    kicker="Unit 4 &middot; US.37 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Causation", "skill")],
    why=("Placing the <b>goals</b> beside the <b>results</b> makes the gap visible &mdash; a law meant to reduce crime "
         "helped create an era of organized crime. "
         "<span class='cite'>Analyzing cause &amp; effect &mdash; including unintended effects &mdash; is TN Social "
         "Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the center policy box first. Then match each <b>goal</b> on the left to what actually happened on the right.",
        extend="Weigh it: did Prohibition cause <b>more harm or more good</b>? Defend your call with evidence from both columns.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>diagram</b> where intent and outcome split apart."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 4 &middot; US.37 (labeled)",
)]
