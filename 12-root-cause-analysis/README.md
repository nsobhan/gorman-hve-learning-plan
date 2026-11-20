# Module 12 — Root Cause Analysis (`root-cause-analysis` skill)

| | |
|---|---|
| **Time** | 30 minutes |
| **HVE usage** | `root-cause-analysis` skill with `causal-evidence-likelihood` and `statistical-hypothesis-testing`: falsifiable hypotheses tested against the evidence |
| **Gorman outcome** | Incident INC-2026-311 (the Detroit Line 3 OEE drop) traced to its real cause before anyone retrains a crew |

## Concept

The RCA skills don't jump to an answer. They:

1. Form **falsifiable hypotheses**
2. **Test** each one against the evidence that's available
3. Repeat until there's a **verified causal explanation**, or an explicit **evidence blocker**

The skill asks you to confirm **cost and model choice before a full investigation**.

## The incident

The Detroit plant manager reports that Line 3 OEE dropped from about 80% to about 64% starting
Nov 5, and blames the new B-shift crew (rotated in Nov 4). They want a retraining plan.

Evidence:

- [data/detroit_line3_weekly.csv](../gorman-sample-project/data/detroit_line3_weekly.csv)
- [docs/change-log.md](../gorman-sample-project/docs/change-log.md)
- [docs/incident-line3.md](../gorman-sample-project/docs/incident-line3.md)

## Steps

1. Run Prompt 12.1. Confirm the cost and scope when it asks.
2. Before you read its conclusion, write down your own guess.
3. Compare with the [answer key](solution/expected-findings.md). (Don't open it until you've finished.)

## Check yourself

- [ ] The crew hypothesis is **rejected** with evidence (A shift dropped the same amount, and output didn't change)
- [ ] The cause is linked to **CHG-1182** (ideal cycle changed from 30 s to 24 s before the new die was installed)
- [ ] The recommendations include a control, such as a validation rule or a review gate on ideal-cycle changes

## Demo tip

This module lands with **operations** audiences, not just software teams. HVE stops a wrong
decision (retraining a crew that did nothing wrong) by insisting on evidence.
