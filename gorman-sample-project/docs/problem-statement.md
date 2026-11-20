# Problem Statement: Plant KPI Standardization Program

**Sponsor:** COO, Gorman Manufacturing Company
**Program lead:** Director of Manufacturing Systems
**Date:** 2026-11-01

## Situation

Gorman runs three plants (Detroit, Monterrey, Pune). Each plant built its own OEE tooling.
The weekly executive OEE report combines three numbers that were calculated three
different ways.

## Pain points

1. **Inconsistent KPI.** For the same shift, the results are 69.6% (DET), 81.2% (MTY) and 72.9% (PNQ). The correct value is 77.2%.
2. **Reliability.** The Monterrey script crashes on any zero-production shift, so the weekly job fails about twice a month.
3. **Security and audit.** IT audit finding GA-2026-14 covers hard-coded credentials and SQL injection risk in plant scripts.
4. **Knowledge silos.** Each script has one owner. Detroit's owner has left the company.
5. **Slow onboarding.** New process engineers need about 3 weeks before they can change KPI code safely.
6. **No decision trail.** Nobody can say why each plant chose its formula.

## Desired outcomes (90 days)

| Outcome | Measure |
|---------|---------|
| One OEE definition in code | 1 shared library; 3 plant adapters; 100% of plants migrated |
| Correctness | Golden-shift test returns 77.2% for every plant format |
| Reliability | 0 weekly-job crashes for 4 consecutive weeks |
| Security | GA-2026-14 closed; 0 secrets in the repo |
| Consistency of engineering | Shared Copilot instructions, skills and agents in `.github/` used by all plant teams |
| Onboarding | A new engineer ships a reviewed change in 3 days or less |

## Constraints

- Python 3.11+ only, standard library preferred (plant PCs have restricted package installs).
- Plant exports can't change this quarter, so adapters must accept today's formats.
- Every change needs a reviewed plan and a passing test run (Gorman change policy).

## Out of scope

- Replacing the MES or the plant historians.
- Real-time OEE (batch per shift is enough for now).
