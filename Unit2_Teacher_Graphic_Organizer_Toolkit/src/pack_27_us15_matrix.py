# -*- coding: utf-8 -*-
"""Unit 2 labeled matrix.
US.15: Progressive reforms that widened democracy -- Initiative, Referendum,
       Recall, Direct Primary, 17th Amendment -- analyzed on two criteria
       (what it lets citizens do | how it expands democracy).
TN tie: statewide prohibition (1909), a decade before the 18th Amendment.
Neutral framing: descriptive criteria; students judge which gave the most power.
"""

CSS = r"""
  .mx{ flex:1 1 auto; display:grid; gap:5px; min-height:0; }
  .mx .corner{ background:transparent; }
  .mx .chead{ color:#fff; font-weight:800; font-size:10.5pt; text-align:center; padding:8px 6px; border-radius:6px; display:flex; flex-direction:column; justify-content:center; background:var(--navy); }
  .mx .rhead{ background:var(--navy); color:#fff; font-weight:800; font-size:10pt; padding:6px 10px; border-radius:6px; display:flex; flex-direction:column; justify-content:center; }
  .mx .rhead small{ font-weight:600; font-size:7.4pt; opacity:.9; font-style:italic; }
  .mx .cell{ background:var(--paper); border:1.5px solid var(--rule); border-radius:6px;
             background-image:repeating-linear-gradient(to bottom, transparent 0 28px, var(--wl) 28px 29px);
             background-position:0 10px; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:7px 12px; display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.9pt; line-height:1.32; color:#3a2f12; }
  .tnbox .t b{ color:#7a5c15; }
  .cbar{ flex:0 0 auto; margin-top:7px; background:var(--cream); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
         border-radius:0 6px 6px 0; padding:7px 11px; font-size:9pt; color:var(--navy); text-align:center; } .cbar b{ color:var(--navy); }
"""

COLS = ["What it lets citizens do", "How it expands democracy"]
REFORMS = [
    ("Initiative", "citizens propose laws"),
    ("Referendum", "voters approve/reject laws"),
    ("Recall", "voters remove officials"),
    ("Direct Primary", "voters pick nominees"),
    ("17th Amendment", "direct election of senators"),
]

def _grid():
    cells = ['<div class="corner"></div>']
    for nm in COLS:
        cells.append(f'<div class="chead">{nm}</div>')
    for nm, sub in REFORMS:
        cells.append(f'<div class="rhead">{nm}<small>{sub}</small></div>')
        for _ in COLS:
            cells.append('<div class="cell"></div>')
    return ('<div class="mx" style="grid-template-columns:0.95fr 1.35fr 1.35fr; '
            'grid-template-rows:auto 1fr 1fr 1fr 1fr 1fr;">' + "".join(cells) + '</div>')

BODY = f"""
    <div class="prompt">Analyze each reform on the same two questions. Track how power shifts <b>toward ordinary citizens</b>.</div>
    {_grid()}
    <div class="tnbox">
      <span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection &mdash;</b> Tennessee adopted several Progressive reforms, including
      statewide <b>prohibition in 1909</b> &mdash; a decade before the 18th Amendment.</span>
    </div>
    <div class="cbar"><b>Decide:</b> Which reform gave ordinary citizens the most power? ____________ <b>because</b> ____________________________________</div>
"""

_UDL = dict(
    scaffold="Complete the Initiative row together; give a word bank (propose, approve, remove, nominate, elect) for the rest.",
    extend="Rank the five reforms by how much power each gives citizens, and defend your order with matrix evidence.",
    show="Students may <b>write</b> in cells, <b>say</b> a row aloud, <b>draw</b> an icon per reform, or <b>build</b> it as a sort.")

ORGANIZERS = [
    dict(
        slug="27_us15_matrix",
        title="Reforms That Widened Democracy",
        kicker="Unit 2 &middot; US.15 &middot; Best-Fit Organizer",
        chips=[("Matrix &middot; Analyze Reforms", "navy"), ("DOK 3 &middot; Analysis", "skill")],
        why=("Analyzing reforms against shared criteria shows how Progressives shifted power toward ordinary citizens &mdash; "
             "and lets students compare their reach side by side. "
             "<span class='cite'>Structured comparison across criteria is Marzano&rsquo;s highest-yield strategy.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL, tn=True,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 2 &middot; US.15 (labeled)",
    ),
]
