#!/usr/bin/env python3
"""Assemble every organizer definition into pages/<slug>.html.
Each pack module in src/ exposes ORGANIZERS = [ dict(...), ... ] where each dict
matches render_page() kwargs: slug,title,kicker,chips,why,body,udl,role,tn.
Pages are ordered by the numeric prefix of their slug.
"""
import os, sys, glob, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAGES = os.path.join(ROOT, "pages")
sys.path.insert(0, HERE)
from toolkit_lib import render_page  # noqa: E402
from times import TIMES  # noqa: E402


def load_packs():
    items = []
    for f in sorted(glob.glob(os.path.join(HERE, "pack_*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        items.extend(getattr(mod, "ORGANIZERS", []))
    return items


def main():
    os.makedirs(PAGES, exist_ok=True)
    items = load_packs()
    items.sort(key=lambda d: d["slug"])
    seen = set()
    for it in items:
        slug = it["slug"]
        if slug in seen:
            raise SystemExit(f"duplicate slug: {slug}")
        seen.add(slug)
        it.setdefault("time", TIMES.get(slug))
        html = render_page(**it)
        out = os.path.join(PAGES, f"{slug}.html")
        with open(out, "w") as fh:
            fh.write(html)
        print(f"wrote {slug}.html")
    print(f"total {len(items)} pages")


if __name__ == "__main__":
    main()
