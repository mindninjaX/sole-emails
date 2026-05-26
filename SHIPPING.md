# Shipping checklist

**Read this before any PR or commit that touches an email template.** It catches the breakages we've seen in the past: missing assets, stale styles, AI-tell phrasing, mobile layout regressions.

The agent will also read this and remind you of these steps. If you're shipping in a hurry, run the four `grep` / `python3` commands at the bottom of this doc — they catch ~90% of issues in under a minute.

---

## 1. Assets to host before sending

Every `TODO_` marker in the templates is a broken send if not swapped. Run this grep first:

```bash
grep -n "TODO_" *.html
```

Common markers you'll see:

| Marker | What it is | What to do |
|---|---|---|
| `TODO_ASSET_HOSTING` | An `<img src="assets/...">` relative path. Works in the playground and GitHub Pages preview, breaks in real email clients | Upload the file from `assets/` to `assets.cdn.filesafe.space`, swap `src` to the absolute URL, remove the comment |
| `TODO_DASHBOARD_IMAGE` | Dashboard screenshot using a temporary placeholder | Same — upload the real screenshot to `assets.cdn.filesafe.space` and swap |
| `TODO_HERO_IMAGE` | Editorial hero photo placeholder (deprecated — we no longer use cover photos) | Should not appear in current emails; if you see one, remove the whole banner block |
| `TODO_FOUNDER_IMAGE` | Johann's portrait | Upload to `assets.cdn.filesafe.space` and swap |

Procedure for each marker:

1. Upload the asset to `assets.cdn.filesafe.space`.
2. Replace the `src="..."` in the template with the hosted URL.
3. Delete the `<!-- TODO_... -->` comment marker.
4. Re-run `grep -n "TODO_" *.html` — should return zero.

> **Why not link Unsplash directly?** The `?w=1200&q=80` Unsplash URLs work in the playground but can be rate-limited, hot-link-blocked, or rewritten by Gmail's image proxy in ways that strip the query string. Always re-host marketing imagery on our own CDN.

---

## 2. CSS rebuild

If you edited `email-styles.css`, run:

```bash
python3 build.py
```

The script inlines the CSS into every `email*.html` `<style>` block. **Commit both the CSS file and the regenerated HTML files.** Forgetting this means production emails ship with stale styles while the source of truth has moved on.

Sanity check after build:

```bash
grep -l "SINGLE SOURCE OF TRUTH" email*.html | wc -l
# Should print 5 (or however many email templates exist)
```

---

## 3. Banned phrases and AI tells

These exact patterns will cause the user to send the email back. Run all four:

```bash
grep -in "—" email*.html              # em dash, the single strongest AI tell
grep -in "&mdash;" email*.html        # HTML-entity em dash
grep -in -E "firm-owned|white-label|software sprawl|stack sprawl" email*.html
grep -in -E "The goal|isn't a magical fix|It's not just|delayed|finally," email*.html
```

All four must return zero matches across the email files. (Matches in `playground.html` are OK — that's the preview UI shell, not customer-facing.)

See `COPY_GUIDE.md` § 2 for the full banned-pattern list and the rationale behind each.

---

## 4. Preview pass

Serve locally and click every tab in both Desktop and Mobile columns:

```bash
python3 -m http.server 8765
open http://localhost:8765/playground.html
```

For each of the 5 emails (Priority Access · Disconnected · How SPM Works · Supported Rollout · Close the Loop), confirm:

- [ ] No broken-image icons anywhere. Hero photos, dashboard screenshots, founder portrait, social icons all load.
- [ ] No em dashes visible in body copy (visually scan headings + paragraphs).
- [ ] End-to-end flow chips are readable on the **Mobile** column (393px). They should stack to one chip per row with readable labels.
- [ ] CTAs route correctly. Primary button → `{{tidycal_link}}` (rendered as `#` in the playground). Secondary → `https://eoi.soleapp.com.au` or `{{video_link}}`.
- [ ] Merge tags render their preview values. `{{contact.first_name}}` → `Sarah`. If you see a raw `{{...}}` in the body, the playground's tag-replacement isn't catching it; add it to `playground.html`.

---

## 5. Real-client check

Before merging to `master`, paste each rendered HTML into [putsmail.com](https://putsmail.com) and send to:

- A Gmail inbox (web + iOS)
- An Apple Mail inbox (macOS)
- An Outlook inbox if any of the audience uses Outlook (some Australian firms do)

Visually confirm the same checklist from section 4 above. Real-client rendering catches things the playground can't — especially Outlook table-rendering quirks and Gmail image-proxy issues.

---

## 6. Final pre-PR sweep (the speedrun)

Copy-paste this block to run all the critical checks in one shot:

```bash
echo "=== TODO_ markers ===" && grep -n "TODO_" email*.html
echo "=== em dashes ==="    && grep -n "—" email*.html
echo "=== &mdash; ==="       && grep -n "&mdash;" email*.html
echo "=== banned phrases ===" && grep -in -E "firm-owned|white-label|software sprawl|The goal" email*.html
echo "=== CSS marker ==="    && grep -l "SINGLE SOURCE OF TRUTH" email*.html | wc -l
echo "=== done ==="
```

If `TODO_` shows any matches: **do not merge.** Either host the assets first, or scope the PR to non-email changes only.

---

## When the agent helps you ship

The agent has been told to read this file before any email PR. Expect it to:

1. Grep for `TODO_` and quote any matches.
2. Confirm `python3 build.py` was run if `email-styles.css` changed.
3. Ask you to upload assets and swap URLs before pushing.

If the agent skips these steps, remind it to re-read `SHIPPING.md`.
