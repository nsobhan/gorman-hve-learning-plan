# Gorman Manufacturing — Plant OEE Tooling (sample project)

> Fictional company and data, built only for learning and demoing
> [microsoft/hve-core](https://github.com/microsoft/hve-core). Every credential in this
> repo is **fake** and is there on purpose so the security modules have something to find.

## The company

**Gorman Manufacturing Company** makes stamped and machined metal brackets for the
automotive and HVAC industries. It runs three plants:

| Plant     | Code | Team that owns the OEE script | Language of comments | Data export format            |
|-----------|------|-------------------------------|----------------------|-------------------------------|
| Detroit   | DET  | Plant IT (1 contractor, 2019) | English              | CSV, minutes                  |
| Monterrey | MTY  | Process engineering           | Spanish              | CSV, hours, Spanish headers   |
| Pune      | PNQ  | Dashboard team                | English              | Semicolon CSV, seconds and ms |

## The problem: same shift, three different answers

Every plant calculates **OEE (Overall Equipment Effectiveness)** for its weekly report to
the COO. Each plant wrote its own script, and they don't agree.

Run the same physical shift (Line 1, shift A, 2026-11-02) through each plant's code:

```bash
python3 plants/detroit/oee_calc.py data/detroit_shift_log.csv        # L1 A -> 69.6%
python3 plants/monterrey/oee.py data/monterrey_registro_turnos.csv   # L1 A -> 81.2%, then crashes
python3 plants/pune/calc_oee_v2.py data/pune_shift_export.csv        # L1 A -> 72.9%
```

The correct OEE per the [Gorman OEE standard](docs/oee-standard.md) is **77.2%**.

| Symptom | Business impact |
|---------|-----------------|
| Three formulas for one KPI | The COO can't compare plants; plant bonuses are disputed |
| Detroit divides performance by planned time, not run time | Detroit under-reports by about 8 points |
| Monterrey leaves out quality and crashes on zero-production shifts | Monterrey over-reports, and the weekly job fails |
| Pune rounds each factor before multiplying | OEE results are off by up to 5 points |
| Hard-coded credentials and SQL built by string concatenation | Failed the 2026 IT audit (finding GA-2026-14) |
| No tests, no docs, no shared conventions | A new engineer needs about 3 weeks before making a safe change |

See [docs/problem-statement.md](docs/problem-statement.md) for the full brief.

## The goal (what HVE Core helps standardize)

1. **One OEE library** (`gorman_oee/`) with one formula, validation and tests.
2. **One adapter per plant** that converts each plant's export into a common `ShiftRecord`.
3. **Engineering standards that Copilot applies automatically** (`.github/` instructions,
   skills and agents), so every plant team and every AI session follows the same rules.
4. **Durable evidence** (research, plans, reviews, ADRs) under `.copilot-tracking/` and
   `docs/`, so decisions can be audited.

## Layout

```text
gorman-sample-project/
├── plants/            # Today's three non-standard scripts (the "before")
├── data/              # Sample exports, one format per plant, plus Line 3 incident data
└── docs/
    ├── problem-statement.md
    ├── oee-standard.md       # The agreed formula: the "rules" HVE will carry
    ├── change-log.md         # MES master-data changes (used in the RCA module)
    └── incident-line3.md     # Line 3 OEE drop (used in the RCA module)
```

The learning modules in `../` walk you through using HVE Core to turn this repo into the
standardized "after" state. A reference solution for each step is in the module's
`solution/` folder.
