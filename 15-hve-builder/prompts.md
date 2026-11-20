# Module 15 — Self-learning prompts

## Prompt 15.1 — Review the whole set

```text
Use hve-builder with mode=review and
targets=.github/copilot-instructions.md, .github/instructions/gorman/,
.github/skills/gorman/, .github/agents/gorman/.
Treat them as one system. Report overlap, conflicts, activation problems (descriptions
and applyTo), context cost, and missing stop-and-ask points.
```

## Prompt 15.2 — Refactor the overlap

```text
Use hve-builder with mode=refactor,
targets=.github/instructions/gorman/gorman-kpi.instructions.md,
.github/skills/gorman/gorman-oee-standard/, and
requirements="The formulas appear in both. Keep the short enforceable rules in the
instruction file, move explanation and reference material to the skill, and link
between them. Behavior must not change."
```

## Prompt 15.3 — Validate

```text
Use hve-builder with mode=validate and targets=.github/.
```

## Prompt 15.4 — Governance (you decide; the AI drafts)

```text
Draft a one-page docs/hve-governance.md for Gorman: who owns .github/ customizations
(a CODEOWNERS entry), how changes are proposed (PR with an hve-builder review attached),
how often we pull new patterns from microsoft/hve-core (quarterly), and how plants
request a new skill or agent. Mark every decision as PROPOSED for me to confirm.
```

## Prompt 15.5 — Adopt a pattern from upstream

```text
Use hve-builder with mode=create,
targets=.github/agents/gorman/plant-onboarding.agent.md, and
requirements="Adapt the patterns RPI Agent used in Module 07 into a Gorman-owned agent
that onboards a new plant: intake (export sample, units, golden shift), adapter,
golden-shift test, plant-data instructions update, and a KPI Steward review before merge."
```

## Reflection

- Which HVE Core components would Gorman copy into its own repo, and which would it keep consuming as a plugin?
