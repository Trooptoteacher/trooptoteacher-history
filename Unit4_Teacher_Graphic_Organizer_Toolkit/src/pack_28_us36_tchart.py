# -*- coding: utf-8 -*-
"""Unit 4 labeled -- US.36 The Scopes Trial: two sides (T-chart).
Two columns (navy = Prosecution / Fundamentalism, red = Defense / Modernism)
weighed on the SAME three lenses: who led it, core argument, what's at stake.
Every cell is a LIGHT writable well with ONE faded italic hint. A factual OUTCOME
band and a reflection line sit below. Neutral framing: both sides stated fairly;
students judge the legacy. Strong Tennessee tie (Dayton, TN). Approved US.36.
"""

CSS = r"""
  .tc{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .tc-head{ display:flex; gap:10px; flex:0 0 auto; }
  .tc-head .lensgap{ flex:0 0 100px; }
  .tc-head .band{ flex:1 1 0; }
  .tc-head .band small{ display:block; font-weight:600; font-size:7.6pt; opacity:.9;
                        letter-spacing:0; text-transform:none; margin-top:1px; }
  .tc-rows{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .lensrow{ flex:1 1 0; display:flex; gap:10px; min-height:0; }
  .lens{ flex:0 0 100px; display:flex; flex-direction:column; align-items:center; justify-content:center;
         text-align:center; background:var(--navy-tint); border:1.6px solid var(--rule);
         border-radius:6px; padding:5px 4px; }
  .lens .lk{ font-family:Georgia,serif; font-weight:700; font-size:9.8pt; color:var(--navy); line-height:1.06; }
  .lens .lq{ font-size:6.9pt; font-style:italic; color:#7a8598; line-height:1.14; margin-top:3px; }
  .cell{ flex:1 1 0; position:relative; min-height:0; }
  .cell .well{ height:100%; }
  .cell .fh{ position:absolute; top:7px; left:11px; right:11px; font-size:8pt; font-style:italic;
             color:#aab3c4; line-height:1.2; pointer-events:none; }
  .outbox{ flex:0 0 auto; background:var(--navy-tint); border:1.5px solid #b9c3d6;
           border-left:6px solid var(--navy); border-radius:0 6px 6px 0; padding:6px 11px;
           font-size:8.3pt; color:#2c3446; line-height:1.32; }
  .outbox b{ color:var(--navy); }
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

# (lens name, lens question, prosecution hint, defense hint)
_lenses = [
    ("Who led it", "the figures",
     "William Jennings Bryan &mdash; 3&#8209;time candidate, fundamentalist",
     "Clarence Darrow &mdash; famed defense lawyer, skeptic"),
    ("Core argument", "the claim",
     "the Bible is literal truth; parents &amp; taxpayers control the curriculum",
     "evolution is backed by science; teachers&rsquo; freedom; church&ndash;state separation"),
    ("What&rsquo;s at stake", "the bigger fight",
     "traditional religious values seen as needed for social order",
     "modern science education; many Christians accept evolution too"),
]

_rows = "\n      ".join(
    f'<div class="lensrow"><div class="lens"><div class="lk">{name}</div>'
    f'<div class="lq">{q}</div></div>{_cell("navy", ph)}{_cell("red", dh)}</div>'
    for name, q, ph, dh in _lenses)

BODY = f"""
    <div class="prompt">John T. Scopes, a 24&#8209;year&#8209;old Dayton teacher, was tried in 1925 for teaching evolution. Weigh the <b>two sides</b> on the same three lenses, then read the outcome and take your own view.</div>
    <div class="tc">
      <div class="tc-head">
        <div class="lensgap"></div>
        <div class="band navy sm">PROSECUTION<small>Fundamentalism &middot; against teaching evolution</small></div>
        <div class="band red sm">DEFENSE<small>Modernism &middot; for teaching evolution</small></div>
      </div>
      <div class="tc-rows">
      {_rows}
      </div>
      <div class="outbox"><b>The outcome.</b> Scopes was convicted and fined <b>$100</b> (later overturned on a technicality).
      Darrow&rsquo;s cross&#8209;examination of Bryan drew national attention, and H.L. Mencken dubbed it the &ldquo;Monkey Trial.&rdquo;
      Tennessee&rsquo;s <b>Butler Act</b> stayed on the books until <b>1967</b>.</div>
      <div class="synth"><b>Your view &mdash;</b> What larger conflict did this trial reveal? ______________________________
      What did it settle &mdash; and what did it leave open? ____________________</div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> The Scopes Trial took place in <b>Dayton, Tennessee, in July 1925.</b>
        It happened here &mdash; a Tennessee teacher, a Tennessee law (the Butler Act), and a Tennessee courtroom that
        drew the whole nation&rsquo;s attention.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="28_us36_tchart",
    title="The Scopes Trial: Two Sides in a National Debate",
    kicker="Unit 4 &middot; US.36 &middot; Best&#8209;Fit Organizer",
    chips=[("T&#8209;Chart &middot; Weigh Two Sides", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 3 &middot; Argument", "skill")],
    why=("The Scopes Trial staged a clash between fundamentalism and modernism. A T&#8209;chart lays both sides on the "
         "same lenses so students see the real disagreement &mdash; then judge the legacy. "
         "<span class='cite'>Constructing and communicating an argument from evidence is a TN Social "
         "Studies Practice (SSP.04).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Sentence starters: &ldquo;The prosecution argued ___.&rdquo; and &ldquo;The defense argued ___.&rdquo; Fill the &ldquo;Who led it&rdquo; row together first.",
        extend="Argue the side you personally <b>disagree</b> with, using only its column &mdash; then name its strongest point.",
        show="Students may <b>write</b> their cells, <b>say</b> a position aloud, or <b>role&#8209;play</b> the courtroom before writing."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 4 &middot; US.36 (labeled)",
)]
