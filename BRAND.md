# Sole Practice Platform — Brand Palette

The canonical color tokens for any Sole-branded design work (emails, web, marketing). Not strictly enforced but important — use these values rather than inventing new shades.

## Brand (primary)

| Token | Hex |
|---|---|
| Primary | `#4D4DFF` |
| Primary Dark | `#4F46E5` |
| Primary Soft | `#EEF0FF` |
| Primary Softer | `#F5F6FF` |

### Brand scale

| Step | Hex | Notes |
|---|---|---|
| 50 | `#EEF0FF` | |
| 100 | `#DDE0FF` | tinted borders |
| 200 | `#BFC4FF` | light text on dark |
| 300 | `#9CA3FF` | secondary text on dark |
| 400 | `#7C83F7` | glow accent |
| 500 | `#5A4FCF` | marketing base |
| 600 | `#4A3FBE` | |
| 700 | `#3C33A4` | |
| 800 | `#2F2880` | |
| 900 | `#251F66` | hero gradient stop |

## Surfaces & text

| Token | Hex |
|---|---|
| Background | `#F5F4F8` |
| Card | `#FFFFFF` |
| Field BG | `#F9FAFB` |
| Text | `#0F1117` |
| Text Soft | `#1F2937` |
| Muted | `#6B7280` |
| Muted Soft | `#9CA3AF` |

## Borders

| Token | Hex |
|---|---|
| Border | `#E5E7EB` |
| Border Strong | `#D1D5DB` |

## Status

| Token | Hex (base) | Hex (soft) |
|---|---|---|
| Success | `#10B981` | `#ECFDF5` |
| Warning | `#D97706` | `#FEF3C7` |
| Danger | `#EF4444` | `#FEE2E2` |
| Info | `#3B82F6` | `#EFF6FF` |

## Chart colors

| # | Hex |
|---|---|
| 1 | `#4D4DFF` |
| 2 | `#10B981` |
| 3 | `#D97706` |
| 4 | `#3B82F6` |
| 5 | `#EF4444` |

## Marketing accent

| Token | Hex |
|---|---|
| Orange | `#F97316` |
| Orange Dark | `#EA580C` |
| Hero BG (gradient) | `#191944 → #1E1B4B` |

## Usage rules

- **Page bg** defaults to `#F5F4F8`. Cards `#FFFFFF`. Inner tinted blocks use `#F5F6FF` / `#EEF0FF`.
- **Primary accent** is `#4D4DFF` — used for CTAs, links, eyebrow labels, and primary-tinted borders.
- **Hero blocks** use the navy gradient `#191944 → #1E1B4B` (extend to `#251F66` for depth). Do **not** introduce non-brand colors into the gradient stops. If you want depth, layer a subtle `#7C83F7` (brand-400) radial glow at low alpha — never mix orange into the navy gradient.
- **Marketing orange** `#F97316` is reserved for small marketing flourishes (tags, accent dots, eyebrows on hype sections). It is not a UI color — never use it for buttons, dividers, or backgrounds.
- **Text on white**: `#0F1117` for headings, `#1F2937` for body, `#6B7280` for muted captions.
- **Text on navy**: `#FFFFFF` for headings, `#BFC4FF` (brand-200) for body, `#9CA3FF` (brand-300) for muted/detail.
