# -*- coding: utf-8 -*-
"""Unit 3 labeled -- US.20 Interventionists vs. Non-Interventionists (T-chart).
Two columns (navy = Interventionists, red = Non-Interventionists / Anti-Imperialist
League) weighed on the SAME three lenses down the left: Political, Economic, Moral.
Every cell is a LIGHT writable well carrying ONE faded italic hint students can
write over. Neutral framing: neither side is labeled right or wrong; expansion is
never called progress. The verdict lives on the student's "___ because ___" line.
Content approved for US.20.
"""

CSS = r"""
  .tc{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .tc-head{ display:flex; gap:10px; flex:0 0 auto; }
  .tc-head .lensgap{ flex:0 0 96px; }
  .tc-head .band{ flex:1 1 0; }
  .tc-head .band small{ display:block; font-weight:600; font-size:7.6pt; opacity:.9;
                        letter-spacing:0; text-transform:none; margin-top:1px; }
  .tc-rows{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .lensrow{ flex:1 1 0; display:flex; gap:10px; min-height:0; }
  .lens{ flex:0 0 96px; display:flex; flex-direction:column; align-items:center; justify-content:center;
         text-align:center; background:var(--navy-tint); border:1.6px solid var(--rule);
         border-radius:6px; padding:5px 4px; }
  .lens .lk{ font-family:Georgia,serif; font-weight:700; font-size:10.4pt; color:var(--navy); line-height:1.05; }
  .lens .lq{ font-size:6.9pt; font-style:italic; color:#7a8598; line-height:1.14; margin-top:3px; }
  .cell{ flex:1 1 0; position:relative; min-height:0; }
  .cell .well{ height:100%; }
  .cell .fh{ position:absolute; top:7px; left:11px; right:11px; font-size:8pt; font-style:italic;
             color:#aab3c4; line-height:1.2; pointer-events:none; }
  .synth{ flex:0 0 auto; background:var(--cream); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:8px 12px; font-size:9.2pt; color:var(--navy); }
  .synth b{ color:var(--navy); }
"""

def _cell(color, hint):
    return (f'<div class="cell"><div class="well {color} lines"></div>'
            f'<div class="fh">{hint}</div></div>')

# (lens name, lens question, interventionist hint, non-interventionist hint)
_lenses = [
    ("Political", "power &amp; self-government?",
     "great&#8209;power status &amp; global influence",
     "violates self&#8209;government &amp; the consent of the governed"),
    ("Economic", "cost vs. gain?",
     "opens new markets &amp; sources of resources",
     "costly wars &amp; colonies to defend and administer"),
    ("Moral", "whose ideals?",
     "the <b>stated</b> goal of spreading democracy &amp; &lsquo;uplift&rsquo;",
     "contradicts America&rsquo;s own founding ideals"),
]

_rows = "\n      ".join(
    f'<div class="lensrow"><div class="lens"><div class="lk">{name}</div>'
    f'<div class="lq">{q}</div></div>{_cell("navy", ih)}{_cell("red", nh)}</div>'
    for name, q, ih, nh in _lenses)

BODY = f"""
    <div class="prompt">Weigh both sides on the <b>same three lenses</b>. Gather evidence in each light box &mdash; then take your own position on the line at the bottom.</div>
    <div class="tc">
      <div class="tc-head">
        <div class="lensgap"></div>
        <div class="band navy sm">INTERVENTIONISTS<small>expand U.S. power overseas</small></div>
        <div class="band red sm">NON&#8209;INTERVENTIONISTS<small>Anti&#8209;Imperialist League &middot; hold back</small></div>
      </div>
      <div class="tc-rows">
      {_rows}
      </div>
      <div class="synth"><b>Your stance &mdash;</b> Should the U.S. expand overseas?
      ____________ <b>because</b> _____________________________________________</div>
    </div>
"""

ORGANIZERS = [dict(
    slug="21_us20_tchart",
    title="Should the U.S. Expand Overseas?",
    kicker="Unit 3 &middot; US.20 &middot; Best&#8209;Fit Organizer",
    chips=[("T&#8209;Chart &middot; Weigh Two Sides", "navy"), ("DOK 3 &middot; Argument", "skill")],
    why=("Interventionists and non-interventionists clashed over whether the U.S. should reach beyond its "
         "borders. A T&#8209;chart forces a decision that rests on evidence from <b>both</b> sides, weighed on "
         "the same lenses. "
         "<span class='cite'>Constructing and communicating an argument from evidence is a TN Social "
         "Studies Practice (SSP.04).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Sentence starters: &ldquo;One reason to intervene is ___.&rdquo; and &ldquo;One reason to hold back is ___.&rdquo; Fill the Political row together first.",
        extend="Argue the side you personally <b>disagree</b> with, using only evidence from its column &mdash; then name the strongest counter-argument.",
        show="Students may <b>write</b> their cells, <b>say</b> a position aloud, or <b>debate</b> it in pairs before writing the verdict."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 3 &middot; US.20 (labeled)",
)]
