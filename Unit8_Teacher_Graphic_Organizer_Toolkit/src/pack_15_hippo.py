# -*- coding: utf-8 -*-
"""Blank reproducible: HIPPO source analysis -- source citation + 5 lettered boxes."""

CSS = r"""
  .hip{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; gap:9px; }
  /* source citation box */
  .hip-src{ flex:0 0 auto; display:flex; flex-direction:column; }
  .hip-src .well{ flex:0 0 46px; }
  /* five lettered rows */
  .hip-rows{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .hip-row{ flex:1 1 0; display:flex; gap:11px; min-height:0; align-items:stretch; }
  /* gold letter tile */
  .hip-tile{ flex:0 0 60px; width:60px; background:var(--gold); border:2.5px solid #a67c1e;
    border-radius:8px; display:flex; align-items:center; justify-content:center;
    font-family:Georgia,serif; font-weight:800; font-size:30pt; color:var(--navy); }
  .hip-box{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; }
  .hip-box .lab{ font-size:9.5pt; font-weight:800; color:var(--navy); text-transform:uppercase;
    letter-spacing:.03em; margin-bottom:2px; }
  .hip-box .lab .q{ font-weight:600; text-transform:none; letter-spacing:0; color:var(--muted); font-size:8.5pt; font-style:italic; }
  .hip-box .well{ flex:1 1 auto; }
"""

def _row(letter, name, q):
    return f"""
        <div class="hip-row">
          <div class="hip-tile">{letter}</div>
          <div class="hip-box">
            <div class="lab">{name} &nbsp;<span class="q">{q}</span></div>
            <div class="well top lines"></div>
          </div>
        </div>"""

BODY = r"""
    <div class="prompt">Cite the source, then interrogate it &mdash; read it like a <b>historian</b>, one <b>H&#8209;I&#8209;P&#8209;P&#8209;O</b> question at a time.</div>
    <div class="canvas">
      <div class="hip">
        <div class="hip-src">
          <div class="band navy sm" style="border-radius:6px 6px 0 0;">SOURCE &mdash; title / author / date</div>
          <div class="well lines" style="border-radius:0 0 6px 6px;"></div>
        </div>
        <div class="hip-rows">
""" + "".join([
    _row("H", "Historical context", "What was happening at the time?"),
    _row("I", "Intended audience", "Who was it made for?"),
    _row("P", "Point of view", "Who made it &mdash; what is their bias / perspective?"),
    _row("P", "Purpose", "Why was it made? What did they want?"),
    _row("O", "Outside information", "What do you already know that connects?"),
]) + r"""
        </div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="15_hippo_blank",
    title="HIPPO &mdash; Source Analysis",
    kicker="Reusable Organizer &middot; Any Unit &middot; Any Subject",
    chips=[("Analyze a source", "navy"), ("DOK 3 &middot; Sourcing", "skill")],
    why=("Use to <b>interrogate a primary source</b> so students read like historians &mdash; questioning "
         "context, audience, point of view, and purpose instead of taking it at face value. "
         "<span class='cite'>Sourcing and contextualizing evidence is a core disciplinary practice "
         "(TN Social Studies Practices).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Model one letter aloud with the class first. Provide a question stem per box and let partners discuss before writing.",
        extend="Rank the five letters: which one most changes how you should <b>trust</b> this source, and why?",
        show="Students may <b>write</b>, <b>say</b> (record) their analysis, or <b>annotate</b> the source directly."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible",
)]
