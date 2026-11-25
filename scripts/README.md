# Library website builder

These scripts turn the Markdown books in this repository into a static, mobile-friendly
website, the English counterpart of the
[Ponomar Library of Liturgical Texts](https://www.ponomar.net/maktabah/). They are the
same pipeline and design as in
[slavonic/cu-md-sandbox](https://github.com/slavonic/cu-md-sandbox/tree/master/scripts),
set up for English texts.

```
scripts/
  build_library.py   build the whole site (or some books)
  cumd_web.py        Markdown → HTML: the cumd rules + page links, notes, images
  library.toml       catalog: display titles, front-page sections, PDF scans
  i18n.py            interface strings
  templates/         Jinja2 page templates
  static/            CSS and JavaScript (copied to assets/)
  fonts/             EB Garamond (SIL Open Font License), self-hosted
  tests/             pytest tests for the converter
```

`cumd_web.py` is identical to the Church Slavonic repository's (the tests here add English
cases), so a fix in one can be copied to the other as is.

## Build

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r scripts/requirements.txt
python scripts/build_library.py                     # → _site/
python -m http.server -d _site 8000                 # → http://localhost:8000
```

* `python scripts/build_library.py MenaionLambertsenSeptember` rebuilds only that book
  (the front page is always rebuilt).
* `--out DIR` chooses the output folder (default `_site/`).
* `--fonts-dir DIR` self-hosts another folder of `*.woff2` files named
  `Family-Regular.woff2`, `Family-Italic.woff2`, `Family-Bold.woff2`, `Family-BoldItalic.woff2`
  (default `scripts/fonts/`); `--fonts-css URL` links a font stylesheet instead.
  The faces offered in the reader are listed in `TYPEFACES` in `build_library.py`.
* `--base-url https://…/` also writes `sitemap.xml`.

At the end the build lists things to fix in the sources (indented lines that Markdown
shows as code, doubled `==`, images that are not in the repository, chapter files
missing from `manifest.xml`).

## What the converter does

All rules of [`cumd`](https://github.com/slavonic/cumd) are used as they are, in its
“simplified” mode, which writes ordinary `<span class="red">` etc., so text copied from
the site keeps its red in Word. The ones the English texts use:

| Markdown | HTML |
|---|---|
| `*rubric*`, `**Be It Known:**` | italic, bold |
| `=He=` | red text |
| `{{text_align=center}}` | `style="text-align:center"` (kept when pasting into Word) |
| `\[Ps. 45: 2\]`, `\(28:10-17\)` | `[Ps. 45: 2]`, `(28:10-17)` |

`cumd_web.py` also understands page tags (`<<25>>`), notes (`[[…]]`) and images, as
described in the Church Slavonic repository; none of the books here use them yet.

## Page scans (PDF)

No book here has scans. If some are added: list each volume in `library.toml` (see the
comments there), put `<<page>>` tags in the chapters, prepare the PDFs with
`prepare_pdf.py` from cu-md-sandbox, and build once with `--fetch-pdfjs`. The build then
also writes the scan viewer (`scan.html`) and links the page numbers to it.

## Adding a book

Add the folder with `manifest.xml` and `chapters/*.md` (and, if you have one, `cover.png`).
It appears under “Other books” until you give it an entry in `library.toml`.

## Automatic builds

`.github/workflows/build-site.yml` tests the converter and builds the site on every push to
`master`; the built site can be downloaded from the run's artifacts. When the `DEPLOY_*`
secrets are set, it also rsyncs the site to the server (leaving `pdf/` alone). Set the
repository variable `SITE_URL` to get a `sitemap.xml`.
