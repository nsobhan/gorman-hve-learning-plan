# Customer Demo: "Gorman Manufacturing standardizes with HVE Core"

A ready-to-run demo built on the fictional Gorman Manufacturing Company. Pick the
**30-minute** or **60-minute** track.

> **Principle to repeat throughout:** *"AI carries the rules, humans keep the judgment."*

## Before the demo (15 minutes, the day before)

- [ ] VS Code with Copilot signed in, and HVE Core installed through **one** route (see [Module 00](../00-setup/README.md))
- [ ] Two workspaces, both with Git baselines:

  ```bash
  demo/setup-demo-workspace.sh ~/gorman-live before
  ```

  ```bash
  demo/setup-demo-workspace.sh ~/gorman-backup full
  ```

  `~/gorman-live` is for live AI steps. `~/gorman-backup` holds the finished state, in case a
  live step is slow.
- [ ] Run each live prompt once in a scratch copy, so you know roughly what the output looks like
- [ ] Increase the font size, and close unrelated chats and notifications
- [ ] Open [the problem statement](../gorman-sample-project/docs/problem-statement.md) in a tab

## 30-minute track

| Min | Scene | What you do | What you say |
|-----|-------|-------------|--------------|
| 0–4 | **The problem** | In `~/gorman-live`, run the three plant scripts ([Module 00](../00-setup/README.md) step 3) | "Same shift, three plants, three answers: 69.6, 81.2, and a crash after 81.2. The standard says 77.2. This is a governance problem, not a coding problem." |
| 4–9 | **AI carries the rules** | Run [Prompt 1.1](../01-copilot-instructions/prompts.md) (before). Then `cp -R ~/gorman-backup/.github ~/gorman-live/`, reload, start a new chat, and run Prompt 1.1 again | "Same question, a Gorman-shaped answer. The standards live in the repo, not in people's heads." |
| 9–19 | **RPI: research before code** | `/rpi-research` with [Prompt 3.1](../03-rpi-research/prompts.md). While it runs, explain the four phases. Open the research artifact and highlight the bug table. | "When AI knows it isn't allowed to implement, it stops writing plausible code and starts finding verified facts. The artifact is the evidence your change board and auditors want." |
| 19–25 | **One answer** | Switch to `~/gorman-backup` and run `python3 -m unittest discover -s tests -t . -v`, then the CLI for MTY and OSR | "77.2 from all four formats. Monterrey's zero-production shift no longer crashes. Ostrava, a new plant with a JSON export, was onboarded with one adapter and one test." |
| 25–30 | **Humans keep the judgment** | Select **Gorman KPI Steward** and run [Prompt 14.2](../14-custom-agents/prompts.md) | "Changing an ideal cycle time is a business decision. Gorman's own agent blocks a change that would have cut Line 3's OEE by 16 points, and leaves the decision to a person." |

**Close:** Show the 90-day rollout table in [Module 17](../17-team-adoption/README.md), then ask:
*"Which of your KPIs or engineering standards is calculated three different ways today?"*

## 60-minute track

Run the 30-minute track, then add:

| Min | Scene | Module |
|-----|-------|--------|
| 30–38 | `/rpi-plan` with critique: show the plan and the critique findings | [04](../04-rpi-plan/prompts.md) |
| 38–46 | **Security Reviewer** finds the planted secrets and SQL injection (audit GA-2026-14) | [09](../09-security-review/prompts.md) |
| 46–54 | **Root cause analysis** of INC-2026-311: the crew hypothesis is rejected, and the cause is CHG-1182 | [12](../12-root-cause-analysis/prompts.md) |
| 54–60 | `/gorman-shift-report plant=MTY`, then Q&A | [13](../13-custom-skills/prompts.md) |

## Audience variants

| Audience | Lead with | Spend less time on |
|----------|-----------|--------------------|
| Plant and operations leaders | The problem (scene 1), RCA (Module 12), KPI Steward | The internals of instruction files |
| Engineering managers | RPI phases and artifacts, code review, rollout metrics | ISA-95 |
| Security and compliance | Audit trail (Prompt 6.4), Security Reviewer, Security Planner | The shift report |
| OT and network architects | ISA-95 Planner (Module 16), Security Planner STRIDE | The CLI |

## Likely questions

| Question | Answer |
|----------|--------|
| "Is this a product we depend on?" | HVE Core is an opinionated, fast-moving framework from Microsoft. Treat it as a source of patterns. HVE Builder helps you adapt those patterns into an SDLC **you** own (Module 15). |
| "Does the AI change our KPIs on its own?" | No. Stop-and-ask rules (Module 01), plan approval (Module 04) and the KPI Steward (Module 14) keep KPI changes as human decisions. Automatic mode still stops for destructive or externally visible actions. |
| "What does it need?" | VS Code or Copilot CLI, a GitHub Copilot subscription, and the `hve-core` plugin. Instructions, skills and agents are plain markdown files in your repo. |
| "How do we roll it out?" | Instructions first, then skills, then agents, one pilot plant at a time (Module 17). |
| "Is the data real?" | No. Gorman, its plants, its data and its credentials are all fictional. |

## If something goes wrong live

- **A slow or odd AI answer:** "This is why the artifact matters. Let me show you the one from the rehearsal." Switch to `~/gorman-backup`.
- **An agent is missing from the picker:** Run **Developer: Reload Window**, then start a new chat.
- **Reset the live workspace:** Run `git -C ~/gorman-live checkout . && git -C ~/gorman-live clean -fd`.
