# Module 10 — Self-learning prompts

## Prompt 10.1 — Capture the decision (select **ADR Creation**)

```text
I need an ADR for how Gorman Manufacturing standardizes OEE calculation across plants.
Options we discussed:
1. Fix each plant script in place to follow GMS-OPS-007
2. One shared Python library with a per-plant adapter for each export format
3. Ask every plant to change its MES export to one corporate format
4. Calculate OEE centrally in the corporate data warehouse instead of at plants
Context is in docs/problem-statement.md and the oee-standardization research.
Coach me through it and save the ADR as docs/decisions/adr-0001-oee-shared-library.md
in MADR format.
```

## Prompt 10.2 — Architecture review (select **System Architecture Reviewer**)

```text
Review the gorman_oee design (model, calculator, adapters, CLI) and
docs/decisions/adr-0001-oee-shared-library.md. Focus on trade-offs: adding new plants,
handling MES export version changes, where master data such as ideal cycle time should
live, and what has to change when we move from batch to near-real-time OEE.
```

## Prompt 10.3 — Documentation drift audit (select **Documentation**)

```text
Audit the documentation in this repository for drift against the code. Check README.md,
docs/oee-standard.md and .github/instructions/gorman/* against gorman_oee/ and tests/.
Report the drift only; do not edit yet.
```

## Prompt 10.4 — Author library docs (select **Documentation**)

```text
Author docs/gorman-oee-library.md for plant process engineers: what the library does,
how to run the CLI for each plant, what each flag means, how to add a plant
adapter, and how to run the tests. Link to the OEE standard and ADR-0001.
Then update README.md's Layout section to include gorman_oee/ and tests/.
```

## Reflection

- Which option did the ADR coach make you rethink?
- How would you add a drift audit to the monthly release checklist?
