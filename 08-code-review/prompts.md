# Module 08 — Self-learning prompts

## Prompt 8.1 — Review the legacy scripts

```text
/code-review plants/ depth=standard
Review the three legacy plant OEE scripts against docs/oee-standard.md and the Gorman
instructions. Rank findings by impact on reported KPIs.
```

## Prompt 8.2 — Plant a bug to review (run in the default agent)

```bash
git checkout -b review-demo
```

```text
In gorman_oee/calculator.py, change calculate_shift so that availability is rounded to
3 decimal places before multiplying. Save the file. Do not change tests.
```

```bash
git commit -am "Tweak availability precision"
```

## Prompt 8.3 — Review the branch

```text
/code-review branch review-demo compared with main depth=standard
```

**Expected:** a high-severity functional finding that intermediate rounding violates GMS-OPS-007
rule 1, plus a note that the golden-shift test may still pass by luck (rounding to 3 decimals
happens not to change 77.2%). That gap is itself worth a follow-up test.

## Prompt 8.4 — Opt in to security and performance

```text
/code-review plants/pune/calc_oee_v2.py vectors=security,performance depth=comprehensive
```

## Clean up

```bash
git checkout main && git branch -D review-demo
```

## Reflection

- Why does HVE keep non-functional vectors opt-in by default?
- How would you make `/code-review` a required step for every plant team? (See Module 17.)
