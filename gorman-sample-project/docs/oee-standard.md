# Gorman OEE Standard (GMS-OPS-007, rev C)

Owner: Corporate Operational Excellence. Approved by the COO on 2026-09-15.

## Definitions

| Term | Definition | Unit |
|------|------------|------|
| Planned production time | Scheduled shift time minus planned breaks | minutes |
| Downtime | Unplanned stops plus changeovers inside planned time | minutes |
| Run time | Planned production time − downtime | minutes |
| Ideal cycle time | Engineering-approved fastest cycle for the part on that line | seconds per part |
| Total count | All parts produced, including rejects | parts |
| Good count | Parts passing quality on the first pass | parts |

## Formula

```text
Availability = run_time / planned_time
Performance  = (ideal_cycle_seconds × total_count) / (run_time × 60)
Quality      = good_count / total_count
OEE          = Availability × Performance × Quality
```

## Rules

1. Calculate with full precision. Round **only the final OEE**, to one decimal place as a percentage.
2. If `total_count == 0` or `run_time == 0`, OEE is **0.0** and the shift is flagged
   `NO_PRODUCTION`. It is never an error and never a crash.
3. Reject records where `downtime > planned_time`, `good_count > total_count`, or any value is negative.
4. Performance above 1.0 means the ideal cycle time is wrong. Keep the value and flag the record `PERF_OVER_100`.
5. Plant averages are **weighted by planned time**, not simple averages of shifts.
6. Changes to an ideal cycle time must reference a change ticket (CHG-xxxx) in `docs/change-log.md`.

## Worked example (Line 1, shift A, 2026-11-02)

planned 480, downtime 47, ideal cycle 30 s, total 780, good 741

- Availability = 433 / 480 = 0.90208
- Performance = (30 × 780) / (433 × 60) = 0.90069
- Quality = 741 / 780 = 0.95000
- **OEE = 77.2%**
