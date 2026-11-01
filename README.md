# Hang Yi — Personal website

An English academic homepage based on al-folio.

## Edit content

- Introduction: `_pages/about.md`
- Research: `_pages/research.md`
- CV: `_data/cv.yml`
- Public profile links: `_data/socials.yml`
- Name and hosting URL: `_config.yml`

The initial version contains education and ongoing research work. Add an email address, portrait, downloadable CV, and publications when ready.

## Local preview

Run `python3 tools/render_preview.py` and open `dist/index.html`. The preview reads the Markdown and CV source files and uses locally cached al-folio CSS. It requires Python Markdown and the YAML parser bundled with Ruby. It does not validate the native Jekyll build.

## Full al-folio build

Use Ruby 3.3 and a compatible Bundler, then run:

```bash
bundle install
npm ci
bundle exec jekyll serve
```

The site is configured for a root domain with an empty baseurl. Its GitHub Pages address is https://traelinb.github.io. A project-subdirectory deployment needs its own baseurl.

See docs/INSTALL.md for the full setup instructions.

## Credits

Built from [al-folio](https://github.com/alshedivat/al-folio), distributed under the MIT license.

## GitHub Pages

The `.github/workflows/pages.yml` workflow publishes the static files in `dist/` whenever `main` changes. Repository Settings → Pages must use **GitHub Actions** as the publishing source.

After editing content or assets, run `python3 tools/render_preview.py` and commit both the source changes and the regenerated `dist/` files. The workflow publishes that export directly, without requiring a Jekyll build.

## Build validation

The three-page static export in `dist/` passed local asset/link checks, JavaScript syntax checks, and the upstream starter style contract. The native Jekyll build has not been validated on this Mac; it requires the Ruby, Bundler, and npm dependencies described above.
