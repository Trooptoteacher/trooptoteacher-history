# -*- coding: utf-8 -*-
"""Unit 2 labeled best-fit organizer -- T-chart.
US.08: Two competing worldviews of the Progressive Era -- Social Darwinism
       ("survival of the fittest," laissez-faire) vs. the Social Gospel (a
       Christian duty to reform society). Same three criteria on each side so
       students can weigh both. TN tie: Nashville's Fisk University + churches.
Neutral framing: no side is labeled right/wrong; the verdict lives on the
student's synthesis line.
"""

CSS = r"""
  .tc{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .tc-cols{ flex:1 1 auto; display:flex; gap:12px; min-height:0; }
  .tc-col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .tc-col .band{ position:relative; }
  .tc-col .band small{ display:block; font-weight:600; font-size:8pt; opacity:.9; letter-spacing:0; text-transform:none; }
  .rowlbl{ display:flex; align-items:flex-start; gap:7px; padding:6px 10px 0; }
  .rowlbl .tagn{ background:var(--navy); color:#fff; font-size:7.5pt; font-weight:800; padding:2px 7px; border-radius:9px; white-space:nowrap; flex:0 0 auto; margin-top:1px; }
  .rowlbl .tagr{ background:var(--red); }
  .rowlbl .q{ font-size:8.6pt; color:#3a4455; }
  .tnbox{ flex:0 0 auto; background:var(--gold-tint); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:7px 12px; display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.9pt; line-height:1.32; color:#3a2f12; }
  .tnbox .t b{ color:#7a5c15; }
  .synth{ flex:0 0 auto; background:var(--cream); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:8px 12px; font-size:9.3pt; color:var(--navy); text-align:center; }
  .synth b{ color:var(--navy); }
"""

BODY = r"""
    <div class="prompt">Two worldviews framed the era&rsquo;s debate over government&rsquo;s role. Gather <b>evidence</b> for each &mdash; then take a position.</div>
    <div class="tc">
      <div class="tc-cols">
        <div class="tc-col">
          <div class="band navy">SOCIAL DARWINISM<small>survival of the fittest &middot; laissez-faire</small></div>
          <div class="rowlbl"><span class="tagn">Core belief</span><span class="q">What is the core idea about people and society?</span></div>
          <div class="rowlbl"><span class="tagn">Government&rsquo;s role</span><span class="q">What should government do &mdash; or not do?</span></div>
          <div class="rowlbl"><span class="tagn">Real-world impact</span><span class="q">Who did it affect, and how?</span></div>
          <div class="well navy lines" style="margin:6px 8px 8px; flex:1 1 0;"></div>
        </div>
        <div class="tc-col">
          <div class="band red">SOCIAL GOSPEL<small>a Christian duty to reform society</small></div>
          <div class="rowlbl"><span class="tagn tagr">Core belief</span><span class="q">What is the core idea about people and society?</span></div>
          <div class="rowlbl"><span class="tagn tagr">Government&rsquo;s role</span><span class="q">What should government do &mdash; or not do?</span></div>
          <div class="rowlbl"><span class="tagn tagr">Real-world impact</span><span class="q">Who did it affect, and how?</span></div>
          <div class="well red lines" style="margin:6px 8px 8px; flex:1 1 0;"></div>
        </div>
      </div>
      <div class="tnbox">
        <span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection &mdash;</b> the Social Gospel had Tennessee roots:
        Nashville&rsquo;s <b>Fisk University</b> and its churches promoted social justice and reform.</span>
      </div>
      <div class="synth"><b>Take a position:</b> Which view should shape government&rsquo;s role in solving social problems?
      ____________ <b>because</b> ________________________________________</div>
    </div>
"""

_UDL = dict(
    scaffold="Fill one strong bullet on each side together, then students add more. Frame: &ldquo;This view says government should ___ because ___.&rdquo;",
    extend="Write a one-paragraph position that uses evidence from <b>both</b> columns and names the trade-off it accepts.",
    show="Students may <b>write</b> bullets, <b>say</b> their position aloud, <b>draw</b> a two-pan balance, or <b>build</b> the chart with evidence cards.")

ORGANIZERS = [
    dict(
        slug="20_us08_tchart",
        title="Social Darwinism <span style='font-family:Georgia;font-style:italic'>or</span> Social Gospel?",
        kicker="Unit 2 &middot; US.08 &middot; Best-Fit Organizer",
        chips=[("T&#8209;Chart &middot; Two Views", "navy"), ("DOK 2&ndash;3 &middot; Analysis", "skill")],
        why=("Two clashing worldviews framed the era&rsquo;s whole debate over government&rsquo;s role in society. "
             "A T&#8209;chart forces students to weigh both on the same criteria before deciding. "
             "<span class='cite'>Comparing similarities and differences is Marzano&rsquo;s highest-yield move.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL, tn=True,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 2 &middot; US.08 (labeled)",
    ),
]
