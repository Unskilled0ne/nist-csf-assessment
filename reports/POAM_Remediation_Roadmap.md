# Plan of Action & Milestones (POAM) Remediation Roadmap
**Framework:** NIST CSF 2.0 | **Organization:** Apex Financial Technologies S.A.  

---

## Phased Remediation Workstreams

### Phase: Q4 2026 (Allocated Budget: €118,000)

| Control ID | Initiative | Remediation Engineering Action | Lead Owner | Investment |
| :--- | :--- | :--- | :--- | :---: |
| `PR.AA-01` | **Credential & Identity Lifecycle Management** | Enforce FIDO2 / WebAuthn hardware security keys for all privileged access; automate IAM key rotation every 90 days. | Cloud Security Architect | €22,000 |
| `RS.MA-01` | **Incident Response Plan & Execution** | Revise IRP with DORA-compliant escalation matrix; conduct bi-annual executive ransomware tabletop simulation. | CISO / Incident Commander | €16,000 |
| `ID.RA-01` | **Vulnerability Identification & Threat Modeling** | Integrate automated DevSecOps container security scanner (Trivy/Snyk) into GitLab CI pipeline with build-blocking policy. | DevSecOps Lead | €12,000 |
| `DE.CM-01` | **Network & Cloud Telemetry Monitoring** | Deploy enterprise EDR (CrowdStrike/Wazuh) across 100% of workstations and integrate into 24/7 MDR SOC. | SOC Lead | €35,000 |
| `ID.AM-01` | **Hardware & Virtual Infrastructure Inventory** | Deploy automated Cyber Asset Attack Surface Management (CAASM) agent syncing all assets into CMDB. | IT Operations Lead | €18,000 |
| `GV.OC-01` | **Organizational Mission & Regulatory Stakeholders** | Establish a Board-level Cybersecurity Committee with quarterly review of quantified risk tolerance. | CISO / Legal | €15,000 |

### Phase: Q1 2027 (Allocated Budget: €67,000)

| Control ID | Initiative | Remediation Engineering Action | Lead Owner | Investment |
| :--- | :--- | :--- | :--- | :---: |
| `GV.SC-04` | **Third-Party Supplier Due Diligence** | Implement an automated Third-Party Risk Management (TPRM) platform and mandate SOC 2 / ISO 27001 for Tier 1 vendors. | Head of Procurement / CISO | €28,000 |
| `RC.RP-01` | **Restoration of Core Banking Services** | Implement immutable AWS S3 Object Lock for air-gapped ransomware backups and conduct full disaster recovery failover drill. | Infrastructure Lead | €14,000 |
| `PR.DS-01` | **Data-at-Rest & In-Transit Protection** | Deploy endpoint DLP to block unencrypted cardholder data exports; implement automated PII tokenization. | Data Protection Officer / SecOps | €25,000 |

