# Module 16 — Manufacturing Specialist: Network ISA-95 Planner

| | |
|---|---|
| **Time** | 45 minutes |
| **HVE usage** | **Network ISA-95 Planner** agent: ISA-95 zones and conduits, allow-listed flows, brownfield and greenfield tracks, `architecture-diagrams` skill |
| **Gorman outcome** | A secure network design and remediation roadmap for moving plant OEE collection to edge Kubernetes connected to Azure |

## Concept

The ISA-95 Planner designs **zones and conduits** for plant networks that connect edge
Kubernetes to Azure:

- Security first: the highest-risk exposures are handled first
- Recommendations come from **explicit zones, conduits and allow-listed flows**
- It supports **mixed maturity**, where a site has only some ISA-95 levels
- It runs separate **brownfield** and **greenfield** tracks
- Every recommendation has an **effort** and **confidence** rating
- **It won't classify alignment or propose final remediation until the required intake is complete.**

## Gorman scenario

Next year Gorman wants OEE every 15 minutes instead of per shift. The plan: a small edge
Kubernetes cluster at each plant collects PLC and MES data and sends results to Azure.

- **Detroit** is **brownfield**: a flat network, a 2019 VPN, and PLCs on the same VLAN as office PCs.
- **Ostrava** is effectively **greenfield**: a new building, designed from scratch.

## Steps

1. Select **Network ISA-95 Planner** and run Prompt 16.1 (Detroit, brownfield). Answer its intake
   questions using the [sample intake answers](intake-detroit.md).
2. Run Prompt 16.2 for Ostrava (greenfield) and compare the two roadmaps.
3. Ask for the diagram (Prompt 16.3).

## Check yourself

- [ ] The agent asked intake questions **before** giving recommendations
- [ ] Detroit's roadmap puts separating PLCs (L1/L2) from office IT (L4) first
- [ ] Each recommendation has effort and confidence ratings
