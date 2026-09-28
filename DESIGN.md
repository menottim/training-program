---
name: Training Program
description: A flat, phone-first coach's sheet in navy and coral for one athlete's week, log and targets.
colors:
  night-navy: "#1a1a2e"
  training-blue: "#0f3460"
  signal-coral: "#e94560"
  paper: "#ffffff"
  paper-alt: "#f8f9fa"
  hairline: "#dee2e6"
  ink: "#212529"
  ink-muted: "#5c636a"
  coral-ink: "#c0233c"
  caution-ink: "#a84300"
  done-green: "#198754"
  caution-orange: "#fd7e14"
  game-wash: "#fde8ec"
  train-wash: "#e8f0fe"
  done-wash: "#e8f5e9"
  caution-wash: "#fff3e0"
typography:
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 700
    lineHeight: 1.6
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    letterSpacing: "0.5px"
rounded:
  xs: "3px"
  sm: "4px"
  md: "6px"
  lg: "8px"
  xl: "10px"
spacing:
  xs: "0.25rem"
  sm: "0.5rem"
  md: "1rem"
  lg: "1.5rem"
components:
  tab-button:
    backgroundColor: "{colors.night-navy}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    padding: "0.7rem 1.2rem"
  today-card:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: "1.25rem 1.5rem"
  insights-section:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.lg}"
    padding: "1rem 1.25rem"
  tag-game:
    backgroundColor: "{colors.game-wash}"
    textColor: "{colors.signal-coral}"
    rounded: "{rounded.sm}"
  tag-train:
    backgroundColor: "{colors.train-wash}"
    textColor: "{colors.training-blue}"
    rounded: "{rounded.sm}"
---

# Design System: Training Program

## Overview

**Creative North Star: "The Clipboard"**

A coach's sheet, not a dashboard product. Information comes first, surfaces are flat and white, and one hot accent is reserved for games, the active tab and hover. The page is a single 900px column that reads on a phone without expanding anything, with detail folded behind toggles.

State is carried by colour and border, never by decoration. A card's border says what kind of day it is: coral for a game, blue for training, green for done, grey for rest.

**Key Characteristics:**
- Flat surfaces with 1px hairline borders; almost no shadow.
- System font only. Hierarchy comes from weight, size and small uppercase labels.
- Colour is a code (game, train, done, rest), not a mood.
- Long text is clamped or collapsed by default; expand on tap.

## Colors

A navy and coral pair on white, with green and orange as status colours and pale washes for tags.

### Primary
- **Night Navy** (#1a1a2e): the fixed top nav bar background.
- **Training Blue** (#0f3460): training-day borders and titles, links, strong text in summary bars, focus ring.
- **Signal Coral** (#e94560): game days, the active tab underline, hover on toggles.

### Neutral
- **Paper** (#ffffff): page and card background.
- **Paper Alt** (#f8f9fa): summary bars, collapsed-section headers.
- **Hairline** (#dee2e6): borders and row dividers.
- **Ink** (#212529): body text.
- **Ink Muted** (#5c636a): metadata, rest-day borders, secondary labels.

### Status
- **Done Green** (#198754): completed sessions.
- **Caution Orange** (#fd7e14): hotel and modified-day warnings.
- **Washes** (#fde8ec game, #e8f0fe train, #e8f5e9 done, #fff3e0 caution): tag backgrounds only.

- **Coral Ink** (#c0233c) and **Caution Ink** (#a84300): text versions of coral and orange, used whenever those colours sit on white or a pale wash (both at least 4.5:1).

### Named Rules
**The Colour-As-Code Rule.** Coral means game, blue means training, green means done, grey means rest. Do not reuse them decoratively.

## Typography

**Font:** the system stack (-apple-system, Segoe UI, Roboto, Arial). No webfont is loaded.

**Character:** neutral and quick to read. Nothing to wait for.

### Hierarchy
- **Title** (700, 1.2rem): day name on the Today Card.
- **Headline** (600, 1rem): card titles, coloured by day type.
- **Body** (400, 0.9rem, 1.6): checklist rows and notes.
- **Label** (600, 0.7 to 0.78rem, +0.3 to 0.5px, uppercase): tabs, meta lines, toggles.

Floor: no rendered text under 11px (`--fs-micro`, 0.6875rem); readable labels use 12px (`--fs-label`, 0.75rem). Charts size their SVG to the viewport so this holds on screen, not just in CSS.

### Named Rules
**The Small Caps Label Rule.** Uppercase is for short labels only. Never set a sentence in uppercase.

## Layout

One centred column, max 900px, 1.5rem side padding, 3.5rem top padding under the fixed nav. Sections stack; the week is a 7-column grid of day cards that tightens at 700px (smaller gaps, 60px minimum height, 0.25rem padding). Breakpoints are 640px and 700px. Tab rail scrolls horizontally with no visible scrollbar.

## Elevation & Depth

Flat by default. No side-stripe borders; callouts use a full 1px tinted border and a tinted fill. Depth is conveyed with 1px borders and Paper Alt fills. Shadows appear only on the Today Card (`0 2px 8px rgba(0,0,0,0.04)`, barely visible), on chart tooltips, and as a 2px focus ring in Training Blue at 15% opacity.

### Named Rules
**The Flat-By-Default Rule.** Surfaces are flat at rest. Do not add shadows to cards to make them feel raised.

## Shapes

Softly squared. Cards 8 to 10px, controls and tags 3 to 6px, dots 50%. Borders are 1px hairline, or 2px in a state colour on the Today Card.

## Components

### Navigation
Fixed Night Navy bar with a 2px coral bottom rule. Tabs are uppercase labels at 70% white. Hover lightens the background by 8%. Active tab is full white with a coral underline.

### Today Card
The primary answer to "what do I do today?". White, 2px state-coloured border, 10px radius. Header row holds the day and a muted meta line, then a coloured title, then a checklist with hairline dividers and target weights on the right. Coaching detail sits behind a toggle.

### Today Checklist
On training days each exercise row has its own check button (22px box, 44px hit area, done-green fill when pressed) and a "N of M done" line. Done rows strike through and mute. State lives in this browser only (`tp-done-<date>`); it never claims to log.

### Profile Bar
Collapsed summary on one or two lines: latest weight and body fat, target, reading date, and a trend word only after three back-to-back weekly readings move the same way or a change over 4 lb. Gap-based layout, no pipe separators.

### Training Plan Groups
Targets and progress bars lead. Everything else folds into closed groups: Strength progress, Body and achilles, Stats and volume, Training Phases.

### Day Card (week grid)
Compact tile with a day-type tag. Shows a short `desc` headline; longer text sits behind a per-tile detail toggle.

### Tags
Small pills with a pale wash and matching text: game (coral), train (blue), recovery (grey), rest (light grey), hotel (orange), deload (green).

### Disclosure Controls
One style for every toggle: uppercase 12px label in Training Blue, one CSS-drawn chevron that rotates when open, 44px minimum hit area, visible focus ring.

### Plan-Change Banner
Flat Paper Alt panel with a hairline border, ink text and a small caution-ink dot before the title. It is information, never louder than the Today Card.

### Collapsible Sections
Insights and athlete profile use `<details>`. Header on Paper Alt with a rotating chevron; body on Paper.

### Log Notes
Clamped to 3 lines (2 on phones) with a small uppercase "more" toggle in Training Blue that turns coral on hover.

### Charts
Inline charts with instant hover and tap tooltips and a dot-and-label legend.

## Do's and Don'ts

### Do:
- **Do** keep the Today Card the first thing on the page.
- **Do** keep each tile headline to about 8 words and fold the rest behind a toggle.
- **Do** use the four state colours only for their meaning.
- **Do** give every control and link a 44px hit area on phones (vertical padding on the inline box, not bigger text).

### Don't:
- **Don't** add nutrition or sleep UI. Both are retired.
- **Don't** put citations, evidence tiers or program self-assessment in any rendered field.
- **Don't** hardcode a schedule in `index.html`; an un-authored week must show as missing.
- **Don't** add a webfont, framework or build step.
