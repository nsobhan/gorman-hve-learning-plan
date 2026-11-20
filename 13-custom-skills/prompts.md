# Module 13 — Self-learning prompts

## Prompt 13.1 — A slash command skill

```text
Use hve-builder with mode=create,
targets=.github/skills/gorman/gorman-shift-report/SKILL.md, and
requirements="A user-invocable slash command named gorman-shift-report that produces
Gorman's weekly shift OEE report. Inputs: plant (DET, MTY, PNQ or OSR, required) and
file (optional, default from the plant-data instructions). Steps: run
python3 -m gorman_oee.cli --plant <plant> <file>; never calculate OEE in chat; build a
markdown report with a header (plant, date range), a table per line (date, shift, OEE,
flags), the weighted plant OEE, and a 'needs attention' list (NO_PRODUCTION,
PERF_OVER_100, any shift below 65%). Save to reports/{plant}-{YYYY-MM-DD}-shift-report.md.
Don't email or publish the report."
```

## Prompt 13.2 — A knowledge skill

```text
Use hve-builder with mode=create,
targets=.github/skills/gorman/gorman-oee-standard/SKILL.md, and
requirements="A knowledge skill for GMS-OPS-007 that agents load when they review or
explain OEE numbers. The body summarizes the formulas, rules and flags, and how to
decompose an OEE change into availability, performance and quality. Put the golden
shift for each plant format in references/golden-shifts.md. The description should
match phrases like 'why did OEE change', 'check this OEE number', and 'explain OEE'."
```

## Prompt 13.3 — Use your skill

```text
/gorman-shift-report plant=MTY
```

Then try the knowledge skill without naming it:

```text
Why is Monterrey's weighted plant OEE so much lower than Detroit's this week?
```

**Expected:** Copilot loads `gorman-oee-standard` and points to the NO_PRODUCTION shift (MTY L2 B)
pulling down the weighted average.

## Prompt 13.4 — Review the skills

```text
Use hve-builder with mode=review and targets=.github/skills/gorman/.
Check description quality for activation, progressive loading (body vs references),
and whether any rule duplicates .github/instructions/gorman/.
```

## Reflection

- Which content did you move from instructions into the skill's `references/`, and why?
- What other Monday-morning task at a plant could become a skill?
