# Module 02 — Scoped Standards: `.instructions.md` with `applyTo`

| | |
|---|---|
| **Time** | 45 minutes |
| **HVE usage** | `.github/instructions/**/*.instructions.md`, `applyTo` globs, `hve-builder` create/review/refactor |
| **Gorman outcome** | Python and KPI rules apply automatically whenever anyone, or any agent, touches matching files |

## Concept

Instruction files carry **scoped** guidance. Each one declares an `applyTo` glob, and Copilot
applies it when a matching file is read or edited. HVE Core recommends starting adoption
here ("Phase 1: Instructions"). Two or three well-targeted files pay off right away.

Always give a file an `applyTo` pattern. A file without one loads into every session.

```yaml
---
description: "Gorman KPI calculation rules (GMS-OPS-007)"
applyTo: 'gorman_oee/**/*.py, plants/**/*.py'
---
```

HVE Core already ships language standards, such as `coding-standards/python-script.instructions.md`.
Gorman adds only what is specific to Gorman.

## Gorman problem it solves

The OEE standard exists as a document, but no one reads it while writing code. Instruction
files put the standard right next to the code: any edit to a KPI file loads the rules.

## Files you will create

| File | `applyTo` | Carries |
|------|-----------|---------|
| `.github/instructions/gorman/gorman-python.instructions.md` | `**/*.py` | Gorman-specific Python conventions (logging, exit codes, no secrets, unittest) |
| `.github/instructions/gorman/gorman-kpi.instructions.md` | `gorman_oee/**/*.py, plants/**/*.py` | The OEE formula, rounding, validation and flag rules |
| `.github/instructions/gorman/gorman-plant-data.instructions.md` | `data/**` | Plant export formats and the unit conversions per plant |

Reference versions are in [solution/.github/instructions/gorman/](solution/.github/instructions/gorman/).

## Steps

1. Create the three files with `hve-builder` (Prompts 2.1 to 2.3).
2. Review them (Prompt 2.4) and fix anything that overlaps `copilot-instructions.md`.
3. Prove scoping works (Prompt 2.5): edit a Python file and confirm the KPI rules were applied.
4. Commit.

## Check yourself

- [ ] Each file has `description` and a narrow `applyTo`
- [ ] No rule appears in two places (baseline and instruction file)
- [ ] When asked to edit `plants/pune/calc_oee_v2.py`, Copilot mentions that rounding intermediate factors breaks rule 1
