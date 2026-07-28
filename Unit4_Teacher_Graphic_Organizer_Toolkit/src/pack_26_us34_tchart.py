# -*- coding: utf-8 -*-
"""Unit 4 labeled -- US.34 Women in the 1920s: Changes vs. Limitations (T-chart).
Two columns (navy = Changes/Gains, red = Limits/Continuities) weighed on the SAME
three lenses down the left: Social & Cultural, Work & Economy, Body & Education.
Every cell is a LIGHT writable well carrying ONE faded italic hint students can
write over. Neutral framing: neither column is labeled right or wrong; the verdict
lives on the student's "___ because ___" line. No TN tie in source. Approved US.34.
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
  .lens .lk{ font-family:Georgia,serif; font-weight:700; font-size:9.8pt; color:var(--navy); line-height:1.06; }
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

# (lens name, lens question, changes/gains hint, limits/continuities hint)
_lenses = [
    ("Social &amp; Cultural", "new freedoms?",
     "flappers &mdash; bob haircuts, shorter skirts, voting, individual choice",
     "sparked backlash &amp; moral debates; older expectations persisted"),
    ("Work &amp; Economy", "better jobs?",
     "clerical work 75,000 (1900) &rarr; 1.4M (1930); cleaner, better&#8209;paid office jobs",
     "lower pay than men; &ldquo;marriage bars&rdquo;; limited advancement"),
    ("Body &amp; Education", "more control?",
     "birth control (Sanger, first clinic 1916); family size 7&rarr;3; women&rsquo;s colleges",
     "Sanger arrested repeatedly; access limited &amp; controversial"),
]

_rows = "\n      ".join(
    f'<div class="lensrow"><div class="lens"><div class="lk">{name}</div>'
    f'<div class="lq">{q}</div></div>{_cell("navy", ch)}{_cell("red", li)}</div>'
    for name, q, ch, li in _lenses)

BODY = f"""
    <div class="prompt">Weigh <b>changes</b> against <b>limits</b> on the <b>same three lenses</b>. Gather evidence in each light box &mdash; then take your own position on the line at the bottom.</div>
    <div class="tc">
      <div class="tc-head">
        <div class="lensgap"></div>
        <div class="band navy sm">CHANGES &amp; GAINS<small>what was new for women</small></div>
        <div class="band red sm">LIMITS &amp; CONTINUITIES<small>what stayed the same or held back</small></div>
      </div>
      <div class="tc-rows">
      {_rows}
      </div>
      <div class="synth"><b>Your call &mdash;</b> Did the 1920s <b>fundamentally</b> change women&rsquo;s status, or mostly the surface?
      ____________ <b>because</b> ______________________________________</div>
    </div>
"""

ORGANIZERS = [dict(
    slug="26_us34_tchart",
    title="Women in the 1920s: How Far Did Change Go?",
    kicker="Unit 4 &middot; US.34 &middot; Best&#8209;Fit Organizer",
    chips=[("T&#8209;Chart &middot; Weigh Two Sides", "navy"), ("DOK 3 &middot; Argument", "skill")],
    why=("The 1920s brought real changes for women &mdash; and real limits. A T&#8209;chart forces a judgment that rests on "
         "evidence from <b>both</b> sides, weighed on the same lenses. "
         "<span class='cite'>Constructing and communicating an argument from evidence is a TN Social "
         "Studies Practice (SSP.04).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Sentence starters: &ldquo;One thing that changed was ___.&rdquo; and &ldquo;One thing that stayed the same was ___.&rdquo; Fill the Social row together first.",
        extend="Which lens shows the <b>biggest</b> change? Which shows the least? Rank them and defend the order.",
        show="Students may <b>write</b> their cells, <b>say</b> a position aloud, or <b>debate</b> it in pairs before writing the verdict."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 4 &middot; US.34 (labeled)",
)]
