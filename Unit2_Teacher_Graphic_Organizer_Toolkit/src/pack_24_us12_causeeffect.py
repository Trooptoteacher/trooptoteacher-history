# -*- coding: utf-8 -*-
"""Unit 2 labeled — US.12 Trusts, Monopolies & the Government's Response.
Cause & Effect: a center EVENT (trusts & monopolies dominate) with two causes
feeding in (arrows) and two effects flowing out (arrows), plus a TN tie.
Topics/dates sourced from the standards inventory (US.12): vertical & horizontal
integration, Sherman Antitrust Act (1890), Clayton Antitrust Act (1914), TCI.
"""

CSS = r"""
  .ce-grid{ flex:1 1 auto; display:flex; align-items:stretch; gap:5px; min-height:0; }
  .ce-col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .ce-colhead{ font-size:8.7pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase;
               text-align:center; margin-bottom:5px; flex:0 0 auto; }
  .ce-stack{ flex:1 1 auto; display:flex; flex-direction:column; gap:12px; min-height:0; }
  .cebox{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .cebox .band{ border-radius:6px 6px 0 0; font-size:9pt; padding:6px 9px; line-height:1.2; }
  .cebox .band .yr{ color:var(--gold); font-weight:800; }
  .cebox.red .band .yr{ color:#f6d9a6; }
  .cebox .well{ flex:1 1 0; }
  .ce-arrs{ flex:0 0 26px; display:flex; flex-direction:column; justify-content:space-around;
            align-items:center; padding:30px 0; }
  .ce-arrs .lbl{ font-size:6.6pt; font-weight:800; color:var(--muted); text-transform:uppercase;
                 letter-spacing:.05em; margin-bottom:3px; text-align:center; }
  .ce-arrs .arr-r{ border-left-width:17px; border-top-width:12px; border-bottom-width:12px; }
  .ce-arrs.out .arr-r{ border-left-color:var(--red); }
  .ce-center{ flex:1.28 1 0; display:flex; flex-direction:column; justify-content:center; min-height:0; }
  .ce-center .band{ font-size:12.5pt; padding:9px 8px; border-radius:7px 7px 0 0; line-height:1.12; }
  .ce-center .well{ flex:1 1 0; }
  .ce-center .cue{ color:#8792a4; }
  .tnbox{ flex:0 0 auto; margin-top:9px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.8pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

BODY = r"""
    <div class="prompt">Two forces built the trusts on the <b>left</b>; two consequences flowed out on the <b>right</b>. Arrows show the flow: <b>causes &rarr; event &rarr; effects</b>.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Causes &middot; what built the trusts</div>
          <div class="ce-stack">
            <div class="cebox"><div class="band navy sm">How trusts formed (vertical &amp; horizontal integration)</div>
              <div class="well navy lines"></div></div>
            <div class="cebox"><div class="band navy sm">The drive to eliminate competition</div>
              <div class="well navy lines"></div></div>
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The event</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">TRUSTS &amp; MONOPOLIES DOMINATE</div>
            <div class="well lines cream"><span class="cue">Describe how a few firms came to control an industry</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Effects &middot; what followed</div>
          <div class="ce-stack">
            <div class="cebox red"><div class="band red sm">Impact on consumers &amp; workers (higher prices, lower wages)</div>
              <div class="well red lines"></div></div>
            <div class="cebox red"><div class="band red sm">Government response &mdash; Sherman Antitrust Act <span class="yr">(1890)</span> &rarr; Clayton Antitrust Act <span class="yr">(1914)</span></div>
              <div class="well red lines"></div></div>
          </div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> The <b>Tennessee Coal, Iron and Railroad Company (TCI)</b> was a major
        site of industrial consolidation. On the lines above, note how one company&rsquo;s growth mirrored the national pattern.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="24_us12_causeeffect",
    title="Trusts, Monopolies &amp; the Government&rsquo;s Response",
    kicker="Unit 2 &middot; US.12 &middot; Best-Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("SSP.05 &middot; DOK 2&ndash;3", "skill")],
    why=("Use to map what <b>created</b> the trusts and what <b>followed</b> from them &mdash; including the "
         "government&rsquo;s regulatory response, from the Sherman Antitrust Act (1890) to the Clayton Antitrust Act (1914). "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY, extra_css=CSS, tn=True,
    udl=dict(
        scaffold="Fill the center box first. Offer frames: &ldquo;Because ___, a few firms controlled the market,&rdquo; and &ldquo;As a result, ___.&rdquo;",
        extend="Argue: did the Sherman and Clayton Acts do enough to restore competition? Cite an effect to defend your answer.",
        show="Students may <b>write</b>, <b>say</b> (record), <b>draw</b> arrows/icons, or <b>build</b> it with cards."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 2 &middot; US.12 (labeled)",
)]
