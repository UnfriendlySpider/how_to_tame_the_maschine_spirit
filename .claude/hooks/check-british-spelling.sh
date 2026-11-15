#!/usr/bin/env bash
# PostToolUse hook: advisory spelling check for the paper prose.
#
# Runs after Edit or Write on paper/paper.md and prints a short list of common
# American spellings found in the file. It never blocks: PostToolUse runs after
# the tool has already acted, and exit 2 there only shows stderr to Claude.
# Code fences and inline code are skipped, so identifiers such as `color`
# and quoted counter-examples such as `Color` are not flagged.
set -euo pipefail

input="$(cat)"
file_path="$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty' 2>/dev/null || true)"

case "$file_path" in
  *paper/paper.md) ;;
  *) exit 0 ;;
esac

[[ -f "$file_path" ]] || exit 0

# Strip fenced code blocks and inline code spans (line numbers stay the same),
# then look for American spellings.
findings="$(awk '/^```/{skip=!skip; print ""; next} skip{print ""; next} {gsub(/`[^`]*`/, ""); print}' "$file_path" \
  | grep -noiwE 'organize[sd]?|organizing|organization|behaviors?|colors?|analyze[sd]?|analyzing|customize[sd]?|optimize[sd]?|recognize[sd]?|summarize[sd]?|standardize[sd]?|initialize[sd]?|centers?|favors?|labor|catalogs?|modeling|traveled|fulfill' \
  || true)"

if [[ -n "$findings" ]]; then
  echo "British English check for $file_path (line:word):" >&2
  echo "$findings" | head -20 >&2
  echo "Re-spell prose only. Leave code, file names, JSON keys and CLI flags alone." >&2
  exit 2
fi
exit 0
