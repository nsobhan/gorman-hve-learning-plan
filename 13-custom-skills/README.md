# Module 13 — Custom Skills: Gorman Slash Commands and Knowledge Packages

| | |
|---|---|
| **Time** | 45 minutes |
| **HVE usage** | `.github/skills/{package}/{skill}/SKILL.md`, `references/`, `scripts/`, slash commands, `hve-builder` |
| **Gorman outcome** | `/gorman-shift-report` for any engineer, and a `gorman-oee-standard` knowledge skill that agents load on demand |

## Concept

| Artifact | Loads when… | Best for |
|----------|-------------|----------|
| Instructions (Module 02) | A file matching `applyTo` is read or edited | Short, always-relevant rules |
| **Skill** | Someone types `/name`, the description matches the task, or an agent preloads it | Reusable workflows and larger reference material |
| Agent (Module 14) | A user picks it, or a parent agent starts it | A multi-turn role with tools and a protocol |

The Copilot harness **doesn't load `.prompt.md` files**. HVE Core builds every reusable slash
command as a **skill**. Skills are loaded progressively: Copilot reads the metadata first, then the
body, then linked files only when needed. This keeps context small.

```text
.github/skills/gorman/
├── gorman-shift-report/
│   └── SKILL.md                 # slash command: /gorman-shift-report
└── gorman-oee-standard/
    ├── SKILL.md                 # knowledge package
    └── references/
        └── golden-shifts.md
```

Reference versions are in [solution/.github/skills/gorman/](solution/.github/skills/gorman/).

## Gorman problem it solves

Every Monday each plant engineer builds the weekly shift report by hand, in a different layout.
One skill gives the same report, in the same format, for every plant.

## Steps

1. Create `/gorman-shift-report` with `hve-builder` (Prompt 13.1).
2. Create the `gorman-oee-standard` knowledge skill (Prompt 13.2).
3. Reload the window, type `/`, and run `/gorman-shift-report plant=MTY` (Prompt 13.3).
4. Review both with `hve-builder` (Prompt 13.4).

## Check yourself

- [ ] `/gorman-shift-report` appears in the slash menu
- [ ] The report uses the library CLI (it doesn't recalculate OEE in chat), and flags `NO_PRODUCTION` shifts
- [ ] The skill's `description` uses the words engineers actually type ("shift report", "weekly OEE")
