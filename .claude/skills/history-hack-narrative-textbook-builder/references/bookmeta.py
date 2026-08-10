#!/usr/bin/env python3
"""
Shared copyright / writing-attribution colophon, image-&-source credits back page,
and PDF metadata stamping for the "To Form a More Perfect Union" narrative textbook
and its Flight Logs. One source of truth so every deliverable carries the same
rights notice and byline (on-page AND in the PDF's document metadata).
"""
import html as _html, re as _re

PUBLISHER    = "TroopToTeacher Technologies LLC"
COPYRIGHT    = "© 2026 TroopToTeacher Technologies LLC. All rights reserved."
AUTHOR_LEGAL = "Sean Reynolds"                # creator / rights holder (real byline)
AUTHOR_VOICE = "Sam Calloway"                 # house-author narrative voice (pen name)
SERIES       = "To Form a More Perfect Union — U.S. History (Grade 11, Tennessee)"
CONTACT      = "legal@trooptoteacher.com"

# ── CODIFIED BUILD STANDARD (single source of truth for "which is most recent") ──
# Bump BUILD_DATE + BUILD_VERSION whenever the codified build/design standard changes.
# It is stamped into every PDF's document metadata AND printed on-page (colophon /
# Flight-Log intro) so the most-recent build is ALWAYS identifiable at a glance.
# The full written standard lives in FLIGHT_LOG_STANDARD.md next to this file.
BUILD_DATE    = "2026-08-10"
BUILD_VERSION = "FL-2026.08.10"

def build_stamp_html():
    """A small dated build-stamp line for on-page display (colophon / FL intro).
    Color #5f6b7d = 4.6:1 on white (passes WCAG AA); size ≥9pt (a11y floor)."""
    return (f'<p class="small" style="margin:2px 0 0;font-size:9pt;color:#5f6b7d">'
            f'Build <b>{BUILD_DATE}</b> · standard <b>{BUILD_VERSION}</b> — most-recent codified build '
            f'(see FLIGHT_LOG_STANDARD.md).</p>')

def _esc(s): return _html.escape(str(s or ""), quote=False)

def _clean_cite(s):
    """Strip inline HTML tags/entities from a citation for a clean credits line."""
    s = _re.sub(r"<[^>]+>", "", str(s or "")).strip()
    s = s.replace("&amp;", "&")
    return s

def colophon_html():
    """The copyright + writing-attribution block (used on the credits page)."""
    return f'''<div class="sec" style="border-left-color:var(--gold)"><div class="eyebrow">Copyright &amp; Attribution</div><h2 style="font-size:14pt">About this book</h2></div>
<p class="small"><b>{_esc(SERIES)}.</b> Written by <b>{_esc(AUTHOR_LEGAL)}</b>, in the narrative voice of house author <b>“{_esc(AUTHOR_VOICE)}”</b>, for {_esc(PUBLISHER)}.</p>
<p class="small"><b>{_esc(COPYRIGHT)}</b> No part of this work may be reproduced, distributed, or transmitted in any form or by any means without the prior written permission of the publisher, except brief quotations in reviews and non-commercial classroom use permitted by copyright law. “History Hack,” “To Form a More Perfect Union,” and the Flight-Crew characters are marks of {_esc(PUBLISHER)}.</p>
<p class="small">The flight crew and era-friends are composite characters; real historical figures appear only in their own recorded words. Assessment and self-grade content is classroom-formative · pre-field-test. Rights &amp; licensing: {_esc(CONTACT)}.</p>
    {build_stamp_html()}'''

def credits_page_html(unit_label, sources):
    """A full back-matter page: colophon + a numbered image/source-credits list."""
    seen, items = set(), []
    for s in sources:
        c = _clean_cite(s)
        if c and c not in seen:
            seen.add(c); items.append(f"<li>{_esc(c)}</li>")
    src_block = (
        f'<div class="sec" style="border-left-color:var(--gold);margin-top:12px"><div class="eyebrow">Image &amp; Source Credits · {_esc(unit_label)}</div></div>'
        f'<ol class="small" style="margin:6px 0 0 20px;line-height:1.55">{"".join(items)}</ol>'
    ) if items else ""
    return (
        f'<section class="page">{colophon_html()}{src_block}'
        f'<p class="small" style="margin-top:12px;color:var(--ink-soft)"><b>Source authenticity.</b> Every primary source in this book — photographs, political cartoons, maps, and documents — is an authentic historical work, public domain or used with permission and credited to its holding institution above. <b>No primary source is AI-generated or AI-altered.</b></p>'
        f'<p class="small" style="color:var(--ink-soft)"><b>AI-generated illustration disclosure.</b> The decorative brand illustrations in this book — the cover art, the flight-crew character portraits, the “History Hack” time-machine concept art, and the C-130 aircraft — are <b>AI-generated under human direction</b>, then curated and owned by {PUBLISHER}. As machine-generated images they are <b>not independently copyrightable</b> as such, and they are <b>illustrations of fictional characters and brand concepts, not historical evidence</b> — never treat them as primary sources. Every genuine primary source keeps its distinct Chicago-style citation and holding-institution credit (above). AI was <b>not</b> used to write, alter, or fabricate any historical content or primary source.</p></section>'
    )

def paginate(pdf_path):
    """Stamp a true document folio (page number) at bottom-center of EVERY page —
    front matter included — numbered by actual position so nothing is unnumbered."""
    import fitz
    d = fitz.open(str(pdf_path))
    n = d.page_count
    for i in range(n):
        pg = d[i]; r = pg.rect
        num = str(i + 1)
        fs = 9
        tw = fitz.get_text_length(num, fontname="Times-Roman", fontsize=fs)
        x = (r.width - tw) / 2
        y = r.height - 26
        # cover (page 1) is a dark full-bleed image → light folio; all others grey
        col = (0.90, 0.91, 0.94) if i == 0 else (0.48, 0.51, 0.56)
        pg.insert_text((x, y), num, fontname="Times-Roman", fontsize=fs, color=col)
    d.saveIncr(); d.close()

def add_th_scope(pdf_path):
    """PDF/UA polish: give every table-header cell (/TH) a /Scope. WeasyPrint tags TH
    inside THead but does not emit /Scope from the HTML scope="col" attribute, so we add
    /A <</O /Table /Scope /Column>> to each /TH struct element post-render. Single-header-row
    tables → all column headers. A full save (garbage/deflate) preserves the structure tree,
    MarkInfo, /Lang, and metadata (verified)."""
    import fitz, re, os
    d = fitz.open(str(pdf_path)); n = 0
    for x in range(1, d.xref_length()):
        try: o = d.xref_object(x)
        except Exception: continue
        if re.search(r'/S\s*/TH\b', o) and '/Scope' not in o:
            d.update_object(x, re.sub(r'(/S\s*/TH)', r'\1/A<</O/Table/Scope/Column>>', o, count=1))
            n += 1
    if n:
        tmp = str(pdf_path) + ".thtmp"          # can't full-save onto the open path; write tmp + replace
        d.save(tmp, garbage=3, deflate=True, clean=True, encryption=fitz.PDF_ENCRYPT_KEEP)
        d.close()
        os.replace(tmp, str(pdf_path))
    else:
        d.close()
    return n

def stamp_metadata(pdf_path, title, subject="U.S. History narrative textbook"):
    """Embed document metadata (title, author byline, rights) into the PDF itself."""
    import fitz
    d = fitz.open(str(pdf_path))
    d.set_metadata({
        "title": title,
        "author": f"{AUTHOR_LEGAL} — {PUBLISHER}",
        "subject": subject,
        "keywords": f"U.S. History; Tennessee; History Hack; To Form a More Perfect Union; "
                    f"build {BUILD_DATE}; standard {BUILD_VERSION}; {COPYRIGHT}",
        "creator": f"History Hack narrative-textbook pipeline (WeasyPrint) · build {BUILD_VERSION}",
        "producer": PUBLISHER,
    })
    d.saveIncr()
    d.close()
