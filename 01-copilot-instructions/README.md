# Module 01 — Repository-wide Baseline: `copilot-instructions.md`

| | |
|---|---|
| **Time** | 30 minutes |
| **HVE usage** | `.github/copilot-instructions.md` (always loaded), with `hve-builder` to author it |
| **Gorman outcome** | Every Copilot session in the Gorman repo knows the company's priorities and guardrails |

## Concept

`.github/copilot-instructions.md` is loaded for **every** Copilot interaction in the repo.
It's the baseline that every agent, skill and instruction file builds on. HVE Core's
guidance is to **start small**: a few precise rules work better than a long manifesto.

Copilot merges guidance from four tiers: your user settings, then the agent or skill in use,
then instruction files whose `applyTo` matches, then `copilot-instructions.md`, which is always loaded.

## Gorman problem it solves

Today each plant team has its own unwritten rules. Detroit uses `print`, Monterrey writes Spanish
docstrings, and Pune stores tokens in code. One baseline file gives every engineer, and every AI
session, the same starting rules.

## Steps

1. **Before:** Without any instructions, ask Copilot (Prompt 1.1) to add a scrap-rate function to
   the Pune script. Save the answer.
2. Use `hve-builder` (Prompt 1.2) to create `.github/copilot-instructions.md` from
   `docs/problem-statement.md` and `docs/oee-standard.md`.
3. Review the draft yourself. Remove anything you wouldn't enforce in a code review.
4. **After:** Start a new chat and repeat Prompt 1.1. Compare the two answers.
5. Commit: `git add .github && git commit -m "Add Gorman Copilot baseline"`.

A reference version is in [solution/.github/copilot-instructions.md](solution/.github/copilot-instructions.md).

## Check yourself

- [ ] The file is under about 60 lines and every rule can be checked
- [ ] The "after" answer uses logging rather than `print`, has no hard-coded secrets, and points to the OEE standard
- [ ] You can explain why domain formulas belong in a scoped instruction file or a skill (Modules 02 and 13), not here

## Demo tip

Show the before and after answers side by side. This is the quickest "aha" moment for
customers: *the same question gets a Gorman-shaped answer.*
