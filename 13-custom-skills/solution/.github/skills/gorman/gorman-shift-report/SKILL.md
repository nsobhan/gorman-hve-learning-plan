---
name: gorman-shift-report
description: "Generates Gorman Manufacturing's weekly shift OEE report for one plant (DET, MTY, PNQ, OSR) using the gorman_oee library. Use when someone asks for a shift report, weekly OEE report, or plant OEE summary."
argument-hint: "plant={DET|MTY|PNQ|OSR} [file=<export path>]"
user-invocable: true
---

# Gorman Shift Report

## Inputs

- `plant` (required): one of `DET`, `MTY`, `PNQ`, `OSR`
- `file` (optional). The defaults are:

| Plant | Default export |
|-------|----------------|
| DET | `data/detroit_shift_log.csv` |
| MTY | `data/monterrey_registro_turnos.csv` |
| PNQ | `data/pune_shift_export.csv` |
| OSR | `data/ostrava_shift_export.json` |

If `plant` is missing or invalid, ask for it. Don't guess.

## Steps

1. Run `python3 -m gorman_oee.cli --plant <plant> <file>` from the repository root.
2. If the exit code isn't 0, stop. Report the error lines and don't write a report.
3. **Never calculate or adjust OEE values in chat.** Use only the CLI output.
4. Write `reports/<plant>-<YYYY-MM-DD>-shift-report.md` using the template below. Use today's date.
5. Reply with the file path and the "Needs attention" list.

## Template

```markdown
# <Plant name> Shift OEE Report: <first date> to <last date>

Weighted plant OEE: **<value>%** (GMS-OPS-007, weighted by planned time)

## Line <line>

| Date | Shift | OEE | Flags |
|------|-------|-----|-------|

## Needs attention

- <shift key>: <reason: NO_PRODUCTION, PERF_OVER_100, or OEE below 65%>
```

## Boundaries

- Don't email, post or publish the report. A person shares it.
- Don't change library code or data files.
