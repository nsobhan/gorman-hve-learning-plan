# Module 03 — Self-learning prompts

> Start a new chat. Type `/rpi-research` (or `/hve-core:rpi-research` with the plugin), then paste the prompt.

## Prompt 3.1 — Main research task

```text
topic=oee-standardization

Research what is needed to replace Gorman's three plant OEE scripts (plants/detroit,
plants/monterrey, plants/pune) with one shared, tested library that follows
docs/oee-standard.md (GMS-OPS-007).

Consider:
* Every place each plant script differs from the standard (formula, units, rounding,
  averaging, zero-production handling), with file and function references
* Each plant's export format in data/, and what an adapter must convert
* Constraints in docs/problem-statement.md (stdlib only, exports can't change)
* Security issues that must not be carried into the new library
* At least two alternative designs (for example, fixing each script in place versus a
  shared library with adapters), with trade-offs
* How to prove correctness: the golden shift in the standard must give 77.2% for
  every plant format

Do not plan or implement. Record open questions that need a Gorman decision.
```

## Prompt 3.2 — Focused follow-up research

```text
/rpi-research topic=oee-standardization posture=focused
Extend the existing research: confirm, by calculating it, what OEE each legacy
script reports for Line 1 shift A on 2026-11-02 and why each differs from 77.2%.
Add the result as a table in the existing artifact.
```

## Prompt 3.3 — Challenge the research (skeptical review)

```text
/rpi-challenger
Subject: the latest research artifact under .copilot-tracking/research/ for
oee-standardization. Challenge its recommendation and its evidence. Focus on whether
the shared-library approach really respects "plant exports can't change this quarter"
and whether any legacy behavior is intentional and must be preserved.
```

## Prompt 3.4 — Learn by walkthrough

```text
/rpi-walkthrough
Walk me through the oee-standardization research artifact one section at a time.
Pause after each section so I can ask questions.
```

## Reflection

- Which finding would you have missed by reading the code yourself?
- What open question needs a decision from the Gorman COO rather than an engineer?
