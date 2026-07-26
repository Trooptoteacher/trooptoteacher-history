# -*- coding: utf-8 -*-
"""Blank reproducible: Frayer Model (Vocabulary) -- 2x2 quadrants + center oval term."""

CSS = r"""
  .fr{ flex:1 1 auto; position:relative; min-height:0; display:flex; flex-direction:column; }
  .fr-grid{ flex:1 1 auto; display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr;
    gap:0; min-height:0; }
  .fr-q{ position:relative; border:1.6px solid var(--rule); background:var(--paper); min-height:0; }
  .fr-q.lines{ background-image:repeating-linear-gradient(to bottom, transparent 0 30px, var(--wl) 30px 31px);
    background-position:0 34px; }
  /* corner rounding to frame the whole 2x2 as one block */
  .fr-q.tl{ border-radius:10px 0 0 0; border-right:none; border-bottom:none; }
  .fr-q.tr{ border-radius:0 10px 0 0; border-bottom:none; }
  .fr-q.bl{ border-radius:0 0 0 10px; border-right:none; }
  .fr-q.br{ border-radius:0 0 10px 0; }
  .fr-lbl{ position:absolute; font-size:9pt; font-weight:800; letter-spacing:.03em;
    color:var(--navy); text-transform:uppercase; z-index:3; background:var(--paper); padding:0 3px; }
  /* all four labels sit at the TOP of their quadrant, so writing space reads
     the same in every quadrant (outer-corner placement clears the center oval) */
  .fr-lbl.tl{ top:8px; left:12px; } .fr-lbl.tr{ top:8px; right:12px; }
  .fr-lbl.bl{ top:8px; left:12px; } .fr-lbl.br{ top:8px; right:12px; }
  .fr-lbl .n{ color:var(--muted); font-weight:800; }
  /* center oval holding the term */
  .fr-oval{ position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
    width:31%; height:26%; min-width:186px; background:var(--cream); border:3.5px solid var(--navy);
    border-radius:50%; display:flex; flex-direction:column; align-items:center; justify-content:center;
    text-align:center; z-index:5; box-shadow:0 0 0 6px var(--paper); padding:6px 10px; }
  .fr-oval .k{ font-size:8pt; font-weight:800; letter-spacing:.08em; text-transform:uppercase; color:var(--red); }
  .fr-oval .wl{ display:block; width:74%; border-bottom:2px solid var(--navy); height:16px; margin:14px auto 0; }
"""

BODY = r"""
    <div class="prompt">Write the <b>term</b> in the center oval. Then fill each corner: your own <b>definition</b>, key <b>characteristics</b>, real <b>examples</b>, and <b>non&#8209;examples</b>.</div>
    <div class="canvas">
      <div class="fr">
        <div class="fr-grid">
          <div class="fr-q tl lines"><div class="fr-lbl tl"><span class="n">1.</span> Definition &mdash; in your own words</div></div>
          <div class="fr-q tr lines"><div class="fr-lbl tr"><span class="n">2.</span> Characteristics / facts</div></div>
          <div class="fr-q bl lines"><div class="fr-lbl bl"><span class="n">3.</span> Examples</div></div>
          <div class="fr-q br lines"><div class="fr-lbl br"><span class="n">4.</span> Non&#8209;examples</div></div>
        </div>
        <div class="fr-oval">
          <span class="k">Term / Word</span>
          <span class="wl"></span>
        </div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="13_frayer_blank",
    title="Frayer Model &mdash; Vocabulary",
    kicker="Reusable Organizer &middot; Any Unit &middot; Any Subject",
    chips=[("Learn a term", "navy"), ("DOK 1&ndash;2 &middot; Vocabulary", "skill")],
    why=("Use to build <b>deep word knowledge</b> &mdash; not just a definition, but traits, examples, and "
         "non&#8209;examples that sharpen the boundary of a concept. "
         "<span class='cite'>Contrasting examples with non&#8209;examples strengthens concept learning "
         "(Marzano &mdash; similarities &amp; differences).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Pre&#8209;fill the term and one example. Offer a definition frame: &ldquo;A ___ is a ___ that ___.&rdquo; Let partners brainstorm non&#8209;examples aloud first.",
        extend="Add a sentence using the term correctly, then explain <b>why</b> one non&#8209;example does <i>not</i> fit.",
        show="Students may <b>write</b>, <b>say</b> (record), <b>draw</b> an icon for each example, or <b>build</b> the quadrants with sticky notes."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible",
)]
