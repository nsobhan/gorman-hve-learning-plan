# Gorman Manufacturing — Copilot Baseline

Plant KPI tooling for Gorman Manufacturing Company (Detroit, Monterrey, Pune).
This repository calculates shift-level OEE and is moving from three plant scripts to one shared library.

## Priority Rules

1. The OEE standard `docs/oee-standard.md` (GMS-OPS-007) is the source of truth for every KPI calculation.
2. Plant export formats must not change this quarter. Adapt to them; don't ask plants to change them.
3. Python 3.11+ and the standard library only. Plant PCs can't install third-party packages.
4. Conventions in `gorman_oee/` take precedence over anything in `plants/` (legacy, being retired).

## Project Structure

- `gorman_oee/`: shared library (model, calculator, plant adapters, CLI)
- `plants/`: legacy per-plant scripts. Read-only reference unless a task says to retire them.
- `data/`: sample plant exports and incident data. Never contains real production data.
- `docs/`: standards, problem statement, change log, decisions (`docs/decisions/`)
- `tests/`: `unittest` tests. Run with `python3 -m unittest discover -s tests -t .`

## Guardrails

- Never put credentials, tokens or connection strings in code. Read them from environment variables.
- Use only parameterized SQL. Never build SQL by string concatenation.
- Use the `logging` module, not `print`, except for CLI result output.
- Use English identifiers, docstrings and log messages.
- Every behavior change comes with a test. Every KPI change must keep the golden-shift test (77.2%) passing.
- Round only the final OEE value. Never round intermediate factors.

## Stop and Ask a Human

Stop and ask for confirmation before you:

- Change an OEE formula, a validation rule or a rounding rule
- Change an ideal cycle time or other master data (this needs a CHG ticket in `docs/change-log.md`)
- Change anything that alters numbers already reported to the COO
- Delete legacy scripts under `plants/`
