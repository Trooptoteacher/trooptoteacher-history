#!/usr/bin/env bash
# Render every deliverable .docx -> .pdf (in place) via LibreOffice headless.
# One soffice process per unit dir (8 files each) — efficient and isolates failures.
# JAVA_TOOL_OPTIONS is stripped (proxy JVM opts break headless soffice).
set -u
ROOT="/home/user/trooptoteacher-history/courses/foundations-constitutional-government"
LOG="${1:-/tmp/render_all.log}"
: > "$LOG"
pkill -9 soffice 2>/dev/null; sleep 1
n_ok=0; n_fail=0
for d in "$ROOT"/BUILD/unit*/deliverables; do
  [ -d "$d" ] || continue
  unit=$(basename "$(dirname "$d")")
  prof="/tmp/lp_$unit"
  rm -rf "$prof"
  echo "=== $unit : $(ls "$d"/*.docx 2>/dev/null | wc -l) docx ===" | tee -a "$LOG"
  env -u JAVA_TOOL_OPTIONS timeout 600 soffice --headless --nologo --nofirststartwizard \
      -env:UserInstallation=file://"$prof" \
      --convert-to pdf --outdir "$d" "$d"/*.docx 2>&1 | grep -vi javaldx | tee -a "$LOG"
  pkill -9 soffice 2>/dev/null; sleep 1
  for f in "$d"/*.docx; do
    pdf="${f%.docx}.pdf"
    if [ -f "$pdf" ] && [ "$pdf" -nt "$f" -o -s "$pdf" ]; then
      n_ok=$((n_ok+1))
    else
      n_fail=$((n_fail+1)); echo "MISSING PDF: $pdf" | tee -a "$LOG"
    fi
  done
done
echo "RENDER_ALL_DONE ok=$n_ok fail=$n_fail" | tee -a "$LOG"
