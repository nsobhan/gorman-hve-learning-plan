---
description: 'Gorman OEE calculation rules (GMS-OPS-007 rev C) for KPI code'
applyTo: 'gorman_oee/**/*.py, plants/**/*.py'
---

# Gorman KPI Rules

Source of truth: `docs/oee-standard.md`. If this file and the standard disagree, the standard wins.
Report the conflict.

## Canonical Units

The canonical units are minutes for planned and downtime, seconds per part for ideal cycle, and
integer part counts. Plant adapters convert to these units **before** any calculation.

## Formulas

```text
run_time     = planned_minutes - downtime_minutes
Availability = run_time / planned_minutes
Performance  = (ideal_cycle_seconds * total_count) / (run_time * 60)
Quality      = good_count / total_count
OEE          = Availability * Performance * Quality
```

## Rules

1. Keep full precision. Round only the final OEE percentage, to 1 decimal place.
2. If `total_count == 0` or `run_time == 0`, OEE is `0.0` with the `NO_PRODUCTION` flag. Never raise an error.
3. Reject `downtime > planned`, `good > total`, and negative values with `InvalidShiftRecordError`.
4. If Performance > 1.0, keep the value and add the `PERF_OVER_100` flag.
5. Weight plant averages by planned minutes.
6. Every KPI change keeps the golden-shift test passing: planned 480, downtime 47, ideal 30, total 780, good 741 gives **77.2%**.

## Common Mistakes Found in Legacy Plant Scripts

- Dividing performance by planned time instead of run time (Detroit)
- Leaving out the quality factor (Monterrey)
- Dividing by zero on zero-production shifts (Monterrey)
- Rounding each factor before multiplying (Pune)
- Simple averages of shifts instead of weighted averages (Detroit)

## Stop and Ask

Any change to a formula, rule or flag needs explicit human approval and an update to `docs/oee-standard.md`.
