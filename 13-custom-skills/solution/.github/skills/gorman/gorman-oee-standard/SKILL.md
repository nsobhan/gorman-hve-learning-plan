---
name: gorman-oee-standard
description: "Gorman Manufacturing OEE standard GMS-OPS-007: formulas, rules, flags and how to explain OEE changes. Use when checking an OEE number, explaining why OEE changed, comparing plants, or reviewing KPI code."
---

# Gorman OEE Standard (GMS-OPS-007 rev C)

The authoritative document is `docs/oee-standard.md`. This skill helps you apply it.

## Formulas (canonical units)

```text
Availability = (planned - downtime) / planned            # minutes
Performance  = ideal_cycle_s * total / (run_min * 60)
Quality      = good / total                               # first-pass good only
OEE          = A * P * Q   -> round only the final %, 1 decimal place
```

## Flags

- `NO_PRODUCTION`: total = 0 or run time = 0, so OEE is 0.0
- `PERF_OVER_100`: performance > 1.0, which suspects a wrong ideal cycle time

## Explaining an OEE Change

1. Break each period down into A, P and Q. Find the factor that moved.
2. If **P** moved but part counts didn't, check ideal-cycle changes in `docs/change-log.md` first.
3. If **A** moved, look at downtime and the shift calendar (planned-time changes).
4. If **Q** moved, look at reject and scrap data. Rework is not "good."
5. For plant averages, check whether one shift with a large weight (or a NO_PRODUCTION shift) moved the weighted average.
6. Every explanation cites the shift keys and the numbers. Never blame people without evidence.

## Golden Shifts

Use [references/golden-shifts.md](references/golden-shifts.md) to check any adapter or calculation.
