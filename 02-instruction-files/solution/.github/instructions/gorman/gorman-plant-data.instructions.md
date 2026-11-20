---
description: 'Gorman plant export formats and conversions to the canonical ShiftRecord'
applyTo: 'data/**'
---

# Gorman Plant Data Formats

All files in `data/` are **fictional samples**. Never commit real plant or production data.

| Plant | File pattern | Delimiter | Units | Conversion to ShiftRecord |
|-------|--------------|-----------|-------|---------------------------|
| DET Detroit | `detroit_*.csv` | `,` | minutes, seconds | `PlannedMin`, `DownMin`, `IdealCycleSec`, `TotalParts`, `GoodParts` map 1:1 |
| MTY Monterrey | `monterrey_*.csv` | `,` | hours, seconds | `horas_planeadas`×60, `horas_paro`×60, `ciclo_ideal_seg`, `piezas_totales`, `piezas_buenas` |
| PNQ Pune | `pune_*.csv` | `;` | seconds, milliseconds | `planned_sec`/60, `downtime_sec`/60, `ideal_cycle_ms`/1000, `produced`, good = `produced` − `rejected` |

## Pune Shift Mapping

The shift letter comes from the UTC hour of `shift_start_utc`: 00 is A, 08 is B, 16 is C.

## Adding a New Plant

Add an adapter function and a sample file containing the golden shift, then register the plant code in `ADAPTERS`.
Don't change existing plant formats.
