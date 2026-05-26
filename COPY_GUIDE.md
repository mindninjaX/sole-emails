# Sole Emails — Copy & Voice Guide

A living reference for writing Sole / SPM emails. Read this **before** drafting any new template. When the user gives feedback, append it to the **Feedback log** at the bottom so the system improves over time instead of re-litigating the same rules every cycle.

> Pair with: `BRAND.md` (visual rules), `email-template.html` (canonical structure), `Launch Strategy - SPM.md` (the master campaign spec, when present in `.context/`).

---

## 1. Voice fundamentals

- **Founder voice, not marketing voice.** Johann is speaking. The reader is a busy accounting firm owner. Drop the chest-puffing.
- **Lead with the firm's pain. Never with the feature list.** The pain block opens; the product block follows. Never the other way around.
- **One idea per sentence.** If you can split it, split it.
- **Short bullet headlines: 5–8 words.** If the headline runs over a line on mobile, it's too long.
- **Specific over abstract.** "Paying for 10+ subscriptions" beats "software sprawl." "Holding the whole firm in their head" beats "operational inefficiency."

---

## 2. The "no AI tells" rules

These are the patterns that immediately flag copy as written-by-AI. Avoid them. If you catch yourself reaching for one, the sentence usually wants to be two sentences.

| Don't write | Why | Write instead |
|---|---|---|
| Em dashes ( — ) in body copy | Single strongest AI tell | Period, comma, or split sentence |
| `It's not just X — it's Y` | Classic LLM cadence | One direct sentence |
| `X isn't a magical fix to Y` | Reads as AI hedge | State the limit plainly |
| `Between A, B, and C — most firms…` | Opener-stack pattern | Lead with the firm, not the list |
| `delayed`, `finally`, `at last` | Implies missed timing | The product was always on track. Drop the word. |
| `stack sprawl`, `tech debt` | Buzzwords | "Too many systems", "double-handling" |
| `firm-owned`, `white-label` | Internal jargon | "Your brand" |
| `The goal is to…` | Cold | "Our goal" |
| Emoji in **headlines or prose paragraphs** | Looks childish, feels AI-generated | Keep prose clean. See § 4a for where emojis ARE allowed |

**Self-check before shipping**: grep the file for `—` (em dash) and `&mdash;`. Both should return zero matches in any text that a human reads.

---

## 3. Locked phrasing

These are settled. Use them verbatim. Do not paraphrase.

- "**You're on the limited shortlist**" — hero subline for warm-list emails.
- "**Our goal**" — never "the goal."
- "**Your brand**" — never "firm-owned", "white-label", "private label", "your own brand option."
- "**A few months ago, you registered interest…**" — opening line for re-engagement emails. Not "last year."
- "**Limited rollout spots**" — replaces any "tax season" urgency. We go live *after* tax season.
- "**Supported rollout**" — frames the offer. Not "early access", not "beta."
- "**Product · 90 second overview**" — video section label, every email.

---

## 4a. Visual enrichment (where emojis, icons, and photos belong)

A page of pure prose reads as low-effort and surprisingly AI. Sole emails earn warmth and skim-ability from the visual system — not from clever phrasing.

**Emojis are allowed (and encouraged) in:**

- **List bullets** — one emoji per row in pain lists, question lists, relevance checklists. Replaces the bare `?` or `•`.
- **Card eyebrows** — small emoji next to a number or section label to anchor the eye.
- **Flow steps** — one emoji per step in end-to-end / rollout flows so the chain reads visually as a sequence.

**Emojis are banned in:**

- Headlines (`<h1>`, `<h2>`, `<h3>`, hero subline).
- Prose paragraphs (founder note, closing CTA body, captions).
- Subject lines and preview text.

**Pick one emoji style and stay consistent within an email.** Don't mix flat 🧾 with 3D 💰 in the same template.

**SVG icons for product cards.** When a card represents a real product capability (the 4-card "What SPM helps your firm manage" grid), use a monochrome SVG icon at `#4D4DFF` rather than emoji. Inline as base64 data URI (the social icons in the footer are the pattern to follow). More premium feel, brand-consistent colour.

**No editorial / stock photos. Period.**

- We tried adding Unsplash banners to Emails 1/2/4 in round 2. The user removed them. They add scroll length, push the founder note further down, and read as marketing fluff in what's meant to be a founder-voice email.
- The only photographic asset allowed is **product screenshots** (dashboards, workflow views) because they prove the product exists.
- Founder portrait in the founder card is the exception — it's a small avatar, not editorial imagery.
- If a section feels visually empty, fix it with an icon, a chip grid, a callout tile, or a real product screenshot. Not with a stock photo.

**The cardinal rule.** Icons reinforce meaning, never replace it. Every icon sits next to a label. Never an icon alone in a card or row.

## 4. Structural rules (every email follows these)

```
Logo bar
  ↓
Hero card (navy gradient, eyebrow + H1 + light H1 + 1 sentence + CTA pair)
  ↓
Founder card (JO portrait, name, role)
  ↓
Founder note (pain-led)
  ↓
[ Pain block | Product block | Visual | etc. — varies per email ]
  ↓
Product · 90 second overview (video thumbnail)
  ↓
Closing CTA (navy gradient, primary + secondary button)
  ↓
Footer (logo, socials, links)
```

Specific structural laws:

- **End-to-end flow** (Lead → Proposal → Onboarding → Job → Review → Billing → Collection → Client value) renders **2 rows of 4** at desktop, **2 columns × 4 rows** on mobile. Never 1 long horizontal strip — text becomes unreadable.
- **Real screenshots** wherever the reader needs to believe the product exists. Icons-only blocks are weak. The dashboard especially must be a screenshot, not an emoji grid.
- **Save-money signal** must appear in any email that frames the value prop. Firms are paying for 10+ subscriptions; this is a real cost SPM eliminates. Don't bury it.
- **Orange marketing accent** (`#F97316`) is for tags/dots/eyebrows only. Never in the navy gradient. Never on a button.

---

## 5. Reusable copy blocks

Pulled verbatim from the launch strategy. Drop these in unchanged.

### Pain block

> We've spoken with 12 Australian accounting firms while building SPM. The pattern is consistent. Firms are either holding too much in someone's head, or paying for 10+ systems and still double-handling work. Client information sits in one place, jobs in another, billing somewhere else, and staff capacity is usually worked out manually. That is the real problem SPM is built to solve.

### Product block

> SPM gives accounting and bookkeeping firms one connected place to manage the work. Leads, proposals, onboarding, jobs, review, billing, collections, staff capacity and the client portal stay in one workflow. The owner gets visibility. The team knows what to move. The client gets a cleaner experience.

### AI block

> AI does not fix disconnected systems by itself. It only becomes useful when it sits inside the workflow. SPM uses AI to help flag what is missing, what is overdue, who is overloaded and what needs attention next.

### Your brand block

> You can use SPM under the Sole brand, or choose to offer it under your own. For firms that want more control of the client experience, your clients can access the platform under your firm's brand — the client portal and, where relevant, an accounting app experience you can package as part of your service.

### Supported rollout block

> The first rollout is limited because we are supporting it properly. Selected firms receive onboarding support, workflow setup, training, migration support and support calls. This is not just access to software. We want to work closely with the right firms and help them get value from the platform.

### Save-money sub-block (use inside the goal/product section)

> SPM is designed to help firms save time and save money — fewer subscriptions to maintain, less duplicated work across systems, and a clearer view of what is moving so owners don't have to chase the answer.

---

## 6. Subject + preview text patterns

- **Subject line**: short, lowercase-feel, factual. No emoji. No exclamation marks. 60 chars max.
- **Preview text**: a second sentence that completes (not repeats) the subject. 90 chars max.

Settled subject lines (per launch strategy):

1. *As promised, Sole Practice Manager is ready to help your accounting firm*
2. *Where accounting firm visibility breaks down*
3. *From lead to collection, in one customisable workflow*
4. *Partnership opportunity, should we include your firm?*
5. *Should we keep you on the SPM shortlist?*

---

## 7. CTA hierarchy (consistent across all emails)

| Position | Label | Link |
|---|---|---|
| Primary, every email | Book a June discovery call | `{{tidycal_link}}` |
| Secondary | View the pre-release page | `https://eoi.soleapp.com.au` |
| Secondary alt (video) | Watch the 90 second overview | `{{video_link}}` |
| Email 5 only | Reply 'later' | text-only, no link |

Primary button: white background, navy text. Secondary: outline on navy, or underlined text link inside the hero.

---

## 8. The merge tags

Always preserved verbatim. The GHL integration populates them at send time.

- `{{contact.first_name}}`
- `{{tidycal_link}}`
- `{{video_link}}`
- `{{custom_values.founders_signature}}`

The playground (`playground.html`) replaces these with preview values; never hard-code a name or link in the template.

---

## 9. Feedback log

Append to the top each round (most recent first). Include the date, the rule, and a one-line *why* so the next agent understands the edge cases.

### 2026-05-26 — Round 2 follow-up

- **Hero pills are always brand-blue (`#4D4DFF`) on white text.** Every email's hero card uses the same blue pill in the same position. The orange marketing accent (`#F97316`) is reserved for small body-level eyebrows in the offer/sales sections (e.g. "For selected pre-release firms"), and as one stop in the top accent gradient bar. *Why:* the user flagged Email 4's orange "Supported rollout" hero pill as inconsistent with the rest of the campaign. Visual consistency across emails matters more than per-email differentiation.
- **Relative `assets/...` paths render in the playground via a `<base href>` injection** added to `playground.html` (around line 480). Email files keep the relative paths; `SHIPPING.md` § 1 reminds the user to swap to absolute CDN URLs before send. *Why:* relative paths in `<img src>` don't resolve from blob: URLs (which is what the playground uses to load each email), so the playground was showing broken-image icons until the base tag was injected.
- **No editorial / stock cover photos at the top of emails.** The Unsplash banners I added in round 2 (Emails 1, 2, 4) were removed by the user. They add scroll length without adding meaning, and accounting-firm owners don't want stock imagery in a founder-voice email. *Why:* "people won't scroll as much" — keep emails short. Product screenshots (dashboards) earn their place because they prove the product exists; stock photos do not. Rule: no banner / hero / editorial photos in emails. Visual variety comes from icons, emoji bullets, chip grids, product screenshots, and the navy hero card — not photos.
- **Never highlight the last chip in a sequence.** In a flow / pipeline / step sequence (end-to-end, rollout, etc.), every chip uses the same neutral treatment (white or brand-soft bg, brand-100 border, dark text). The instinct to mark the final state in brand-blue reads as "selected" / "active," not "destination." *Why:* user flagged the highlighted final chip in Email 1's end-to-end flow as confusing, and noted it had been wrong in earlier emails too. Rule applies across every email.

### 2026-05-26 — Round 2 visual audit

- **Round 1 emails were too text-heavy.** Add emojis to list bullets, card eyebrows, and flow steps. Add SVG icons to product cards. Add one Unsplash editorial photo per non-flow email (max one). *Why:* the rendered output read as walls of words; visual variety lifts skim-ability without compromising the voice.
- **"No emoji in body copy" was over-broad.** Refined: emojis are fine in **bullets / eyebrows / flow steps**, banned in **headlines / prose / subjects**. *Why:* the old blanket rule killed legitimate visual aids.
- **Dashboard placeholder navy block was sterile.** Swap to a real product screenshot (we already had one in the video thumbnail). Keep a `TODO_DASHBOARD_IMAGE` comment so the high-fidelity asset swap is tracked. *Why:* "Real screenshot coming soon" reads as unfinished; readers expected a product.
- **Single CSS source of truth is now `email-styles.css`.** Edit there, run `python3 build.py`, commit both. *Why:* maintaining 5 nearly-identical `<style>` blocks was a recurring drift risk.
- **`SHIPPING.md` is the pre-PR checklist.** Agent reads it before any email PR and reminds the user about asset uploads and URL swaps. *Why:* `TODO_` placeholders and broken founder portrait kept slipping through.

### 2026-05-26 — Initial campaign feedback (Emails 1–5 first pass)

- **"You're on the limited shortlist"** replaces any "first look before we open broadly" framing. *Why:* the prior line read as marketing-speak; the user wants it factual.
- **Use "our goal" not "the goal"**, and **"your brand" not "firm-owned"** or "white-label." *Why:* "the goal" sounds distant; "firm-owned" is internal language the reader doesn't share.
- **Kill all em dashes in body copy.** Period/comma/sentence split instead. *Why:* em dashes are the strongest AI-written tell and the user pattern-matched the prior copy as AI.
- **Pain bullets must be 5–8 word headlines.** Drop long supporting paragraphs if they sound AI-generated. *Why:* the prior bullets had long explanatory sentences that read as generated.
- **Surface "save money" / "fewer subscriptions" explicitly.** *Why:* firms are paying for 10+ tools; this is a real, quantifiable hook the prior copy missed.
- **The end-to-end flow chips were too small.** Render across two rows if needed; make the labels readable on mobile. *Why:* the 7-chip single-row layout becomes a thin line that no one reads.
- **No tax-season urgency.** We go live *after* tax season. Reframe as "limited rollout spots" (driven by onboarding support, not deadlines). *Why:* the old "tax season is around the corner" banner was factually wrong for this campaign's timing.
- **Dashboards card needs a real screenshot, not third-party app icons.** *Why:* an icon grid doesn't prove the product exists. The dashboard is the hero asset.
- **"AI isn't a magical fix to connect all of your subscriptions and systems."** Acceptable rewrite of the AI hedge — short, direct. *Why:* the original "AI on top of silos is just more silos" was abstract.
- **Make headline text larger** in the goal and end-to-end sections — even at the cost of wrapping to two rows. *Why:* legibility beats compactness.

---

## 10. How to update this guide

When the user gives a new round of feedback:

1. **Add a dated section to the top of the Feedback log** (section 9).
2. **If a phrase becomes locked**, add it to section 3 (Locked phrasing).
3. **If a new "AI tell" surfaces**, add it to section 2's table.
4. **If a structural rule changes** (e.g. flow layout, video position), update section 4.
5. Never delete prior feedback — it explains why current rules exist.

A guide that grows is worth more than a guide that's "clean."
