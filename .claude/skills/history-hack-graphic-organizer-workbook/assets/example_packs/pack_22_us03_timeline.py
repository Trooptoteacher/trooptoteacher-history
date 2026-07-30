# -*- coding: utf-8 -*-
"""Unit 1 labeled — US.03 End of Reconstruction -> Jim Crow -> Plessy.
Vertical timeline (DATE at LEFT of the event, per toolkit rule).
Topics sourced from the standards inventory (US.03: Compromise of 1877, Jim Crow,
Plessy). TN tie (T.C.A. 49-6-1006 requires this instruction) per the guide.
"""

CSS = r"""
  .tl{ flex:1 1 auto; position:relative; display:flex; flex-direction:column; min-height:0; padding-left:150px; }
  .tl::before{ content:""; position:absolute; left:132px; top:6px; bottom:6px; width:4px; background:var(--navy); border-radius:2px; }
  .ev{ flex:1 1 0; display:flex; align-items:stretch; position:relative; min-height:0; padding:5px 0; }
  .ev .date{ position:absolute; left:-150px; top:5px; width:120px; text-align:right; }
  .ev .date .d{ font-family:Georgia,serif; font-size:15pt; font-weight:700; color:var(--red); line-height:1; }
  .ev .date .w{ display:block; border-bottom:1.6px solid var(--rule); height:15px; margin-top:6px; }
  .ev .date .wl{ font-size:7pt; color:#8792a4; font-style:italic; }
  .ev .node{ position:absolute; left:-24px; top:6px; width:20px; height:20px; border-radius:50%;
             background:#fff; border:4px solid var(--gold); }
  .ev .card{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; }
  .ev .nm{ font-size:12pt; font-weight:800; color:var(--navy); }
  .ev .nm .q{ font-weight:600; font-size:8.6pt; color:#5a6579; font-style:italic; }
  .ev .well{ margin-top:3px; }
  .tnbox{ flex:0 0 auto; margin-top:6px; background:var(--gold-tint); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:7px 12px; display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.8pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

BODY = r"""
    <div class="prompt">Write each <b>date</b> on the left, then explain why the event mattered. Watch how one election reshaped a generation.</div>
    <div class="tl">
      <div class="ev">
        <div class="date"><div class="d">1876</div><span class="w"></span><span class="wl">write the date</span></div>
        <div class="node"></div>
        <div class="card"><div class="nm">Disputed presidential election <span class="q">&mdash; Hayes vs. Tilden; who really won?</span></div>
          <div class="well navy lines fill"></div></div>
      </div>
      <div class="ev">
        <div class="date"><div class="d">1877</div><span class="w"></span></div>
        <div class="node"></div>
        <div class="card"><div class="nm">Compromise of 1877 <span class="q">&mdash; federal troops leave the South; Reconstruction ends</span></div>
          <div class="well navy lines fill"></div></div>
      </div>
      <div class="ev">
        <div class="date"><div class="d">1880s&ndash;90s</div><span class="w"></span></div>
        <div class="node"></div>
        <div class="card"><div class="nm">Jim Crow &amp; disenfranchisement <span class="q">&mdash; segregation laws; poll taxes, literacy tests</span></div>
          <div class="well navy lines fill"></div></div>
      </div>
      <div class="ev">
        <div class="date"><div class="d">1896</div><span class="w"></span></div>
        <div class="node" style="border-color:var(--red);"></div>
        <div class="card"><div class="nm" style="color:var(--red)">Plessy v. Ferguson <span class="q">&mdash; &ldquo;separate but equal&rdquo; upheld</span></div>
          <div class="well red lines fill"></div></div>
      </div>
    </div>
    <div class="tnbox"><span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection.</b> Tennessee law (<b>T.C.A. &sect; 49-6-1006</b>) requires that this history &mdash;
      the end of Reconstruction, Jim Crow, and the disenfranchisement of Black Tennesseans &mdash; be taught. On the line above, mark where
      Tennessee&rsquo;s own laws followed the national pattern.</span></div>
"""

ORGANIZERS = [dict(
    slug="22_us03_timeline",
    title="From a Disputed Election to <span style='font-family:Georgia;font-style:italic'>Plessy</span>",
    kicker="Unit 1 &middot; US.03 &middot; Best-Fit Organizer",
    chips=[("Timeline &middot; Change Over Time", "navy"), ("SSP.05 &middot; DOK 2&ndash;3", "skill")],
    why=("A timeline makes the through-line visible: the 1876 election bargain (Compromise of 1877) ended Reconstruction "
         "and opened the door to Jim Crow and <span style='font-family:Georgia;font-style:italic'>Plessy</span> (1896). "
         "<span class='cite'>Chronological reasoning is TN Social Studies Practice SSP.05.</span>"),
    body=BODY, extra_css=CSS, tn=True,
    udl=dict(
        scaffold="Give the four dates on cards; students place them on the spine first, then add one &ldquo;this mattered because ___&rdquo; per node.",
        extend="Draw arrows between nodes to show cause &amp; effect: how did each step make the next one possible?",
        show="Students may <b>write</b> the dates, <b>say</b> the sequence, <b>draw</b> the line, or <b>build</b> it with a card timeline."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 1 &middot; US.03 (labeled)",
)]
