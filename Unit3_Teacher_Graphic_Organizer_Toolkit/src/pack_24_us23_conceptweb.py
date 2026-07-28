# -*- coding: utf-8 -*-
"""Unit 3 labeled -- US.23 Causes of World War I & U.S. Neutrality (concept web).
Center hub = "WORLD WAR I" as a faint watermark over writing lines. Four spokes =
the M.A.I.N. causes, each a LIGHT bubble with a bold M/A/I/N anchor label and a
FADED italic content hint students write over. A red "spark" callout sits by the
hub; a separate LIGHT box captures reasons for early U.S. neutrality.
Content approved for US.23. No TN box, no star. Neutral, causal framing.
"""

CSS = r"""
  .web-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .web-wrap > svg{ position:absolute; inset:0; width:100%; height:100%; }
  .node{ position:absolute; transform:translate(-50%,-50%);
         display:flex; flex-direction:column; align-items:stretch; justify-content:flex-start;
         background:var(--paper); border:2px solid var(--navy); border-radius:16px; padding:6px 12px 8px; }
  .node .nlab{ font-family:Georgia,serif; font-weight:700; font-size:10.4pt; color:var(--navy);
         line-height:1.04; text-align:center; }
  .node .nlab b{ color:var(--red); }
  .node .nsub{ font-size:7.4pt; font-style:italic; color:#9aa6bd; text-align:center; line-height:1.16; margin-top:3px; }
  .node .nline{ border-bottom:1.4px dashed #C4CCDA; height:0; margin-top:9px; }
  .hub{ background:var(--navy-tint); border:3px solid var(--navy); border-radius:50%;
        align-items:center; justify-content:center; padding:0; }
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:13pt; color:#97a2ba;
              letter-spacing:.02em; text-align:center; line-height:1.02; text-transform:uppercase; }
  .hub .hguides{ position:absolute; left:15%; right:15%; bottom:22%; }
  .hub .hguides .nline{ border-bottom-color:#9aa6bd; margin-top:12px; }
  .spark{ position:absolute; transform:translate(-50%,-50%); background:var(--red-tint);
          border:2px dashed var(--red); border-radius:12px; padding:5px 10px 6px;
          display:flex; flex-direction:column; align-items:center; text-align:center; }
  .spark .scue{ font-size:7pt; font-weight:800; letter-spacing:.08em; text-transform:uppercase; color:var(--red); }
  .spark .stx{ font-size:8pt; color:#7a2731; line-height:1.14; margin-top:2px; font-weight:600; }
  .neut{ flex:0 0 auto; margin-top:7px; display:flex; flex-direction:column; }
  .neut .band{ border-radius:6px 6px 0 0; }
  .neut .well{ min-height:76px; }
  .neut .fh{ position:absolute; top:7px; left:12px; right:12px; font-size:8pt; font-style:italic;
             color:#9aa6bd; line-height:1.4; }
"""


def _node(x, y, w, h, lab, sub):
    return (f'<div class="node" style="left:{x}%; top:{y}%; width:{w}px; height:{h}px;">'
            f'<div class="nlab">{lab}</div><div class="nsub">{sub}</div>'
            f'<div class="nline"></div><div class="nline"></div></div>')


# four M.A.I.N. spokes: (x%, y%, anchor label, faded content hint)
_outer = [
    (21, 20, "<b>M</b>&middot; Militarism", "arms race &middot; glorifying military power"),
    (79, 20, "<b>A</b>&middot; Alliances", "one conflict pulls in many nations"),
    (21, 82, "<b>I</b>&middot; Imperialism", "competition for colonies &amp; resources"),
    (79, 82, "<b>N</b>&middot; Nationalism", "national pride &amp; rivalry &middot; self-determination"),
]
_outer_html = "\n        ".join(_node(x, y, 202, 96, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is the war itself. On each <b>M.A.I.N.</b> bubble, write how that force pushed Europe toward war &mdash; the faint notes are starters. The dashed callout is the <b>spark</b>.</div>
    <div class="canvas">
      <div class="web-wrap">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none">
          <g stroke="#C4CCDA" stroke-width="0.7">
            <line x1="50" y1="50" x2="21" y2="20"/>
            <line x1="50" y1="50" x2="79" y2="20"/>
            <line x1="50" y1="50" x2="21" y2="82"/>
            <line x1="50" y1="50" x2="79" y2="82"/>
          </g>
          <g stroke="#E0A9AE" stroke-width="0.7" stroke-dasharray="1.6 1.6">
            <line x1="50" y1="50" x2="50" y2="12"/>
          </g>
        </svg>
        {_outer_html}
        <div class="spark" style="left:50%; top:12%; width:206px;">
          <span class="scue">&#9889; The Spark</span>
          <span class="stx">Assassination of Archduke Franz Ferdinand (1914)</span>
        </div>
        <div class="node hub" style="left:50%; top:51%; width:206px; height:150px;">
          <div class="hcue">World<br/>War&nbsp;I</div>
          <div class="hguides"><div class="nline"></div><div class="nline"></div></div>
        </div>
      </div>
      <div class="neut">
        <div class="band navy sm">Why did the U.S. stay neutral (at first)?</div>
        <div class="well lines" style="position:relative;">
          <span class="fh">geographic distance &nbsp;&middot;&nbsp; a diverse immigrant population with ties to both sides &nbsp;&middot;&nbsp;
          the tradition of avoiding &ldquo;entangling alliances&rdquo; &nbsp;&middot;&nbsp; profitable trade with both sides</span>
        </div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="24_us23_conceptweb",
    title="What Set the World on Fire",
    kicker="Unit 3 &middot; US.23 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web &middot; M.A.I.N.", "navy"), ("DOK 2 &middot; Causation", "skill")],
    why=("The web makes the <b>M.A.I.N.</b> mnemonic visible as one system feeding the war &mdash; four long-run "
         "forces plus a single spark. "
         "<span class='cite'>Tracing multiple causes of an event is TN Social Studies Practice SSP.05 (causation).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the <b>M.A.I.N.</b> word bank (Militarism, Alliances, Imperialism, Nationalism) and fill one bubble together.",
        extend="Which cause made the war hardest to avoid? Draw links <b>between</b> bubbles to show how the forces reinforced each other.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>draw</b> an icon for each cause."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 3 &middot; US.23 (labeled)",
)]
