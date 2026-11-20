# Module 14 — Self-learning prompts

## Prompt 14.1 — Build the agent

```text
Use hve-builder with mode=create,
targets=.github/agents/gorman/kpi-steward.agent.md, and
requirements="A user-selectable agent named 'Gorman KPI Steward' that reviews proposed
changes to KPI calculations or master data (ideal cycle times, shift calendars) before
they ship. Tools: read, search, execute (only to run the unittest suite and the
gorman_oee CLI), skill, ask_user. No edit tool. Preload the gorman-oee-standard skill.
disable-model-invocation: true. Protocol: 1) restate the change; 2) require a CHG ticket
in docs/change-log.md, or ask for one; 3) quantify the impact on reported OEE by running
the CLI before and after, if a branch is given; 4) check golden-shift tests; 5) list who
must sign off (Corporate OpEx for formula changes, Tooling engineering for ideal cycle);
6) recommend Approve, Approve with conditions, or Block, with reasons. The human decides."
```

## Prompt 14.2 — A change that should be blocked (select **Gorman KPI Steward**)

```text
Tooling engineering wants to set Detroit Line 3 ideal cycle time to 24 s today (die
spec DS-88). The new die arrives next month. Please review.
```

**Expected:** Block, or Approve with the condition "effective only when the die is installed."
It should cite INC-2026-311 and the roughly 16-point OEE impact.

## Prompt 14.3 — A change that should be approved with conditions

```text
Corporate OpEx proposes GMS-OPS-007 rev D: count rework as good if it passes
re-inspection on the same shift. Ticket CHG-1201. Review the impact on Ostrava,
the only plant that reports rework separately.
```

## Prompt 14.4 — Improve the agent from what you saw

```text
Use hve-builder with mode=improve, targets=.github/agents/gorman/kpi-steward.agent.md,
and requirements="In my last two sessions it <describe the weakness>. Fix the protocol
so this doesn't happen again, without adding new tools."
```

## Reflection

- Why is having no `edit` tool a feature for this role?
- What would a Gorman **Plant Onboarding** agent's protocol look like? (Hint: Module 07.)
