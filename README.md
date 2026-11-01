# Hang Yi — Personal Website

**[Visit my website → traelinb.github.io](https://traelinb.github.io/)**

My personal academic website, featuring my background, research in tabular data synthesis, and CV.

## Update content

| Content | Source |
| --- | --- |
| Introduction, education, and profile links | [`_pages/about.md`](_pages/about.md) |
| Research | [`_pages/research.md`](_pages/research.md) |
| CV | [`_data/cv.yml`](_data/cv.yml) |
| Styles | [`tools/preview-assets/css/preview.css`](tools/preview-assets/css/preview.css) |
| Browser icon | [`assets/img/favicon-ginkgo.png`](assets/img/favicon-ginkgo.png) |

## Preview and deploy

Requires Python 3 with [Python-Markdown](https://python-markdown.github.io/) and Ruby for YAML parsing.

Generate the static website:

```bash
python3 tools/render_preview.py
```

Open `dist/index.html` for a local preview. Commit the source changes and regenerated `dist/` files to `main`; GitHub Actions publishes the website to GitHub Pages automatically.

## Credits

Based on [al-folio](https://github.com/alshedivat/al-folio). See [LICENSE](LICENSE) for license details.
