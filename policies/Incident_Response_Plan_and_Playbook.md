# Enterprise Incident Response Plan & Playbook
**Standard Mapping:** NIST CSF 2.0 (RS.MA, RS.AN, RS.CO) | ISO 27001:2022 (A.5.24 - A.5.28) | EU DORA (Art. 11, 19)  
**Document ID:** IRP-SEC-001  
**Version:** 3.0 | **Classification:** Confidential  

---

## 1. Incident Response Lifecycle
Apex Financial Technologies adopts the NIST SP 800-61r2 / CSF 2.0 incident lifecycle:
1. **Preparation:** Hardened telemetry, logging retention (1 year hot/warm), trained Incident Response Team (IRT).
2. **Detection & Analysis:** Correlation of SIEM/EDR alerts, IOC extraction, severity triage.
3. **Containment, Eradication & Recovery:** Network isolation, account revocation, artifact purging, restored from clean immutable backups.
4. **Post-Incident Activity:** Root-cause post-mortem within 5 business days; remediation POAM update.

---

## 2. Severity Classification Matrix

| Level | Severity | Criteria | Escalation SLA | Regulatory Notification |
| :---: | :--- | :--- | :---: | :---: |
| **SEV-1** | Critical | Active ransomware, confirmed exfiltration of financial/PII data, total outage of payment gateway. | Immediate (<15m) | **< 4 Hours** (EU DORA / Supervisory Authority) |
| **SEV-2** | High | Privileged root credential compromise, critical vulnerability actively exploited in production. | < 30 Minutes | < 24 Hours (Internal Executive Escalation) |
| **SEV-3** | Medium | Isolated malware detection on single workstation (neutralized by EDR), suspicious brute-force activity. | < 2 Hours | None required |
| **SEV-4** | Low | Routine phishing attempt reported by employee with no credentials submitted. | < 8 Hours | None required |

---

## 3. Incident Command Structure
- **Incident Commander (IC):** Leads coordination, operational decisions, and containment approval. (Designee: Head of SecOps / CISO).
- **Technical Lead:** Directs forensic imaging, network packet analysis, and malware reverse-engineering.
- **Legal & Compliance Counsel:** Manages legal liability, law enforcement communication, and regulatory filings (EU DORA, GDPR 72-hour notifications).
- **Communications Lead:** External media, customer status page updates, and investor relations.

---

## 4. Ransomware Containment Playbook
1. **Immediate Network Isolation:** Do NOT power off systems. Disconnect infected VLANs and trigger EDR host isolation.
2. **Credential Revocation:** Force global password reset for all Active Directory / Okta / IAM users.
3. **Forensic Preservation:** Snapshot volatile RAM memory before rebooting or terminating virtual machines.
4. **Restore Verification:** Restore exclusively from air-gapped AWS S3 Object Lock backups after validating hash integrity. Never pay extortion demands.
