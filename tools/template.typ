// Layout and rendering helpers for the paper.
// Hand-edited source of truth for how the PDF looks. The build script
// (tools/build_paper.py) generates out/main.typ, which does
//   #import "/tools/template.typ": *
//   #show: conf.with(title: ..., author: ...)
// and then stitches the paper body from Markdown segments via `md`, `callout`,
// `figurebox`, `filecard`, `pitfallcard`, `reflist` and `refentry`. Everything that needs
// a file lookup (does the card's file exist, which references are cited) is
// resolved in Python; the helpers here only lay things out.
//
// Markdown is rendered by the vendored `cmarker` package (fully offline, no
// network fetch). Section numbers come from the heading show-set below and are
// NEVER typed into paper.md.

#import "/tools/vendor/cmarker/lib.typ" as cmarker

// Flatten heading content to a plain string (Typst has no built-in for this).
#let to-string(content) = {
  if type(content) == str {
    content
  } else if content.has("text") {
    let t = content.text
    if type(t) == str { t } else { "" }
  } else if content.has("children") {
    content.children.map(to-string).join("")
  } else if content.has("body") {
    to-string(content.body)
  } else {
    ""
  }
}

// --- Palette --------------------------------------------------------------
// Evidenze green (#27B564, the green bar of the logo's E, as in the talk)
// for rules and bands, and a darker shade of it for text, which keeps
// 5:1 contrast on white (the author's choice of 2026-10-26, over purple).
#let brand = rgb("#27b564")
#let accent = rgb("#1b7e46")
#let ink = rgb("#1a1a1a")
#let muted = rgb("#666666")

// --- Callout boxes --------------------------------------------------------
// Four kinds: `note` (neutral aside, sparingly used for small analogies),
// `warning`, `tip`, and `disclaimer` (used once, after the abstract, to say
// how the paper was made; neutral grey on a light fill, a note on method
// rather than an alarm). An unknown kind is rendered loudly so typos are caught in
// proofreading instead of silently styled as a tip.
#let callout(kind: "note", body) = {
  let col = if kind == "note" {
    accent
  } else if kind == "warning" {
    rgb("#b0342b")
  } else if kind == "tip" {
    rgb("#2a7a4b")
  } else if kind == "disclaimer" {
    muted   // a note on method, not an alarm: neutral grey, like the header
  } else {
    rgb("#e08a00") // unknown kind — deliberately conspicuous
  }
  let label = if kind == "note" {
    "Note"
  } else if kind == "warning" {
    "Warning"
  } else if kind == "tip" {
    "Tip"
  } else if kind == "disclaimer" {
    "How this paper was made"
  } else {
    "Unknown callout: " + kind
  }
  block(
    width: 100%,
    inset: (x: 10pt, y: 8pt),
    radius: (right: 4pt),   // square on the bar side, so the bar ends straight
    fill: if kind == "disclaimer" { luma(246) } else { col.lighten(90%) },
    stroke: (left: 2pt + col),
    above: 12pt,
    below: 12pt,
  )[
    #text(size: 7.5pt, weight: "bold", fill: col, tracking: 0.6pt)[#upper(label)]
    #v(5pt, weak: true)
    #set text(size: 9.5pt)   // every aside one size: callouts, file cards
    #body
  ]
}

// --- Image path resolution ------------------------------------------------
// Images appear only in `::: figure` fences. The build resolves each path
// (relative to paper/, so the talk's images are `../slides/beats/…`), checks
// the file exists and hands `figurebox` project-root paths. Figures have a
// fixed height, not a width: the page budget then does not depend on the
// aspect ratio of the images. At 40 mm two 16:9 drawings and their gutter
// take 147 mm of the 164 mm text width, so a pair costs no more height than
// one image; 44 mm would fill the width but cost the page a line.
#let figure-height = 40mm
#let img(path, alt: none) = image(
  "/paper/" + path, alt: alt, width: 100%, height: figure-height, fit: "contain",
)

// --- Markdown tables ------------------------------------------------------
// cmarker emits plain `table(columns: n, ...)` calls with auto columns. The
// show rule below re-lays them out: each column's width is measured from its
// cells, narrow columns keep their natural width, wide ones share the rest,
// and no column gets narrower than its widest code span, so identifiers never
// wrap. Smaller face, striped rows: the header row sits on a light accent
// band, every second body row on a light grey one, and a thin accent rule
// closes the table. Lines inside a cell sit closer together than the rows,
// so a cell of two lines still reads as one row. The first column holds each
// row's key (mechanism, scope, option, step) and is set bold, except in a
// two-column table whose first column is the wider one. Tables of up to ten
// body rows stay on one page; longer ones may break, and Typst repeats the
// header row on the continuation page.

// Inline code spans inside a cell: they should not wrap, so the widest one
// sets the column's minimum width.
#let raw-spans(c) = {
  if type(c) != content { return () }
  if c.func() == raw { return (c,) }
  if c.has("children") { return c.children.map(raw-spans).flatten() }
  if c.has("body") { return raw-spans(c.body) }
  ()
}

// Wide columns share the space in proportion to the square root of their
// natural width, so a long prose column does not starve its neighbour.
#let table-weight = w => calc.sqrt(w / 1pt)

#let restyle-table(t) = {
  // Guard against recursion: our own table has fixed columns, cmarker's has auto.
  if type(t.columns) == int or not t.columns.all(c => c == auto) { return t }
  let n = t.columns.len()
  let cells = ()
  for it in t.children {
    if it.func() == table.header { cells += it.children } else { cells.push(it) }
  }
  let rows = calc.quo(cells.len(), n)
  let inset = (x: 6pt, y: 3.1pt)
  set text(size: 9pt)
  set par(justify: false, leading: 0.42em)
  block(
    breakable: rows > 11,   // header row plus ten body rows
    above: 10pt,
    below: 10pt,
    layout(size => {
      // Natural one-line width of each column and its minimum (the widest
      // code span), measured in the table's own styles, plus the cell inset.
      let body(c) = if c.func() == table.cell { c.body } else { c }
      let nat = (0pt,) * n
      let low = (0pt,) * n
      for (i, c) in cells.enumerate() {
        let col = calc.rem(i, n)
        // The header row and the key column are measured bold, as they are set.
        let shown = if i < n or col == 0 { text(weight: "bold", body(c)) } else { body(c) }
        nat.at(col) = calc.max(nat.at(col), measure(shown).width + 2 * inset.x)
        for r in raw-spans(body(c)) {
          low.at(col) = calc.max(low.at(col), measure(r).width + 2 * inset.x)
        }
      }
      let W = size.width
      // Narrow columns keep their natural width; wide ones share the rest,
      // never below their minimum.
      let weight(i) = table-weight(nat.at(i))
      let fix = (none,) * n
      let again = true
      while again {
        again = false
        let open = range(n).filter(i => fix.at(i) == none)
        if open.len() == 0 { break }
        let rest = W - fix.filter(w => w != none).sum(default: 0pt)
        for i in open {
          if nat.at(i) <= rest / open.len() { fix.at(i) = nat.at(i); again = true }
        }
        if again { continue }
        let total = open.map(weight).sum()
        for i in open {
          if weight(i) / total * rest < low.at(i) { fix.at(i) = low.at(i); again = true }
        }
      }
      let open = range(n).filter(i => fix.at(i) == none)
      let widths = if open.len() > 0 {
        let rest = W - fix.filter(w => w != none).sum(default: 0pt)
        let total = open.map(weight).sum()
        range(n).map(i => if fix.at(i) != none { fix.at(i) } else { weight(i) / total * rest })
      } else {
        let total = fix.sum()
        if total <= W {
          fix.map(w => w + (W - total) / n)   // spread the slack evenly
        } else {
          // Over-full: take the excess from what each column has above its minimum.
          let give = range(n).map(i => fix.at(i) - low.at(i))
          let g = give.sum()
          range(n).map(i => fix.at(i) - give.at(i) / g * (total - W))
        }
      }
      // Key column: in every table of three or more columns, and in a
      // two-column table whose first column is the narrower one.
      let key = n >= 3 or nat.at(0) < nat.at(1)
      show table.cell.where(y: 0): set text(fill: accent.darken(15%))
      show table.cell.where(x: 0): it => if key and it.y > 0 { text(weight: "bold", it) } else { it }
      let tbl = table(
        columns: widths,
        align: left + top,
        inset: inset,
        fill: (x, y) => if y == 0 { accent.lighten(84%) } else if calc.even(y) { luma(244) } else { none },
        stroke: (x, y) => if y == rows - 1 { (bottom: 0.8pt + accent.lighten(45%)) } else { none },
        ..t.children,
      )
      tbl
    }),
  )
}

// --- Markdown segment renderer -------------------------------------------
// Reads a segment file written by the build script and renders it, wiring the
// image and table overrides into cmarker's scope.
#let md(path) = cmarker.render(read(path), scope: (image: img))

// --- Figure with caption --------------------------------------------------
// One image, or two side by side with a 4 mm gutter, each at the fixed
// figure height, the caption below. Figures float by default: one that does
// not fit at its position moves to the top or bottom of a page and the text
// flows on. A `placement: none` line in the fence pins the figure where it
// stands; the paper's figures use it, so the page rule decides where they go.
// Every drawing is generated, so each carries the EU icon for AI-generated
// content in its top right corner, as on the slides: the basic "AI" in a black
// circle, `slides/brand/eu-ai-black.png` as the EU published it. In that file
// of 2363 × 2364 px the circle is 1524 px across and starts at (372, 420), so
// the box clips the transparent margin. At 4 mm the letters stand about
// 1.5 mm tall, readable in print. A white rim, invisible on white, ends any
// line of the drawing just short of the icon.
#let ai-label-size = 4mm
#let ai-label-inset = 2mm
#let ai-label-rim = 0.5mm
#let ai-label = {
  let px = ai-label-size / 1524   // one pixel of the EU's file at this size
  // Both sides are set: with the width alone, the image would take the box's height as
  // its own and crop itself to cover it.
  box(width: ai-label-size, height: ai-label-size, clip: true, place(
    dx: -372 * px, dy: -420 * px,
    image("/slides/brand/eu-ai-black.png", alt: "AI generated", width: 2363 * px, height: 2364 * px),
  ))
}
#let labelled(path, alt, height: figure-height) = box({
  image(path, alt: alt, height: height, fit: "contain")
  place(top + right, dx: -ai-label-inset + ai-label-rim, dy: ai-label-inset - ai-label-rim,
    circle(radius: ai-label-size / 2 + ai-label-rim, fill: white))
  place(top + right, dx: -ai-label-inset, dy: ai-label-inset, ai-label)
})

#let figurebox(paths, alts, caption-path, placement: auto, height: figure-height) = figure(
  grid(
    columns: paths.len(),
    column-gutter: 4mm,
    ..paths.zip(alts).map(((p, a)) => labelled(p, a, height: height)),
  ),
  caption: md(caption-path),
  placement: placement,
)

// A single image beside a paragraph, the caption under the image: the
// image keeps its height, its column is as wide as the image, and the
// paragraph takes the rest of the line. The Introduction uses it, on a page
// with no line to spare.
#let sidefigure(text-path, paths, alts, caption-path, side: "right", height: figure-height) = context {
  let pic = labelled(paths.first(), alts.first(), height: height)
  let w = measure(pic).width
  let fig = figure(pic, caption: md(caption-path), placement: none)
  let txt = md(text-path)
  block(above: 0.8em, below: 0.8em, grid(
    columns: if side == "right" { (1fr, w) } else { (w, 1fr) },
    column-gutter: 6mm,
    ..(if side == "right" { (txt, fig) } else { (fig, txt) }),
  ))
}

// --- File card ------------------------------------------------------------
// A `::: filecard` fence describes one repository file instead of quoting
// it: a coloured tag for the kind of file, the path linked to GitHub, and a
// few bullets on what the file does. Rendered as a numbered figure of its own
// kind ("File 2"), caption on top, so the prose refers to cards by number.
// Cards do not float and do not break; the source keeps them short.
#let filecard-colour(kind) = (
  rules: accent,
  skill: rgb("#2a7a4b"),
  hook: rgb("#b0342b"),
  settings: rgb("#1f5f8b"),
  agent: rgb("#8a6d1f"),
  script: rgb("#5b5b5b"),
).at(kind, default: rgb("#e08a00"))

#let filecard-label(kind) = (
  rules: "Rules file",
  skill: "Skill",
  hook: "Hook",
  settings: "Settings",
  agent: "Subagent",
  script: "Script",
).at(kind, default: "Unknown kind: " + kind)

#let filecard(kind: "hook", path: "", url: none, caption-path, body-path) = {
  let col = filecard-colour(kind)
  let shown = raw(path)
  figure(
    kind: "file",
    supplement: [File],
    caption: md(caption-path),
    block(
      width: 100%,
      breakable: false,
      inset: (x: 10pt, y: 7pt),
      radius: 4pt,
      fill: luma(248),
      stroke: 0.5pt + luma(215),
      {
        set align(left)
        set text(size: 9.5pt)
        set par(justify: false)
        box(
          fill: col,
          inset: (x: 5pt, y: 3pt),
          radius: 3pt,
          baseline: 25%,
          text(size: 7.5pt, weight: "bold", fill: white, tracking: 0.6pt, upper(filecard-label(kind))),
        )
        h(7pt)
        if url != none { link(url, shown) } else { shown }
        v(5pt, weak: true)
        line(length: 100%, stroke: 0.4pt + luma(215))
        v(5pt, weak: true)
        md(body-path)
      },
    ),
  )
}

// --- Pitfall card ---------------------------------------------------------
// A `::: pitfalls` fence closes each mechanism chapter: the bullets on the
// left and the chapter's warning, which follows a `---` line, as a narrower
// box on the right. One red card instead of a numbered
// subsection and a separate warning box. Not a figure: no number, no float,
// and it does not break across pages.
#let pitfall-red = rgb("#b0342b")

#let pitfallcard(bullets-path, warning: none) = {
  let tag = box(
    fill: pitfall-red,
    inset: (x: 5pt, y: 3pt),
    radius: 3pt,
    baseline: 25%,
    text(size: 7.5pt, weight: "bold", fill: white, tracking: 0.6pt, upper("Pitfalls")),
  )
  let warning-box = if warning != none {
    block(
      width: 100%,
      inset: (left: 8pt, y: 2pt),
      stroke: (left: 2pt + pitfall-red),
      {
        text(size: 7.5pt, weight: "bold", fill: pitfall-red, tracking: 0.6pt, upper("Warning"))
        v(4pt, weak: true)
        set text(size: 9pt)
        md(warning)
      },
    )
  }
  block(
    width: 100%,
    breakable: false,
    inset: (x: 8pt, y: 6pt),
    radius: 4pt,
    fill: pitfall-red.lighten(93%),
    stroke: 0.5pt + pitfall-red.lighten(55%),
    above: 10pt,
    below: 10pt,
    {
      set align(left)
      set text(size: 9pt)
      set par(justify: false)
      tag
      v(4pt, weak: true)
      line(length: 100%, stroke: 0.4pt + pitfall-red.lighten(60%))
      v(4pt, weak: true)
      if warning != none {
        grid(
          columns: (2fr, 1fr),
          column-gutter: 12pt,
          md(bullets-path),
          warning-box,
        )
      } else {
        md(bullets-path)
      }
    },
  )
}

// --- Reference list -------------------------------------------------------
// The build script reads paper/references.md and emits one `reflist` with
// every source, in the order of the numbers, which follow the order of
// first citation. Each entry carries the label `ref-n`, which the citations
// in the prose (`[n]`, rewritten to links by the build) point at.
//
// An entry is a pair (number, segment path). Documentation pages cited one
// after another share one entry: (number, group name, pages), where each
// page is (number, page name, URL, date note) and the first page takes the
// entry's number. The list stands in two columns of equal height: each
// entry is measured at the column's width, and the right column starts with
// the entry that would carry the left one past half the total.
#let refline(n, body) = block(width: 100%, breakable: false, {
  set text(size: 9pt, hyphenate: false)
  set par(justify: false, leading: 0.45em)
  grid(
    columns: (2.2em, 1fr),
    column-gutter: 4pt,
    align: (right, left),
    text(fill: accent)[\[#n\]],
    body,
  )
})

#let refentry(n, body-path) = [
  #refline(n, {
    // The URL tail is set as code by the build; in a 9pt list the serif
    // is calmer and a third narrower. Undo the raw size (0.8em x 1.08em).
    // A URL breaks only after a slash, a hyphen or a question mark, never
    // inside a word, so a long page name or query still fits the narrow column.
    show raw: it => {
      set text(font: "Libertinus Serif", size: 1em / 0.864)
      show regex("[^/?-]+[/?-]*"): box
      text(it.text)
    }
    md(body-path)
  }) #label("ref-" + str(n))
]

#let refpages(n, group, pages) = {
  let page-link(p) = {
    let (m, name, url, note) = p
    link(url, name) + note
  }
  [#refline(n, {
    group + ", " + page-link(pages.first())
    for p in pages.slice(1) {
      "; "
      [#box[#text(fill: accent)[\[#p.first()\]] #page-link(p)]#label("ref-" + str(p.first()))]
    }
    "."
  }) #label("ref-" + str(n))]
}

#let reflist(items, gap: 2pt) = block(above: 6pt, width: 100%, layout(size => {
  let gutter = 14pt
  let col = (size.width - gutter) / 2
  let entries = items.map(it => if it.len() == 2 { refentry(..it) } else { refpages(..it) })
  let heights = entries.map(e => measure(block(width: col, e)).height)
  let half = (heights.sum() + gap * (entries.len() - 2)) / 2
  let split = entries.len()
  let acc = 0pt
  for (i, h) in heights.enumerate() {
    if acc + h / 2 > half {
      split = i
      break
    }
    acc += h + gap
  }
  grid(
    columns: (col, col),
    column-gutter: gutter,
    stack(spacing: gap, ..entries.slice(0, split)),
    stack(spacing: gap, ..entries.slice(split)),
  )
}))

// --- Document shell -------------------------------------------------------
#let conf(
  title: "",
  subtitle: none,
  author: "",
  affiliation: "",
  city: "",
  country: "",
  conference: "",
  date: "",
  paper-number: "",
  subject: "",
  keywords: (),
  doc,
) = {
  // PDF document properties. PHUSE asks for title, keywords and first author,
  // and for the paper number in the subject field; `description` is what
  // Typst writes into the PDF subject.
  set document(
    title: if subtitle == none { title } else { title + " — " + subtitle },
    author: author,
    keywords: keywords,
    description: if subject == "" { none } else { subject },
  )
  set page(
    paper: "a4",
    margin: (top: 2.4cm, bottom: 2.2cm, x: 2.3cm),
    header: context {
      if counter(page).get().first() > 1 {
        set text(size: 8pt, fill: muted)
        title
        h(1fr)
        conference
        if paper-number != "" [ · Paper #paper-number]
        line(length: 100%, stroke: 0.4pt + muted.lighten(30%))
      }
    },
    footer: context {
      set text(size: 8pt, fill: muted)
      line(length: 100%, stroke: 0.4pt + muted.lighten(30%))
      v(2pt)
      author
      h(1fr)
      counter(page).display("1")
    },
  )
  set text(font: "Libertinus Serif", size: 10.5pt, fill: ink, lang: "en", region: "gb")
  set par(justify: true, leading: 0.62em, spacing: 0.9em)

  // Numbered section headings: "1." for chapters, "1.1" for sections (no
  // trailing dot below the top level). Never typed into paper.md.
  set heading(numbering: (..nums) => {
    let n = nums.pos()
    if n.len() == 1 { str(n.first()) + "." } else { n.map(str).join(".") }
  })
  show heading: set block(above: 1.1em, below: 0.55em)
  show heading.where(level: 1): set block(above: 1.5em, below: 0.7em)
  show heading.where(level: 2): set text(size: 12pt)
  show heading.where(level: 3): set text(size: 10.5pt, style: "italic")

  // Front/back matter (Abstract, References, Contact Information) arrives from
  // the build as `heading(numbering: none)`: it neither steps the chapter
  // counter nor carries a number in the PDF bookmarks, and is set styled but
  // without a number.
  show heading.where(level: 1): it => {
    if it.numbering == none {
      // The reference list gets its own page so its heading and lead-in
      // never sit alone at the bottom of the conclusion's page.
      if to-string(it.body) == "References" { pagebreak(weak: true) }
      block(above: 1.5em, below: 0.7em, text(size: 14pt, fill: accent, weight: "bold", it.body))
    } else {
      // Chapter opener: the number large beside the title, a thin rule
      // below. Chapters 2 to 11 start on a new page, so the reader never
      // meets a chapter in the middle of one; the Introduction shares
      // page 1 with the Abstract and the Conclusion follows chapter 11's
      // page, as do References and Contact Information.
      context {
        let n = counter(heading).get().first()
        if n >= 2 and n <= 11 { pagebreak(weak: true) }
        block(above: 1.5em, below: 0.9em, width: 100%, {
          grid(
            columns: (auto, 1fr),
            column-gutter: 10pt,
            align: bottom,   // number and title share a baseline
            text(size: 24pt, fill: accent, weight: "bold", str(n)),
            text(size: 14pt, fill: accent, weight: "bold", it.body),
          )
          v(6pt, weak: true)
          line(length: 100%, stroke: 0.6pt + brand.lighten(30%))
        })
      }
    }
  }

  // Code: Libertinus Mono, bundled under tools/fonts/ so it needs no system
  // install. Its x-height is about 15% taller than the serif's and every glyph
  // is 0.64em wide, so at the same size code looks heavy and oversized. Typst
  // sets raw text to 0.8em; the 1.08em here multiplies with it to 0.864 of the
  // surrounding size (body, table, caption), where the x-heights match. Short
  // identifiers are boxed so that `/context` never splits after its slash,
  // up to 30 characters so that a flag such as --dangerously-skip-permissions
  // never splits at its own hyphen; longer paths may still wrap. Block code
  // has a fixed small size.
  show raw: set text(font: ("Libertinus Mono", "DejaVu Sans Mono"))
  show raw.where(block: false): set text(size: 1.08em)
  show raw.where(block: false): it => if it.text.len() <= 30 { box(it) } else { it }
  show raw.where(block: true): set text(size: 8pt)
  // Code blocks stay whole: no orphaned first line at a page bottom. The
  // paper carries no code blocks any more (file cards replaced them), but
  // the rule stays so a short one renders sensibly if one returns. Each
  // source line is its own paragraph so that a line too long for the box
  // wraps with a hanging indent and reads as a continuation.
  show raw.where(block: true): it => block(
    width: 100%,
    breakable: false,
    fill: luma(246),
    inset: 8pt,
    radius: 3pt,
    stroke: 0.4pt + luma(220),
    {
      set align(left)
      set par(hanging-indent: 1.5em, spacing: 0.65em, leading: 0.65em, justify: false)
      for l in it.lines { par(l) }
    },
  )

  // Keep a number with the word before it, so "File 1", "Figure 2",
  // "chapter 6" or "Haiku 4.5" never break across two lines.
  show regex("\b(File|Figure|chapter|Chapter|version|Opus|Sonnet|Haiku|Fable) \d"): it => it.text.replace(" ", "\u{a0}")

  // Links are how the paper points at the complete files in the repository
  // (file-card headers, the companion-repository link) and at the reference
  // entries. Tint them so a reader of the PDF can tell them apart from plain
  // text without an underline.
  show link: set text(fill: accent)

  set figure(numbering: "1")
  show figure.caption: set text(size: 9pt, fill: muted)
  show figure.caption: set align(left)
  show figure.caption: it => {
    // "Figure 1." in the ink colour, then the caption
    text(fill: ink, weight: "bold", [#it.supplement #context it.counter.display(it.numbering).])
    [ ]
    it.body
  }
  // File cards carry their caption above the card, like a heading for the
  // file, and sit flush left rather than centred like an image.
  show figure.where(kind: "file"): set figure.caption(position: top)
  show figure.where(kind: "file"): set align(left)
  show figure.where(kind: "file"): set block(above: 10pt, below: 10pt)

  // Tables: header row bold, layout via `restyle-table` (defined above).
  show table.cell.where(y: 0): set text(weight: "bold")
  // Libertinus Mono has no bold; in a header cell, code is set in the bold
  // serif so the header row reads as one weight.
  show table.cell.where(y: 0): it => {
    show raw: r => text(font: "Libertinus Serif", size: 1em / 0.864, r.text)
    it
  }
  show table: restyle-table

  // --- Title block ---
  // Laid out as PHUSE asks: the paper number centred above the title, the
  // title centred, then "Author, Company, City, Country" on one line, no job
  // title and no address. The conference line and the accent rule are ours.
  let author-line = (author, affiliation, city, country).filter(s => s != "").join(", ")
  block(width: 100%)[
    #set align(center)
    #if paper-number != "" [
      #text(size: 10pt, fill: muted)[Paper #paper-number]
      #v(10pt, weak: true)
    ]
    #text(size: 20pt, weight: "bold", fill: ink)[#title]
    #if subtitle != none [
      #v(7pt, weak: true)
      #text(size: 12pt, fill: muted)[#subtitle]
    ]
    #v(12pt, weak: true)
    #text(size: 10.5pt)[#author-line]
    #v(4pt, weak: true)
    #text(size: 9pt, fill: muted)[#(
      (conference, date).filter(s => s != "").join(" · ")
    )]
    #v(8pt, weak: true)
    #line(length: 100%, stroke: 1.2pt + brand)
  ]
  v(6pt)

  doc
}
