# Module 04 — RPI Phase 2: Plan (`/rpi-plan`)

| | |
|---|---|
| **Time** | 30 minutes |
| **HVE usage** | `/rpi-plan` with research input, independent plan critique, phase and task IDs (`Pxx-Txx`) |
| **Gorman outcome** | A reviewed, task-level plan for the shared `gorman_oee` library, which Gorman's change policy requires before any change |

## Concept

`/rpi-plan` turns research into an **evidence-based plan** with phases and tasks
(`P01-T01`, `P01-T02`…). It can also run an **independent critique** (`critique=standard|deep`),
where a separate review looks for gaps before any code is written. The artifacts are:

```text
.copilot-tracking/plans/{date}/{task-slug}-plan.md
.copilot-tracking/reviews/plans/{date}/{task-slug}-plan-critique.md
```

## Gorman problem it solves

Gorman's change policy says *every change needs a reviewed plan*. The plan and critique
artifacts **are** that evidence, ready for an auditor or a change advisory board.

## Steps

1. Type `/clear`. The research artifact carries the context forward.
2. Run `/rpi-plan` with Prompt 4.1.
3. Read the plan **and** the critique. Answer any decisions it raises (Prompt 4.2).
4. Make sure the plan contains the tasks in the checklist below.
5. Commit the plan.

## A good plan for this task includes

- [ ] P01: canonical model (`ShiftRecord`, `OeeResult`, flags, validation error)
- [ ] P02: calculator per GMS-OPS-007 (formula, rounding, zero production, weighting)
- [ ] P03: three plant adapters, keeping today's export formats unchanged
- [ ] P04: CLI with exit codes and logging
- [ ] P05: tests, including the golden shift for **every** plant format, edge cases and validation
- [ ] Explicit out of scope: deleting legacy scripts, changing exports, real-time OEE
- [ ] Validation commands: `python3 -m unittest discover -s tests -t .`

## Check yourself

- [ ] Every task traces back to a research finding
- [ ] The critique found at least one improvement, and the plan was updated
- [ ] Still no code changed
