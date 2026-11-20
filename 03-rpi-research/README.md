# Module 03 — RPI Phase 1: Research (`/rpi-research`)

| | |
|---|---|
| **Time** | 30 minutes |
| **HVE usage** | `/rpi-research` skill, research artifacts in `.copilot-tracking/research/`, `/clear` |
| **Gorman outcome** | An evidence-backed research document about how to standardize OEE across the three plants |

## Concept

RPI stands for **Research → Plan → Implement → Review**. The key idea: *AI can't tell
investigating from implementing.* When you ask for code, it writes plausible code. When it
**knows it must not implement**, it optimizes for verified truth instead.

`/rpi-research` writes a dated artifact:

```text
.copilot-tracking/research/{YYYY-MM-DD}/{task-slug}-research.md
```

**The artifact, not the chat reply, is the source of truth.** It carries verified context into the
next phase, so you can `/clear` the chat between phases without losing anything.

## Gorman problem it solves

No one at Gorman can say exactly *how* the three scripts differ, or which plant is "right."
Research produces that answer with evidence (file and line references), before anyone writes code.

## Steps

1. Start a new chat and type `/rpi-research`.
2. Paste Prompt 3.1.
3. Open the artifact it writes. Check the findings against the table below.
4. Challenge it (Prompt 3.3). If a finding is wrong, ask it to correct the artifact. Don't just correct the chat.
5. Commit the artifact: `git add .copilot-tracking && git commit -m "Research: OEE standardization"`.

## Findings a good research artifact should contain

| # | Finding | Evidence |
|---|---------|----------|
| 1 | Detroit's performance uses `planned * 60`, not run time | `plants/detroit/oee_calc.py`, `calcOEE` |
| 2 | Detroit averages shifts without weighting | `plants/detroit/oee_calc.py`, `main` |
| 3 | Monterrey has no quality factor | `plants/monterrey/oee.py`, `oee_turno` comment |
| 4 | Monterrey divides by zero when run time is 0 | `rendimiento`, plus the MTY L2 B row in the data |
| 5 | Pune rounds A, P and Q to 1 decimal before multiplying | `plants/pune/calc_oee_v2.py`, `oee` |
| 6 | Hard-coded credentials (DET, PNQ) and SQL concatenation (PNQ) | both scripts |
| 7 | Three export formats, so adapters are needed (exports can't change this quarter) | `data/`, problem statement |
| 8 | Recommended approach: shared library plus per-plant adapters plus golden-shift tests | synthesis |

## Check yourself

- [ ] The artifact exists under `.copilot-tracking/research/` and has a summary at the top
- [ ] At least 6 of the 8 findings above are present, with file references
- [ ] **No code was changed** (`git status` shows only `.copilot-tracking/`)
