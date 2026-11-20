# Module 07 — RPI Agent: Full Lifecycle in One Session

| | |
|---|---|
| **Time** | 45 minutes |
| **HVE usage** | **RPI Agent** from the agent picker (or `/rpi`), manual and automatic modes, follow-up choices, RPI Workflow canvas |
| **Gorman outcome** | A fourth plant (Ostrava, Czech Republic, code `OSR`) onboarded to the standard library in one guided session |

## Concept

Modules 03 to 06 ran each phase separately so you could see each responsibility. **RPI Agent**
wraps the whole lifecycle: Research readiness → Plan → Implement → Review → Follow-up.

- **Research readiness:** It researches only when there's a real gap. Evidence that already exists is reused.
- **Modes:** It asks how you want to work: end to end, end to end with check-ins on unclear decisions,
  research and plan with you and stop before implementing, or phase by phase. Asking for
  "full auto" starts an automatic session without that question.
- **Guardrails:** Even in automatic mode, it stops for blockers, required human review, and
  destructive or externally visible actions.
- **Canvas:** When your host supports canvases, the RPI Workflow canvas shows each phase beside the chat.

## Gorman scenario

Gorman acquired a plant in **Ostrava**. Its MES exports **JSON**, not CSV
([starter/ostrava_shift_export.json](starter/ostrava_shift_export.json)):

- Planned time is in **hours**, and the ideal cycle is in **minutes**
- Downtime is a **list of stops** that must be summed
- Counts are `total`, `scrap` and `rework`. **Is rework "good"?** GMS-OPS-007 says *good = first-pass
  quality*, so it isn't. This is a decision the agent should surface, not guess.

Golden shift check: L1 A should give **77.2%** (47 minutes of stops, and good = 780 − 25 − 14 = 741).

## Steps

1. Copy the starter file: `cp starter/ostrava_shift_export.json ~/gorman-mes/data/`
2. In Copilot Chat, select **RPI Agent** from the agent picker.
3. Paste Prompt 7.1. When it asks how to work, choose **"keep going but check with me on unclear decisions."**
4. When it asks about rework, answer using the standard ("first-pass good only").
5. At the end, look at the ranked follow-up choices, then stop the session.
6. Run the tests and the CLI with `--plant OSR`.

A reference result is in [solution/](solution/): `adapters.py` with `read_ostrava`, plus
`tests/test_ostrava.py`. Overlay it after the Module 05 solution.

## Check yourself

- [ ] `read_ostrava` exists, is registered as `OSR`, and the golden-shift test covers four formats
- [ ] The agent asked you about rework rather than assuming
- [ ] The research, plan, changes and review artifacts all share one task ID
