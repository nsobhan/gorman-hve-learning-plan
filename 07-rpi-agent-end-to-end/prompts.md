# Module 07 — Self-learning prompts

> Select **RPI Agent** in the agent picker.

## Prompt 7.1 — Onboard Ostrava (guided)

```text
Task: onboard Gorman's new Ostrava plant (code OSR) to the gorman_oee library.
The export is data/ostrava_shift_export.json (JSON, planned time in hours, ideal cycle
in minutes, downtime as a list of stops, counts as total, scrap and rework).

Acceptance criteria:
* A read_ostrava adapter registered in ADAPTERS as "OSR"
* Conversion to canonical ShiftRecord units per .github/instructions/gorman/*
* The golden shift (L1, A, 2026-11-02) gives 77.2%, added to the existing
  every-plant-format test
* No changes to other plants' adapters, plants/ or existing data files
* The gorman-plant-data instructions updated with the OSR format

Reuse the existing oee-standardization research and plan where they are adequate.
Ask me about any decision that affects reported KPIs.
```

## Prompt 7.2 — Try automatic mode on a small task

```text
full auto
Task: add a --format csv option to gorman_oee/cli.py that prints
plant,line,date,shift,availability,performance,quality,oee_percent,flags
with full-precision factors. Include tests. Stop before anything that would change
existing output when --format isn't given.
```

## Prompt 7.3 — Manual mode, phase by phase

```text
Work phase by phase with me. Task: add a per-line weekly summary
(gorman_oee/summary.py) that groups OeeResults by plant and line and reports
weighted OEE. Start with research readiness and stop after each phase.
```

Then type `/rpi-plan`, `/rpi-implement` and `/rpi-review` yourself to move between phases.

## Reflection

- Which mode would you use for a KPI formula change? Which for a CLI flag? Why?
- Did the agent's research readiness skip research for Ostrava? Was that the right call?
