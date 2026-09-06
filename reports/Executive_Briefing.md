# Executive Cybersecurity Maturity & Risk Assessment
## NIST Cybersecurity Framework (CSF) 2.0 Briefing

**Client Organization:** Apex Financial Technologies S.A.  
**Industry Vertical:** FinTech / Payment Service Provider (210 employees)  
**Lead Cybersecurity Auditor:** Vasilis Tsiamouras  
**Assessment Date:** 2026-09-06  
**Applicable Regulations:** EU DORA, PCI-DSS v4.0, GDPR, ISO 27001:2022  

---

## 1. Executive Summary

Apex Financial Technologies underwent a formal cybersecurity posture evaluation benchmarked against the **NIST Cybersecurity Framework (CSF) 2.0**. 

The current enterprise maturity is evaluated at **Tier 2.17 / 4.0** (Risk-Informed with Significant Control Gaps), against a defined Board target of **Tier 3.72 / 4.0** (Repeatable & Adaptive).

To achieve regulatory compliance under the impending **EU Digital Operational Resilience Act (DORA)** and satisfy **PCI-DSS v4.0** merchant obligations, an estimated total remediation capital investment of **€185,000** across Q4 2026 and Q1 2027 is required.

```
Maturity Progression:
Current: [████████████░░░░░░░░] Tier 2.17 (Partial / Risk-Informed)
Target:  [██████████████████░░] Tier 3.72 (Repeatable / Adaptive)
```

---

## 2. NIST CSF 2.0 Function Breakdown

| Function Code | Core Function Name | Current Tier | Target Tier | Maturity Gap | Status |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **GV** | GOVERN | **2.0** | **3.5** | +1.5 | ⚠️ Action Required |
| **ID** | IDENTIFY | **2.25** | **3.75** | +1.5 | ⚠️ Action Required |
| **PR** | PROTECT | **2.5** | **4.0** | +1.5 | ⚠️ Action Required |
| **DE** | DETECT | **2.0** | **3.5** | +1.5 | ⚠️ Action Required |
| **RS** | RESPOND | **1.5** | **3.5** | +2.0 | ⚠️ Action Required |
| **RC** | RECOVER | **2.5** | **4.0** | +1.5 | ⚠️ Action Required |

---

## 3. Top Strategic Enterprise Risks (Prioritized POAM)

The following vulnerabilities present immediate operational disruption or regulatory penalty exposure:

| Risk ID | Category | Threat / Control Deficiency | Risk Score (L×I) | Severity | Required Investment | Owner |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| `PR.AA-01` | **Credential & Identity Lifecycle Management** | CRITICAL: Multiple privileged IAM users have non-expiring access keys and SMS MFA vulnerable to SIM-swapping. | **25 / 25** | `CRITICAL` | €22,000 | Cloud Security Architect |
| `RS.MA-01` | **Incident Response Plan & Execution** | High risk of non-compliance with EU DORA strict 4-hour major incident notification requirements. | **20 / 25** | `CRITICAL` | €16,000 | CISO / Incident Commander |
| `GV.SC-04` | **Third-Party Supplier Due Diligence** | High risk of third-party breach via critical cloud providers without SOC 2 Type II validation. | **16 / 25** | `HIGH` | €28,000 | Head of Procurement / CISO |
| `ID.RA-01` | **Vulnerability Identification & Threat Modeling** | Zero automated container image scanning in CI/CD pipeline leading to vulnerable third-party packages in production. | **16 / 25** | `HIGH` | €12,000 | DevSecOps Lead |
| `DE.CM-01` | **Network & Cloud Telemetry Monitoring** | No EDR deployed on 40% of macOS/Linux engineer workstations; blind spots in lateral movement detection. | **16 / 25** | `HIGH` | €35,000 | SOC Lead |

---

## 4. Board Recommendations & Next Steps

1. **Mandate FIDO2 MFA for Privileged Accounts (`PR.AA-01`):** Eliminate SMS authentication and non-expiring cloud IAM credentials immediately.
2. **Standardize DORA-Compliant Incident Response (`RS.MA-01`):** Upgrade 2023 IRP to support 4-hour regulatory notification SLA and conduct an executive tabletop exercise.
3. **Automate Third-Party Risk Management (`GV.SC-04`):** Ensure all external payment and cloud API vendors maintain active SOC 2 Type II certifications.
4. **Approve Capital Budget (€185,000):** Allocate phased spending across Q4 2026 (€118,000) and Q1 2027 (€67,000).
