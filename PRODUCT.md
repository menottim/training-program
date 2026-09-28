# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

One user: Menotti, a 40-year-old recreational athlete (basketball and hockey) with bilateral achilles tendinopathy. He works Monday to Friday, 9 to 5. He opens the site mostly on his phone, before or during a session and to check the week. Desktop is secondary.

## Product Purpose

A personal training tracker. It shows today's prescription with target loads, then records what was done: sessions, lifts, game entries and weekly body readings, against strength targets. Success is that the site always shows the current coaching decision and the athlete can act on it without reading anything long.

## Positioning

Built around one athlete's injury, game slate and goals. It renders a hand-authored week from `data.json` rather than a generic template, and it says so plainly when no week has been authored.

## Operating Context

- Static site on GitHub Pages: `index.html` with an inline renderer, reading `data.json`. Live at https://menottim.github.io/training-program/.
- The week runs Sunday to Saturday. Game slate changes by season and lives in `data.modifiedWeeks`.
- The site is updated by committing `data.json`; Pages rebuilds in about 2 minutes.
- Terminology: RIR, reps-plus set ("5+"), HSR (calf heavy slow resistance), carried weight, modified week.

## Capabilities and Constraints

- Static only, no build step. Confirmed by the user.
- No nutrition or sleep UI. Both were removed and must not return. Confirmed by the user.
- Also stated in the repo's `CLAUDE.md` and to be honored: `data.json` is the only source of changing data and no schedule is hardcoded in `index.html`; rendered fields carry the plan only, with no citations or program self-assessment; short `desc` headlines (about 8 words) and word caps on long fields.
- An un-authored week must show as missing, not as a fabricated default.

## Evidence on Hand

Real data only: `activityLog`, `bodyLog`, `modifiedWeeks`, `targets` in `data.json`. No testimonials, external users or benchmarks exist. Do not invent any.

## Product Principles

1. The current plan is the first thing visible; history and charts come second.
2. Phone first. Every tile must read on a small screen without expanding.
3. Say what is known and no more: a missing week, a missing reading and a carried weight are all labeled as such.
4. Keep rendered copy short and instructional; reasoning and evidence stay out of the site.
5. Show only what the athlete acts on. Retired tracking (nutrition, sleep) stays gone.
