# Training Program — LLM Instructions

## Overview

This is a personal training program tracker for a 40-year-old male athlete (6'2", ~220 lbs) with bilateral achilles tendinopathy. Goals in priority order: injury prevention > strength/power > vertical jump. He plays basketball (Tue PM, Sun AM) and hockey (Sun PM), works M-F 9-5.

Live site: https://menottim.github.io/training-program/

## Architecture

- **data.json** — All mutable data: athlete stats, baseline lifts, targets, `activityLog[]`, `bodyLog[]`
- **index.html** — Static training plan + inline JS renderer that fetches data.json
- **Everything renders dynamically** from data.json — dashboard cards, charts, progress logs, activity log table

## Git Identity

Always commit and push with the personal identity, NOT any corporate identity:

```
git -c user.name="menottim" -c user.email="menottim@users.noreply.github.com" commit -m "message"
```

## How to Log Activity

When the user reports a workout, game, or recovery session:

### Step 1: Determine what was done

Parse the user's message for:
- Date (default: yesterday if not specified, or "today" if they say so)
- Activity type: `game`, `training`, or `recovery`
- Exercises with weights/sets/reps
- Achilles pain level (0-10) if mentioned
- Body weight / body fat if mentioned
- Game performance notes if mentioned

### Step 2: Match "as prescribed" exercises

If the user says "the rest as prescribed," look up the prescribed exercises for that day in `index.html`. The training plan is organized by phase and day (Wed = Lower Body, Thu = Upper Body + Core, Fri = Lower Moderate). Log prescribed exercises with weight "as prescribed" unless the user gave specific numbers.

### Step 3: Append to activityLog in data.json

This is the **ONLY file you need to edit** for activity logging. Append a new entry to the `activityLog[]` array.

#### Activity name format (CRITICAL for progress log rendering)

Training sessions MUST use this naming convention in the `activity` field:

```
"<Description> (<Day> Phase <N>)"
```

Examples:
- `"Lower Body (Wed Phase 1)"`
- `"Upper Body + Core (Thu Phase 1)"`

The renderer uses a regex `/\((\w+)\s+Phase\s+(\d+)\)/` to extract the day and phase, then renders progress log tables grouped by phase+day. If you don't follow this format, the session won't appear in progress logs.

#### Exercise entry format

```json
{
  "date": "2026-03-19",
  "type": "training",
  "activity": "Upper Body + Core (Thu Phase 1)",
  "exercises": [
    { "name": "DB Bench Press", "sets": "4x6", "weight": "65 lbs" },
    { "name": "Lat Pulldown", "sets": "1x6, 1x6, 2x6", "weight": "95/110/135/135 lbs" }
  ],
  "notes": "Summary of session, progression notes"
}
```

#### Game entry format

```json
{
  "date": "2026-03-17",
  "type": "game",
  "activity": "Basketball",
  "duration": "40 min",
  "intensity": "high",
  "achillesPain": 0,
  "notes": "Session notes"
}
```

#### Recovery entry format

```json
{
  "date": "2026-03-09",
  "type": "recovery",
  "activity": "Recovery day",
  "details": "Bike 12 min, seated calf raise HSR 3x10, stretches",
  "notes": "How it felt"
}
```

### Step 4: Append to bodyLog if body stats reported

```json
{ "date": "2026-03-13", "weight": 220.5, "bodyFatPct": 23.2 }
```

### Step 5: Commit and push

Commit with a descriptive message summarizing the key lifts/weights. Push to main. GitHub Pages deploys automatically.

### Step 6: Review and advise

After logging, review recent trends and surface observations:
- Progression compared to previous weeks (weight increases, rep improvements)
- Progress toward strength targets (Trap Bar DL 385x5, Squat 315x5, Bench 225x5)
- Achilles pain trends
- Whether a deload week is coming up
- Any program adjustments worth considering

## Things NOT to Do

- **Do NOT manually update `currentLifts`** in data.json — the renderer derives current lifts automatically from activityLog by scanning for the latest logged weight of each main lift
- **Do NOT edit index.html** for activity logging — only data.json needs to change
- **Do NOT map DB Bench Press to the benchPress current lift** — DB bench and barbell bench are different lifts with different weight ranges

## Lift Name Mapping (for derived currentLifts)

The renderer scans `activityLog` exercises and maps these exact names:
- `"Trap Bar Deadlift"` → trapBarDeadlift
- `"Back Squat"` → backSquat
- `"Bench Press"` → benchPress (barbell only)

## Schedule

- **Week 1 start date: March 8, 2026** (Sunday)
- Weeks run Sunday–Saturday
- Phase 1: Foundation — Weeks 1–6 (Mar 8 – Apr 18)
- Phase 2: Strength-Power — Weeks 7–12 (Apr 19 – May 30)
- Phase 3: Power Realization — Weeks 13+ (May 31 onward)
- **Deload weeks: every 4th week** (Weeks 4, 8, 12, ...)
- To calculate current week: `ceil((days since March 8 + 1) / 7)`

## Equipment Notes

- Has access to seated calf raise machine
- GHR machine available (preferred over Nordic hamstring curl)
