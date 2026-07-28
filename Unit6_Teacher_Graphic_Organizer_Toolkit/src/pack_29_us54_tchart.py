# -*- coding: utf-8 -*-
"""Unit 6 labeled -- US.54 Japanese American Internment & Korematsu (T-chart).
Two columns (navy = the government's wartime justification, red = the
constitutional objection) weighed on the SAME three lenses: the order, the
rationale, and the Korematsu ruling. Every cell is a LIGHT writable well with ONE
faded hint. A factual note names the constitutional principles at stake. Verdict
on the student's line. No TN tie in source. Approved US.54.
"""

CSS = r"""
  .tc{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .tc-head{ display:flex; gap:10px; flex:0 0 auto; }
  .tc-head .lensgap{ flex:0 0 104px; }
  .tc-head .band{ flex:1 1 0; }
  .tc-head .band small{ display:block; font-weight:600; font-size:7.6pt; opacity:.9;
                        letter-spacing:0; text-transform:none; margin-top:1px; }
  .tc-rows{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .lensrow{ flex:1 1 0; display:flex; gap:10px; min-height:0; }
  .lens{ flex:0 0 104px; display:flex; flex-direction:column; align-items:center; justify-content:center;
         text-align:center; background:var(--navy-tint); border:1.6px solid var(--rule);
         border-radius:6px; padding:5px 4px; }
  .lens .lk{ font-family:Georgia,serif; font-weight:700; font-size:9.6pt; color:var(--navy); line-height:1.06; }
  .lens .lq{ font-size:6.9pt; font-style:italic; color:#7a8598; line-height:1.14; margin-top:3px; }
  .cell{ flex:1 1 0; position:relative; min-height:0; }
  .cell .well{ height:100%; }
  .cell .fh{ position:absolute; top:7px; left:11px; right:11px; font-size:7.9pt; font-style:italic;
             color:#aab3c4; line-height:1.2; pointer-events:none; }
  .note{ flex:0 0 auto; background:var(--navy-tint); border:1.5px solid #b9c3d6;
         border-left:6px solid var(--navy); border-radius:0 6px 6px 0; padding:6px 11px;
         font-size:8.2pt; color:#2c3446; line-height:1.3; } .note b{ color:var(--navy); }
  .synth{ flex:0 0 auto; background:var(--cream); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:8px 12px; font-size:9pt; color:var(--navy); }
  .synth b{ color:var(--navy); }
"""

def _cell(color, hint):
    return (f'<div class="cell"><div class="well {color} lines"></div>'
            f'<div class="fh">{hint}</div></div>')

# (lens, question, government justification hint, constitutional objection hint)
_lenses = [
    ("The Order", "what happened?",
     "EO 9066 (Feb. 1942) removed ~120,000 from &ldquo;military areas&rdquo;",
     "two&#8209;thirds were U.S. <b>citizens</b>; no hearings or evidence of disloyalty"),
    ("The Rationale", "why?",
     "&ldquo;military necessity&rdquo; &mdash; fear of espionage after Pearl Harbor",
     "no such detention of German/Italian Americans &rarr; a <b>racial</b> basis"),
    ("Korematsu (1944)", "the ruling",
     "the Supreme Court <b>upheld</b> the order 6&ndash;3 as wartime necessity",
     "dissenters: racial discrimination; detention without charges"),
]

_rows = "\n      ".join(
    f'<div class="lensrow"><div class="lens"><div class="lk">{name}</div>'
    f'<div class="lq">{q}</div></div>{_cell("navy", gh)}{_cell("red", oh)}</div>'
    for name, q, gh, oh in _lenses)

BODY = f"""
    <div class="prompt">Weigh the government&rsquo;s <b>justification</b> against the <b>constitutional objection</b> on the same three lenses. Gather evidence in each light box &mdash; then take your own position on the line at the bottom.</div>
    <div class="tc">
      <div class="tc-head">
        <div class="lensgap"></div>
        <div class="band navy sm">THE GOVERNMENT&rsquo;S CASE<small>wartime security</small></div>
        <div class="band red sm">THE CONSTITUTIONAL OBJECTION<small>civil liberties</small></div>
      </div>
      <div class="tc-rows">
      {_rows}
      </div>
      <div class="note"><b>The principles at stake:</b> internment raised questions of <b>due process</b> (no individual
      hearings), <b>equal protection</b> (a race&#8209;based policy), and <b>habeas corpus</b> (detention without charges) &mdash;
      the core protections the Constitution is meant to guarantee even in wartime.</div>
      <div class="synth"><b>Your verdict &mdash;</b> When national security and civil liberties collide, which should win &mdash; and who decides?
      ____________ <b>because</b> ______________________</div>
    </div>
"""

ORGANIZERS = [dict(
    slug="29_us54_tchart",
    title="Security vs. the Constitution: Japanese American Internment",
    kicker="Unit 6 &middot; US.54 &middot; Best&#8209;Fit Organizer",
    chips=[("T&#8209;Chart &middot; Weigh Two Sides", "navy"), ("DOK 3 &middot; Argument", "skill")],
    why=("Internment forced a clash between wartime security and constitutional rights. A T&#8209;chart lays the "
         "government&rsquo;s case beside the constitutional objection on the same lenses, so students judge from evidence. "
         "<span class='cite'>Constructing and communicating an argument from evidence is a TN Social "
         "Studies Practice (SSP.04).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Define <b>due process</b>, <b>equal protection</b>, and <b>habeas corpus</b> first. Fill the &ldquo;Order&rdquo; row together.",
        extend="The Court sided with the government in 1944. Using the objection column, argue how a court might rule differently today.",
        show="Students may <b>write</b> their cells, <b>say</b> a position aloud, or hold a structured <b>debate</b> before writing."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 6 &middot; US.54 (labeled)",
)]
