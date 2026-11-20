# Module 04 — Self-learning prompts

> Type `/clear` first. Then type `/rpi-plan` and paste the prompt.

## Prompt 4.1 — Create the plan with critique

```text
task=oee-standardization research=<path to your research artifact> critique=standard

Create an implementation plan for a shared Python package gorman_oee/ that replaces the
legacy plant OEE calculations:
* gorman_oee/model.py: ShiftRecord (frozen dataclass, canonical units, validation),
  OeeResult (full-precision factors, flags, oee_percent rounded once), OeeFlag,
  InvalidShiftRecordError
* gorman_oee/calculator.py: calculate_shift() and weighted_plant_oee() per GMS-OPS-007
* gorman_oee/adapters.py: read_detroit, read_monterrey, read_pune, plus an ADAPTERS registry
* gorman_oee/cli.py: python3 -m gorman_oee.cli --plant DET|MTY|PNQ <file>
* tests/test_oee.py: unittest, including the golden shift (77.2%) for every plant format

Constraints: Python 3.11+ stdlib only; don't modify plants/ or data/; follow
.github/copilot-instructions.md and .github/instructions/gorman/*.
Include validation steps and an explicit out-of-scope list.
```

## Prompt 4.2 — Resolve a decision the plan raises

```text
/rpi-plan task=oee-standardization
decisions="Plant OEE is weighted by planned minutes (GMS-OPS-007 rule 5).
Pune shift letters map from UTC start hour 00/08/16 to A/B/C.
Legacy scripts stay in plants/ until all three plants sign off (separate change)."
Update the plan and record these decisions with their source.
```

## Prompt 4.3 — Deep critique for a high-risk change

```text
/rpi-plan task=oee-standardization critique=deep
Critique the current plan for risks to reported KPIs: anything that could change a
number already reported to the COO without being flagged, and any missing test.
```

## Reflection

- Which critique finding would have caused a production incident if you had skipped it?
- How would you show this plan to Gorman's change advisory board?
