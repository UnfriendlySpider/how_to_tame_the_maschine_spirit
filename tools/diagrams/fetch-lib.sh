#!/bin/sh
# Fetch what export.mjs renders with into tools/diagrams/lib/ (git-ignored):
# Excalidraw's export library, pinned to @excalidraw/utils 0.1.2 on jsDelivr,
# and Excalidraw's two fonts, Virgil (hand-drawn) and Cascadia (code). Each
# file is checked against the checksum of the copy the paper's diagrams were
# made with on 2026-10-26.
set -eu
LIB="$(dirname "$0")/lib"
mkdir -p "$LIB"
fetch() {
  curl -fsSL "$1" -o "$LIB/$2"
  echo "$3  $LIB/$2" | sha256sum -c -
}
fetch https://cdn.jsdelivr.net/npm/@excalidraw/utils@0.1.2/dist/excalidraw-utils.min.js excalidraw-utils.min.js \
  67be3ac9b245ba979aa638d9a7dc24becb967b3e7e3f91cf2b7a4e4bd27e4e6a
fetch https://excalidraw.com/Virgil.woff2 Virgil.woff2 \
  9976295bfe709bdea64839a4d4e9a1d436dd6eb67538399a5a0e8b8fadbcf1cf
fetch https://excalidraw.com/Cascadia.woff2 Cascadia.woff2 \
  6d27c0474bb6c7922911f90ae811918f6be943005f1c4a6ec0e5b70a2bfddf16
