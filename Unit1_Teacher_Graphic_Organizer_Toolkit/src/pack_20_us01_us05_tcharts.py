# -*- coding: utf-8 -*-
"""Unit 1 labeled best-fit organizers — two T-charts.
US.01: Who benefited vs. who bore the costs of westward expansion (TN: George Jordan).
US.05: 'Captain of Industry' vs. 'Robber Baron' — same figures, two lenses.
Standard topics sourced from the course standards inventory (US.01 Homestead Act,
Transcontinental Railroad, Buffalo Soldiers; US.05 Bell/Carnegie/Edison/Rockefeller/
Walker/Carver). TN tie (George Jordan, Williamson County) sourced from the guide.
"""

CSS = r"""
  .tc{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .tc-cols{ flex:1 1 auto; display:flex; gap:12px; min-height:0; }
  .tc-col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .tc-col .band{ position:relative; }
  .tc-col .band small{ display:block; font-weight:600; font-size:8pt; opacity:.9; letter-spacing:0; text-transform:none; }
  .seed{ font-size:9pt; color:var(--navy); font-weight:700; }
  .seed.r{ color:var(--red); }
  .rowlbl{ display:flex; align-items:flex-start; gap:7px; padding:6px 10px 0; }
  .rowlbl .tagn{ background:var(--navy); color:#fff; font-size:7.5pt; font-weight:800; padding:2px 7px; border-radius:9px; white-space:nowrap; flex:0 0 auto; margin-top:1px; }
  .rowlbl .tagr{ background:var(--red); }
  .rowlbl .q{ font-size:8.6pt; color:#3a4455; }
  .midbar{ flex:0 0 auto; background:var(--navy-tint); border:1.5px solid var(--navy); border-radius:6px; padding:6px 11px; font-size:9pt; }
  .midbar b{ color:var(--navy); }
  .tnbox{ flex:0 0 auto; background:var(--gold-tint); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:7px 12px; display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.9pt; line-height:1.32; color:#3a2f12; }
  .tnbox .t b{ color:#7a5c15; }
  .subj{ flex:0 0 auto; background:var(--cream); border:1.4px dashed var(--gold); border-radius:6px; padding:6px 10px; font-size:9pt; text-align:center; color:var(--navy); }
"""

US01_BODY = r"""
    <div class="prompt">One event can help some groups and harm others. List the <b>evidence</b> on each side &mdash; then decide.</div>
    <div class="tc">
      <div class="tc-cols">
        <div class="tc-col">
          <div class="band navy">WHO BENEFITED<small>settlers &middot; railroads &middot; the growing nation</small></div>
          <div class="rowlbl"><span class="tagn">Homestead Act</span><span class="q">Who gained land &mdash; and what did it let them do?</span></div>
          <div class="rowlbl"><span class="tagn">Transcontinental RR</span><span class="q">Who profited from building &amp; using it?</span></div>
          <div class="rowlbl"><span class="tagn">Buffalo Soldiers</span><span class="q">What role did the U.S. Army play out West?</span></div>
          <div class="well navy lines" style="margin:6px 8px 8px; flex:1 1 0;"></div>
        </div>
        <div class="tc-col">
          <div class="band red">WHO BORE THE COSTS<small>American Indian nations</small></div>
          <div class="rowlbl"><span class="tagn tagr">Land &amp; treaties</span><span class="q">What was taken or broken?</span></div>
          <div class="rowlbl"><span class="tagn tagr">Way of life</span><span class="q">What changed for Plains nations (e.g., the bison)?</span></div>
          <div class="rowlbl"><span class="tagn tagr">Sovereignty</span><span class="q">How did U.S. policy limit self-rule?</span></div>
          <div class="well red lines" style="margin:6px 8px 8px; flex:1 1 0;"></div>
        </div>
      </div>
      <div class="tnbox">
        <span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection &mdash; George Jordan, Williamson County, TN.</b>
        Jordan was a <b>Buffalo Soldier</b>: a sergeant in the 9th U.S. Cavalry and a <b>Medal of Honor</b> recipient.
        His service is a source of pride <em>and</em> sits inside the very expansion that displaced American Indian nations.
        Where does his story belong on this chart &mdash; benefit, cost, or both? Defend your placement.</span>
      </div>
      <div class="midbar"><b>Weigh it:</b> Was westward expansion &ldquo;progress&rdquo;? Use evidence from <b>both</b> columns to answer &mdash; for whom, and at what cost? ______________________________________________</div>
    </div>
"""

US05_BODY = r"""
    <div class="prompt">Same person, two labels. Gather <b>evidence</b> for each lens &mdash; then judge with your own reasoning.</div>
    <div class="tc">
      <div class="subj"><b>Figure under study:</b> ________________________&nbsp;&nbsp; <span class="hint">e.g., Carnegie &middot; Rockefeller &middot; Edison &middot; Bell &middot; Madam C.J. Walker &middot; Carver</span></div>
      <div class="tc-cols">
        <div class="tc-col">
          <div class="band navy">&ldquo;CAPTAIN OF INDUSTRY&rdquo;<small>built industry, jobs, wealth, philanthropy</small></div>
          <div class="rowlbl"><span class="tagn">Innovation</span><span class="q">What did they create or improve?</span></div>
          <div class="rowlbl"><span class="tagn">Public good</span><span class="q">Jobs, growth, giving &mdash; what helped society?</span></div>
          <div class="well navy lines" style="margin:6px 8px 8px; flex:1 1 0;"></div>
        </div>
        <div class="tc-col">
          <div class="band red">&ldquo;ROBBER BARON&rdquo;<small>ruthless tactics, monopoly, worker harm</small></div>
          <div class="rowlbl"><span class="tagn tagr">Tactics</span><span class="q">Monopoly, price-fixing, crushing rivals?</span></div>
          <div class="rowlbl"><span class="tagn tagr">Human cost</span><span class="q">Wages, hours, conditions for workers?</span></div>
          <div class="well red lines" style="margin:6px 8px 8px; flex:1 1 0;"></div>
        </div>
      </div>
      <div class="midbar"><b>Your verdict:</b> Captain, robber baron, or both? ____________ &mdash; <b>because</b> ____________________________________________</div>
    </div>
"""

_UDL_TC = dict(
    scaffold="Pre-fill one strong bullet on each side together, then students add two more. Sentence frame: &ldquo;This shows a ___ because ___.&rdquo;",
    extend="Write a one-paragraph judgment that uses evidence from <b>both</b> columns and names the trade-off explicitly.",
    show="Students may <b>write</b> bullets, <b>say</b> their verdict aloud, <b>draw</b> a two-pan balance, or <b>build</b> the chart with evidence cards.")

ORGANIZERS = [
    dict(
        slug="20_us01_tchart",
        title="Winners &amp; Costs of Westward Expansion",
        kicker="Unit 1 &middot; US.01 &middot; Best-Fit Organizer",
        chips=[("T&#8209;Chart &middot; Two Sides", "navy"), ("DOK 3 &middot; Perspective", "skill")],
        why=("Westward expansion (the Homestead Act, the Transcontinental Railroad, the Army out West) "
             "lifted some groups and devastated others. A T&#8209;chart forces students to hold both truths at once. "
             "<span class='cite'>Comparing across perspectives is Marzano&rsquo;s highest-yield move.</span>"),
        body=US01_BODY, extra_css=CSS, udl=_UDL_TC, tn=True,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 1 &middot; US.01 (labeled)",
    ),
    dict(
        slug="24_us05_tchart",
        title="Captain of Industry <span style='font-family:Georgia;font-style:italic;font-size:16pt'>or</span> Robber Baron?",
        kicker="Unit 1 &middot; US.05 &middot; Best-Fit Organizer",
        chips=[("T&#8209;Chart &middot; Two Lenses", "navy"), ("DOK 3 &middot; Evaluate", "skill")],
        why=("The same Gilded Age figures &mdash; Carnegie, Rockefeller, Edison, Bell, Walker, Carver &mdash; can be framed "
             "as builders or as ruthless monopolists. Collecting evidence for each lens teaches students that labels are arguments. "
             "<span class='cite'>Same/different analysis drives evaluation (Marzano; DOK 3).</span>"),
        body=US05_BODY, extra_css=CSS, udl=_UDL_TC,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 1 &middot; US.05 (labeled)",
    ),
]
