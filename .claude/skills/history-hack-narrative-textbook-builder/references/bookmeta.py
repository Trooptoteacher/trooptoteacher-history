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
<p class="small">The flight crew and era-friends are composite characters; real historical figures appear only in their own recorded words. Assessment and self-grade content is classroom-formative · pre-field-test. Rights &amp; licensing: {_esc(CONTACT)}.</p>'''

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
        f'<p class="small" style="margin-top:12px;color:var(--ink-soft)">Every primary source above is public domain or used with permission, credited to its holding institution. Covers and crew portraits are original illustrations © {PUBLISHER} — no AI-generated cover art.</p></section>'
    )

def stamp_metadata(pdf_path, title, subject="U.S. History narrative textbook"):
    """Embed document metadata (title, author byline, rights) into the PDF itself."""
    import fitz
    d = fitz.open(str(pdf_path))
    d.set_metadata({
        "title": title,
        "author": f"{AUTHOR_LEGAL} — {PUBLISHER}",
        "subject": subject,
        "keywords": f"U.S. History; Tennessee; History Hack; To Form a More Perfect Union; {COPYRIGHT}",
        "creator": "History Hack narrative-textbook pipeline (WeasyPrint)",
        "producer": PUBLISHER,
    })
    d.saveIncr()
    d.close()
