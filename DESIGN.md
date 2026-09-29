---
name: Training Program
description: A flat, phone-first coach's sheet in navy and blue, with coral kept for games, for one athlete's week, log and targets.
colors:
  night-navy: "#1a1a2e"
  training-blue: "#0f3460"
  signal-coral: "#e94560"
  coral-ink: "#c0233c"
  paper: "#ffffff"
  paper-alt: "#f8f9fa"
  paper-hover: "#eef0f3"
  hairline: "#dee2e6"
  neutral-wash: "#e9ecef"
  ink: "#212529"
  ink-soft: "#495057"
  ink-muted: "#5c636a"
  done-green: "#198754"
  done-ink: "#146c43"
  done-ink-deep: "#1b5e20"
  caution-orange: "#fd7e14"
  caution-ink: "#a84300"
  game-wash: "#fde8ec"
  train-wash: "#e8f0fe"
  done-wash: "#e8f5e9"
  caution-wash: "#fff3e0"
  info-border: "#c9d6f2"
  caution-border: "#f5d3ae"
  done-border: "#bfe3cb"
  series-mid-blue: "#3b6fb6"
  standard-1: "#e9ecef"
  standard-2: "#dbe5f4"
  standard-3: "#bccfe9"
  standard-4: "#8eaad6"
  standard-5: "#3b5f93"
  standard-6: "#0f3460"
typography:
  stat:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 700
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 700
    lineHeight: 1.6
  headline:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 600
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.6
  body-small:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 400
    lineHeight: 1.5
  note:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.4
  meta:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "0.8rem"
    fontWeight: 400
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    letterSpacing: "0.5px"
  micro:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "0.6875rem"
    fontWeight: 600
    letterSpacing: "0.5px"
rounded:
  xs: "3px"
  sm: "4px"
  md: "6px"
  lg: "8px"
  xl: "10px"
  pill: "50%"
spacing:
  xs: "0.25rem"
  sm: "0.5rem"
  md: "1rem"
  lg: "1.5rem"
  tap: "44px"
components:
  tab-button:
    backgroundColor: "{colors.night-navy}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    height: "44px"
  today-card:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: "1.25rem 1.5rem"
  check-button:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.sm}"
    size: "44px"
  insights-section:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.lg}"
    padding: "1rem 1.25rem"
  tag-game:
    backgroundColor: "{colors.game-wash}"
    textColor: "{colors.coral-ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.sm}"
  tag-train:
    backgroundColor: "{colors.train-wash}"
    textColor: "{colors.training-blue}"
    typography: "{typography.micro}"
    rounded: "{rounded.sm}"
  tag-done:
    backgroundColor: "{colors.done-wash}"
    textColor: "{colors.done-ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.sm}"
  tag-caution:
    backgroundColor: "{colors.caution-wash}"
    textColor: "{colors.caution-ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.sm}"
  weight-chip-hold:
    backgroundColor: "{colors.neutral-wash}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.micro}"
    rounded: "{rounded.sm}"
  weight-chip-up:
    backgroundColor: "{colors.train-wash}"
    textColor: "{colors.training-blue}"
    typography: "{typography.micro}"
    rounded: "{rounded.sm}"
  weight-chip-down:
    backgroundColor: "{colors.caution-wash}"
    textColor: "{colors.caution-ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.sm}"
---

# Design System: Training Program

## Overview

**Creative North Star: "The Clipboard"**

A coach's sheet, not a dashboard product. Information comes first, surfaces are flat and white, and one hot accent, coral, is reserved for games and the active tab. The page is a single 900px column that reads on a phone without expanding anything, with detail folded behind toggles.

State is carried by colour and border, never by decoration. A card's border says what kind of day it is: coral for a game, blue for training, green for done, grey for rest.

**Key Characteristics:**
- Flat surfaces with 1px hairline borders; almost no shadow.
- System font only. Hierarchy comes from weight, size and small uppercase labels.
- Colour is a code (game, train, done, rest), not a mood.
- Long text is clamped or collapsed by default; expand on tap.
- Every control and link has a 44px hit area on phones; no text below 11px.

## Colors

Navy and Training Blue carry the page; coral, green and orange are reserved for state, each with a darker "ink" version for text.

### Primary
- **Night Navy**: fixed nav bar, header stat values, target numbers.
- **Training Blue**: training days, links, strength bars, the dark end of the standards ramp, focus rings.
- **Signal Coral**: game days only. As text on white or its wash it becomes **Coral Ink**.

### Neutral
- **Paper** and **Paper Alt**: page, cards, summary bars, plan-change banner. **Paper Hover** on section headers.
- **Hairline**: borders and dividers. **Neutral Wash**: hold chips, recovery tags, the lightest standards zone.
- **Ink**, **Ink Soft** and **Ink Muted**: body text, secondary text, metadata and "last weight" references.

### Status
- **Done Green** fills checks; **Done Ink** (and **Done Ink Deep** for pills) is its text version.
- **Caution Orange** is a fill only; **Caution Ink** is used for any caution text (hotel, rehab, behind on HSR, deload chips).
- **Washes** (game, train, done, caution) back tags and chips; the matching **borders** frame info, caution and done callouts.

### Charts and gauge
Series use Training Blue (solid), **Series Mid Blue** (dashed) and Ink Muted (dotted). The strength-standards gauge is a six-step blue ramp (**Standard 1** to **Standard 6**) with ink text on the four light zones and white on the two dark ones.

### Named Rules
**The Colour-As-Code Rule.** Coral means game, blue means training, green means done, grey means rest or hold, orange means caution. Do not reuse them decoratively.

**The Ink Rule.** A state colour used as text on white or a wash always uses its ink version, so every label reaches 4.5:1.

## Typography

**Font:** the system stack. No webfont is loaded.

**Character:** neutral and quick to read on a phone in a gym.

### Hierarchy
- **Stat** (700, 1.5rem): dashboard values.
- **Title** (700, 1.2rem): the Today Card day name.
- **Headline** (600, 1rem): card titles, profile stat values.
- **Body** (400, 0.9rem, 1.6) and **Body small** (0.85rem): checklist rows, tables, Reference copy.
- **Note** (0.8125rem): log notes and exercise notes on phones, "last weight" on the Today Card.
- **Meta** (0.8rem): secondary lines.
- **Label** (600, 0.75rem, `--fs-label`): tabs, toggles, chart labels people read.
- **Micro** (600, 0.6875rem, `--fs-micro`): pills, chips, gauge zones, dense ticks. This is the floor.

Off-ramp sizes still in the code (0.95, 1.05, 1.3, 0.82, 0.78, 0.72 and 0.7rem) are drift from earlier passes; fold them into the nearest step when a component is next touched rather than adding new steps.

### Named Rules
**The 11px Floor Rule.** No rendered text below 11px on screen, including SVG text scaled to its rendered width.

**The Small Caps Label Rule.** Uppercase is for short labels only. Never set a sentence in uppercase.

## Layout

One centred column, max 900px, 1.5rem side padding, 3.5rem top padding under the fixed nav. Sections stack; the week is a 7-column grid of day cards that tightens at 700px (smaller gaps, 60px minimum height, 0.25rem padding). Breakpoints are 640px (phones: stacked cards, 44px link padding, hidden gauge ticks) and 700px (tighter grid and tabs). Tab rail scrolls horizontally with no visible scrollbar.

## Elevation & Depth

Flat by default. No side-stripe borders; callouts use a full 1px tinted border and a tinted fill. Depth is conveyed with 1px borders and Paper Alt fills. Shadows appear only on the Today Card (`0 2px 8px rgba(0,0,0,0.04)`, barely visible), on chart tooltips, and as a 2px focus ring in Training Blue at 15% opacity.

### Named Rules
**The Flat-By-Default Rule.** Surfaces are flat at rest. Do not add shadows to cards to make them feel raised.

## Shapes

Softly squared. Cards and sections 8 to 10px, controls, tags and chips 3 to 6px, check dots and markers 50%. Borders are 1px hairline, or 2px in a state colour on the Today Card. The 12px, 2px and 1px radii in the code are one-offs; use the scale.

## Components

### Navigation
Fixed Night Navy bar with a 2px coral bottom rule. Tabs are uppercase labels at 70% white. Hover lightens the background by 8%. Active tab is full white with a coral underline.

### Today Card
The primary answer to "what do I do today?". White, 2px state-coloured border, 10px radius. Header row holds the day and a muted meta line, then a coloured title, then a checklist with hairline dividers and target weights on the right. Coaching detail sits behind a toggle.

### Today Checklist
On training days each exercise row has its own check button (22px box, 44px hit area, done-green fill when pressed) and a "N of M done" line. Done rows strike through and mute. State lives in this browser only (`tp-done-<date>`); it never claims to log.

### Weight Chips
After each target weight a small chip states the change against the last logged weight: "hold" (grey wash), "+5" (Training Blue on the train wash), "−10" (caution ink on the caution wash). Screen readers get the full phrase; no tooltip-only meaning.

### Session Close
The first row with a 5+ set carries a 1 to 10 reps field. At M of M the progress line becomes "Session done" with the 5+ count, plus a Copy summary button. Browser-only, never "logged".

### Profile Bar
Collapsed summary on one or two lines; the expanded panel is a compact left-aligned block with a label/value stat grid and a plain list of all four goals: latest weight and body fat, target, reading date, and a trend word only after three back-to-back weekly readings move the same way or a change over 4 lb. Gap-based layout, no pipe separators.

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
Series are told apart by blue and neutral shades plus dash patterns (solid, dashed, dotted), never by coral or green, which keep their game and done meanings. Legends show line samples. The strength-standards gauge is a light-to-dark blue ramp with ink or white text per zone.
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
