# Golden Shifts: Line 1, shift A, 2026-11-02, expected OEE 77.2%

The same physical shift, written in each plant's export format.

| Plant | Raw values | Canonical |
|-------|------------|-----------|
| DET | `PlannedMin=480, DownMin=47, IdealCycleSec=30, TotalParts=780, GoodParts=741` | 480 / 47 / 30 / 780 / 741 |
| MTY | `horas_planeadas=8.0, horas_paro=0.783333, ciclo_ideal_seg=30, piezas_totales=780, piezas_buenas=741` | 480 / 47 / 30 / 780 / 741 |
| PNQ | `planned_sec=28800; downtime_sec=2820; ideal_cycle_ms=30000; produced=780; rejected=39` | 480 / 47 / 30 / 780 / 741 |
| OSR | `plannedTime 8 h; stops 22+15+10 min; idealCycle 0.5 min; total 780, scrap 25, rework 14` | 480 / 47 / 30 / 780 / 741 |

Factors: A = 0.90208, P = 0.90069, Q = 0.95000, **OEE = 77.2%**

## Legacy Results (for comparison)

| Script | Reported | Cause |
|--------|----------|-------|
| `plants/detroit/oee_calc.py` | 69.6% | Performance divided by planned time |
| `plants/monterrey/oee.py` | 81.2% | No quality factor |
| `plants/pune/calc_oee_v2.py` | 72.9% | Factors rounded to 0.9 before multiplying |
