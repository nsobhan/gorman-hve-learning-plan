# Module 15 — HVE Builder: Maintain and Govern Your Own HVE Artifacts

| | |
|---|---|
| **Time** | 30 minutes |
| **HVE usage** | `/hve-builder` modes: `create`, `improve`, `refactor`, `replace`, `review`, `validate` |
| **Gorman outcome** | Gorman's `.github/` customizations reviewed as a set, cleaned up, and owned by Gorman |

## Concept

HVE Core is **highly opinionated and changes quickly**. Microsoft recommends treating it as a
*source of patterns*, not a stable dependency. **HVE Builder** is how you adapt those patterns
into an agentic SDLC that **you** own:

| Mode | Use it to… |
|------|------------|
| `create` | Write a new instruction, skill, agent or subagent |
| `improve` | Fix a known weakness while keeping intent |
| `refactor` | Consolidate overlapping artifacts without changing behavior |
| `replace` | Rewrite an artifact from scratch |
| `review` | Get a read-only quality report |
| `validate` | Check structure and frontmatter against conventions |

## Gorman problem it solves

By now Gorman has a baseline, three instruction files, two skills and an agent. Without
governance they'll drift, just like the plant scripts did. HVE Builder gives the customizations
the same review discipline as the code.

## Steps

1. Review the whole Gorman set (Prompt 15.1).
2. Refactor any overlap it finds (Prompt 15.2).
3. Validate everything (Prompt 15.3).
4. Decide on an owner and a review cadence (Prompt 15.4). That's a human decision.

## Check yourself

- [ ] No rule is defined in more than one artifact
- [ ] Every artifact has frontmatter that validates
- [ ] There's a named owner for `.github/` (for example, in `CODEOWNERS`)
