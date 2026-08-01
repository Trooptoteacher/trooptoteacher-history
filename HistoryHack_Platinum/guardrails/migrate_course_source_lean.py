#!/usr/bin/env python3
"""
Source-lean course migration (SUITE_CONSOLIDATION_PLAN.md, Option A).

Extract a finished course's SOURCE + CONTENT from a git ref into the canonical
`courses/<subject-id>/` tree, WITHOUT pulling the heavy print binaries into the
committed tree. Instead of committing ~800 MB of .docx/.pdf/decks, we:

  • extract text/source files (json, md, py, js, html<=cap, css, csv, svg, …)
    into courses/<subject-id>/ (renaming the source subtree root),
  • record every deliverable binary (.docx/.pdf/.pptx/.jpg/.png/.zip/.xlsx) in
    07_DEPLOY/DELIVERABLES_MANIFEST.json (path, bytes, git blob sha1, source
    branch, + null release_url/drive_url to be filled at publish time),
  • skip everything under BUILD/ (regenerable intermediates),
  • write a .gitignore so BUILD/ never gets committed.

Integrity ref for binaries is the git blob sha1 (already in the tree — no binary
download needed; verifiable via `git cat-file` / the GitHub blob URL). The
SHA-256 + hosting URL are filled in when the binaries are published to a Release
or the Drive deploy folder.

Usage:
  migrate_course_source_lean.py <git-ref> <source-subtree> <subject-id> [--apply]
      [--repo-root PATH] [--text-cap-mb N]

Dry-run by default: prints the extract/manifest/skip plan. --apply writes files.
"""
import subprocess, sys, os, json, hashlib

argv = sys.argv[1:]
flags = {a.split("=")[0].lstrip("-"): (a.split("=", 1)[1] if "=" in a else True)
         for a in argv if a.startswith("--")}
pos = [a for a in argv if not a.startswith("--")]
if len(pos) < 3:
    sys.exit(__doc__)
REF, SRC_SUBTREE, SUBJECT_ID = pos[0], pos[1].rstrip("/"), pos[2]
REPO = flags.get("repo-root", os.getcwd())
APPLY = bool(flags.get("apply"))
TEXT_CAP = int(flags.get("text-cap-mb", 2)) * 1024 * 1024

TEXT_EXT = {".json", ".md", ".py", ".js", ".ts", ".css", ".csv", ".tsv",
            ".txt", ".yml", ".yaml", ".svg", ".html", ".htm", ".xml",
            ".gitignore", ".gitkeep", ".sh"}
BIN_EXT = {".docx", ".dotx", ".pdf", ".pptx", ".pptx", ".xlsx", ".xls",
           ".jpg", ".jpeg", ".png", ".gif", ".zip", ".mp4", ".webp"}

def git(*args):
    return subprocess.run(["git", "-C", REPO, *args],
                          capture_output=True, text=True, check=True).stdout

def git_bytes(*args):
    return subprocess.run(["git", "-C", REPO, *args],
                          capture_output=True, check=True).stdout

TARGET_ROOT = os.path.join("courses", SUBJECT_ID)

# `git ls-tree -r -l <ref> <subtree>` → mode  type  sha1  size\tpath
rows = []
for line in git("ls-tree", "-r", "-l", REF, SRC_SUBTREE).splitlines():
    meta, path = line.split("\t", 1)
    _mode, _type, sha1, size = meta.split()
    rows.append((sha1, int(size) if size != "-" else 0, path))

extracted, manifested, skipped = [], [], []
for sha1, size, path in rows:
    rel = path[len(SRC_SUBTREE):].lstrip("/")          # strip source root
    ext = os.path.splitext(path)[1].lower()
    base = os.path.basename(path)
    ext_key = base if base in (".gitignore", ".gitkeep") else ext
    # Skip regenerable intermediates entirely.
    if rel.split("/", 1)[0] == "BUILD" or "/BUILD/" in ("/" + rel):
        skipped.append((rel, size, "BUILD intermediate"))
        continue
    if ext_key in BIN_EXT:
        manifested.append({"path": rel, "bytes": size, "git_blob_sha1": sha1,
                           "source_ref": REF, "release_url": None, "drive_url": None})
        continue
    if ext_key in TEXT_EXT:
        if size > TEXT_CAP:
            skipped.append((rel, size, f"text >{TEXT_CAP//1048576}MB cap"))
            continue
        extracted.append((sha1, rel, size))
        continue
    skipped.append((rel, size, f"unclassified ext '{ext}'"))

# ── report ──
print(f"REF={REF}  SRC={SRC_SUBTREE}  ->  {TARGET_ROOT}  ({'APPLY' if APPLY else 'DRY-RUN'})")
print(f"  extract (source):   {len(extracted)} files, "
      f"{sum(s for _,_,s in extracted)/1048576:.2f} MB")
print(f"  manifest (binaries):{len(manifested)} files, "
      f"{sum(m['bytes'] for m in manifested)/1048576:.1f} MB (NOT committed)")
print(f"  skip (BUILD/other): {len(skipped)} files")

if APPLY:
    for sha1, rel, _ in extracted:
        dest = os.path.join(REPO, TARGET_ROOT, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as fh:
            fh.write(git_bytes("cat-file", "blob", sha1))
    man = {
        "subject_id": SUBJECT_ID, "source_ref": REF, "source_subtree": SRC_SUBTREE,
        "policy": "source-lean (SUITE_CONSOLIDATION_PLAN.md Option A): binaries "
                  "hosted as Release/Drive assets, not committed to main.",
        "count": len(manifested),
        "total_bytes": sum(m["bytes"] for m in manifested),
        "deliverables": sorted(manifested, key=lambda m: m["path"]),
    }
    mpath = os.path.join(REPO, TARGET_ROOT, "07_DEPLOY", "DELIVERABLES_MANIFEST.json")
    os.makedirs(os.path.dirname(mpath), exist_ok=True)
    json.dump(man, open(mpath, "w"), indent=2)
    open(mpath, "a").write("\n")
    gi = os.path.join(REPO, TARGET_ROOT, ".gitignore")
    with open(gi, "w") as fh:
        fh.write("# Regenerable build intermediates — never committed (source-lean).\n"
                 "BUILD/\n")
    print(f"  wrote {len(extracted)} source files, "
          f"{TARGET_ROOT}/07_DEPLOY/DELIVERABLES_MANIFEST.json, {TARGET_ROOT}/.gitignore")
else:
    print("  (dry-run — pass --apply to write)")
