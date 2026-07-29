#!/usr/bin/env python3
"""Build only the given pack module(s) -> pages/<slug>.html, in isolation.
Usage: python3 src/build_one.py pack_04_tchart.py [pack_05_matrix.py ...]
Lets parallel authors render their own pages without importing others' packs.
"""
import os, sys, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAGES = os.path.join(ROOT, "pages")
sys.path.insert(0, HERE)
from toolkit_lib import render_page  # noqa: E402
from times import TIMES  # noqa: E402

os.makedirs(PAGES, exist_ok=True)
for arg in sys.argv[1:]:
    path = arg if os.path.isabs(arg) else os.path.join(HERE, os.path.basename(arg))
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for it in getattr(mod, "ORGANIZERS", []):
        it.setdefault("time", TIMES.get(it["slug"]))
        with open(os.path.join(PAGES, f"{it['slug']}.html"), "w") as fh:
            fh.write(render_page(**it))
        print(f"wrote {it['slug']}.html")
