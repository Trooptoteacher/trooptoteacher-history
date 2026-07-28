# -*- coding: utf-8 -*-
"""Unit 3 labeled -- US.24 American Entry into WWI (cause & effect).
FOUR reasons converge on ONE decision: unrestricted submarine warfare (Lusitania,
1915), the Zimmermann Telegram, defense of democracy, and economic ties to the
Allies all feed the U.S. declaration of war (April 1917). A LIGHT "first effects"
strip below captures what happened next. Faded italic hints seed each cause box.
Framed as "four reasons -> one decision" to stay distinct from US.21 outcomes.
TN tie: over 90,000 Tennesseans served; state camps trained the troops.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .ce-grid{ flex:1 1 auto; display:flex; align-items:stretch; gap:6px; min-height:0; }
  .ce-col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .ce-colhead{ font-size:8.7pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase;
               text-align:center; margin-bottom:5px; flex:0 0 auto; }
  .ce-stack{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .cebox{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .cebox .band{ border-radius:6px 6px 0 0; font-size:8.8pt; padding:5px 9px; line-height:1.18; }
  .cebox .well{ flex:1 1 0; position:relative; }
  .cebox .fh{ position:absolute; top:6px; left:10px; right:10px; font-size:7.6pt; font-style:italic;
              color:#9aa6bd; line-height:1.22; }
  .ce-arrs{ flex:0 0 26px; display:flex; flex-direction:column; justify-content:space-around;
            align-items:center; padding:20px 0; }
  .ce-arrs .arr-r{ border-left-width:17px; border-top-width:12px; border-bottom-width:12px;
            border-left-color:var(--navy); }
  .ce-center{ flex:1.18 1 0; display:flex; flex-direction:column; justify-content:center; min-height:0; }
  .ce-center .band.navy{ font-size:12pt; padding:10px 8px; border-radius:7px 7px 0 0; line-height:1.14;
                        box-shadow:0 0 0 3px var(--navy-tint); }
  .ce-center .band.navy .when{ display:block; font-size:9pt; color:#e8c979; margin-top:3px;
                        font-weight:800; letter-spacing:.03em; }
  .ce-center .well{ flex:1 1 0; }
  .ce-center .cue{ color:#8792a4; }
  .ce-down{ flex:0 0 auto; display:flex; flex-direction:column; align-items:center; margin:5px 0 2px; }
  .ce-down .arr-d{ border-top-color:var(--red); margin:0; }
  .ce-down .lbl{ font-size:7.6pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase;
                 color:var(--red); margin-top:2px; }
  .effect{ flex:0 0 auto; display:flex; flex-direction:column; }
  .effect .band{ border-radius:6px 6px 0 0; }
  .effect .well{ min-height:58px; position:relative; }
  .effect .fh{ position:absolute; top:7px; left:11px; right:11px; font-size:8pt; font-style:italic;
               color:#9aa6bd; line-height:1.3; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.8pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

# four reasons -> faded starter hint each
CAUSES = [
    ("Unrestricted submarine warfare", "sinking of the RMS Lusitania (1915)"),
    ("The Zimmermann Telegram", "Germany&rsquo;s secret offer to Mexico"),
    ("Defense of democracy", "&ldquo;make the world safe for democracy&rdquo;"),
    ("Economic ties to the Allies", "loans &amp; wartime trade"),
]


def _causes():
    out = []
    for lab, hint in CAUSES:
        out.append(f'<div class="cebox"><div class="band navy sm">{lab}</div>'
                   f'<div class="well lines"><span class="fh">{hint}</span></div></div>')
    return "\n            ".join(out)


BODY = f"""
    <div class="prompt">Four separate reasons on the <b>left</b> converged on one <b>decision</b> in the center. Arrows show the flow: <b>four reasons &rarr; one decision &rarr; first effects</b>.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Four reasons &middot; what pushed toward war</div>
          <div class="ce-stack">
            {_causes()}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">One decision</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">U.S. Declares War on Germany<span class="when">April 1917</span></div>
            <div class="well lines cream"><span class="cue">Which reason weighed most? Why now?</span></div>
          </div>
        </div>
      </div>
      <div class="ce-down"><div class="arr-d"></div><div class="lbl">then &mdash; the first effects</div></div>
      <div class="effect">
        <div class="band red sm">First effects &middot; what happened next</div>
        <div class="well lines">
          <span class="fh">the draft (Selective Service) and the American Expeditionary Force mobilize &mdash; add what followed &hellip;</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Over <b>90,000 Tennesseans</b> served in World War I, and
        Tennessee&rsquo;s military camps trained thousands of soldiers for the war effort.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="25_us24_causeeffect",
    title="The Road to War, 1917",
    kicker="Unit 3 &middot; US.24 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Causation", "skill")],
    why=("Use when several reasons <b>converge</b> on a single decision &mdash; here, four pressures leading the "
         "U.S. to declare war in April 1917. "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY, extra_css=CSS,
    udl=dict(
        scaffold="Which reason was the final trigger? Offer a word bank (Lusitania, Zimmermann, democracy, trade) and fill the center box first.",
        extend="Could the U.S. have stayed neutral? Defend your answer using at least two of the four reasons.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>analyze</b> the Zimmermann Telegram as a primary source."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 3 &middot; US.24 (labeled)",
)]
