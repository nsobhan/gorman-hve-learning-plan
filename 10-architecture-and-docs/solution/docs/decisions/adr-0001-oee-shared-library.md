---
status: accepted
date: 2026-11-12
decision-makers: Director of Manufacturing Systems; plant engineering leads (DET, MTY, PNQ)
consulted: Corporate Operational Excellence; IT Security
informed: COO
---

# ADR-0001: Standardize OEE with a shared library and per-plant adapters

## Context and Problem Statement

Gorman's three plants calculate OEE with three different scripts. For the same shift,
they report 69.6%, 81.2% and 72.9%, while the standard (GMS-OPS-007) says 77.2%. Plant
exports can't change this quarter, plant PCs can only run the Python standard library,
and audit finding GA-2026-14 requires the credential and SQL issues to be removed.

## Decision Drivers

- One KPI definition, enforced in code and proven by tests
- No change to plant MES exports this quarter
- Python standard library only
- Adding a new plant (for example Ostrava) must be cheap
- Changes must leave an audit trail

## Considered Options

1. Fix each plant script in place
2. Shared library `gorman_oee` with per-plant adapters
3. A corporate export format adopted by every plant
4. Central calculation in the corporate data warehouse

## Decision Outcome

Chosen option: **2, shared library with per-plant adapters.** It is the only option that gives
one tested formula without changing plant exports this quarter.

### Consequences

- Good: one formula, and a golden-shift test across every plant format
- Good: onboarding a plant means one adapter and one test (proven with Ostrava)
- Bad: each adapter is coupled to a plant's export format, so an MES upgrade can break it.
  This is mitigated by an export-version check and the golden-shift sample per plant.
- Neutral: option 3 is still the long-term target. Revisit it in FY27 when the MES upgrade is planned.

## Pros and Cons of the Options

| Option | Pros | Cons |
|--------|------|------|
| 1. Fix in place | Smallest change per plant | Three codebases keep drifting; three sets of tests |
| 2. Shared library + adapters | One formula; cheap to add plants; testable | Adapters must track export changes |
| 3. Corporate export format | Simplest code | Not allowed this quarter; needs MES changes at every plant |
| 4. Central warehouse calc | Central governance | Needs data-platform work; loses plant-level offline runs |
