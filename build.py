#!/usr/bin/env python3
"""
Inline `email-styles.css` into every email*.html / email-template.html.

Email clients (Gmail, Outlook, Apple Mail in some configs) strip <link rel="stylesheet">
tags, so we keep styles inside a <style> block in each email's <head>. To stay DRY we
maintain one CSS source of truth and run this script to fan it out.

Usage:
    python3 build.py

Idempotent. Run it after every edit to email-styles.css and commit both the CSS file
and the regenerated email*.html files. See SHIPPING.md.
"""

import pathlib
import re
import sys

REPO = pathlib.Path(__file__).parent
CSS_PATH = REPO / "email-styles.css"
GENERATED_MARKER = "<!-- styles: generated from email-styles.css; run python3 build.py to regenerate -->"

# Match the FIRST <style>…</style> block (case-insensitive, multiline).
STYLE_BLOCK_RE = re.compile(r"<style>.*?</style>", re.DOTALL | re.IGNORECASE)
# Match an existing generated-marker comment immediately before <style>, so we don't pile them up.
MARKER_AND_STYLE_RE = re.compile(
    rf"(?:{re.escape(GENERATED_MARKER)}\s*)?<style>.*?</style>",
    re.DOTALL | re.IGNORECASE,
)


def main() -> int:
    if not CSS_PATH.is_file():
        print(f"[build] ERROR: {CSS_PATH.name} not found at repo root", file=sys.stderr)
        return 1

    css = CSS_PATH.read_text(encoding="utf-8").strip()
    new_block = f"{GENERATED_MARKER}\n<style>\n{css}\n</style>"

    # Glob `email-template.html` + `email-*.html` but skip `email-styles.css`.
    targets = sorted(
        [p for p in REPO.glob("email*.html")]
    )
    if not targets:
        print("[build] no email*.html files found")
        return 0

    changed = 0
    for path in targets:
        text = path.read_text(encoding="utf-8")
        if not STYLE_BLOCK_RE.search(text):
            print(f"[build] skip {path.name}: no <style> block to replace")
            continue

        new_text = MARKER_AND_STYLE_RE.sub(new_block, text, count=1)
        if new_text == text:
            print(f"[build] unchanged {path.name}")
            continue

        path.write_text(new_text, encoding="utf-8")
        changed += 1
        print(f"[build] wrote   {path.name}")

    print(f"[build] done — {changed} file(s) updated, source: {CSS_PATH.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
