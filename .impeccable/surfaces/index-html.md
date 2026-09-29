---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: []
---

# Surface brief: index.html (whole site)

Scope: all three tabs (This Week, Training Plan, Reference), nav, profile panel, footer. Visitor mode: Operate. One athlete, mostly on a phone at the gym between sets, sometimes desktop for review.

Job: see today's prescription, tick it off, record the 5+ count, send the session; check the week; look up the protocol and progress.

Constraints: static index.html plus data.json, no build step, no webfont, no nutrition or sleep UI, no citations on the site, colour-as-code meanings kept (game, training, done, rest, caution), 44px targets on phones, 11px text floor, 4.5:1 contrast. Not dark, not gamified.

## Direction contract

THESIS: The site is the exercise sheet a clinician or S&C coach hands the athlete: numbered moves, a dosing table, tick boxes, and the rules in the margin. It refuses the tracker-app stack of rounded cards and the dashboard of stat tiles.

OWN-WORLD: White sheet, near-black ink, one clinical blue (#2456a6) for numbers, ticks and links, pale blue-grey margin panels (#e6ebf2). Ruled tables with a heavy rule under headers and hairlines between rows. Square tick boxes. System sans, tabular numerals. Game red, done green and caution orange appear only as small marks and pills.

STORY: He opens the sheet, reads today's numbered moves and loads, ticks each box, writes the 5+ reps on the line, and sends it. The margin tells him the pain rule and what to do if something feels off.

FIRST VIEWPORT: Sheet header line (day, date, session, week and phase) under a thin nav; then the numbered dosing table: # | exercise with cue | dose | load with change | tick box. The first four rows visible at 390px. The margin panel follows the table.

FORM: Physio Exercise Sheet, my list position 1 (the pick), seed key a64f4d0e.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

Signature interaction: ticking a box fills it in clinical blue and strikes the row to one line; the sheet shortens as the session runs. Motion: a 120ms fill, nothing else.
