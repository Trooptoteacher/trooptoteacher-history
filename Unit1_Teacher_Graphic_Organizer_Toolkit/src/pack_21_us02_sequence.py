# -*- coding: utf-8 -*-
"""Unit 1 labeled — US.02 Federal Policies Toward American Indians.
Sequence / cause-effect chain: reservations -> assimilation -> boarding schools
-> Dawes Act (1887). Topics sourced from the course standards inventory (US.02).
"""

CSS = r"""
  .seq{ flex:1 1 auto; display:flex; flex-direction:column; gap:0; min-height:0; }
  .stage{ display:flex; gap:11px; align-items:stretch; flex:1 1 0; min-height:0; }
  .stage .num{ flex:0 0 40px; display:flex; align-items:center; justify-content:center;
               background:var(--navy); color:#fff; font-family:Georgia,serif; font-weight:700; font-size:17pt; border-radius:8px; }
  .stage.gold .num{ background:var(--gold); color:var(--navy); }
  .stage .card{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; }
  .stage .lab{ display:flex; align-items:baseline; gap:9px; }
  .stage .lab .nm{ font-size:12.5pt; font-weight:800; color:var(--navy); }
  .stage .lab .yr{ font-size:9pt; font-weight:800; color:var(--red); letter-spacing:.04em; }
  .stage .lab .q{ font-size:8.5pt; color:#5a6579; font-style:italic; }
  .stage .well{ margin-top:4px; }
  .seq-arrow{ height:22px; display:flex; align-items:center; padding-left:14px; flex:0 0 auto; }
  .seq-arrow .a{ width:0;height:0;border-left:9px solid transparent;border-right:9px solid transparent;border-top:12px solid var(--gold); }
  .seq-arrow .cap{ font-size:7.6pt; font-weight:800; color:var(--muted); text-transform:uppercase; letter-spacing:.06em; margin-left:10px; }
  .endbox{ flex:0 0 auto; margin-top:6px; background:var(--red-tint); border:1.6px solid var(--red); border-left:6px solid var(--red);
           border-radius:0 6px 6px 0; padding:7px 12px; font-size:9pt; color:#3a1f22; }
  .endbox b{ color:var(--red); }
"""

BODY = r"""
    <div class="prompt">Federal policy toward American Indian nations moved step by step. Explain each step &mdash; and where it was heading.</div>
    <div class="seq">
      <div class="stage">
        <div class="num">1</div>
        <div class="card">
          <div class="lab"><span class="nm">Reservations</span><span class="q">Confine nations to bounded land &mdash; why, and with what promises?</span></div>
          <div class="well navy lines fill"></div>
        </div>
      </div>
      <div class="seq-arrow"><span class="a"></span><span class="cap">led to &mdash;</span></div>
      <div class="stage">
        <div class="num">2</div>
        <div class="card">
          <div class="lab"><span class="nm">Assimilation policy</span><span class="q">Pressure to give up language, land-holding &amp; culture &mdash; what was the goal?</span></div>
          <div class="well navy lines fill"></div>
        </div>
      </div>
      <div class="seq-arrow"><span class="a"></span><span class="cap">led to &mdash;</span></div>
      <div class="stage">
        <div class="num">3</div>
        <div class="card">
          <div class="lab"><span class="nm">Boarding schools</span><span class="q">Children removed from families &mdash; what was taken, and what was the aim?</span></div>
          <div class="well navy lines fill"></div>
        </div>
      </div>
      <div class="seq-arrow"><span class="a"></span><span class="cap">led to &mdash;</span></div>
      <div class="stage gold">
        <div class="num">4</div>
        <div class="card">
          <div class="lab"><span class="nm">Dawes Act</span><span class="yr">1887</span><span class="q">Communal land split into individual allotments; &ldquo;surplus&rdquo; sold &mdash; who lost land?</span></div>
          <div class="well gold lines fill"></div>
        </div>
      </div>
      <div class="endbox"><b>Cause &rarr; Effect:</b> These four steps shared one goal: ____________________________. Their combined effect on American Indian nations was ____________________________________________.</div>
    </div>
"""

ORGANIZERS = [dict(
    slug="21_us02_sequence",
    title="Federal Policy Toward American Indian Nations",
    kicker="Unit 1 &middot; US.02 &middot; Best-Fit Organizer",
    chips=[("Sequence &middot; Cause &rarr; Effect", "navy"), ("SSP.05 &middot; DOK 2&ndash;3", "skill")],
    why=("A sequence chain shows students that federal policy was a deliberate, escalating campaign &mdash; "
         "reservations, assimilation, boarding schools, and the 1887 Dawes Act &mdash; not a set of unrelated events. "
         "<span class='cite'>Ordering causes &amp; effects builds TN Social Studies Practice SSP.05.</span>"),
    body=BODY, extra_css=CSS,
    udl=dict(
        scaffold="Provide the four stage names on cards; students sequence them first, then explain one clause each using &ldquo;so that ___.&rdquo;",
        extend="Argue: which single step did the most lasting damage to tribal sovereignty? Cite the chain to defend it.",
        show="Students may <b>write</b> each step, <b>say</b> the chain aloud, <b>draw</b> arrows &amp; icons, or <b>build</b> it with sequence cards."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 1 &middot; US.02 (labeled)",
)]
