---
name: In-Season Training Program
description: One athlete's training plan, set out as the exercise sheet a clinician hands over.
colors:
  sheet: "#ffffff"
  ink: "#16181b"
  ink-2: "#3d434b"
  ink-3: "#5b6470"
  rule: "#16181b"
  hair: "#d7dde5"
  margin: "#e6ebf2"
  margin-2: "#f4f6f9"
  margin-hair: "#c9d2de"
  clin: "#2456a6"
  clin-wash: "#e8eef8"
  clin-deep: "#0a2440"
  game-ink: "#c0233c"
  game-cap: "#e94560"
  game-wash: "#fde8ec"
  done-ink: "#146c43"
  done-wash: "#e8f5e9"
  caution-ink: "#a84300"
  caution-wash: "#fff3e0"
  chart-game-tint: "#8aa3cf"
  chart-squat: "#3b6fb6"
  standard-1: "#dbe5f4"
  standard-2: "#bccfe9"
  standard-3: "#8eaad6"
  standard-4: "#3b5f93"
  standard-5: "#0f3460"
typography:
  sheet-day:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "1.625rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
    fontFeature: "tnum"
  sheet-day-phone:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
    fontFeature: "tnum"
  entry:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.01em"
    fontFeature: "tnum"
  headline:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "1.3rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 600
    lineHeight: 1.3
  section:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.005em"
  row:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.4
    fontFeature: "tnum"
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.5
    fontFeature: "tnum"
  meta:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.45
    fontFeature: "tnum"
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.5px"
  micro:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: "0.6875rem"
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: "0.5px"
rounded:
  box: "1px"
  mark: "2px"
  panel: "3px"
spacing:
  row-y: "0.6rem"
  col-gap: "0.75rem"
  panel-x: "0.875rem"
  gutter: "1.5rem"
  section: "2.5rem"
  tap: "44px"
  measure: "900px"
components:
  nav-tab:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink-3}"
    typography: "{typography.label}"
    height: "44px"
    padding: "0 1.2rem"
  nav-tab-active:
    textColor: "{colors.ink}"
  tick-box:
    backgroundColor: "{colors.sheet}"
    rounded: "{rounded.box}"
    size: "22px"
  tick-box-checked:
    backgroundColor: "{colors.clin}"
    textColor: "{colors.sheet}"
    rounded: "{rounded.box}"
    size: "22px"
  write-in:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.clin}"
    width: "3.5rem"
    height: "44px"
  send-button:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.clin}"
    rounded: "{rounded.mark}"
    height: "44px"
    padding: "0 1rem"
  send-button-hover:
    backgroundColor: "{colors.clin}"
    textColor: "{colors.sheet}"
  margin-panel:
    backgroundColor: "{colors.margin}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.panel}"
    padding: "0.75rem 0.875rem"
  pill-training:
    backgroundColor: "{colors.clin-wash}"
    textColor: "{colors.clin}"
    typography: "{typography.micro}"
    rounded: "{rounded.mark}"
    padding: "1px 6px"
  pill-game:
    backgroundColor: "{colors.game-wash}"
    textColor: "{colors.game-ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.mark}"
    padding: "1px 6px"
  pill-done:
    backgroundColor: "{colors.done-wash}"
    textColor: "{colors.done-ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.mark}"
    padding: "1px 6px"
  pill-caution:
    backgroundColor: "{colors.caution-wash}"
    textColor: "{colors.caution-ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.mark}"
    padding: "1px 6px"
  pill-rest:
    backgroundColor: "{colors.margin}"
    textColor: "{colors.ink-2}"
    typography: "{typography.micro}"
    rounded: "{rounded.mark}"
    padding: "1px 6px"
  chip-up:
    backgroundColor: "{colors.clin-wash}"
    textColor: "{colors.clin}"
    typography: "{typography.micro}"
    rounded: "{rounded.mark}"
    padding: "0 5px"
  chip-hold:
    backgroundColor: "{colors.margin}"
    textColor: "{colors.ink-2}"
    typography: "{typography.micro}"
    rounded: "{rounded.mark}"
    padding: "0 5px"
  chip-down:
    backgroundColor: "{colors.caution-wash}"
    textColor: "{colors.caution-ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.mark}"
    padding: "0 5px"
---

# Design System: In-Season Training Program

## Overview

**Creative North Star: "The Physio Exercise Sheet"**

The site is the sheet a clinician or strength coach hands the athlete: numbered moves, a dosing table, square tick boxes, a line to write the 5+ count on, and the rules set off in the margin. Everything sits on one white sheet in near-black ink. Structure comes from rules, never from boxes: a heavy ink rule opens every table and section, hairlines separate rows, and pale blue-grey margin panels carry the rules and coaching notes.

Density is that of a printed handout read at arm's length in a gym. Rows are tight but every control has a 44px target. One clinical blue carries the numbers that matter, the ticks and the links; the other state inks (game red, done green, caution orange) appear only as small marks and pills. The sheet shortens as the session runs: a ticked row fills its box blue and strikes down to one line.

The world rejects the tracker-app stack of rounded cards, the dashboard of stat tiles, dark themes, gamified feedback and webfonts. It is set in the system sans with tabular numerals throughout.

**Key Characteristics:**
- White sheet, near-black ink, one clinical blue.
- Ruled tables: 2px ink rule under headers and at section tops, 1px hairlines between rows.
- Square tick boxes and a write-in line, drawn in CSS.
- Margin panels in flat blue-grey for rules and detail.
- Colour-as-code confined to small marks and pills.
- System sans, tabular numerals, 11px floor.

## Colors

A monochrome ink sheet with one clinical blue, plus four state inks that only ever appear as marks.

### Primary
- **Clinical Blue** (clin): exercise numbers, tick fills, the 5+ label and entry, links, progress fills, rank names, margin-panel labels, focus rings, the active nav underline and the current-day square in the week schedule. It is the only colour allowed to carry a number at large size.
- **Clinical Wash** (clin-wash): the background of training pills and up chips, text selection and the focused write-in line.
- **Deep Clinical** (clin-deep): hover ink for content links on Plan and Reference, where the underline turns solid and 2px.

### Secondary (state inks, marks only)
- **Game Red** (game-ink) on **Game Wash** (game-wash): game pills and the game mark in the sheet header.
- **Game Cap** (game-cap): the 2px cap on game bars in the weekly volume chart. Nowhere else.
- **Done Green** (done-ink) on **Done Wash** (done-wash): the done mark, completed-day pills, deload pills and the copied-status line.
- **Caution Orange** (caution-ink) on **Caution Wash** (caution-wash): hotel and rehab pills, down chips, out-of-range lab marks, pain points above 3/10, invalid write-in entries, a body-composition value moving the wrong way.

### Neutral
- **Sheet** (sheet): the page. There is no other page background.
- **Ink** (ink) and **Rule** (rule): body text, exercise names, loads, and the heavy rules. Rule is the same ink as text, named for its role.
- **Ink 2** (ink-2): secondary text, dose, notes, prose on Reference.
- **Ink 3** (ink-3): column heads, dates, history lines, done rows, the dashed sign-off rule, chart baselines.
- **Hairline** (hair): row dividers, footer rule, chart gridlines on body composition.
- **Margin** (margin): margin panels, rest and hold marks, chart gridlines, the untrained zone of the standards scale.
- **Margin 2** (margin-2): nav hover, tooltip fill, the copy-fallback textarea.
- **Margin Hairline** (margin-hair): dividers between list items inside a margin panel.

### Chart series
- Trap bar deadlift in Clinical Blue solid, bench in Ink 2 dotted (2,3), back squat in **Squat Blue** (chart-squat) dashed (6,4). Series are told apart by dash, not by hue alone.
- Games in the volume chart are **Game Tint** (chart-game-tint) with the red cap; training in Clinical Blue; recovery in Ink 3.
- The strength standards ramp runs **standard-1** to **standard-5** (Beginner to Elite), light to dark in the clinical hue, with Margin for Untrained. Segments are separated by a 1px sheet-coloured inset.

### Named Rules
**The One Blue Rule.** Clinical Blue is the only accent that carries emphasis. A second accent hue for emphasis is off-system.

**The Marks Only Rule.** Game red, done green and caution orange appear as pills, chips, small squares, dots and short text marks. They never fill a row, tint a panel, colour a heading or run down an edge.

**The Code Holds Rule.** Red means game, blue means training, green means done, orange means caution, grey means rest or hold. A colour is never borrowed for a different meaning, including hover states.

## Typography

**Body Font:** the system sans stack (-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif)
**Display Font:** the same stack; there is no second family.

**Character:** A plain clinical handout face. Weight and size carry hierarchy; tabular numerals are on for the whole body so loads, dates and counts align down a column.

### Hierarchy
- **Sheet day** (700, 1.625rem, 1.15, -0.02em; the sheet-day-phone step, 1.5rem, at 640px and below): the day and date at the top of This Week. The largest type on the site.
- **Headline** (700, 1.3rem): page-level h2 over the strength targets table, with a 2px rule beneath.
- **Entry** (700, 1.25rem, -0.01em): the h1 in the expanded patient block, and the count written on the 5+ line.
- **Title** (600, 1.0625rem, 1.3, balanced wrap): the session headline under the sheet day.
- **Section** (700, 1rem, -0.005em, sentence case): the disclosure line that heads each Plan and Reference section. Sub-heads inside are 700 at 0.9375rem.
- **Row** (0.9375rem, 1.4): dosing-table rows; exercise names at 600, loads at 700 in Ink.
- **Body** (0.875rem, 1.5, max 68 to 70ch): prose, margin panels, week rows.
- **Meta** (0.8125rem): header meta line, cues, week stats, log text.
- **Label** (600, 0.75rem, 0.5px, uppercase): nav tabs, column heads, disclosure toggles such as detail and show all.
- **Micro** (700, 0.6875rem, 0.5px, uppercase): pills, chips, dosing-table column heads, margin-panel labels, scale zone names. This is the floor.

### Named Rules
**The 11px Floor Rule.** No rendered text below 0.6875rem (11px), including chart labels.

**The Tabular Rule.** Numerals are tabular everywhere. Any new number column inherits it; never switch it off.

**The Sentence Case Heading Rule.** Headings and section lines are sentence case. Uppercase is reserved for label and micro sizes, where it names a column, a control or a panel.

## Layout

A single column, max 900px, with 1.5rem side gutters and a fixed thin nav on top (body top padding 3.5rem). The sheet reads top to bottom: profile line, sheet header, dosing table, sign-off line, margin panels, week schedule, then the log. Plan and Reference are a stack of ruled sections opened by disclosure lines.

The dosing table is a five-column grid (1.5rem number, flexible exercise, 8.5rem dose, 9.5rem load, 44px tick) with a 0.75rem column gap. At 640px and below it becomes four columns with dose stacked above load (1.25rem, flexible, 6.25rem, 44px) so the exercise name keeps its width. The week schedule is a six-column row (marker, day, date, type, headline, toggle) that wraps its headline to a second line at 700px. Activity-log and reference tables stack into ruled entries on phones rather than scrolling sideways. The label/value dashboard list goes two-up above 700px.

Rhythm: rows pad about 0.6rem vertically; sections open 1rem to 2.5rem apart; prose is capped near 70ch. Every interactive element keeps a 44px target on phones, grown with padding on inline links so the line does not move.

## Elevation & Depth

Flat. The sheet has no shadows, no layered cards and no gradients; depth is carried by rules and by the margin fill. The one exception is the chart tooltip, which floats over the chart and takes a small ambient shadow.

### Shadow Vocabulary
- **Tooltip** (`box-shadow: 0 2px 6px rgba(0,0,0,0.12)`): chart hover tooltip only.

### Named Rules
**The Paper Rule.** Nothing sits above the sheet except a transient tooltip. Separation is a rule or a margin fill, never a shadow.

## Shapes

Square by default. Tick boxes and printed checklist boxes are 1px-radius squares with a 1.5px ink stroke. Pills, chips, the send button and marks are 2px. Margin panels are 3px. Tables, sections, rows and the nav have no radius at all. Chevrons are drawn with two 2px borders on a rotated square, legend keys are drawn swatches or short SVG lines, and progress bars are a 6px outlined bar with a flat blue fill. Round shapes appear only as chart dots and the small out-of-range lab dot.

## Components

### Navigation
Thin and quiet. Three tabs on the sheet in Label type, Ink 3 at rest, Ink with Margin 2 behind on hover, Ink with a 3px Clinical Blue underline when active. A 2px ink rule runs under the whole bar. It scrolls sideways on narrow screens with the scrollbar hidden.

### Sheet header
The day and date in Sheet day type with the done count at right, the session title beneath, then a meta line (day-type mark, week and phase, block, athlete) separated by middots and closed by a 2px ink rule. Game and done marks are a 0.5rem square in the state ink before the word.

### Dosing table (signature)
Numbered rows: number in bold Clinical Blue, exercise name at 600 with a dotted-underline link, cue and history in smaller Ink 2 and Ink 3, dose in Ink 2, load in bold Ink with a change chip, and the tick box at right. Column heads are Micro in Ink 3 over a 1px ink rule; rows are divided by hairlines.
- **Tick box:** a 44px button drawing a 22px square with a 1.5px ink stroke. Hover turns the stroke blue. Pressed fills Clinical Blue in 120ms with a white CSS check. This fill is the site's only motion beyond disclosure chevrons.
- **Done row:** strikes to one 44px line (number, name struck through in Ink 3 at 500, load, tick); dose, cue, history and chips hide.
- **5+ write-in line:** a blue 600 label, then a 3.5rem underlined field (1.5px ink bottom border, no box) set at 1.25rem 700 in Clinical Blue. Focus thickens the line to 2px blue on Clinical Wash; an invalid count turns the line and hint Caution Orange.
- **Change chips:** Micro, 2px radius, beside the load. Up is Clinical on Clinical Wash, hold is Ink 2 on Margin, down is Caution on Caution Wash.

### Sign-off line
Appears when every row is ticked. A dashed Ink 3 rule, a bold status line, and a send button: 44px tall, 1.5px Clinical Blue outline, 2px radius, blue text, filling blue with white text on hover. The copied status is Done Green.

### Margin panel
Every callout on the sheet: the pain rule, coaching detail, the week-change note and reference callouts. Flat Margin fill, 3px radius, no border, Ink text at 0.875rem. A panel may open with a Clinical Blue label; list items inside are divided by Margin Hairline.

### Day-type pills
Micro uppercase, 2px radius, 1px 6px padding: training, game, hotel or rehab, deload or done, rest or recovery, in the pairs listed under Colors.

### Weekly schedule
Seven ruled rows under a 2px ink rule. Each row is a disclosure: a 10px marker (filled Clinical Blue square on today), bold day, date in Ink 3, type pill, headline (bold on today, Ink 3 once done), and a blue Label toggle with a CSS chevron. The open body lists exercises with dose right-aligned and the long description in Ink 2.

### Section disclosure line
Plan and Reference sections open with a 2px ink rule and a 48px summary line in Section type, with a CSS chevron in Ink 3 at right. Hover turns the line Clinical Blue. Small toggles elsewhere use Label type in Clinical Blue with the same chevron.

### Strength targets table
Ruled table: lift, now, target, due, progress. Secondary values sit beneath in Label size Ink 3. Progress is a blue percentage over a 6px bar outlined in Clinical Blue and filled flat blue.

### Standards scale
One ruled row per lift: name, rank in all-small-caps Clinical Blue, then a 6px segmented gauge in the standards ramp with a 2px ink mark for now and a 2px dotted Ink 3 mark for the target. Zone names sit beneath in Micro Ink 3, shortened on phones.

### Activity log
Per week, a bold heading and mini-stats over a 2px ink rule, then a ruled table (date, type pill, detail, notes) with hairline rows and exercise lines divided by hairlines. On phones each entry stacks: date and pill on one line, detail and notes below. Notes clamp to three lines with a blue more toggle.

### Profile patient block
Collapsed, a single line of weight, body fat and target in tabular Ink with a Label toggle. Open, it shows a 2px rule, the h1, a ruled label/value list, and a numbered priorities list with Clinical Blue counters under a Micro Ink 3 label.

### Footer
One hairline and a Label-size Ink 3 update line, left-aligned.

## Do's and Don'ts

### Do:
- **Do** open every table and section with a 2px ink rule and divide rows with 1px hairlines.
- **Do** keep Clinical Blue as the only emphasis colour, and put state inks on pills, chips and small marks only.
- **Do** draw tick boxes, chevrons, checks and legend keys in CSS or inline SVG.
- **Do** use the system sans with tabular numerals and keep text at 11px or above.
- **Do** give every control a 44px target on phones, and keep contrast at 4.5:1.
- **Do** set rules, notes and cautions in a flat Margin panel with an optional blue label.
- **Do** limit motion to the 120ms tick fill and disclosure chevrons.

### Don't:
- **Don't** build rounded cards, stat tiles or boxed dashboards; use ruled rows and label/value lists.
- **Don't** use a coloured side stripe or edge bar on any row, panel or callout.
- **Don't** add an uppercase kicker or eyebrow label above a heading.
- **Don't** use glyph or emoji icons, or icon fonts.
- **Don't** add shadows to anything that is not a transient tooltip.
- **Don't** ship a dark theme or gamified feedback.
- **Don't** load a webfont.
- **Don't** use game red, done green or caution orange for hover, emphasis or decoration.
