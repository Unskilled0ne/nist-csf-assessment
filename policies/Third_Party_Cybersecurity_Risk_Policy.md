# Third-Party Cybersecurity & Vendor Risk Policy
**Standard Mapping:** NIST CSF 2.0 (GV.SC) | ISO 27001:2022 (A.5.19 - A.5.23) | EU DORA (Art. 28 - 44)  
**Document ID:** POL-TPRM-002  
**Version:** 2.0 | **Classification:** Internal  

---

## 1. Scope & Objective
This policy governs the onboarding, continuous monitoring, and termination of all third-party software, SaaS vendors, cloud service providers, and subcontracted technology partners.

## 2. Vendor Criticality Classification

| Tier | Category | Definition | Due Diligence Mandate |
| :---: | :--- | :--- | :--- |
| **Tier 1** | Critical / Systemic | Providers hosting customer PII, payment rails, cloud infrastructure (AWS/GCP), or direct database access. | Mandatory annual SOC 2 Type II, ISO 27001, external penetration test review, business continuity drill. |
| **Tier 2** | Operational | Internal productivity SaaS (Slack, Jira, Zoom) with access to non-sensitive corporate data. | Annual SIG Lite questionnaire + automated attack surface scan score >= 80. |
| **Tier 3** | Low Risk | Hardware suppliers, office facilities, marketing tools with zero access to internal networks. | Basic vendor code of conduct sign-off. |

## 3. Mandatory Contractual Clauses (EU DORA Compliance)
All Tier 1 vendor contracts must legally include:
1. **Right to Audit:** ApexFin or its designated regulators reserve the right to audit vendor facilities and controls.
2. **Breach Notification:** The vendor must formally notify ApexFin within **24 hours** of any confirmed security incident impacting services.
3. **Data Localization & Portability:** Clear exit strategies ensuring customer financial records can be extracted in standard format within 30 days of contract termination.
4. **Subcontracting Oversight:** Mandatory prior written consent before the vendor delegates critical functions to fourth-party subcontractors.
