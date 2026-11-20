# HVE Core Learning Plan: The Gorman Manufacturing Case

A hands-on, self-paced course for [microsoft/hve-core](https://github.com/microsoft/hve-core)
(Hypervelocity Engineering), built around one realistic project. The same material works as
a **customer demo** ([demo/](demo/customer-demo-script.md)).

> **HVE Core in one line:** an agentic SDLC framework for GitHub Copilot that puts your standards,
> security rules and processes into agents, instructions and skills. In its own words: **"AI
> carries the rules, humans keep the judgment."**

## The story

**Gorman Manufacturing Company** (fictional) has three plants, Detroit, Monterrey and Pune, and
is acquiring a fourth in Ostrava. Each plant calculates OEE with its own script, so one shift
reports **69.6%, 81.2% and 72.9%** when the company standard says **77.2%**. The Monterrey job
crashes, there are hard-coded credentials, and nobody knows why the formulas differ.

You'll use HVE Core to **standardize** the work at three levels:

| Level | Before | After (with HVE Core) |
|-------|--------|------------------------|
| **The KPI** | 3 formulas | 1 tested library, with a golden-shift test for every plant format |
| **The engineering** | Each plant has its own habits | Shared instructions, skills and agents in `.github/` |
| **The process** | Change first, explain later | Research → Plan → Implement → Review, with evidence artifacts |

The full brief is in [gorman-sample-project/README.md](gorman-sample-project/README.md).

## Folder map

```text
hve-core/
├── README.md                     ← you are here (the learning plan)
├── gorman-sample-project/        ← the shared "before" repo every module uses
├── 00-setup/                     ← install HVE Core, reproduce the problem
├── 01-copilot-instructions/      ← repository-wide baseline
├── 02-instruction-files/         ← scoped standards with applyTo
├── 03-rpi-research/              ← /rpi-research
├── 04-rpi-plan/                  ← /rpi-plan + critique
├── 05-rpi-implement/             ← /rpi-implement (reference library in solution/)
├── 06-rpi-review/                ← /rpi-review + follow-up routing
├── 07-rpi-agent-end-to-end/      ← RPI Agent: onboard the Ostrava plant
├── 08-code-review/               ← Code Review agent
├── 09-security-review/           ← Security Reviewer + Security Planner
├── 10-architecture-and-docs/     ← ADR Creation, Architecture Reviewer, Documentation
├── 11-requirements-and-backlog/  ← BRD, PRD, Functional Planner, Backlog Manager
├── 12-root-cause-analysis/       ← root-cause-analysis skill on a plant incident
├── 13-custom-skills/             ← build Gorman slash commands and knowledge skills
├── 14-custom-agents/             ← build the Gorman KPI Steward agent
├── 15-hve-builder/               ← review, refactor and govern your own artifacts
├── 16-isa95-network-planning/    ← Network ISA-95 Planner (plant edge to Azure)
├── 17-team-adoption/             ← roll HVE out across plants, with metrics
└── demo/                         ← customer demo script + workspace setup script
```

Every module folder contains:

- **`README.md`**: the concept, the Gorman problem it solves, the steps, and a "check yourself" list
- **`prompts.md`**: copy-paste self-learning prompts, each with what to look for
- **`solution/`** (where it applies): reference files laid out as they sit in the project root

## Learning paths

| Path | Who | Modules | Time |
|------|-----|---------|------|
| **Core** (start here) | Everyone | 00 → 06 | ~4 h |
| **Practitioner** | Engineers on plant teams | Core + 07, 08, 09, 12 | ~7 h |
| **Builder** | Tech leads, platform team | Core + 13, 14, 15 | ~6 h |
| **Planner** | Architects, PMs, OT and security | 00, 03, 09, 10, 11, 16 | ~5 h |
| **Leader** | Managers rolling out HVE | 00, 01, 07, 17 + demo | ~2.5 h |

## Suggested 5-day schedule (about 1.5–2 hours a day)

| Day | Modules | Milestone |
|-----|---------|-----------|
| 1 | 00, 01, 02 | Gorman standards apply automatically in Copilot |
| 2 | 03, 04, 05 | The shared library passes the golden-shift test (77.2%) for every plant |
| 3 | 06, 07, 08 | A reviewed change, and Ostrava onboarded with RPI Agent |
| 4 | 09, 12, 10 | Audit finding closed, incident explained, decision recorded |
| 5 | 13, 14, 15, 17 (+ 11, 16 optional) | Gorman's own skills and agent, and a rollout plan |

## Module catalog

| # | Module | HVE usage | Time | Level |
|---|--------|-----------|------|-------|
| 00 | [Setup](00-setup/README.md) | Plugin install, agent picker, slash commands | 30 m | Beginner |
| 01 | [Copilot instructions](01-copilot-instructions/README.md) | `copilot-instructions.md`, `hve-builder` | 30 m | Beginner |
| 02 | [Instruction files](02-instruction-files/README.md) | `*.instructions.md`, `applyTo` | 45 m | Beginner |
| 03 | [RPI Research](03-rpi-research/README.md) | `/rpi-research`, `/rpi-challenger`, `/rpi-walkthrough` | 30 m | Beginner |
| 04 | [RPI Plan](04-rpi-plan/README.md) | `/rpi-plan`, critique | 30 m | Beginner |
| 05 | [RPI Implement](05-rpi-implement/README.md) | `/rpi-implement`, changes log | 45 m | Beginner |
| 06 | [RPI Review](06-rpi-review/README.md) | `/rpi-review`, `/rpi-refine`, follow-up routing | 30 m | Beginner |
| 07 | [RPI Agent end-to-end](07-rpi-agent-end-to-end/README.md) | RPI Agent, manual and automatic modes | 45 m | Intermediate |
| 08 | [Code review](08-code-review/README.md) | Code Review agent, `/code-review` vectors | 30 m | Intermediate |
| 09 | [Security](09-security-review/README.md) | Security Reviewer, Security Planner (STRIDE) | 45 m | Intermediate |
| 10 | [Architecture and docs](10-architecture-and-docs/README.md) | ADR Creation, System Architecture Reviewer, Documentation | 45 m | Intermediate |
| 11 | [Requirements and backlog](11-requirements-and-backlog/README.md) | BRD Builder, PRD Builder, Functional Planner, Backlog Manager | 45 m | Intermediate |
| 12 | [Root cause analysis](12-root-cause-analysis/README.md) | `root-cause-analysis` skill | 30 m | Intermediate |
| 13 | [Custom skills](13-custom-skills/README.md) | `SKILL.md`, slash commands, references | 45 m | Advanced |
| 14 | [Custom agents](14-custom-agents/README.md) | `.agent.md`, tools, preloaded skills | 45 m | Advanced |
| 15 | [HVE Builder](15-hve-builder/README.md) | `hve-builder` create, improve, refactor, review, validate | 30 m | Advanced |
| 16 | [ISA-95 network planning](16-isa95-network-planning/README.md) | Network ISA-95 Planner | 45 m | Specialist |
| 17 | [Team adoption](17-team-adoption/README.md) | `settings.json`, `hve-core-installer`, phased rollout | 30 m | Leader |

## How to use the prompts

1. Work in **your own copy** of the sample project, not in this folder (see [Module 00](00-setup/README.md)):

   ```bash
   cp -R gorman-sample-project ~/gorman-mes
   ```

2. **Commit before each module.** `git diff` shows exactly what HVE did, and `git checkout .` undoes it.
3. When a prompt says "select X," pick that agent in the Copilot **agent picker**. When it starts with `/`, it's a skill.
   With the plugin, skills show a prefix (`/hve-core:rpi-research`).
4. Type **`/clear` between RPI phases.** The artifacts carry the context.
5. Fell behind? Copy a module's `solution/` folder into your workspace and continue.

## Verify the reference solution yourself

```bash
demo/setup-demo-workspace.sh ~/gorman-check full
```

```bash
cd ~/gorman-check && python3 -m unittest discover -s tests -t . -v
```

Expected: 10 tests pass, and the golden shift gives 77.2% for the DET, MTY, PNQ and OSR formats.

## Important notes

- **HVE Core changes quickly.** Agent names, skill arguments and artifact paths in this course match
  the repository as of November 2026. If something differs, the
  [official docs](https://microsoft.github.io/hve-core/) win.
- **Everything about Gorman is fictional**, including companies, people, data and credentials. The fake secrets are
  there on purpose, for the security modules.
- AI output varies. Use each module's **"check yourself"** list as the success criteria, not an exact match with the solution.
