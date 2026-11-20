# Module 17 — Team Adoption: Rolling HVE Out Across Gorman's Plants

| | |
|---|---|
| **Time** | 30 minutes |
| **HVE usage** | `.github/copilot/settings.json` (offer the plugin to the whole team), the `hve-core-installer` skill, phased adoption (instructions → skills → agents), optional Copilot OTel metrics |
| **Gorman outcome** | A 90-day rollout plan, with metrics, for four plant teams |

## Concept

**Offer the plugin to everyone who opens the repo.** Commit
[solution/.github/copilot/settings.json](solution/.github/copilot/settings.json):

```json
{
  "extraKnownMarketplaces": {
    "hve-core": { "source": { "source": "github", "repo": "microsoft/hve-core" } }
  },
  "enabledPlugins": { "hve-core@hve-core": true }
}
```

To **own** the HVE files instead (pinned and customized), ask an agent to use the
`hve-core-installer` skill to copy the components into your `.github/` folders.

**Pick one install route for the whole team.** Mixing routes makes agents appear twice.

### HVE Core's recommended phases

1. **Instructions:** cheapest, quickest payoff (Modules 01 and 02)
2. **Skills:** repeatable workflows (Module 13)
3. **Agents:** roles and protocols (Modules 07 and 14)

## Gorman rollout plan (90 days)

| Weeks | Scope | Plants | Exit criteria |
|-------|-------|--------|---------------|
| 1–2 | Baseline + 3 instruction files + `settings.json` | Detroit (pilot) | 3 engineers complete Modules 00–06; golden-shift test in CI |
| 3–4 | RPI for every KPI change; `/code-review` on every PR | Detroit, Monterrey | 100% of KPI PRs have plan and review artifacts |
| 5–8 | `/gorman-shift-report`, KPI Steward, security review | + Pune | GA-2026-14 closed; weekly report generated with the skill at all 3 plants |
| 9–12 | Ostrava onboarding with RPI Agent; HVE Builder governance | + Ostrava | Ostrava live in 5 days or less; `.github/` has an owner and a quarterly review |

## Measure it

| Metric | Baseline | 90-day target |
|--------|----------|---------------|
| OEE definitions in code | 3 | 1 |
| Weekly-job crashes per month | ~2 | 0 |
| Secrets in the repo | 2 | 0 |
| Time for a new engineer to ship a reviewed KPI change | ~3 weeks | ≤ 3 days |
| KPI changes with research, plan and review evidence | 0% | 100% |
| Time to onboard a new plant | (never done) | ≤ 5 days |

Optional: HVE Core's experimental `copilot-otel-metrics` skill can help you analyze Copilot usage telemetry.

## Steps

1. Run Prompt 17.1 to tailor the rollout plan to your organization.
2. Commit `settings.json` and check that a teammate's fresh clone gets the plugin offer.
3. Present the plan using the [customer demo script](../demo/customer-demo-script.md).
