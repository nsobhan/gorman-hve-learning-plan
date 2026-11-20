# Module 11 — Self-learning prompts

## Prompt 11.1 — BRD (select **BRD Builder**)

```text
Create a Business Requirements Document for Gorman Manufacturing's "Plant KPI
Standardization Program." Use docs/problem-statement.md as the primary reference.
Sponsor: COO. Stakeholders: plant managers (DET, MTY, PNQ, and soon OSR), process
engineers, Corporate Operational Excellence, IT Security, Internal Audit.
Keep it solution-agnostic. Every requirement must link to a business objective.
```

## Prompt 11.2 — PRD (select **PRD Builder**)

```text
Create a PRD for "Gorman OEE Library v1," the product that delivers the BRD's KPI
consistency requirements. References: the BRD, docs/oee-standard.md,
docs/decisions/adr-0001-oee-shared-library.md. Users: plant process engineers (run and
extend it) and plant managers (read results). Include measurable acceptance criteria and
a non-goals section (real-time OEE, MES replacement).
```

To resume later: select **PRD Builder** and say `Resume the gorman-oee-library-v1 PRD session.`

## Prompt 11.3 — Plan the work items (select **Functional Planner**)

```text
Analyze the Gorman OEE Library v1 PRD and plan an Azure DevOps work-item hierarchy:
Epic -> Features -> User Stories, with acceptance criteria and a suggested order.
Include a feature per plant rollout (DET, MTY, PNQ, OSR) and one for retiring the
legacy scripts. Planning only; output the plan as markdown.
```

## Prompt 11.4 — Optional: create items in a SANDBOX tracker (select **Backlog Manager**)

```text
Using the Functional Planner output, create the epic and features in my sandbox
GitHub project <owner/repo>. Show me the full list and wait for my confirmation before
creating anything.
```

## Reflection

- Which BRD requirement surprised the plant managers you would demo this to?
- Why does HVE keep the planning agent separate from the agent that writes to trackers?
