# Personal homepage

This is Hang Yi's own site, based on al-folio. The source of truth is `_pages/`, `_data/`, and `_config.yml`.

- Keep biographical claims grounded in supplied or verified facts.
- Do not add a personal email, portrait, publications, or external contact details without the user's choice.
- Regenerate the static preview with `python3 tools/render_preview.py` after content edits. This requires Python Markdown and Ruby's bundled YAML parser.
- The static preview uses official al-folio compiled CSS and a small preview shell. It does not validate the full Jekyll build.
- The native al-folio build requires Ruby 3.3, Bundler, and the Gemfile dependencies. Keep shared theme runtime in the upstream gems.
- `.openai/hosting.json` identifies the private Site and declares `dist/` as its static output. Preserve its project ID.
