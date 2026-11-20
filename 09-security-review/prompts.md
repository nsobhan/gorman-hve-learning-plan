# Module 09 — Self-learning prompts

## Prompt 9.1 — Vulnerability assessment (select **Security Reviewer**)

```text
Assess this repository for security vulnerabilities. Context: Gorman Manufacturing's
plant KPI tooling, Python 3.11, runs as a scheduled batch job on plant servers, reads
plant export files and (legacy) writes to SQL. IT audit finding GA-2026-14 cited
hard-coded credentials and SQL injection risk. Include plants/ and gorman_oee/.
Produce the consolidated report with verified findings only.
```

## Prompt 9.2 — Remediate with RPI (select **RPI Agent**)

```text
Task: close audit finding GA-2026-14 using the latest security report. Remove the
hard-coded credentials in plants/detroit and plants/pune (read them from
environment variables GORMAN_DET_DB_PASSWORD and GORMAN_PNQ_API_TOKEN), and replace
the SQL string concatenation in plants/pune/calc_oee_v2.py with a parameterized query.
Behavior and output must otherwise stay the same. Add a short docs/security/GA-2026-14.md
remediation note. Ask me before changing anything else in plants/.
```

## Prompt 9.3 — Threat model the target pipeline (select **Security Planner**)

```text
Build a security model for Gorman's target OEE pipeline.

System: each plant MES exports a shift file nightly to a plant file share; a scheduled
job on a plant server runs python3 -m gorman_oee.cli; results are copied to a
corporate SharePoint folder that feeds the weekly COO report. Plants: Detroit,
Monterrey, Pune, Ostrava. Users: plant process engineers (edit code), plant managers
(read reports), the COO (reads reports). Identity: Entra ID. No internet-facing
components. Data classification: internal, confidential (it affects bonuses).

Focus on integrity of KPI numbers (tampering with export files, ideal cycle master
data and reports) and on credential handling.
```

## Reflection

- Which finding was most likely to be exploited at a plant, rather than just flagged by an auditor?
- STRIDE flagged threats in design, not code. Which belongs in the backlog first?
