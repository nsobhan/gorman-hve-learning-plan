# Sample Intake Answers: Gorman Detroit (fictional)

Paste these answers when the Network ISA-95 Planner asks.

| Question | Answer |
|----------|--------|
| Site profile | Brownfield |
| ISA-95 levels in scope | L1 (PLCs on 3 stamping lines), L2 (HMI and historian), L3 (MES server), L4 (office IT and ERP) |
| Edge Kubernetes | Planned: 3-node K3s cluster managed by Azure Arc |
| Azure connectivity | Site-to-site VPN (2019 appliance), no ExpressRoute |
| Segmentation maturity | Flat: PLCs, HMIs, MES and office PCs share VLAN 10 |
| Critical cloud dependencies | Container registry, Entra ID, Key Vault for certificates, Azure Monitor for telemetry, Azure Policy |
| Identity for cloud integrations | Today, a shared service account with a password in a script (see audit GA-2026-14). Target: managed identity or workload identity. |
| Logging destinations and retention | Historian keeps 90 days locally; nothing goes to the cloud today |
| Operational constraints | Downtime only in the Sunday 02:00–06:00 window; low risk tolerance for L1/L2 |
| Reusable infrastructure | 1 reverse proxy (NGINX) in the office DMZ; VPN edge appliance; a firewall with NAT and no OT rules |
| Ownership and change authority | Plant IT owns the firewall and VPN; Controls engineering owns PLCs and HMIs; Corporate IT owns the DMZ |
| Compensating controls | Antivirus on HMIs; no network monitoring on OT |
| Replacement windows | VPN appliance end-of-support in Q3 next year |
