# Sole Emails

Repository of transactional and marketing email templates for the Sole Practice Platform, plus a local playground for previewing them across Desktop / Tablet / Mobile viewports simultaneously.

## Layout

| Path | Purpose |
|---|---|
| `email-template.html` | Priority Access email — the only template so far |
| `playground.html` | Multi-viewport preview UI (Desktop · Tablet · Mobile, scroll-synced) |
| `BRAND.md` | Canonical color palette — **always reference this for any visual change** |
| `.github/workflows/pages.yml` | Deploys `playground.html` + templates to GitHub Pages |

## Running locally

```bash
python3 -m http.server 8765
```

Then open `http://localhost:8765/playground.html`. `fetch()` against `file://` is blocked by browsers, so the server is required — opening the HTML directly will leave the iframes empty.

The playground polls the template's `Last-Modified` header every 1.5s and auto-reloads — no manual refresh needed when editing.

## Email template conventions

These are **email**, not web. Quirks that look weird in a web codebase are correct here:

- **Table-based layout, inline styles.** Gmail/Outlook/Apple Mail require it. Resist the urge to convert to semantic HTML or external stylesheets.
- **No CSS variables in inline styles** — Outlook strips them. Use the literal hex values from `BRAND.md`.
- **Light only.** The `<meta name="color-scheme">` is `only light`. There is no dark-mode block — Apple Mail / Outlook are told not to auto-invert.
- **All assets are absolute URLs** hosted at `assets.cdn.filesafe.space`. Do not introduce relative paths or local files.
- **Merge tags** use GHL syntax: `{{contact.first_name}}`, `{{tidycal_link}}`, `{{custom_values.founders_signature}}`, `{{video_link}}`. Preserve them exactly when editing — they're populated by the GHL integration when the email is sent. The playground replaces them with preview values via the script in `playground.html`.
- **Rounded corners**: use `border-radius` on the `<td>` that carries the background color, and use generous radii (`999px` for pills, `14–22px` for cards, `12px` minimum for chips). Outlook ignores radius — that's accepted.
- **Gradients**: brand-only. Use `#191944 → #1E1B4B` (extend to `#251F66` for depth). Never blend orange into a navy gradient — orange is a tag/accent color, not a gradient stop. If you want glow, layer a `#7C83F7` radial at low alpha.

## Adding a new template

1. Save the HTML file at the repo root (e.g. `welcome.html`).
2. Open `playground.html`, find the `TEMPLATES` object near the top of the `<script>` block, add an entry:
   ```js
   'welcome': { label: 'Welcome', file: 'welcome.html' }
   ```
3. Reload the playground — the new template appears as a tab.

## Brand colors

See `BRAND.md`. **Do not invent new shades.** If you need a tint not in the palette, pick the closest scale value (e.g. `#DDE0FF` for a tinted border, `#F5F6FF` for a soft fill) rather than mixing your own.

The key tokens, for quick reference:

- **Page bg** `#F5F4F8` · **Card** `#FFFFFF` · **Tinted block** `#F5F6FF` / `#EEF0FF`
- **Text** `#0F1117` · **Body** `#1F2937` · **Muted** `#6B7280`
- **Primary** `#4D4DFF` · **Brand-100 border** `#DDE0FF` · **Border** `#E5E7EB`
- **Hero navy** `#191944 → #1E1B4B → #251F66`
- **On-navy text**: white / `#BFC4FF` (body) / `#9CA3FF` (muted)
- **Marketing orange** `#F97316` — small flourishes only (tags, dots)

## Deployment

GitHub Pages, deployed by `.github/workflows/pages.yml` on push to `master`. Manual trigger available via Actions → Deploy to Pages → Run workflow. Requires Pages → Source set to "GitHub Actions" in repo settings (one-time).

Live URL: `https://mindninjaX.github.io/sole-emails/playground.html` (once Pages is enabled).

## Testing in real clients

Before shipping a template, paste the rendered HTML into [putsmail.com](https://putsmail.com) and send to a Gmail + Apple Mail inbox to sanity-check real-client rendering. The playground catches most issues but cannot perfectly simulate Outlook/Gmail rendering quirks.
