# english-md
Liturgical texts in English in Markdown format

This repository contains liturgical texts in English
in Markdown format. The format is described
in the [cumd package](https://github.com/slavonic/cumd).

The extended Markdown syntax is described in the
[Sandbox](https://github.com/slavonic/cu-md-sandbox/blob/master/markup-tags.md)
## Building the website

The [scripts/](scripts/) folder contains a static site builder that turns these Markdown
books into a mobile-friendly reading website. It is the same pipeline and design as the
[Ponomar Library of Liturgical Texts](https://www.ponomar.net/maktabah/) built from the
[Sandbox](https://github.com/slavonic/cu-md-sandbox).

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r scripts/requirements.txt
python scripts/build_library.py      # → _site/
```

For all options, the converter's rules and automatic builds, see
[scripts/README.md](scripts/README.md).
