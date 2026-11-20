# Module 06 — RPI Phase 4: Review (`/rpi-review`) and Follow-up

| | |
|---|---|
| **Time** | 30 minutes |
| **HVE usage** | `/rpi-review`, review logs, follow-up routing, `/rpi-refine` |
| **Gorman outcome** | One acceptance record that reconciles research, plan and changes. Remaining work is routed, not forgotten |

## Concept

`/rpi-review` compares the **plan** against the **changes** and the **evidence**, then writes
one review record:

```text
.copilot-tracking/reviews/logs/{date}/{task-slug}-review.md
```

Follow-up routing is what keeps RPI honest:

| Review finds… | Routed to… |
|---------------|------------|
| A defect | Implement |
| A decision that's needed | Plan |
| An evidence gap | Research |
| Out-of-scope or remaining work | A new, separate work item |

## Gorman problem it solves

Gorman's auditors (finding GA-2026-14) want proof that changes were reviewed against
requirements. The review log is that proof, and it lives next to the code.

## Steps

1. Type `/clear`, then run `/rpi-review` with Prompt 6.1.
2. Read the outcome. Is it accepted, or are there follow-ups?
3. Route each follow-up (Prompt 6.2). Typical ones: retire the legacy scripts, move credentials to a secret
   store, onboard a fourth plant (Module 07).
4. Commit the review record.

## Check yourself

- [ ] The review states pass or fail for every plan task, with evidence (test output, file references)
- [ ] Every follow-up has a destination (Implement, Plan, Research, or a new item)
- [ ] You can show an auditor the trail: research → plan → critique → changes → review
