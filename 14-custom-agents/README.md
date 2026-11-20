# Module 14 — Custom Agents: the Gorman KPI Steward

| | |
|---|---|
| **Time** | 45 minutes |
| **HVE usage** | `.github/agents/{package}/*.agent.md`: frontmatter (`tools`, `skills`, `disable-model-invocation`), protocol body, subagents |
| **Gorman outcome** | A **KPI Steward** agent that any plant engineer can select to review a proposed KPI or master-data change before it ships |

## Concept

An agent is a role with **tools**, **preloaded skills** and a **protocol**. Key frontmatter:

| Field | Purpose |
|-------|---------|
| `name`, `description` | What shows in the picker. The only required fields. |
| `tools` | What the agent can do (`read`, `search`, `edit`, `execute`, `skill`, `agent`, `ask_user`…) |
| `skills` | Skills injected at session start |
| `disable-model-invocation` | `true` means only a person can pick it. Other agents can't start it on their own. |

The Copilot harness **doesn't load `#file:` directives**. Agents reach skills by name and read
instruction files by name.

## Gorman problem it solves

Changing an OEE rule or an ideal cycle time is a **business decision**, as INC-2026-311 showed.
The KPI Steward runs the same checklist every time: is there a CHG ticket, what's the impact on
reported numbers, do the golden-shift tests still pass, and is a sign-off needed?

## Steps

1. Create the agent with `hve-builder` (Prompt 14.1). Compare it with
   [solution/.github/agents/gorman/kpi-steward.agent.md](solution/.github/agents/gorman/kpi-steward.agent.md).
2. Reload the window and select **Gorman KPI Steward** in the picker.
3. Give it the bad change from INC-2026-311 (Prompt 14.2). It should block the change.
4. Give it a good change (Prompt 14.3). It should approve the change, with conditions.

## Check yourself

- [ ] The agent preloads `gorman-oee-standard` and has no `edit` tool (it's read-only by design)
- [ ] It refuses to approve a change without a CHG ticket
- [ ] Its output always ends in a decision the person makes: **Approve / Approve with conditions / Block**
