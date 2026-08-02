#!/usr/bin/env python3
"""
Canonical skill-set lint (anti-drift gate).

Fails (exit 1) on any of:
  1. A skill dir whose SKILL.md `name:` does not match the directory name.
  2. A retired skill name appearing anywhere in .claude/skills/ WITHOUT a
     retirement annotation on the same line (retire / supersed / absorb /
     replaced / renamed / -> ...). This catches stale pointers to old names.
  3. An orchestrator/builder INLINING a gate/engine instead of invoking it
     (the exact phrasing that caused the drift this set was built to end).
  4. A skill dir missing from the registry, or a registry entry with no dir
     (excluding the External and Retired sections).

Usage:  python3 .claude/skills/lint_skills.py
"""
import re
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parent
REGISTRY = SKILLS_DIR / "SKILLS.md"

# Names that must never reappear as an active reference.
RETIRED = {
    "history-hack-north-star",
    "history-hack-platinum-workbook",
    "tcap-item-writer-v2",
    "history-hack-question-forge",
    "history-hack-course-standard-builder",
    "teacher-deck-workbook-aligner",
}
# Skills referenced by the set but intentionally not vendored here.
EXTERNAL = {"history-hack-print-qc-auditor"}

# Words that make a retired-name mention legitimate (it's documenting the retirement).
ANNOTATION = re.compile(
    r"retire|supersed|absorb|replaced|renamed|no longer|do not|old name|->|→|\(was",
    re.IGNORECASE,
)
# Inlining phrases forbidden in the orchestrators.
INLINE_BAD = [
    "not separate skills to load",
    "internal to this skill",
    "do not treat them as siblings",
    "defined and enforced *within this skill*",
    "defined and enforced within this skill",
]
ORCHESTRATORS = {
    "history-hack-platinum-unit-builder",
    "history-hack-new-course-builder",
}

errors = []


def skill_dirs():
    return sorted(
        p.name for p in SKILLS_DIR.iterdir() if p.is_dir() and (p / "SKILL.md").exists()
    )


def frontmatter_name(skill_md: Path):
    for line in skill_md.read_text(encoding="utf-8", errors="replace").splitlines()[:15]:
        m = re.match(r"\s*name:\s*(.+?)\s*$", line)
        if m:
            return m.group(1).strip().strip("\"'")
    return None


def main():
    dirs = skill_dirs()

    # 1. name/dir match
    for d in dirs:
        nm = frontmatter_name(SKILLS_DIR / d / "SKILL.md")
        if nm is None:
            errors.append(f"[name] {d}/SKILL.md has no `name:` field")
        elif nm != d:
            errors.append(f"[name] {d}/SKILL.md name '{nm}' != directory '{d}'")

    # 2 & 3. scan every markdown file in the set
    for md in SKILLS_DIR.rglob("*.md"):
        rel = md.relative_to(SKILLS_DIR.parent.parent)
        text = md.read_text(encoding="utf-8", errors="replace")
        owner = md.relative_to(SKILLS_DIR).parts[0] if md != REGISTRY else None
        for i, line in enumerate(text.splitlines(), 1):
            # retired names — allowed only when annotated as retired (registry table is all annotated)
            if md != REGISTRY:
                for r in RETIRED:
                    if r in line and not ANNOTATION.search(line):
                        errors.append(
                            f"[retired] {rel}:{i} references retired '{r}' without a retirement note"
                        )
            # inlining phrases in the orchestrators
            if owner in ORCHESTRATORS:
                low = line.lower()
                for bad in INLINE_BAD:
                    if bad in low:
                        errors.append(
                            f"[inline] {rel}:{i} orchestrator inlines instead of invokes: \"{bad}\""
                        )

    # 4. registry coverage
    reg = REGISTRY.read_text(encoding="utf-8", errors="replace")
    # split off the Retired + External sections so their names aren't treated as active
    active_reg = reg.split("## External")[0]
    listed = set(re.findall(r"`([a-z0-9][a-z0-9-]+-[a-z0-9-]+)`", active_reg))
    listed = {x for x in listed if x not in RETIRED}
    for d in dirs:
        if d not in listed:
            errors.append(f"[registry] skill '{d}' has no entry in SKILLS.md")
    for name in listed:
        if name not in dirs and name not in EXTERNAL and not name.startswith("build_"):
            # tokens in registry prose that aren't skills (scripts, file names) will trip this;
            # keep the allowlist tight — only flag things that look like skill names.
            if name.count("-") >= 1 and not name.endswith(".py") and "/" not in name:
                errors.append(
                    f"[registry] SKILLS.md lists '{name}' but no such skill dir exists"
                )

    if errors:
        print("SKILL LINT FAILED:\n")
        for e in errors:
            print("  " + e)
        print(f"\n{len(errors)} problem(s).")
        return 1
    print(f"skill lint OK — {len(dirs)} skills, names match, no retired refs, "
          f"no inlined gates, registry complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
