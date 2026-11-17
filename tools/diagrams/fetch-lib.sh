#!/bin/sh
# Fetch what export.mjs renders with into tools/diagrams/lib/ (git-ignored):
# Excalidraw's export library, pinned to @excalidraw/utils 0.1.2 on jsDelivr,
# and Excalidraw's two fonts, Virgil (hand-drawn) and Cascadia (code). The
# expected checksums are in lib.sha256, the checksums of the copy the paper's
# diagrams were made with on 2026-10-26. A download is checked in lib/ under a
# temporary name and moved into place only when it matches, so a file that
# fails never stands where export.mjs would read it; a file that is already
# there and matches is left alone.
set -eu
HERE="$(dirname "$0")"
LIB="$HERE/lib"
SUMS="$HERE/lib.sha256"

if command -v sha256sum >/dev/null 2>&1; then
  hash_of() { sha256sum "$1" | cut -d ' ' -f 1; }
elif command -v shasum >/dev/null 2>&1; then
  hash_of() { shasum -a 256 "$1" | cut -d ' ' -f 1; }
else
  echo "error: needs sha256sum or shasum -a 256 to check the downloads; install one and run again" >&2
  exit 1
fi

mkdir -p "$LIB"
fetch() {   # URL, file name
  want="$(grep "  $2\$" "$SUMS" | cut -d ' ' -f 1)"
  if [ -z "$want" ]; then
    echo "error: $SUMS has no checksum for $2" >&2
    exit 1
  fi
  if [ -f "$LIB/$2" ] && [ "$(hash_of "$LIB/$2")" = "$want" ]; then
    echo "ok       $2 (already there)"
    return
  fi
  curl -fsSL "$1" -o "$LIB/$2.part"
  got="$(hash_of "$LIB/$2.part")"
  if [ "$got" != "$want" ]; then
    rm -f "$LIB/$2.part" "$LIB/$2"
    echo "error: $2 from $1 has the checksum $got, expected $want; nothing was kept" >&2
    exit 1
  fi
  mv "$LIB/$2.part" "$LIB/$2"
  echo "ok       $2 (downloaded)"
}
fetch https://cdn.jsdelivr.net/npm/@excalidraw/utils@0.1.2/dist/excalidraw-utils.min.js excalidraw-utils.min.js
fetch https://excalidraw.com/Virgil.woff2 Virgil.woff2
fetch https://excalidraw.com/Cascadia.woff2 Cascadia.woff2
