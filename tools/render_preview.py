"""Build a local static preview from the site's Markdown and CV data.

Uses the official al-folio compiled CSS stored in tools/preview-assets/css.
This is a lightweight content preview, not a replacement for a Jekyll build.
Requires Python Markdown and the YAML parser bundled with Ruby.
"""

from html import escape
from pathlib import Path
import json
import os
import re
import subprocess
import shutil

import markdown

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist"


def yaml_file(path):
    result = subprocess.check_output(
        ["ruby", "-rjson", "-ryaml", "-e", "puts JSON.generate(YAML.load_file(ARGV[0]))", str(path)],
        text=True,
    )
    return json.loads(result)


def link(target, page):
    destination = "index.html" if target == "/" else target.strip("/") + "/index.html"
    return os.path.relpath(destination, str(Path(page).parent))


def render_markdown(path, page):
    text = path.read_text().split("\n---\n", 1)[1]
    text = re.sub(
        r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}",
        lambda match: link(match.group(1), page),
        text,
    )
    return markdown.markdown(text, extensions=["extra", "sane_lists"])


def format_date(value):
    return re.sub(r"^(\d{4})-(\d{2})$", r"\1.\2", str(value))


def render_cv(cv):
    parts = ["<section class='cv-section'><h2>Education</h2>"]
    for item in cv["sections"]["Education"]:
        details = [item.get("area"), *item.get("highlights", []), item.get("location")]
        parts.append(
            "<div class='cv-entry'><p class='cv-date'>"
            + escape(format_date(item["start_date"])) + "–"
            + escape(format_date(item["end_date"])) + "</p><div><h3>"
            + escape(item["institution"]) + "</h3><p>"
            + "<br>".join(escape(str(detail)) for detail in details if detail)
            + "</p></div></div>"
        )
    parts.append("</section><section class='cv-section'><h2>Research experience</h2>")
    for item in cv["sections"]["Experience"]:
        parts.append(
            "<div class='cv-entry'><p class='cv-date'>"
            + escape(format_date(item["start_date"])) + "–"
            + escape(format_date(item["end_date"])) + "</p><div><h3>"
            + escape(item["company"]) + "</h3><p class='muted'>"
            + escape(item["position"]) + "</p><ul>"
            + "".join("<li>" + escape(line) + "</li>" for line in item["highlights"])
            + "</ul></div></div>"
        )
    parts.append("</section><section class='cv-section'><h2>Technical tools</h2><dl class='skills'>")
    for item in cv["sections"]["Skills"]:
        parts.append("<dt>" + escape(item["name"]) + "</dt><dd>" + escape(item["keywords"]) + "</dd>")
    parts.append("</dl></section>")
    if cv["sections"].get("Languages"):
        parts.append("<section class='cv-section'><h2>Languages</h2><dl class='skills'>")
        for item in cv["sections"]["Languages"]:
            parts.append("<dt>" + escape(item["name"]) + "</dt><dd>" + escape(item["summary"]) + "</dd>")
        parts.append("</dl></section>")
    return "".join(parts)


SHELL = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Hang Yi, a Data Science undergraduate at Tongji University working on tabular data synthesis and reproducible experiments.">
<title>__TITLE__</title>
<link rel="icon" type="image/png" href="__PREFIX__assets/img/favicon-ginkgo.png">
<link rel="stylesheet" href="__PREFIX__assets/css/tailwind.css">
<link rel="stylesheet" href="__PREFIX__assets/css/main.css">
<link rel="stylesheet" href="__PREFIX__assets/css/preview.css">
<script>try{document.documentElement.dataset.theme=localStorage.getItem('hang-yi-theme')||'light'}catch(e){}</script>
</head>
<body id="top">
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><nav class="site-nav container" aria-label="Main navigation">
<a class="site-brand" href="__HOME__"><strong>Hang</strong> Yi</a>
<div class="site-nav-links">__NAV__<button id="theme-toggle" class="theme-toggle" type="button" aria-label="Switch color theme" title="Switch color theme"><svg aria-hidden="true" viewBox="0 0 24 24" width="19" height="19"><path d="M20.8 13A8.7 8.7 0 0 1 11 3.2 9 9 0 1 0 20.8 13Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg></button></div>
</nav></header>
<main id="main" class="container site-main">
<div class="post"><header class="post-header"><h1 class="post-title">__HEADING__</h1><p class="desc">__SUBTITLE__</p></header>
<article class="site-content">__CONTENT__</article></div>
</main>
<footer class="site-footer container"><span>© 2026 Hang Yi</span></footer>
<script src="__PREFIX__assets/js/preview.js"></script>
</body></html>
"""


def write_page(page, heading, subtitle, content, active):
    prefix = "../" if "/" in page else ""
    nav = "".join(
        '<a class="site-nav-link' + (' active' if label == active else '')
        + '" href="' + link(target, page) + '"'
        + (' aria-current="page"' if label == active else '') + '>' + label + '</a>'
        for label, target in [("About", "/"), ("Research", "/research/"), ("CV", "/cv/")]
    )
    values = {"__TITLE__": "Hang Yi" if active == "About" else active + " | Hang Yi",
              "__PREFIX__": prefix, "__HOME__": link("/", page), "__NAV__": nav,
              "__HEADING__": heading, "__SUBTITLE__": subtitle, "__CONTENT__": content}
    output = SHELL
    for token, value in values.items():
        output = output.replace(token, value)
    path = OUT / page
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output)
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    shutil.copytree(ROOT / "tools/preview-assets", OUT / "assets", dirs_exist_ok=True)
    shutil.copytree(ROOT / "assets/img", OUT / "assets/img", dirs_exist_ok=True)
    shutil.copyfile(ROOT / "LICENSE", OUT / "LICENSE.txt")
    cv = yaml_file(ROOT / "_data/cv.yml")["cv"]
    write_page("index.html", "<strong>Hang</strong> Yi",
               '<a href="https://www.tongji.edu.cn/">Tongji University</a> · Guohao College',
               render_markdown(ROOT / "_pages/about.md", "index.html"), "About")
    write_page("research/index.html", "Research", "Tabular data synthesis and reproducible experiments.",
               render_markdown(ROOT / "_pages/research.md", "research/index.html"), "Research")
    write_page("cv/index.html", "CV", "Education, research experience, and technical tools.", render_cv(cv), "CV")
