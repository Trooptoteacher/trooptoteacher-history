# -*- coding: utf-8 -*-
"""Unit 2 labeled — US.18 The Long Road to the 19th Amendment.
Vertical timeline (DATE well at LEFT of the event, per toolkit rule). The
movement organizes, tactics sharpen, then Tennessee ratifies (Aug 18, 1920 —
the 'Perfect 36') and the amendment is certified (Aug 26, 1920). Topics/dates
sourced from the standards inventory (US.18). Only 1920 is a given date.
"""

CSS = r"""
  .tl{ flex:1 1 auto; position:relative; display:flex; flex-direction:column; min-height:0; padding-left:120px; }
  .tl::before{ content:""; position:absolute; left:102px; top:6px; bottom:6px; width:4px; background:var(--navy); border-radius:2px; }
  .ev{ flex:1 1 0; display:flex; align-items:stretch; position:relative; min-height:0; padding:5px 0; }
  .ev .date{ position:absolute; left:-120px; top:5px; width:92px; text-align:right; }
  .ev .date .d{ font-family:Georgia,serif; font-size:15pt; font-weight:700; color:var(--red); line-height:1; }
  .ev .date .w{ display:block; border-bottom:1.6px solid var(--rule); height:16px; margin-top:5px; }
  .ev .date .wl{ font-size:7pt; color:#8792a4; font-style:italic; }
  .ev .date .ph{ display:block; font-size:7pt; font-weight:800; letter-spacing:.04em; text-transform:uppercase;
                 color:var(--navy); margin-top:5px; }
  .ev .node{ position:absolute; left:-24px; top:6px; width:20px; height:20px; border-radius:50%;
             background:#fff; border:4px solid var(--gold); }
  .ev .card{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; }
  .ev .nm{ font-size:11.5pt; font-weight:800; color:var(--navy); line-height:1.15; }
  .ev .nm .q{ font-weight:600; font-size:8.4pt; color:#5a6579; font-style:italic; }
  .ev .well{ margin-top:3px; }
  .tnbox{ flex:0 0 auto; margin-top:8px; background:var(--gold-tint); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:7px 12px; display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.8pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

BODY = r"""
    <div class="prompt">Read top to bottom. Write each <b>date</b> in the well on the left; on the right, explain why the step mattered. Two dates are given &mdash; you supply the rest.</div>
    <div class="tl">
      <div class="ev">
        <div class="date"><span class="w"></span><span class="wl">write the date</span><span class="ph">Movement organizes</span></div>
        <div class="node"></div>
        <div class="card"><div class="nm">The movement organizes &mdash; NAWSA &amp; the &ldquo;Winning Plan&rdquo; <span class="q">(Carrie Chapman Catt)</span></div>
          <div class="well navy lines fill"></div></div>
      </div>
      <div class="ev">
        <div class="date"><span class="w"></span><span class="wl">write the date</span><span class="ph">Bolder tactics</span></div>
        <div class="node"></div>
        <div class="card"><div class="nm">The National Woman&rsquo;s Party &amp; bolder tactics <span class="q">(Alice Paul)</span></div>
          <div class="well navy lines fill"></div></div>
      </div>
      <div class="ev">
        <div class="date"><div class="d">1920</div></div>
        <div class="node" style="border-color:var(--red);"></div>
        <div class="card"><div class="nm" style="color:var(--red)">Aug 18, 1920 &mdash; Tennessee ratifies: the &ldquo;Perfect 36&rdquo; <span class="q">&mdash; the 36th and final state</span></div>
          <div class="well red lines fill"></div></div>
      </div>
      <div class="ev">
        <div class="date"><div class="d">1920</div></div>
        <div class="node"></div>
        <div class="card"><div class="nm">Aug 26, 1920 &mdash; the 19th Amendment is certified <span class="q">&mdash; women win the vote</span></div>
          <div class="well navy lines fill"></div></div>
      </div>
    </div>
    <div class="tnbox"><span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection.</b> On <b>August 18, 1920</b>, Tennessee became the <b>36th and final state</b> to ratify the
      19th Amendment (the &ldquo;Perfect 36&rdquo;); Nashville suffragist <b>Anne Dallas Dudley</b> led the state campaign.</span></div>
"""

ORGANIZERS = [dict(
    slug="29_us18_timeline",
    title="The Long Road to the 19th Amendment",
    kicker="Unit 2 &middot; US.18 &middot; Best-Fit Organizer",
    chips=[("Timeline &middot; Change Over Time", "navy"), ("SSP.05 &middot; DOK 2&ndash;3", "skill")],
    why=("A timeline makes the movement&rsquo;s build to ratification &mdash; and Tennessee&rsquo;s decisive role as the "
         "&ldquo;Perfect 36&rdquo; &mdash; visible from organizing, to bolder tactics, to the 1920 vote. "
         "<span class='cite'>Chronological reasoning is TN Social Studies Practice SSP.05.</span>"),
    body=BODY, extra_css=CSS, tn=True,
    udl=dict(
        scaffold="Give the two named dates on cards; students place them, then add one &ldquo;this mattered because ___&rdquo; per node.",
        extend="Draw arrows between nodes: how did organizing and bolder tactics each make ratification possible?",
        show="Students may <b>write</b> the dates, <b>say</b> the sequence, <b>draw</b> the line, or <b>build</b> it with a card timeline."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 2 &middot; US.18 (labeled)",
)]
