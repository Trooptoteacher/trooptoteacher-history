# -*- coding: utf-8 -*-
"""Unit 4 labeled -- US.38 Credit, Consumerism & Financial Speculation (concept web).
Center hub = "THE 1920s BOOM" as a faint watermark over writing lines. Four spokes
= buying on credit, consumerism, advertising, stock speculation -- each a LIGHT
bubble with a bold anchor label and a FADED italic content hint. A bottom RED
"warning signs" box captures the hidden risks that bridge to Unit 5 (the crash).
Neutral framing: drivers described factually. No TN tie in source. Approved US.38.
"""

CSS = r"""
  .web-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .web-wrap > svg{ position:absolute; inset:0; width:100%; height:100%; }
  .node{ position:absolute; transform:translate(-50%,-50%);
         display:flex; flex-direction:column; align-items:stretch; justify-content:flex-start;
         background:var(--paper); border:2px solid var(--navy); border-radius:16px; padding:6px 12px 8px; }
  .node .nlab{ font-family:Georgia,serif; font-weight:700; font-size:10pt; color:var(--navy);
         line-height:1.04; text-align:center; }
  .node .nsub{ font-size:7.3pt; font-style:italic; color:#9aa6bd; text-align:center; line-height:1.16; margin-top:3px; }
  .node .nline{ border-bottom:1.4px dashed #C4CCDA; height:0; margin-top:9px; }
  .hub{ background:var(--navy-tint); border:3px solid var(--navy); border-radius:50%;
        align-items:center; justify-content:center; padding:0; }
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:12pt; color:#97a2ba;
              letter-spacing:.02em; text-align:center; line-height:1.04; text-transform:uppercase; }
  .hub .hguides{ position:absolute; left:14%; right:14%; bottom:20%; }
  .hub .hguides .nline{ border-bottom-color:#9aa6bd; margin-top:12px; }
  .warnbox{ flex:0 0 auto; margin-top:7px; display:flex; flex-direction:column; }
  .warnbox .band{ border-radius:6px 6px 0 0; display:flex; align-items:center; gap:7px; }
  .warnbox .band .wsig{ font-size:11pt; }
  .warnbox .well{ min-height:66px; }
  .warnbox .fh{ position:absolute; top:7px; left:12px; right:12px; font-size:8pt; font-style:italic;
             color:#c69aa0; line-height:1.4; }
  .bridge{ flex:0 0 auto; margin-top:7px; background:var(--cream); border:1.6px solid var(--gold);
           border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 11px;
           font-size:8.6pt; color:var(--navy); line-height:1.3; } .bridge b{ color:var(--navy); }
"""


def _node(x, y, w, h, lab, sub):
    return (f'<div class="node" style="left:{x}%; top:{y}%; width:{w}px; height:{h}px;">'
            f'<div class="nlab">{lab}</div><div class="nsub">{sub}</div>'
            f'<div class="nline"></div><div class="nline"></div></div>')


# four spokes: (x%, y%, anchor label, faded content hint)
_outer = [
    (21, 20, "Buying on Credit", "installment &ldquo;buy now, pay later&rdquo;; debt $3.3B (1920) &rarr; $7.6B (1929)"),
    (79, 20, "Consumerism", "possessions become identity &amp; status; mass&#8209;produced goods for all"),
    (21, 82, "Advertising", "brand loyalty through emotional appeals &amp; lifestyle marketing"),
    (79, 82, "Stock Speculation", "buying &ldquo;on margin&rdquo; (10% down); ordinary people invest savings"),
]
_outer_html = "\n        ".join(_node(x, y, 208, 96, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is the boom. On each bubble, write how that force drove 1920s prosperity &mdash; the faint notes are starters. Then fill the red box: what <b>warning signs</b> hid beneath the boom?</div>
    <div class="canvas">
      <div class="web-wrap">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none">
          <g stroke="#C4CCDA" stroke-width="0.7">
            <line x1="50" y1="50" x2="21" y2="20"/>
            <line x1="50" y1="50" x2="79" y2="20"/>
            <line x1="50" y1="50" x2="21" y2="82"/>
            <line x1="50" y1="50" x2="79" y2="82"/>
          </g>
        </svg>
        {_outer_html}
        <div class="node hub" style="left:50%; top:51%; width:210px; height:150px;">
          <div class="hcue">The 1920s<br/>Boom</div>
          <div class="hguides"><div class="nline"></div><div class="nline"></div></div>
        </div>
      </div>
      <div class="warnbox">
        <div class="band red sm"><span class="wsig">&#9888;</span>Warning signs beneath the prosperity</div>
        <div class="well tint-red lines" style="position:relative;">
          <span class="fh">overproduction &nbsp;&middot;&nbsp; income inequality limiting buying power &nbsp;&middot;&nbsp; a small price drop could trigger forced selling (margin calls) &mdash; an unsustainable bubble</span>
        </div>
      </div>
      <div class="bridge"><b>Looking ahead &rarr;</b> credit, consumerism, and speculation fed each other into a bubble.
      In <b>Unit 5</b>, you&rsquo;ll see what happened when it burst &mdash; the Great Depression.</div>
    </div>
"""

ORGANIZERS = [dict(
    slug="30_us38_conceptweb",
    title="The 1920s Boom &mdash; and Its Hidden Risks",
    kicker="Unit 4 &middot; US.38 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("DOK 3 &middot; Analyze", "skill")],
    why=("A web shows credit, consumerism, advertising, and speculation as one system driving the boom &mdash; and how "
         "the same forces built a hidden risk. "
         "<span class='cite'>Connecting causes into one picture and reasoning about consequences builds SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the four bubble labels as a word bank and fill one together. Ask: how does &ldquo;buy now, pay later&rdquo; grow sales?",
        extend="Draw links <b>between</b> bubbles to show how they fed each other &mdash; then explain how prosperity became risk.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>draw</b> the boom&#8209;to&#8209;bubble cycle as a diagram."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 4 &middot; US.38 (labeled)",
)]
