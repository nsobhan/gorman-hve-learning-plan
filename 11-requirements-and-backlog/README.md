# Module 11 — Requirements and Backlog: BRD, PRD and Work Items

| | |
|---|---|
| **Time** | 45 minutes |
| **HVE usage** | **BRD Builder** (business requirements), **PRD Builder** (product requirements, with resumable sessions), **Functional Planner** (plans work-item hierarchies, never changes a tracker), **Backlog Manager** (Azure DevOps, GitHub, Jira) |
| **Gorman outcome** | The KPI Standardization Program goes from a problem statement to a BRD, a PRD and a ready backlog |

## Concept

```text
Problem statement ─► BRD Builder ─► PRD Builder ─► Functional Planner ─► Backlog Manager
   (why)              (business      (what the       (epics, features,     (creates items
                      objectives)    product does)   stories: plan only)   after you confirm)
```

- **BRD Builder** stays solution-agnostic and links every requirement to a business objective.
- **PRD Builder** asks iterative questions and saves session state in
  `.copilot-tracking/prd-sessions/`, so you can resume after a break.
- **Functional Planner** is *planning only*. It never changes a tracker.
- **Backlog Manager** writes to real trackers through MCP tools, so confirm before it creates anything.

## Gorman problem it solves

The COO's program lacked shared, traceable requirements. Every plant read the goal differently,
which is the same problem as the OEE formula, one level up.

## Steps

1. Select **BRD Builder** and run Prompt 11.1.
2. Select **PRD Builder** and run Prompt 11.2.
3. Select **Functional Planner** and run Prompt 11.3 (offline, no tracker needed).
4. Optional: if you have a sandbox Azure DevOps or GitHub project with MCP configured, use
   **Backlog Manager** (Prompt 11.4). Use a sandbox only.

## Check yourself

- [ ] Every BRD requirement traces to an outcome in `docs/problem-statement.md`
- [ ] The PRD has measurable acceptance criteria (golden shift 77.2%, 0 crashes, 0 secrets)
- [ ] The work-item plan has epics → features → stories, with acceptance criteria on each story
