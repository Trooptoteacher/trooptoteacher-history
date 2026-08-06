#!/usr/bin/env python3
"""
Assemble the web-served PDFs from the code pipeline and write them into public/.

- Per-unit textbook readers (public/textbook-pdf/unit-N.pdf) are self-contained:
  cover + How-This-Book-Works + that unit's stops (each stop inline-cited) + arc.
  Unit 1 is the full render_proof reader; Units 2–3 get the cover + How-This-Book-
  Works pages prepended to their unit body (matching the per-unit split spec).
- Flight Logs (public/flight-logs/unit-N/) are copied student + teacher-key.

Web builds use the lighter cover (cover_web.jpg) for fast serving; full-res
masters remain under scripts/print-book/out/. The served full-book part PDFs are
NOT touched here (they remain the authored volumes — recompose separately).

Usage: python3 assemble_web.py
"""
import os, shutil, subprocess, sys
from pathlib import Path
import fitz
import bookmeta

BASE = Path(__file__).parent
OUT  = BASE/"out"
PUB  = BASE.parents[1]/"public"
TB   = PUB/"textbook-pdf"
FL   = PUB/"flight-logs"

def run(cmd, env=None):
    e = dict(os.environ); e.update(env or {})
    subprocess.run([sys.executable, *cmd], cwd=str(BASE), env=e, check=True)

# 1) Render web-optimized sources (light cover; content identical to masters)
run(["render_proof.py"], {"PROOF_COVER": "cover_web.jpg"})   # -> out/..._Unit1_PROOF.pdf
run(["render_proof.py"], {"PROOF_COVER": "cover_web.jpg", "PROOF_FRONTMATTER_ONLY": "1"})  # -> out/_frontmatter.pdf
run(["build_unit.py", "2"])
run(["build_unit.py", "3"])
for u in (1, 2, 3):
    run(["build_flightlog.py", str(u)],            {"FL_COVER": "assets/cover_web.jpg"})
    run(["build_flightlog.py", str(u), "teacher"], {"FL_COVER": "assets/cover_web.jpg"})

u1 = OUT/"ToFormAMorePerfectUnion_Unit1_PROOF.pdf"   # cover+frontmatter+unit1+arc (web cover)
fm = OUT/"_frontmatter.pdf"                            # clean 2-page: cover + How-This-Book-Works
bodies = {2: OUT/"ToFormAMorePerfectUnion_Unit2.pdf", 3: OUT/"ToFormAMorePerfectUnion_Unit3.pdf"}

TB.mkdir(parents=True, exist_ok=True)

# unit-1.pdf = the full web Unit-1 reader (already self-contained; ends with credits)
shutil.copyfile(str(u1), str(TB/"unit-1.pdf"))
bookmeta.stamp_metadata(TB/"unit-1.pdf", "To Form a More Perfect Union — Unit 1: The Nation Turns West")

# unit-2/3.pdf = [cover + How-This-Book-Works] + that unit's body (body ends with credits)
titles = {2: "Turning the Light On", 3: "On the Menu"}
for u, body in bodies.items():
    doc = fitz.open(str(fm))
    b = fitz.open(str(body)); doc.insert_pdf(b); b.close()
    doc.save(str(TB/f"unit-{u}.pdf"), garbage=4, deflate=True)
    doc.close()
    bookmeta.stamp_metadata(TB/f"unit-{u}.pdf", f"To Form a More Perfect Union — Unit {u}: {titles[u]}")

# Full-book Part 1 (recomposed from code) = front matter + Unit 1 + Unit 2 + Unit 3,
# each unit ending with its own copyright/attribution + source credits back page.
part1 = fitz.open(str(u1))                      # cover+foreword+toc+crew+how+unit1(+credits)
for u in (2, 3):
    b = fitz.open(str(bodies[u])); part1.insert_pdf(b); b.close()
part1_path = TB/"to-form-a-more-perfect-union-part-1.pdf"
part1.save(str(part1_path), garbage=4, deflate=True)
part1.close()
bookmeta.stamp_metadata(part1_path, "To Form a More Perfect Union — Part 1 (Units 1–3, US.01–US.27)")
print(f"part-1 (full book) {part1_path.stat().st_size/1048576:5.2f} MB")

# 2) Flight Logs (student + teacher-key) for units 1–3
for u in (1, 2, 3):
    (FL/f"unit-{u}").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(str(OUT/f"ToFormAMorePerfectUnion_Unit{u}_FlightLog.pdf"),
                    str(FL/f"unit-{u}"/f"unit-{u}-flight-log-student.pdf"))
    shutil.copyfile(str(OUT/f"ToFormAMorePerfectUnion_Unit{u}_FlightLog_TeacherEdition.pdf"),
                    str(FL/f"unit-{u}"/f"unit-{u}-flight-log-teacher-key.pdf"))

# Report
for u in (1, 2, 3):
    p = TB/f"unit-{u}.pdf"
    print(f"textbook unit-{u}.pdf  {p.stat().st_size/1048576:5.2f} MB")
for u in (1, 2, 3):
    for k in ("student", "teacher-key"):
        p = FL/f"unit-{u}"/f"unit-{u}-flight-log-{k}.pdf"
        print(f"flightlog unit-{u} {k:11} {p.stat().st_size/1024:6.0f} KB")
print("done → served into public/textbook-pdf and public/flight-logs")
