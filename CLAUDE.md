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

---

## Science-Based Programming Guidelines

Use these evidence-based decision frameworks when recommending load changes, flagging recovery concerns, or adjusting the program. All recommendations are calibrated for a 40-year-old in-season recreational athlete with bilateral achilles tendinopathy.

### 1. Loading & Progression Rules

**Primary progression model: Double progression (reps → load)**
When all prescribed reps are completed with good form across 2 consecutive sessions at the same weight, increase load. This is the most reliable progression method for intermediate lifters training 2–3x/week (Schoenfeld 2017, NSCA guidelines).

- **Compound lower body** (trap bar DL, squat): increase 10 lbs per cycle
- **Compound upper body** (bench, rows): increase 5 lbs per cycle
- **Dumbbell accessories** (DB press, OH press, RDLs): increase 5 lbs per cycle
- **Machine/cable exercises**: increase by one plate increment when top of rep range is hit for all sets
- **Bodyweight exercises** (GHR, pull-ups): add reps first, then add external load in 5–10 lb increments

**RPE targets by phase:**
- Phase 1 (Foundation): RPE 6–7 on compounds — building movement quality, not grinding. Leave 3–4 reps in reserve.
- Phase 2 (Strength-Power): RPE 7–8 on compounds — working sets should feel challenging but controlled. 2–3 reps in reserve.
- Phase 3 (Power Realization): RPE 7–9 on primary lifts, RPE 6–7 on accessories — peak performance window, manage fatigue carefully.

**When progression stalls (same weight for 3+ sessions):**
1. First: check recovery factors (sleep, nutrition, game load that week)
2. Second: try microloading — fractional plates or 2.5 lb increases if available
3. Third: add one set at the current weight before increasing load (volume before intensity)
4. Last resort: reset 10% and build back up over 2–3 weeks

References: Schoenfeld et al. (2017) "Dose-response relationship between weekly resistance training volume and increases in muscle mass"; NSCA Essentials of Strength Training (4th ed.) Ch. 18 Program Design.

### 2. Deload Protocol

**Frequency:** Every 4th week (already programmed). For a 40-year-old athlete with 3 weekly games, this is on the conservative end — if accumulated fatigue or achilles symptoms spike mid-cycle, an earlier deload is warranted.

**How to deload (evidence-based approach):**
- **Reduce volume 40–50%** — cut total sets roughly in half. This is the primary fatigue driver (Pritchard et al. 2015).
- **Maintain intensity at 85–95% of current working weights** — preserves neuromuscular adaptations. Dropping weight too far causes detraining without additional recovery benefit.
- **Practical implementation:** Keep the same exercises, same weight, cut sets from e.g., 4x5 → 2x5, and 3x8 → 2x8.
- **Keep games on normal schedule** — deload applies to lifting, not sport participation.
- **HSR protocol stays at full load during deload** — tendons have longer adaptation cycles (6–12 weeks) and don't benefit from reduced load the way muscles do (Magnusson et al. 2010).
- **Friday session during deload:** Can be replaced entirely with mobility/recovery work if fatigue is high.

**Signs a deload is needed earlier than scheduled:**
- RPE on working sets is 1–2 points higher than previous week at the same weight
- Achilles morning stiffness lasting >30 min (up from typical <15 min)
- Sleep quality declining for 3+ consecutive nights
- Game performance noticeably worse (self-reported)

References: Pritchard et al. (2015) "Tapering practices of New Zealand's elite raw powerlifters"; Magnusson et al. (2010) on tendon adaptation timelines; Hausswirth & Mujika (2013) "Recovery for Performance in Sport."

### 3. In-Season Volume Management

**Context:** 3 games/week (2 basketball + 1 hockey) imposes significant systemic and lower-body training stress. Basketball and hockey contribute substantial eccentric load, reactive agility, and cardiovascular demand.

**Weekly set targets (in-season athlete, per muscle group):**
- **Quads/Glutes/Hamstrings:** 6–10 hard sets/week from lifting. Games add ~4–6 equivalent sets of lower body work (Impellizzeri et al. 2004). Total effective volume is higher than the log shows.
- **Chest/Back/Shoulders:** 6–10 hard sets/week. Less competition interference.
- **Core:** 4–6 direct sets/week. Games provide substantial indirect core work.

For reference, hypertrophy-oriented research suggests 10–20 sets/muscle/week for growth (Schoenfeld et al. 2017), but in-season athletes should target the lower end and count sport exposure. The goal is maintenance and modest strength gain, not maximizing volume.

**Counting game load:**
- Each basketball session ≈ moderate lower body training stimulus
- Each hockey session ≈ moderate-to-high lower body + core stimulus
- A 3-game week means the lifter is already accumulating significant lower body fatigue before Wednesday's training session
- If game load increases (extra games, tournaments), reduce lifting volume that week — drop Friday session first, then reduce Wednesday sets

References: Impellizzeri et al. (2004) internal vs external training load; Schoenfeld et al. (2017) dose-response for volume; Suchomel et al. (2018) in-season programming for team sport athletes.

### 4. Achilles Tendinopathy — Evidence-Based Load Management

**HSR Protocol (Heavy Slow Resistance):**
The program uses HSR over isolated eccentric protocols based on Beyer et al. (2015), which found HSR and eccentric training equally effective for Achilles tendinopathy at 12 weeks, with higher patient satisfaction for HSR due to simpler execution and gym-friendly loading.

**HSR dosing:**
- 3x/week (Wed, Fri, + 1 recovery day) — current protocol is correct
- 3×6 at 6RM with 3-sec concentric / 3-sec eccentric — ~6 sec per rep, emphasizing time under tension
- Progress load when 6 reps are completed with good form and pain ≤3/10 during the exercise
- HSR load progression is independent of deload cycles — maintain full HSR load even during deload weeks

**Pain monitoring decision tree:**
- **0–3/10 during exercise:** Acceptable. Continue current protocol. This level of pain during loaded tendon exercises is expected and does not indicate harm (Silbernagel et al. 2007 "pain-monitoring model").
- **4–5/10 during exercise:** Caution. Maintain current load but do not increase. If pain persists at this level for 2+ weeks, reduce HSR load by 15–20%.
- **>5/10 during exercise:** Stop the exercise. Reduce load by 25% next session. If >5/10 persists after reduction, flag for possible clinical review.
- **Game-day achilles pain >5/10:** Drop Friday plyometrics for 2 weeks (already in plan), increase HSR frequency temporarily to 4x/week.
- **Morning stiffness >30 minutes:** Flag as a regression signal. Consider earlier deload or reduced game minutes.
- **24-hour rule:** Pain should return to pre-exercise baseline within 24 hours. If achilles pain remains elevated the day after exercise, load was too high — reduce by 10–15% next session.

**Tendon adaptation timeline:**
Tendons adapt more slowly than muscle (Magnusson et al. 2010). Expect measurable tendon remodeling improvements at 12+ weeks of consistent HSR. Do not judge HSR effectiveness before 8 weeks minimum. Early improvements are often neural/pain-science related, not structural.

References: Beyer et al. (2015) "Heavy Slow Resistance versus Eccentric Training as Treatment for Achilles Tendinopathy"; Silbernagel et al. (2007) pain-monitoring model for Achilles tendinopathy; Magnusson et al. (2010) tendon collagen adaptation.

### 5. Recovery & Fatigue Monitoring

**Session spacing (current schedule is evidence-aligned):**
- 48+ hours between heavy lifting and games (Suchomel et al. 2018)
- Wednesday heavy → Sunday game = 3.5 days (optimal)
- Wednesday heavy → Tuesday game = 6 days (optimal)
- Friday is deliberately the lightest lifting session, ~36 hours before Sunday AM basketball

**Auto-regulation signals — when to reduce that session's intensity/volume:**
- Warm-up sets feel RPE 2+ higher than expected → drop one working set per exercise
- Achilles morning stiffness persists past warm-up → skip plyometric/explosive components
- Slept <6 hours → reduce volume 25%, maintain intensity (partial deload)
- 3+ high-intensity games in the past 5 days → drop Friday session entirely or replace with recovery

**Sleep (the highest-ROI recovery tool):**
- Target 7–9 hours. For a 40-year-old athlete, sleep is the single most impactful recovery variable (Vitale et al. 2019).
- Sleep <6 hours for 3+ nights is a deload trigger (see section 2).

**Nutrition timing (simple rules):**
- Protein: 1.6–2.2 g/kg/day (~160–220g at 220 lbs). Distribute across 4+ meals with 30–40g per meal for maximal muscle protein synthesis (Morton et al. 2018).
- Carb timing: higher carbs on game days (Sun, Tue) and training days (Wed, Thu, Fri) to fuel glycogen-dependent activity. Lower carbs on recovery days (Mon, Sat).
- Post-game/training: protein + carbs within 2 hours. Not magic, but supports glycogen replenishment and reduces cortisol (Aragon & Schoenfeld 2013).

References: Vitale et al. (2019) "Sleep Hygiene for Optimizing Recovery in Athletes"; Morton et al. (2018) protein dose-response meta-analysis; Aragon & Schoenfeld (2013) nutrient timing review; Suchomel et al. (2018).

### 6. Plyometric Introduction (Phase 2+)

**Rationale:** Plyometrics produce the most sport-transferable power gains for vertical jump, with diminishing returns after ~4 weeks of consistent training (Markovic 2007). The program introduces them in Phase 2 after a 6-week strength base.

**Dosing for in-season athletes:**
- **Frequency:** 1–2x/week max. Friday is the designated plyo day.
- **Volume:** 40–60 ground contacts per session for a non-specialized athlete. Start at the low end (Ebben et al. 2010).
- **Intensity progression:** Box jumps (step down, never rebound) → depth drops → depth jumps. Only advance when landing mechanics are consistent.
- **Always step down from box jumps** — rebounding adds eccentric achilles load with minimal additional power benefit, and is contraindicated with achilles tendinopathy.

**Vertical jump–specific evidence:**
- Plyometric training produces ~4–8% vertical jump improvement over 6–12 weeks in trained athletes (Markovic 2007 meta-analysis).
- Combined strength + plyometric training is superior to either alone ("complex training" — Ebben 2002). The program is structured this way: heavy strength Wed/Thu + plyo Fri.
- For a 220 lb athlete, relative strength (strength-to-bodyweight ratio) is the primary limiter of vertical jump. Reducing body fat while maintaining muscle will improve jump height even without plyometrics.

**When to pull back on plyos:**
- Achilles pain >3/10 during plyometric exercises → stop, substitute with concentric-only power work (e.g., sled push, kettlebell swings)
- If game load increases that week → drop plyos first (highest achilles risk, lowest priority relative to strength work)

References: Markovic (2007) "Does plyometric training improve vertical jump height?"; Ebben et al. (2010) "Optimal Depth Jump Parameters"; Ebben (2002) complex training review.

### 7. Strength Standards & Target Validation

**12-month targets in context:**

| Lift | Current | Target | Required Gain | Assessment |
|------|---------|--------|---------------|------------|
| Trap Bar DL | 230×5 | 385×5 | +155 lbs (+67%) | Ambitious but achievable if progression is consistent. TB DL is more forgiving than conventional DL. ~3 lbs/week average increase needed. |
| Back Squat | 185×5 | 315×5 | +130 lbs (+70%) | Aggressive. Squat is harder to progress in-season due to leg fatigue from games. May need 15–18 months. |
| Bench Press | 155×5 | 225×5 | +70 lbs (+45%) | Most realistic of the three. Upper body is less affected by game load. ~1.5 lbs/week average. |

**Rate-of-progression reality check (for a 40-year-old returning lifter):**
- First 3–6 months: fastest gains (neural adaptation + muscle memory if previously trained). Expect 5–15 lbs/month on compounds.
- Months 6–12: progression slows to 2–5 lbs/month on compounds.
- Age factor: recovery capacity is ~10–15% lower than a 25-year-old at equivalent training levels (Lexell 1995). This is already accounted for by the 3-day lifting schedule and conservative volume.
- In-season factor: expect ~30–40% slower progression on lower body lifts during active game seasons compared to off-season training blocks (Baker 2001).

**When to revisit targets:**
- At the Phase 1 → Phase 2 transition (Week 7): re-evaluate whether the 12-month targets need adjustment based on actual 6-week progression rate.
- At any point where a lift stalls for 3+ weeks despite proper deloading and recovery.

References: Lexell (1995) "Human aging, muscle mass, and fiber type composition"; Baker (2001) "Comparison of upper-body strength and power between professional and college-aged rugby league players"; Rhea et al. (2003) dose-response meta-analysis for strength training.
