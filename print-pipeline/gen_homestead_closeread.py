#!/usr/bin/env python3
"""U.S. History Hack™ — Homestead Act of 1862 CLOSE READ (single primary source).

A leveled close-reading packet built on the print-first WeasyPrint path (no .docx):
  US01_Homestead_CloseRead_<ts>.pdf
    p1  Authentic verbatim excerpt (line-numbered, wide annotation margin) for a close read.
    p2  "The Same Law in Simpler Words" — ~3rd-grade Lexile English + EN/ES word bank.
    p3  "La Ley de Heredades — en español" — Spanish leveled version + glosario/cognados.
    p4  A few OPTIONAL close-read questions + UDL 3.0 supports + IEP/504 guardrail.

Statute text is a verbatim public-domain excerpt of the Homestead Act of 1862
(12 Stat. 392; 8 sections; approved May 20, 1862), verified against the U.S.
National Archives, NPS Homestead National Historical Park, Gilder Lehrman, and
the State Historical Society of North Dakota transcript. America 250 palette;
™ not (R); ISBN "[to be assigned]"; version timestamp in filename + on-page.
UDL 3.0 (CAST 2024): multiple means of representation (authentic + leveled +
Spanish + vocabulary). Supports work ALONGSIDE — never in place of — IEP/504.
"""
from datetime import datetime, timezone
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "HistoryHack_Platinum/homestead_close_read"
OUT.mkdir(parents=True, exist_ok=True)
TS = datetime.now(timezone.utc)
STAMP = TS.strftime("%Y%m%d_%H%M")
ISO = TS.strftime("%Y-%m-%dT%H:%M:%SZ")

NAVY, NAVY2, RED, GOLD, CARD, LIGHT, BORDER, INK = \
    "#1F3A5F", "#2C3E63", "#B22234", "#C9A227", "#F8F5EF", "#EEF2F8", "#C9C2B4", "#20262E"

CITE = ("Homestead Act of 1862, 12 Stat. 392 (37th Cong., Sess. II, ch. 75); approved May 20, 1862. "
        "General Records of the U.S. Government, RG 11, U.S. National Archives. Verbatim excerpt; "
        "public domain.")

# Authentic verbatim segments (minimal [bracketed] clarifications), numbered for close reading.
SEGMENTS = [
    "That any person who is the head of a family, or who has arrived at the age of twenty-one years, "
    "and is a citizen of the United States, or who shall have filed his declaration of intention to "
    "become such &hellip; shall &hellip; be entitled to enter one quarter section [160 acres] &hellip; "
    "of unappropriated public lands &hellip;",
    "&hellip; and who has never borne arms against the United States Government or given aid and comfort "
    "to its enemies &hellip;",
    "&hellip; subject to preemption at one dollar and twenty-five cents [$1.25], or less, per acre.",
    "[Sec. 2.] &hellip; the person applying &hellip; shall make affidavit [a sworn promise] &hellip; that "
    "said entry is made for the purpose of actual settlement and cultivation, and not &hellip; for the use "
    "or benefit of any other person &hellip;",
    "&hellip; and on payment of ten dollars [$10], he or she shall thereupon be permitted to enter the "
    "quantity of land specified.",
    "[Sec. 3.] &hellip; no certificate shall be given, or patent [legal title] issued &hellip; until the "
    "expiration of five years from the date of such entry &hellip;",
    "&hellip; [the settler] shall prove by two credible witnesses that he, she, or they have resided upon "
    "or cultivated the same for the term of five years &hellip;",
    "&hellip; [but] if &hellip; [the settler] shall have &hellip; abandoned the said land for more than "
    "six months at any time, then &hellip; the land so entered shall revert to [go back to] the government.",
]

# ~3rd-grade Lexile English (short sentences, common words). Honest about the cost.
SIMPLE_EN = [
    "In 1862, the United States made a new law. It was called the Homestead Act.",
    "The law offered free land in the West. An adult could ask for up to 160 acres.",
    "To ask for land, you had to be 21 years old, or the head of a family. You had to be a "
    "citizen, or be working to become one. You could not have fought against the United States.",
    "First, you went to a land office. You signed a paper called an affidavit. You promised the "
    "land was for your own family farm. You paid a small fee of ten dollars.",
    "Then you had to live on the land for five years. You had to farm it and build on it. Two "
    "people had to say that you really lived there.",
    "If you left the land for more than six months, you lost it. The land went back to the government.",
    "After five years, the government gave you a patent. A patent is a paper that says the land is yours.",
    "But the land was not empty. Native nations already lived on it. The law called their land "
    "&ldquo;unclaimed.&rdquo; Many Native families lost their homeland so settlers could get farms.",
]

# Spanish leveled version (natural, accurate translation of the simplified English).
SIMPLE_ES = [
    "En 1862, Estados Unidos aprobó una nueva ley. Se llamó la Ley de Heredades (Homestead Act).",
    "La ley ofrecía tierra gratis en el Oeste. Un adulto podía pedir hasta 160 acres.",
    "Para pedir la tierra, tenías que tener 21 años, o ser jefe o jefa de familia. Tenías que ser "
    "ciudadano, o estar tramitando la ciudadanía. No podías haber luchado contra Estados Unidos.",
    "Primero, ibas a una oficina de tierras. Firmabas un papel llamado declaración jurada (affidavit). "
    "Prometías que la tierra era para la granja de tu propia familia. Pagabas una cuota de diez dólares.",
    "Después tenías que vivir en la tierra por cinco años. Tenías que cultivarla y construir en ella. "
    "Dos personas tenían que confirmar que de verdad vivías allí.",
    "Si dejabas la tierra por más de seis meses, la perdías. La tierra regresaba al gobierno.",
    "Después de cinco años, el gobierno te daba un patent (título de propiedad). El título es un papel "
    "que dice que la tierra es tuya.",
    "Pero la tierra no estaba vacía. Las naciones indígenas ya vivían allí. La ley llamó a sus tierras "
    "&ldquo;no reclamadas.&rdquo; Muchas familias indígenas perdieron su hogar para que los colonos "
    "consiguieran granjas.",
]

# Key vocabulary: term, plain EN meaning, Spanish.
VOCAB = [
    ("homestead", "a home and piece of land a family lives on and works", "heredad / granja familiar"),
    ("public land", "land owned by the government", "tierra pública"),
    ("claim", "to formally ask to own or use land", "reclamar / solicitar"),
    ("affidavit", "a written promise a person swears is true", "declaración jurada"),
    ("citizen", "a legal member of a country", "ciudadano / ciudadana"),
    ("cultivate", "to prepare the soil and grow crops", "cultivar"),
    ("patent", "the paper that proves you own the land", "título de propiedad"),
    ("unappropriated", "&lsquo;unclaimed&rsquo; by the government &mdash; but often Native homeland", "no asignada / no reclamada"),
    ("revert", "to go back to an earlier owner", "revertir / regresar"),
    ("dispossession", "the forced loss of land or home", "despojo"),
]

# Cognates that help Spanish readers.
COGNATES = [("acre", "acre"), ("family", "familia"), ("citizen", "ciudadano"), ("cultivate", "cultivar"),
            ("government", "gobierno"), ("declaration", "declaración"), ("patent", "título / patente"),
            ("Native nations", "naciones indígenas")]

QUESTIONS = [
    ("Right there", "How many years did a settler have to live on and farm the land before they owned it? "
     "(Use the simpler version and word bank if you need them.)",
     "A settler had to live on and farm the land for ______ years."),
    ("Word choice", "The law calls the land <b>&ldquo;unappropriated&rdquo;</b> (unclaimed). Who really lived "
     "there already? What does that word choice leave out?",
     "The land was really the home of ______. Calling it &ldquo;unclaimed&rdquo; hides that ______."),
    ("Your view", "Do you think the Homestead Act was fair? Use <b>one</b> detail from the text to explain.",
     "I think the law was (fair / not fair) because ______."),
]

CSS = """
* { box-sizing:border-box; }
body { font-family:'DejaVu Serif', Georgia, serif; color:%(INK)s; margin:0; font-size:11pt; line-height:1.45; }
h1,h2,h3,.k,.brand,.pill,.type { font-family:'DejaVu Sans', Arial, sans-serif; }
.page { page-break-after:always; }
.page:last-child { page-break-after:auto; }
.band { background:%(NAVY)s; color:#fff; padding:14px 18px; border-left:14px solid %(RED)s; }
.band .brand { color:%(GOLD)s; font-weight:bold; letter-spacing:1px; font-size:10.5pt; }
.band h1 { font-size:20pt; margin:5px 0 3px; }
.band .sub { color:#DCE6F1; font-size:11pt; }
.wrap { padding:14px 4px 0; }
.sec { color:%(NAVY)s; border-bottom:2px solid %(GOLD)s; padding-bottom:3px; margin:4px 0 10px; font-size:15pt; page-break-after:avoid; }
.instr { background:%(LIGHT)s; border-left:5px solid %(NAVY)s; border-radius:4px; padding:8px 12px; margin:8px 0 12px; font-size:10pt; }
.instr b { color:%(NAVY)s; }
.crtable { width:100%%; border-collapse:collapse; }
.crtable td { vertical-align:top; padding:0; }
.seg { display:flex; gap:10px; margin:0 0 6px; page-break-inside:avoid; }
.seg .num { background:%(NAVY)s; color:#fff; font-family:'DejaVu Sans'; font-weight:bold; min-width:22px; height:22px;
  border-radius:50%%; text-align:center; line-height:22px; font-size:9.5pt; }
.seg .txt { flex:1; font-size:10.4pt; line-height:1.38; }
.notecol { width:2.0in; border-left:1.5pt dashed %(BORDER)s; padding-left:12px; }
.notecol .k { color:%(RED)s; font-family:'DejaVu Sans'; font-weight:bold; font-size:8.5pt; letter-spacing:.4px; }
.noteline { border-bottom:0.6pt solid #C7CDD7; height:0.42in; }
.src { font-size:8.2pt; color:#5C6470; font-style:italic; margin:10px 0 0; }
.simple { display:flex; gap:11px; margin:0 0 6px; page-break-inside:avoid; }
.simple .num { background:%(GOLD)s; color:%(NAVY)s; font-family:'DejaVu Sans'; font-weight:bold; min-width:23px;
  height:23px; border-radius:50%%; text-align:center; line-height:23px; font-size:9.5pt; }
.simple .txt { flex:1; font-size:11pt; line-height:1.42; }
.es .txt { font-size:11pt; }
.starter { font-size:9pt; color:%(NAVY)s; font-family:'DejaVu Sans'; margin:0 0 5px; }
.starter i { color:%(NAVY2)s; }
table.v { width:100%%; border-collapse:collapse; margin-top:6px; }
table.v th { background:%(NAVY)s; color:#fff; font-family:'DejaVu Sans'; padding:5px 8px; font-size:9.5pt; text-align:left; }
table.v tr { page-break-inside:avoid; }
table.v td { border:1pt solid %(BORDER)s; padding:4px 8px; font-size:9.5pt; vertical-align:top; }
table.v td.t { background:%(CARD)s; font-weight:bold; color:%(NAVY)s; width:22%%; }
.cog { background:%(CARD)s; border:1pt solid %(GOLD)s; border-radius:6px; padding:9px 13px; margin:10px 0; font-size:10pt; }
.cog .k { color:%(RED)s; font-family:'DejaVu Sans'; font-weight:bold; }
.cog span.c { display:inline-block; background:#fff; border:1pt solid %(BORDER)s; border-radius:9px; padding:1px 8px;
  margin:3px 4px 0 0; font-size:9pt; }
.q { background:%(CARD)s; border:1pt solid %(BORDER)s; border-left:4px solid %(RED)s; border-radius:5px; padding:6px 11px;
  margin:7px 0; page-break-inside:avoid; }
.q .tag { font-family:'DejaVu Sans'; font-size:8pt; font-weight:bold; color:#fff; background:%(NAVY)s; padding:1px 8px;
  border-radius:9px; }
.q .stem { font-size:10.5pt; margin:4px 0 4px; }
.aline { border-bottom:0.6pt solid #AEB6C2; height:0.30in; }
.udl { background:%(LIGHT)s; border:1pt solid %(BORDER)s; border-left:5px solid %(NAVY)s; border-radius:5px;
  padding:8px 12px; margin:8px 0 5px; font-size:9.2pt; }
.udl .k { color:%(NAVY)s; font-family:'DejaVu Sans'; font-weight:bold; }
ul.tight { margin:5px 0 0 18px; padding:0; }
ul.tight li { margin:3px 0; }
.note { font-size:8.4pt; color:#5C6470; font-style:italic; }
@page { size:Letter portrait; margin:0.7in 0.7in 0.85in 0.7in;
  @bottom-left { content:"U.S. History Hack™ · Homestead Act of 1862 · Close Read (US.01)"; font:8pt 'DejaVu Sans'; color:#5C6470; }
  @bottom-right { content:"© 2026 TroopToTeacher Technologies LLC · p. " counter(page); font:8pt 'DejaVu Sans'; color:#5C6470; } }
""" % dict(INK=INK, NAVY=NAVY, NAVY2=NAVY2, RED=RED, GOLD=GOLD, CARD=CARD, LIGHT=LIGHT, BORDER=BORDER)


def notelines(n):
    return "".join('<div class="noteline"></div>' for _ in range(n))


def alines(n):
    return "".join('<div class="aline"></div>' for _ in range(n))


def build():
    # ---- Page 1: authentic excerpt, line-numbered, annotation margin ----
    segs = "".join(f'<div class="seg"><div class="num">{i+1}</div><div class="txt">{t}</div></div>'
                   for i, t in enumerate(SEGMENTS))
    p1 = f"""<div class="band"><div class="brand">U.S. HISTORY HACK™ · AMERICA 250 · STANDARD US.01</div>
      <h1>The Homestead Act of 1862 — Close Read</h1>
      <div class="sub">Read the real words of the law. Simpler English, Spanish, and a word bank are on the next pages.</div></div>
      <div class="wrap">
      <div class="instr"><b>How to read this (UDL).</b> Read each numbered part <b>slowly</b>. Circle or underline any
      word you don't know. Jot a quick note or a &#9733;/&#63; in the <b>Notes</b> column. Stuck on the old-style
      wording? Read the <b>Simpler Words</b> page or the <b>versión en español</b>, then come back. A read-aloud is
      available in the app.<br><span class="note">Example — beside Part 1 you might jot: &ldquo;Who can get land?
      &rarr; adults &amp; citizens.&rdquo;</span></div>
      <table class="crtable"><tr>
        <td>{segs}<div class="src">Source: {CITE}</div></td>
        <td class="notecol"><div class="k">NOTES / MY THINKING</div>{notelines(13)}</td>
      </tr></table>
      </div>"""

    # ---- Page 2: simpler English + word bank ----
    simp = "".join(f'<div class="simple"><div class="num">{i+1}</div><div class="txt">{t}</div></div>'
                   for i, t in enumerate(SIMPLE_EN))
    vrows = "".join(f'<tr><td class="t">{t}</td><td>{d}</td><td>{es}</td></tr>' for t, d, es in VOCAB)
    p2 = f"""<div class="wrap">
      <h2 class="sec">The Same Law in Simpler Words</h2>
      <div class="instr"><b>Same meaning, easier reading.</b> This tells you what the law on the first page says,
      in shorter sentences.</div>
      {simp}
      <h3 class="sec" style="font-size:13pt;margin-top:14px">Word Bank &mdash; Palabras Clave (English / Español)</h3>
      <table class="v"><tr><th style="width:22%">Word / Palabra</th><th style="width:46%">What it means</th>
      <th style="width:32%">Español</th></tr>{vrows}</table>
      </div>"""

    # ---- Page 3: Spanish leveled version + cognates ----
    esp = "".join(f'<div class="simple es"><div class="num">{i+1}</div><div class="txt">{t}</div></div>'
                  for i, t in enumerate(SIMPLE_ES))
    cogs = "".join(f'<span class="c">{en} = {es}</span>' for en, es in COGNATES)
    p3 = f"""<div class="wrap">
      <h2 class="sec">La Ley de Heredades (Homestead Act) — en español</h2>
      <div class="instr"><b>Para lectores de español.</b> Esta es la misma ley, explicada en español sencillo. Puedes
      leerla <b>antes</b> o <b>después</b> del texto original en inglés. Las palabras clave están en el Word Bank de la
      página anterior. <span class="note">(This is the same leveled text in Spanish; read it before or after the English.)</span></div>
      {esp}
      <div class="cog"><span class="k">Cognados que ayudan (words that look alike in both languages):</span><br>{cogs}</div>
      <p class="note">Traducción de apoyo elaborada por TroopToTeacher Technologies LLC para acceso lingüístico; el
      texto legal original (página 1) es la fuente primaria en dominio público.</p>
      </div>"""

    # ---- Page 4: optional questions + UDL ----
    qs = "".join(f'<div class="q"><span class="tag">{tag}</span><div class="stem">{i+1}. {stem}</div>'
                 f'<div class="starter">Sentence starter: <i>{starter}</i></div>{alines(2)}</div>'
                 for i, (tag, stem, starter) in enumerate(QUESTIONS))
    p4 = f"""<div class="wrap">
      <h2 class="sec">A Few Close-Read Questions <span style="font-size:10pt;color:#5C6470">(optional)</span></h2>
      <div class="instr"><b>Optional.</b> Use these if you want to check understanding — or skip them and just read and
      discuss. Every answer can be found in, or reasoned from, the text.</div>
      {qs}
      <div class="udl"><span class="k">Supports on this sheet (UDL 3.0 · CAST 2024):</span> the real law + a
      3rd-grade retelling + a Spanish version + an English/Spanish word bank + cognates + a Notes column for
      annotation + sentence starters, plus a read-aloud in the app — so every reader has a way in.
      <b>These add to — never replace — a student's IEP/504 accommodations.</b></div>
      <p class="note">U.S. History Hack™ · Standard US.01 · © 2026 TroopToTeacher Technologies LLC · single-classroom
      reproduction license · ISBN [to be assigned] · Homestead Act of 1862 (12 Stat. 392), public domain ·
      Generated {ISO}.</p>
      </div>"""

    body = (f'<div class="page">{p1}</div><div class="page">{p2}</div>'
            f'<div class="page">{p3}</div><div class="page">{p4}</div>')
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def main():
    name = f"US01_Homestead_CloseRead_{STAMP}.pdf"
    HTML(string=build()).write_pdf(str(OUT / name))
    print("wrote", name, "| out:", OUT, "| ts", ISO)


if __name__ == "__main__":
    main()
