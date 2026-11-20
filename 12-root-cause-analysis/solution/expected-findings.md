# Answer Key: INC-2026-311 (read this only after you finish)

## Verified cause

**Master-data change CHG-1182 (2026-11-05):** Line 3's ideal cycle time was lowered from **30 s to
24 s** "per new die spec DS-88 (die not yet installed)." The line still runs the old die and
produces the same number of parts, so the Performance factor fell from about 0.89 to about 0.71. OEE dropped about
16 points even though **nothing physical changed**.

| Period | Ideal cycle | Avg availability | Avg performance | Avg quality | Avg OEE |
|--------|-------------|------------------|-----------------|-------------|---------|
| Nov 2–4 | 30 s | ~0.92 | ~0.89 | ~0.98 | **~79.7%** |
| Nov 5–7 | 24 s | ~0.92 | ~0.71 | ~0.98 | **~63.7%** |

## Hypotheses rejected

| Hypothesis | Why it's rejected |
|------------|-------------------|
| New B-shift crew is slower (CHG-1177, Nov 4) | A shift (unchanged crew) dropped by the same amount. B shift on Nov 4, with the new crew, had normal OEE (78.9%). Part counts and downtime were flat. |
| More downtime | Downtime stayed at 34–45 minutes per shift throughout |
| Quality problem | Good/total stayed at about 0.975 throughout |
| Historian firmware patch (CHG-1185) | That patch was on Line 1, and it happened on Nov 6, after the drop began |

## Recommended controls

1. Revert Line 3's ideal cycle to 30 s until die DS-88 is installed, and restate the affected weekly KPI.
2. Require ideal-cycle changes to take effect only when the tooling change is confirmed (process control).
3. Add an `IDEAL_CYCLE_CHANGED` flag or warning in `gorman_oee` (Prompt 12.2).
4. No crew retraining is needed.
