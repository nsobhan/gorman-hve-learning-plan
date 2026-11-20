# Module 12 — Self-learning prompts

## Prompt 12.1 — Investigate

```text
/root-cause-analysis
Investigate incident INC-2026-311 described in docs/incident-line3.md: Detroit Line 3
OEE dropped from about 80% to about 64% from 2026-11-05. The plant manager believes the
new B-shift crew (rotated in 2026-11-04) is the cause.

Evidence: data/detroit_line3_weekly.csv, docs/change-log.md, docs/oee-standard.md,
and the gorman_oee library (python3 -m gorman_oee.cli --plant DET
data/detroit_line3_weekly.csv).

Form falsifiable hypotheses (include the crew hypothesis), test each against the
evidence, decompose OEE into availability, performance and quality per shift, and
state the verified cause or the evidence blocker. Recommend a control that stops this
class of problem from happening again. Do not change any files except the RCA report.
```

## Prompt 12.2 — Turn the RCA into a prevention control (select **RPI Agent**)

```text
Task: based on the INC-2026-311 RCA, add a safeguard to gorman_oee. When the ideal cycle time
for a plant and line changes between consecutive shifts in one export, log a warning
with both values and add an IDEAL_CYCLE_CHANGED flag to the later shift. This is a new
flag, so update docs/oee-standard.md only after asking me. Include tests using
data/detroit_line3_weekly.csv.
```

## Prompt 12.3 — Communicate the result

```text
Write a five-sentence message from the Director of Manufacturing Systems to the Detroit
plant manager explaining the INC-2026-311 finding. Be respectful: the plant manager's
hypothesis was reasonable. Do not send it; show it to me.
```

## Reflection

- What evidence made the crew hypothesis falsifiable?
- What would have happened if the plant had retrained the B-shift crew?
