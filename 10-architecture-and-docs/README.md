# Module 10 — Architecture Decisions and Documentation

| | |
|---|---|
| **Time** | 45 minutes |
| **HVE usage** | **ADR Creation** agent (Socratic ADR coaching, `adr-author` skill), **System Architecture Reviewer**, **Documentation** agent (audit, drift, validate, author) |
| **Gorman outcome** | A recorded decision for "shared library + adapters," an architecture review, and library docs that stay in sync with the code |

## Concept

- **ADR Creation** coaches you through a decision with questions. It doesn't decide for you.
  Output uses Y-Statement or MADR v4 templates.
- **System Architecture Reviewer** reviews a design for trade-offs and alignment with ADRs. It
  passes security concerns on to the security agents.
- **Documentation** audits docs, detects **drift** (docs that no longer match code), validates
  them, and writes new docs.

## Gorman problem it solves

Pain point 6: *nobody can say why each plant chose its formula.* From now on every significant
choice is an ADR in `docs/decisions/`, and docs are checked for drift instead of quietly going stale.

## Steps

1. Select **ADR Creation** and run Prompt 10.1. Answer its questions as the Gorman Director of
   Manufacturing Systems. A sample result is in [solution/docs/decisions/](solution/docs/decisions/).
2. Select **System Architecture Reviewer** and run Prompt 10.2.
3. Select **Documentation** and run Prompts 10.3 and 10.4.

## Check yourself

- [ ] `docs/decisions/adr-0001-*.md` lists at least three options and their consequences
- [ ] The architecture review mentions the ADR and at least one risk (for example, adapters drifting from MES export changes)
- [ ] The documentation drift audit finds that the README's "Layout" section doesn't mention `gorman_oee/`
