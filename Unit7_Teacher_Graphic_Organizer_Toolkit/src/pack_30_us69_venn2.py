# -*- coding: utf-8 -*-
"""Unit 7 labeled -- US.69 The Space Race (2-circle Venn).
Compare U.S. and Soviet achievements in the race to space: what was unique to each
and what drove them both. Per the house Venn rule, ALL region labels and faded
hints live as <text> INSIDE the SVG; topic labels sit in a legend row ABOVE. HAS a
Tennessee Connection. Content approved for US.69.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .legend{ flex:0 0 auto; display:flex; gap:10px; margin-bottom:4px; }
  .legend .lg{ flex:1 1 0; border-radius:6px; padding:6px 11px; color:#fff; font-size:8.6pt; line-height:1.2; }
  .legend .lg.a{ background:var(--navy); } .legend .lg.b{ background:var(--red); }
  .legend .lg b{ font-size:9.6pt; letter-spacing:.02em; } .legend .lg small{ opacity:.9; }
  .venn-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .venn-wrap svg{ width:100%; height:100%; display:block; }
  .tnbox{ flex:0 0 auto; margin-top:4px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:6px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:13pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.4pt; line-height:1.28; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

BODY = r"""
    <div class="prompt">The two superpowers raced to space. Write what was <b>unique</b> to each on its side, and what <b>drove them both</b> in the middle &mdash; the faint notes are starters.</div>
    <div class="canvas">
      <div class="legend">
        <div class="lg a"><b>UNITED STATES</b> <small>&mdash; NASA &middot; von Braun</small></div>
        <div class="lg b"><b>SOVIET UNION</b> <small>&mdash; Korolev</small></div>
      </div>
      <div class="venn-wrap">
        <svg viewBox="0 0 900 560" preserveAspectRatio="xMidYMid meet">
          <circle cx="330" cy="285" r="245" fill="#EEF1F7" stroke="#1B2A4A" stroke-width="3.5"/>
          <circle cx="570" cy="285" r="245" fill="#FBEEEF" stroke="#B22234" stroke-width="3.5"/>
          <path d="M 450,72.5 A 245,245 0 0,1 450,497.5 A 245,245 0 0,1 450,72.5 Z"
                fill="#FAF3E2" stroke="#C89B3C" stroke-width="2.5"/>
          <text x="208" y="150" text-anchor="middle" font-family="Georgia,serif" font-size="18" font-weight="700" fill="#1B2A4A">Only the U.S.</text>
          <text x="450" y="92" text-anchor="middle" font-family="Georgia,serif" font-size="17" font-weight="700" fill="#8a6a1e">Both</text>
          <text x="686" y="151" text-anchor="middle" font-family="Georgia,serif" font-size="18" font-weight="700" fill="#B22234">Only the USSR</text>
          <g font-family="Helvetica,Arial,sans-serif" font-size="14.5" font-style="italic" fill="#9aa6bd" text-anchor="middle">
            <text x="203" y="230">John Glenn orbits (1962)</text>
            <text x="203" y="280">Apollo 11 Moon</text>
            <text x="203" y="330">landing (1969)</text>
            <text x="450" y="220">Cold War prestige</text>
            <text x="450" y="270">rocket / ICBM tech</text>
            <text x="450" y="320">huge spending</text>
            <text x="697" y="230">Sputnik (1957) &mdash;</text>
            <text x="697" y="280">first satellite</text>
            <text x="697" y="330">Gagarin: first human (1961)</text>
          </g>
        </svg>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee helped power the space race: the <b>Arnold Engineering
        Development Complex (AEDC)</b> at <b>Tullahoma</b> &mdash; one of the world&rsquo;s most advanced aerospace test sites &mdash;
        tested rocket engines and spacecraft parts for NASA&rsquo;s Mercury, Gemini, and Apollo programs.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="30_us69_venn2",
    title="The Race to Space",
    kicker="Unit 7 &middot; US.69 &middot; Best&#8209;Fit Organizer",
    chips=[("Venn &middot; Compare Two", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Compare", "skill")],
    why=("A Venn makes the <b>overlap</b> visible &mdash; both superpowers raced for the same prestige &mdash; while sorting "
         "who reached each milestone first. The USSR led early; the U.S. reached the Moon. "
         "<span class='cite'>Identifying similarities &amp; differences is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the <b>Both</b> region first (why <i>both</i> raced), then place each achievement with the right country.",
        extend="The USSR led early, but the U.S. reached the Moon &mdash; who &ldquo;won&rdquo; the space race, and by what measure?",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>build</b> a timeline of milestones alongside the Venn."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 7 &middot; US.69 (labeled)",
)]
