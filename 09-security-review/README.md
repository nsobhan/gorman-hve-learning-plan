# Module 09 — Security: Security Reviewer and Security Planner

| | |
|---|---|
| **Time** | 45 minutes |
| **HVE usage** | **Security Reviewer** agent (OWASP-based assessment with subagent verification) and **Security Planner** agent (STRIDE threat model, standards mapping, backlog handoff) |
| **Gorman outcome** | Audit finding GA-2026-14 closed, with evidence, plus a threat model for the OEE pipeline |

## Concept

| Agent | Question it answers | Output |
|-------|---------------------|--------|
| **Security Reviewer** | "What's vulnerable in this code right now?" | Profiles the codebase, runs the applicable skill assessments (for example OWASP Top 10), verifies FAIL and PARTIAL findings adversarially, and writes a consolidated report |
| **Security Planner** | "What could go wrong in this system design?" | A six-phase conversational STRIDE analysis, mapped to standards, handed off as backlog items |

Both are **experimental** in HVE Core, and both are advisory. People decide what to fix.

## Gorman problem it solves

The IT audit found hard-coded credentials and SQL injection risk (GA-2026-14). Gorman needs
proof of *what* was found, *what* was fixed, and *what* threats remain.

## Planted issues the reviewer should find

| Issue | Location |
|-------|----------|
| Hard-coded DB password (fake) | `plants/detroit/oee_calc.py`, `dbPassword` |
| Hard-coded API token (fake) | `plants/pune/calc_oee_v2.py`, `API_TOKEN` |
| SQL built by string concatenation (injection) | `plants/pune/calc_oee_v2.py`, `save()` |
| Unclosed file handle, no input validation | `plants/detroit/oee_calc.py`, `main()` |

## Steps

1. Select **Security Reviewer** and run Prompt 9.1.
2. Fix the findings with RPI (Prompt 9.2) and run the reviewer again to confirm.
3. Select **Security Planner** and threat-model the target pipeline (Prompt 9.3). Use the intake
   answers given in the prompt.

## Check yourself

- [ ] The report lists all four planted issues with severity and verification status
- [ ] After the fix, a second review shows them resolved and no secrets remain (`git grep -n -i "password\|token"`)
- [ ] The STRIDE output includes at least one tampering threat to plant export files and one to the KPI report
