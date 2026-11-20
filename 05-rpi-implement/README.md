# Module 05 — RPI Phase 3: Implement (`/rpi-implement`)

| | |
|---|---|
| **Time** | 45 minutes |
| **HVE usage** | `/rpi-implement` following an approved plan, a changes log in `.copilot-tracking/changes/` |
| **Gorman outcome** | A working `gorman_oee` library. The golden shift gives 77.2% for all three plants |

## Concept

`/rpi-implement` follows the approved plan, checks off tasks, keeps the plan up to date
when it learns something new, and writes a short changes log:

```text
.copilot-tracking/changes/{date}/{task-slug}-changes.md
```

Because the plan is detailed, implementation is mostly mechanical. That's the goal.

## Steps

1. Type `/clear`, then run `/rpi-implement` with Prompt 5.1.
2. While it works, watch for any task it marks as blocked or changed. Those are decisions for you.
3. Run the tests yourself:

   ```bash
   python3 -m unittest discover -s tests -t . -v
   ```

   ```bash
   python3 -m gorman_oee.cli --plant MTY data/monterrey_registro_turnos.csv
   ```

4. Compare your code with the reference in [solution/](solution/). The two don't need to match exactly.
   What matters is that both pass the same golden-shift test.
5. Commit the code and the changes log.

## Expected result

```text
DET/L1/2026-11-02/A          OEE  77.2%  flags=-
...
MTY/L2/2026-11-02/B          OEE   0.0%  flags=NO_PRODUCTION
MTY plant OEE (weighted by planned time): 58.7%
```

Same shift, **one** answer: 77.2% from all three plant formats. Monterrey's zero-production
shift no longer crashes.

## Using the reference solution

If you're short on time, or you're preparing a demo, copy the reference into your workspace:

```bash
cp -R solution/gorman_oee solution/tests ~/gorman-mes/
```

## Check yourself

- [ ] All tests pass
- [ ] `git diff --stat` shows no changes under `plants/` or `data/` (that was out of scope)
- [ ] The changes log lists every file changed and maps it to plan tasks
