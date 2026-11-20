# Module 05 — Self-learning prompts

> Type `/clear` first.

## Prompt 5.1 — Implement the approved plan

```text
/rpi-implement plan=<path to your oee-standardization plan>
Implement all phases. After each phase, run
python3 -m unittest discover -s tests -t . and record the result in the changes log.
Stop and ask me if any task would change files under plants/ or data/.
```

## Prompt 5.2 — Resume after an interruption

```text
/rpi-implement plan=<path to your plan> phase=P03
Resume at the adapters phase. Re-read the plan and the changes log first, and continue
from the first unchecked task.
```

## Prompt 5.3 — Learn from the result

```text
Using the changes log for oee-standardization, explain for each legacy bug in the
research artifact which file and function in gorman_oee now prevents it, and which
test proves it. Answer as a table.
```

## Prompt 5.4 — Try to break it (good for demos)

```text
Add a test for a Detroit record where downtime is greater than planned time, and a
Pune record where rejected is greater than produced. Run the tests and show me the
result. Do not change library code unless a test exposes a real bug.
```

## Reflection

- How much of the implementation needed your judgment? Where?
- What would have gone differently if you had asked "write me an OEE library" without research or a plan?
