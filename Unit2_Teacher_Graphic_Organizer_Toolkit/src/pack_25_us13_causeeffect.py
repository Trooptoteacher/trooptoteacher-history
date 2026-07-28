# -*- coding: utf-8 -*-
"""Unit 2 labeled — US.13 Working Conditions -> Reform.
Cause & Effect with a tragedy as the pivot: industrial conditions & child/woman
labor feed into the Triangle Shirtwaist Factory Fire (1911), which drives reform.
Topics/dates sourced from the standards inventory (US.13): Triangle fire (1911),
National Child Labor Committee, Lewis Hine, workers' comp & child-labor laws.
"""

CSS = r"""
  .ce-grid{ flex:1 1 auto; display:flex; align-items:stretch; gap:5px; min-height:0; }
  .ce-col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .ce-colhead{ font-size:8.7pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase;
               text-align:center; margin-bottom:5px; flex:0 0 auto; }
  .ce-stack{ flex:1 1 auto; display:flex; flex-direction:column; gap:12px; min-height:0; }
  .cebox{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .cebox .band{ border-radius:6px 6px 0 0; font-size:9pt; padding:6px 9px; line-height:1.2; }
  .cebox .well{ flex:1 1 0; }
  .ce-arrs{ flex:0 0 26px; display:flex; flex-direction:column; justify-content:space-around;
            align-items:center; padding:30px 0; }
  .ce-arrs .arr-r{ border-left-width:17px; border-top-width:12px; border-bottom-width:12px; }
  .ce-arrs.in .arr-r{ border-left-color:var(--navy); }
  .ce-arrs.out .arr-r{ border-left-color:var(--red); }
  .ce-center{ flex:1.3 1 0; display:flex; flex-direction:column; justify-content:center; min-height:0; }
  .ce-center .band.red{ font-size:11.5pt; padding:9px 8px; border-radius:7px 7px 0 0; line-height:1.14;
                        box-shadow:0 0 0 3px var(--red-tint); }
  .ce-center .band.red .died{ display:block; font-size:9pt; color:#f6d9a6; margin-top:2px; font-weight:800; letter-spacing:.03em; }
  .ce-center .well{ flex:1 1 0; }
  .ce-center .cue{ color:#b58189; }
  .tnbox{ flex:0 0 auto; margin-top:9px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.8pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

BODY = r"""
    <div class="prompt">Harsh conditions on the <b>left</b> led to a tragedy in the <b>center</b>, which drove reform on the <b>right</b>. Arrows show the flow: <b>causes &rarr; event &rarr; effects</b>.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Causes &middot; what led to it</div>
          <div class="ce-stack">
            <div class="cebox"><div class="band navy sm">Industrial working conditions (sweatshops &middot; long hours &middot; danger)</div>
              <div class="well navy lines"></div></div>
            <div class="cebox"><div class="band navy sm">Women &amp; child labor</div>
              <div class="well navy lines"></div></div>
          </div>
        </div>
        <div class="ce-arrs in"><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--red);">The turning point</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band red">Triangle Shirtwaist Factory Fire (1911)<span class="died">146 workers died</span></div>
            <div class="well red lines tint-red"><span class="cue">Why did this tragedy become a turning point?</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Effects &middot; what followed</div>
          <div class="ce-stack">
            <div class="cebox"><div class="band red sm">Reforms (workers&rsquo; compensation &middot; child-labor laws &middot; factory-safety codes)</div>
              <div class="well red lines"></div></div>
            <div class="cebox"><div class="band red sm">The reform push (National Child Labor Committee &middot; Lewis Hine&rsquo;s photographs)</div>
              <div class="well red lines"></div></div>
          </div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee&rsquo;s <b>textile mills, coal mines, and factories</b> employed
        women and children under harsh conditions. On the lines above, connect a Tennessee workplace to the national reform story.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="25_us13_causeeffect",
    title="Working Conditions &rarr; Reform",
    kicker="Unit 2 &middot; US.13 &middot; Best-Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("SSP.05 &middot; DOK 2&ndash;3", "skill")],
    why=("Use to show how brutal industrial conditions &mdash; and a single tragedy, the 1911 Triangle Shirtwaist "
         "Factory Fire &mdash; drove the Progressive push for workplace reform. "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY, extra_css=CSS, tn=True,
    udl=dict(
        scaffold="Fill the center box first. Offer frames: &ldquo;Workers faced ___,&rdquo; and &ldquo;After the fire, lawmakers ___.&rdquo;",
        extend="Argue: which reform on the right did the most to protect workers? Cite a cause or the fire to defend it.",
        show="Students may <b>write</b>, <b>say</b> (record), <b>draw</b> arrows/icons, or <b>build</b> it with cards."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 2 &middot; US.13 (labeled)",
)]
