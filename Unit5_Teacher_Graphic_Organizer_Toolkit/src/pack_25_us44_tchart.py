# -*- coding: utf-8 -*-
"""Unit 5 labeled -- US.44 New Deal: Effects vs. Controversies (T-chart).
Two columns (navy = Effects & Achievements, red = Criticisms & Controversies)
weighed on the SAME three lenses: the economy, the role of government, and the
courts & power. The socialism charge and the court-packing fight live in the red
column; a factual note keeps the framing balanced. Every cell is a LIGHT writable
well with ONE faded hint. Verdict on the student's line. HAS a Tennessee
Connection (enduring programs). Content approved for US.44.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
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
  .tnbox{ flex:0 0 auto; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.5pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

def _cell(color, hint):
    return (f'<div class="cell"><div class="well {color} lines"></div>'
            f'<div class="fh">{hint}</div></div>')

# (lens, question, effects/achievements hint, criticisms/controversies hint)
_lenses = [
    ("The Economy", "did it work?",
     "unemployment 25% &rarr; 14%; manufacturing +60%; farm income doubled",
     "recovery incomplete &mdash; unemployment back to 19% in 1938; rising deficits"),
    ("Role of Government", "how far?",
     "FDIC, SEC &amp; Social Security &mdash; a permanent safety net",
     "&ldquo;<b>socialism</b>&rdquo; &mdash; too much control, regulation &amp; redistribution"),
    ("Courts &amp; Power", "who decides?",
     "programs survived and many still operate today",
     "&ldquo;<b>court&#8209;packing</b>&rdquo; &mdash; adding justices seen as a threat to the Court"),
]

_rows = "\n      ".join(
    f'<div class="lensrow"><div class="lens"><div class="lk">{name}</div>'
    f'<div class="lq">{q}</div></div>{_cell("navy", ah)}{_cell("red", ch)}</div>'
    for name, q, ah, ch in _lenses)

BODY = f"""
    <div class="prompt">Weigh the New Deal&rsquo;s <b>effects</b> against the <b>controversies</b> on the same three lenses. Gather evidence in each light box &mdash; then take your own position on the line at the bottom.</div>
    <div class="tc">
      <div class="tc-head">
        <div class="lensgap"></div>
        <div class="band navy sm">EFFECTS &amp; ACHIEVEMENTS<small>what the New Deal did</small></div>
        <div class="band red sm">CRITICISMS &amp; CONTROVERSIES<small>what critics charged</small></div>
      </div>
      <div class="tc-rows">
      {_rows}
      </div>
      <div class="note"><b>For balance:</b> New Deal reforms largely <b>preserved private ownership</b> while adding
      regulation and social welfare &mdash; they did not put the government in charge of industry. The court&#8209;packing
      plan <b>failed in Congress</b> but cost FDR political capital.</div>
      <div class="synth"><b>Your verdict &mdash;</b> Were the &ldquo;socialism&rdquo; charges fair? Did the New Deal go too far, or not far enough?
      ____________ <b>because</b> ______________________</div>
    </div>
    <div class="tnbox"><span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection.</b> The debate still touches daily life: New Deal creations
      &mdash; <b>Social Security, the FDIC, the SEC, and the TVA</b> &mdash; are all still operating today, in Tennessee and
      nationwide.</span></div>
"""

ORGANIZERS = [dict(
    slug="25_us44_tchart",
    title="The New Deal: Achievements &amp; Controversies",
    kicker="Unit 5 &middot; US.44 &middot; Best&#8209;Fit Organizer",
    chips=[("T&#8209;Chart &middot; Weigh Two Sides", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 3 &middot; Argument", "skill")],
    why=("The New Deal drew both praise and sharp criticism. A T&#8209;chart lays its effects beside its controversies on "
         "the same lenses, so students judge the &ldquo;socialism&rdquo; charge and the court&#8209;packing fight from evidence. "
         "<span class='cite'>Constructing and communicating an argument from evidence is a TN Social "
         "Studies Practice (SSP.04).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Define <b>socialism</b> and <b>court&#8209;packing</b> first. Fill the &ldquo;Economy&rdquo; row together before students finish.",
        extend="Argue the side you personally <b>disagree</b> with, using only its column &mdash; then weigh the balance note.",
        show="Students may <b>write</b> their cells, <b>say</b> a position aloud, or <b>debate</b> it in pairs before writing the verdict."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 5 &middot; US.44 (labeled)",
)]
