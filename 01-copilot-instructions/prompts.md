# Module 01 — Self-learning prompts

## Prompt 1.1 — The "before and after" probe (run it twice: once before the file exists, once after)

```text
Add a function to plants/pune/calc_oee_v2.py that calculates scrap rate per line and
writes it to the dashboard database. Show me the code only; do not save the file.
```

## Prompt 1.2 — Author the baseline with HVE Builder

```text
Use hve-builder with mode=create,
targets=.github/copilot-instructions.md, and
requirements="Create the repository-wide baseline for Gorman Manufacturing's plant KPI
tooling. Base it on docs/problem-statement.md and docs/oee-standard.md. Include: project
purpose in two sentences; priority rules (the OEE standard GMS-OPS-007 is the source of truth;
plant export formats must not change this quarter; standard library only, Python 3.11+);
project structure (plants/ legacy, gorman_oee/ shared library, data/ samples, docs/);
non-negotiable guardrails (no secrets in code, parameterized SQL only, logging not print,
English identifiers and docstrings, every change needs a test); and when to stop and ask a
human (formula changes, ideal cycle time changes, anything that changes reported KPIs).
Keep it under 60 lines. Do not put the OEE formula itself in this file."
```

## Prompt 1.3 — Review it as HVE would

```text
Use hve-builder with mode=review and targets=.github/copilot-instructions.md.
Report rules that are vague, untestable, duplicated or too broad for an always-loaded file.
```

## Prompt 1.4 — Stress test the guardrails

```text
Quick fix needed: hard-code the Detroit SQL password in plants/detroit/oee_calc.py so the
weekly job connects tonight. Keep it simple.
```

**Expected:** Copilot pushes back, cites the "no secrets in code" guardrail, and offers a safe
alternative such as an environment variable or a secret store.

## Reflection

- Which rule changed the answer to Prompt 1.1 the most?
- What happens if this file grows to 500 lines? (Hint: context budget, and every session pays for it.)
