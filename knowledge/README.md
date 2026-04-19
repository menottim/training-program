# Knowledge Base

Primary-source evidence files that back the recommendations in `CLAUDE.md`. Each file is built from actual peer-reviewed papers verified via PubMed, journal sites, or authoritative reviews. The purpose of this directory is to ensure the coaching voice cites real, retrievable research rather than paraphrased or hallucinated sources.

## Principles

- __Every claim cites a retrievable paper.__ Include PubMed ID, DOI, or full journal citation.
- __Evidence tiers are explicit.__ Strong / Moderate / Emerging. Tiers follow the rubric in `../CLAUDE.md` (Persona & Coaching Style → Evidence Standards).
- __Corrections are part of the record.__ When subsequent research overturns or nuances a claim, amend the file and note the change inline rather than deleting the prior position.
- __Calibrated for the athlete.__ Findings are interpreted for a 40-year-old in-season recreational athlete with bilateral achilles tendinopathy. Do not import recommendations from cohorts with materially different profiles (young untrained, elite elderly, clinical populations) without flagging the extrapolation.

## Topic index

| File | Scope | Last verified |
|---|---|---|
| [sodium-hydration.md](sodium-hydration.md) | Sodium-water balance, acute scale-weight spikes, potassium counterbalance, hyponatremia risk, hydration strategy | 2026-04-18 |
| [protein-distribution.md](protein-distribution.md) | Daily protein ceiling, per-meal anabolic window, distribution strategy, high-protein safety | 2026-04-18 |
| [body-composition-measurement.md](body-composition-measurement.md) | Daily weight variance, BIA scales, DEXA protocol, skinfolds, trailing averages, measurement-method tradeoffs | 2026-04-18 |
| [achilles-tendinopathy-hsr.md](achilles-tendinopathy-hsr.md) | HSR protocol (Beyer), pain monitoring (Silbernagel), tendon adaptation timelines, collagen + vit C, PRP/ESWT/GTN evidence | 2026-04-18 |
| [in-season-volume.md](in-season-volume.md) | Weekly set targets, minimum effective dose, RPE auto-regulation, tapers vs deloads, progression rules | 2026-04-18 |
| [recovery-sleep.md](recovery-sleep.md) | Sleep targets, recovery modality hierarchy, CWI tradeoffs, alcohol effects, overtraining red flags | 2026-04-18 |
| [supplements.md](supplements.md) | Menotti's daily stack reviewed (multivitamin, fish oil, iron, magnesium, creatine); iron flag; fish oil dose review; collagen/vit D/caffeine alternatives | 2026-04-19 |

## When to consult

- __Before making a novel recommendation__ in a topic area covered here, read the relevant file first to avoid drifting from verified evidence.
- __When a user claim conflicts__ with what is in a knowledge file, the knowledge file is the default source of truth. Update the file if new evidence supersedes it.
- __When a new topic arises repeatedly in conversations__, create a new file and add it to the index above.

## Contribution pattern

1. Pick the topic.
2. Run targeted web searches for primary papers (PubMed, Google Scholar, journal sites). Use at least 3 independent sources per major claim.
3. Draft the file using the standard structure (Scope, Key Findings table, Mechanism, Practical Application, Unresolved Questions, References).
4. Include PubMed IDs and DOIs for every cited study.
5. Note any claims from `CLAUDE.md` or prior coaching that the new evidence corrects or nuances.
6. Commit with a descriptive message and update the README index.
