# -*- coding: utf-8 -*-
"""Unit 7 labeled -- US.63 Brinkmanship vs. Peaceful Coexistence (2-circle Venn).
Compare the two competing Cold War approaches of the Eisenhower era. Per the house
Venn rule, ALL region labels and faded hints live as <text> INSIDE the SVG; topic
labels sit in a legend row ABOVE the diagram. A bottom note names what they shared.
No TN tie in source. Content approved for US.63.
"""

CSS = r"""
  .legend{ flex:0 0 auto; display:flex; gap:10px; margin-bottom:4px; }
  .legend .lg{ flex:1 1 0; border-radius:6px; padding:6px 11px; color:#fff; font-size:8.6pt; line-height:1.2; }
  .legend .lg.a{ background:var(--navy); } .legend .lg.b{ background:var(--red); }
  .legend .lg b{ font-size:9.6pt; letter-spacing:.02em; } .legend .lg small{ opacity:.9; }
  .venn-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .venn-wrap svg{ width:100%; height:100%; display:block; }
  .note{ flex:0 0 auto; margin-top:4px; background:var(--cream); border:1.6px solid var(--gold);
         border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 11px;
         font-size:8.8pt; color:var(--navy); line-height:1.3; } .note b{ color:var(--navy); }
"""

BODY = r"""
    <div class="prompt">Two competing Cold War approaches. Write what was <b>unique</b> to each on its side, and what they <b>shared</b> in the middle &mdash; the faint notes are starters.</div>
    <div class="canvas">
      <div class="legend">
        <div class="lg a"><b>BRINKMANSHIP</b> <small>&mdash; Dulles &middot; push to the edge of war</small></div>
        <div class="lg b"><b>PEACEFUL COEXISTENCE</b> <small>&mdash; Khrushchev &middot; compete, not fight</small></div>
      </div>
      <div class="venn-wrap">
        <svg viewBox="0 0 900 560" preserveAspectRatio="xMidYMid meet">
          <circle cx="330" cy="285" r="245" fill="#EEF1F7" stroke="#1B2A4A" stroke-width="3.5"/>
          <circle cx="570" cy="285" r="245" fill="#FBEEEF" stroke="#B22234" stroke-width="3.5"/>
          <path d="M 450,72.5 A 245,245 0 0,1 450,497.5 A 245,245 0 0,1 450,72.5 Z"
                fill="#FAF3E2" stroke="#C89B3C" stroke-width="2.5"/>
          <text x="205" y="120" text-anchor="middle" font-family="Georgia,serif" font-size="18" font-weight="700" fill="#1B2A4A">Only Brinkmanship</text>
          <text x="450" y="92" text-anchor="middle" font-family="Georgia,serif" font-size="17" font-weight="700" fill="#8a6a1e">Both</text>
          <text x="695" y="120" text-anchor="middle" font-family="Georgia,serif" font-size="18" font-weight="700" fill="#B22234">Only Coexistence</text>
          <g font-family="Helvetica,Arial,sans-serif" font-size="14.5" font-style="italic" fill="#9aa6bd" text-anchor="middle">
            <text x="203" y="235">threaten nuclear war</text>
            <text x="203" y="285">Suez &amp; Berlin crises</text>
            <text x="203" y="335">aggressive, risk-taking</text>
            <text x="450" y="220">Cold War strategy</text>
            <text x="450" y="270">avoid all-out war</text>
            <text x="450" y="320">keep competing</text>
            <text x="697" y="235">compete economically</text>
            <text x="697" y="285">more diplomatic</text>
            <text x="697" y="335">opened the door to talks</text>
          </g>
        </svg>
      </div>
      <div class="note"><b>Why it matters &rarr;</b> Both accepted that a nuclear war had to be avoided &mdash; they disagreed on
      <b>how</b>: brinkmanship gambled with the <b>threat</b> of war, while coexistence leaned on <b>diplomacy</b>.</div>
    </div>
"""

ORGANIZERS = [dict(
    slug="24_us63_venn2",
    title="Two Ways to Fight a Cold War",
    kicker="Unit 7 &middot; US.63 &middot; Best&#8209;Fit Organizer",
    chips=[("Venn &middot; Compare Two", "navy"), ("DOK 2&#8211;3 &middot; Compare", "skill")],
    why=("Brinkmanship and peaceful coexistence were rival answers to the same danger. A Venn makes the <b>overlap</b> "
         "visible &mdash; both feared nuclear war &mdash; while sharpening how their methods differed. "
         "<span class='cite'>Identifying similarities &amp; differences is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the <b>Both</b> region first (both wanted to avoid nuclear war), then find what made each approach different.",
        extend="Which approach was more dangerous &mdash; and which more effective? Defend your answer with evidence.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>sort</b> example cards into the three regions."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 7 &middot; US.63 (labeled)",
)]
