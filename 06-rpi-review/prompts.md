# Module 06 — Self-learning prompts

> Type `/clear` first.

## Prompt 6.1 — Acceptance review

```text
/rpi-review task=oee-standardization depth=standard
Review the implementation against the plan and the research. Verify the acceptance
criteria by running python3 -m unittest discover -s tests -t . and the CLI for all
three plants. Confirm nothing under plants/ or data/ changed. Record the outcome and
route every follow-up.
```

## Prompt 6.2 — Route the follow-ups

```text
For each follow-up in the oee-standardization review, tell me whether it goes back to
Implement, Plan or Research, or becomes a new work item. Draft a one-paragraph
description for each new work item that I could paste into our tracker.
Do not create anything in a tracker.
```

## Prompt 6.3 — Refine instead of restart

```text
/rpi-refine task=oee-standardization
Plant managers asked for a --strict option: when any shift is flagged PERF_OVER_100,
the CLI should exit with EXIT_FAILURE (1) so the weekly job alerts someone. Make the
smallest change that does this, add a test, and update the plan and changes log.
(Or refine using the smallest finding from your own review instead.)
```

## Prompt 6.4 — Audit trail summary (for Gorman's auditors)

```text
Create docs/audit/oee-standardization-evidence.md that lists, with links, the research,
plan, critique, changes log and review artifacts for this change, plus the test
command and its result. Two paragraphs maximum, plus a table.
```

## Reflection

- Which artifact would an auditor read first?
- What did the review find that you, as the human, had missed?
