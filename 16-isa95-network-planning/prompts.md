# Module 16 — Self-learning prompts

> Select **Network ISA-95 Planner**.

## Prompt 16.1 — Detroit (brownfield)

```text
Plan a secure network design for Gorman Manufacturing's Detroit plant. Goal: run an
edge Kubernetes cluster that collects PLC and MES data every 15 minutes, calculates OEE
with the gorman_oee library, and sends results to Azure. The site is brownfield with
a flat network. Ask me your intake questions first, then assess current-state risk and
build a phased remediation roadmap with effort and confidence for each step.
```

Answer the intake questions using [intake-detroit.md](intake-detroit.md).

## Prompt 16.2 — Ostrava (greenfield)

```text
Now plan Gorman's new Ostrava plant (greenfield). Same goal as Detroit. ISA-95 levels:
L0 to L4. We want Microsoft-recommended patterns, private connectivity for all
cloud flows, managed identity, and Azure Arc-managed Kubernetes. Ask for anything else
you need. Then compare the Ostrava target design with the Detroit roadmap: what should
Detroit copy from Ostrava once its remediation is complete?
```

## Prompt 16.3 — Diagram

```text
Produce the zones-and-conduits diagram for Detroit's target state, showing each
allow-listed flow between L1/L2, the edge cluster, L3 MES, the DMZ and Azure.
```

## Reflection

- Which Detroit risk would you fix even if the edge-OEE project were cancelled?
- How does this module connect back to the Security Planner's STRIDE output in Module 09?
