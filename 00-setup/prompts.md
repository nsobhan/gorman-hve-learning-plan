# Module 00 — Self-learning prompts

Paste these into Copilot Chat inside your `~/gorman-mes` workspace. Run them in order.

## Prompt 0.1 — Orientation (default agent, read-only)

```text
Explain what this repository does for Gorman Manufacturing. List the three plant OEE
scripts under plants/ and, for each one, summarize the formula it uses, the units it
expects and how it handles a shift with zero production. Compare each against
docs/oee-standard.md. Do not change any files.
```

**What to look for:** Copilot should spot that Detroit divides performance by planned time,
Monterrey leaves out quality, and Pune rounds each factor before multiplying.

## Prompt 0.2 — Learn what HVE gives you

```text
Which HVE Core agents and skills are available in this session? Group them into
lifecycle (research, plan, implement, review), quality and security, planning and
requirements, and customization (building our own instructions, skills and agents).
For each group, give one way Gorman Manufacturing could use it to standardize plant
KPI tooling.
```

## Prompt 0.3 — Explain the core principle in your own context

```text
HVE Core's principle is "AI carries the rules, humans keep the judgment." Using
docs/problem-statement.md, list which Gorman rules the AI should carry (formulas,
conventions, security policy) and which decisions must stay with Gorman engineers
and managers. Put the answer in a two-column table.
```

## Reflection

- Which of the six pain points in `docs/problem-statement.md` costs Gorman the most?
- Which decisions from Prompt 0.3 would you never hand to an AI, and why?
