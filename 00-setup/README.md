# Module 00 — Setup and Orientation

| | |
|---|---|
| **Time** | 30 minutes |
| **HVE usage** | Installing the `hve-core` plugin, the agent picker, slash-command skills |
| **Gorman outcome** | Your own copy of the Gorman repo, with the "three different OEE numbers" problem reproduced |

## Why this matters for Gorman

Before you standardize anything, everyone has to see the problem on their own machine.
This module also checks that HVE Core's agents and skills load, because every later
module depends on them.

## Prerequisites

- VS Code with the GitHub Copilot extension, signed in to an account with a Copilot subscription
- Git and Python 3.11 or later (`python3 --version`)
- The chat must use the **Copilot** harness (Copilot appears at the start of the chat title). HVE Core doesn't support VS Code's Local harness.

## Steps

### 1. Install HVE Core (choose one route only)

**VS Code:** Run **Chat: Open Customizations**, select **Browse**, add the `microsoft/hve-core`
marketplace through **Configure Marketplaces**, and install `hve-core`.

**GitHub Copilot CLI:**

```bash
copilot plugin marketplace add microsoft/hve-core
```

```bash
copilot plugin install hve-core@hve-core
```

> Use only one install route (plugin, Marketplace extension, or clone). If you use more than
> one, every agent appears twice in the picker.

### 2. Create your Gorman workspace

Run these from the `hve-core` learning folder:

```bash
cp -R gorman-sample-project ~/gorman-mes
```

```bash
cd ~/gorman-mes && git init && git add . && git commit -m "Baseline: Gorman plant OEE scripts (before HVE)"
```

```bash
code ~/gorman-mes
```

A Git baseline lets you `git diff` every change HVE makes and roll back any experiment
with `git checkout .`.

### 3. Reproduce the problem

```bash
python3 plants/detroit/oee_calc.py data/detroit_shift_log.csv
```

```bash
python3 plants/monterrey/oee.py data/monterrey_registro_turnos.csv
```

```bash
python3 plants/pune/calc_oee_v2.py data/pune_shift_export.csv
```

Write down the Line 1, shift A result from each plant. You should see **69.6%, 81.2% (followed by a
crash), and 72.9%**. The standard ([docs/oee-standard.md](../gorman-sample-project/docs/oee-standard.md)) says **77.2%**.

### 4. Check that HVE Core is loaded

1. Open Copilot Chat (`Ctrl+Alt+I` / `Cmd+Alt+I`).
2. Open the **agent picker** and confirm you can see **RPI Agent**, **Security Reviewer**, **ADR Creation** and **Code Review**.
3. Type `/` in the chat box and confirm the RPI skills are listed. With the plugin they appear with a prefix, such as
   `/hve-core:rpi-research`. In this course they're written without the prefix, as `/rpi-research`.

## Self-learning prompts

See [prompts.md](prompts.md).

## Check yourself

- [ ] `git log` shows the baseline commit
- [ ] You can explain in one sentence why the three plants disagree
- [ ] RPI Agent shows in the picker, and `/rpi-research` shows in the slash menu

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Agents are missing | Run **Developer: Reload Window**, then start a new chat session |
| Agents appear twice | Remove the extra install route (for example, the Marketplace extension *and* the plugin) |
| `python3` isn't found | Install Python 3.11+ and reopen the terminal |
