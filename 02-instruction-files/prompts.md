# Module 02 — Self-learning prompts

## Prompt 2.1 — Python conventions

```text
Use hve-builder with mode=create,
targets=.github/instructions/gorman/gorman-python.instructions.md, and
requirements="applyTo '**/*.py'. Gorman Python conventions on top of HVE Core's
python-script instructions: Python 3.11+, standard library only (plant PCs can't
install packages, so do NOT require uv or pip); a main() that returns exit codes
EXIT_SUCCESS=0, EXIT_FAILURE=1, EXIT_ERROR=2; the logging module instead of print except
for CLI result lines; type hints on public functions; secrets only from environment variables;
parameterized SQL only; unittest tests under tests/ named test_*.py. Use the
existing HVE Core python-script.instructions.md as a structural reference and do not
duplicate rules already in .github/copilot-instructions.md."
```

## Prompt 2.2 — KPI rules (the core of standardization)

```text
Use hve-builder with mode=create,
targets=.github/instructions/gorman/gorman-kpi.instructions.md, and
requirements="applyTo 'gorman_oee/**/*.py, plants/**/*.py'. Encode docs/oee-standard.md
(GMS-OPS-007 rev C) as rules an AI must follow when it writes or reviews KPI code: the four
formulas with units, full-precision calculation and rounding only the final OEE,
the NO_PRODUCTION and PERF_OVER_100 flags, the validation rejections, plant averages
weighted by planned time, and the golden-shift test (planned 480, downtime 47,
ideal 30 s, total 780, good 741 -> 77.2%). Include a short 'common mistakes found in
legacy plant scripts' list."
```

## Prompt 2.3 — Plant data formats

```text
Use hve-builder with mode=create,
targets=.github/instructions/gorman/gorman-plant-data.instructions.md, and
requirements="applyTo 'data/**'. Describe each plant export format by reading the files
in data/: delimiter, header names, units, and the conversion to the canonical
ShiftRecord (minutes, seconds per part, total and good counts). State that sample data is
fictional and that real plant data must never be committed."
```

## Prompt 2.4 — Review the set for overlap

```text
Use hve-builder with mode=review and
targets=.github/copilot-instructions.md, .github/instructions/gorman/*.instructions.md.
Look for overlapping or conflicting rules, applyTo globs that are too broad, and rules
that belong in a skill instead because they are large reference material.
```

## Prompt 2.5 — Prove the scoping works

```text
Open plants/pune/calc_oee_v2.py and tell me which instruction files are applied to it
and why. Then, without saving, show how you would fix the oee() function so it
follows Gorman rules.
```

**Expected:** It names `gorman-python` and `gorman-kpi` and removes the per-factor `round()` calls.

## Reflection

- Why is `data/**` a better glob than `**/*.csv` for plant data rules?
- Which rule would you move into a skill once it grows past one screen?
