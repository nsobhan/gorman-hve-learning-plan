# Module 08 — Code Review Agent

| | |
|---|---|
| **Time** | 30 minutes |
| **HVE usage** | **Code Review** agent and `/code-review` skill: functional by default, opt-in vectors (`security`, `performance`, `privacy`, `rai`, `sssc`), depth levels |
| **Gorman outcome** | A consistent review standard for every plant team, instead of "whoever is around" reviewing |

## Concept

The Code Review agent captures **one snapshot** (a PR, branch comparison, commit, local changes or
selected code) and reviews it for **functional** problems first. Non-functional review vectors are
**strictly opt-in**: `vectors=security,performance,privacy,rai,sssc`. Depth can be `basic`,
`standard` or `comprehensive`, and **posting to a PR needs your consent**.

## Gorman problem it solves

Each plant reviewed code differently, or not at all. That's how three different OEE formulas
shipped. One review agent, applying the same instructions from Module 02, gives every plant the
same review bar.

## Steps

1. **Review the legacy code** (Prompt 8.1). Compare the findings with the research from Module 03.
2. **Review a real change.** Create a branch, make a deliberately buggy change (Prompt 8.2), commit it,
   and review the branch against `main` (Prompt 8.3).
3. Add the security vector (Prompt 8.4) and compare the extra findings.

## Check yourself

- [ ] The legacy review flags all three formula bugs and the divide-by-zero
- [ ] The branch review catches the planted bug and cites the golden-shift rule
- [ ] Security findings appear only when you opt in to the `security` vector
