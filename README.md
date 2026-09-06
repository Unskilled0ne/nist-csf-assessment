# NIST CSF 2.0 Enterprise GRC Maturity & Risk Assessment Platform 🏛️📊

**Automated Cybersecurity Maturity Assessment, Risk Quantification (Likelihood × Impact), and Executive POAM Roadmap**  
*Benchmarked against NIST CSF 2.0, ISO/IEC 27001:2022, and EU DORA*  
*Lead Cybersecurity Auditor: [Vasilis Tsiamouras](https://www.linkedin.com/in/vasilis-tsiamouras/)*

[![NIST CSF 2.0](https://img.shields.io/badge/Standard-NIST%20CSF%202.0-blue.svg)](https://www.nist.gov/cyberframework)
[![ISO 27001](https://img.shields.io/badge/Standard-ISO%2027001%3A2022-green.svg)](https://www.iso.org/)
[![EU DORA](https://img.shields.io/badge/Regulation-EU%20DORA%20Ready-purple.svg)](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Executive Overview

While most cybersecurity portfolios focus exclusively on technical hacking or CTFs, modern Chief Information Security Officers (CISOs) and consultancies (Big 4, financial auditors, boutique MSSPs) demand professionals who understand **enterprise risk management, governance, and regulatory compliance**.

This repository provides an automated, enterprise-ready **Governance, Risk & Compliance (GRC) Assessment Framework** centered around the **NIST Cybersecurity Framework 2.0 (CSF 2.0)**.

The project evaluates an enterprise target (**Apex Financial Technologies S.A.**—a 210-employee FinTech payment gateway under EU DORA, PCI-DSS v4.0, and GDPR scope), calculates function-level implementation tiers, quantifies operational risk, and automatically exports C-suite executive briefings, engineering roadmaps, and compliance crosswalks.

---

## 🏗️ Architecture & GRC Engine Flow

```
                           [ Enterprise Security Evidence & Audit Telemetry ]
                                                  │
                                                  ▼
                                   ┌──────────────────────────────┐
                                   │  data/apexfin_assessment.json│
                                   │    (NIST CSF 2.0 Schema)     │
                                   └──────────────┬───────────────┘
                                                  │
                                                  ▼
                                   ┌──────────────────────────────┐
                                   │      engine/analyzer.py      │
                                   │ - Function Tier Averages     │
                                   │ - Risk Scoring (L × I)       │
                                   │ - POAM Cost & Owner Grouping │
                                   └──────────────┬───────────────┘
                                                  │
                         ┌────────────────────────┴────────────────────────┐
                         ▼                                                 ▼
             ┌────────────────────────┐                        ┌────────────────────────┐
             │   engine/reporter.py   │                        │   FastAPI Web Engine   │
             └───────────┬────────────┘                        └───────────┬────────────┘
                         │                                                 │
          ┌──────────────┼──────────────┐                                  ▼
          ▼              ▼              ▼                     ┌────────────────────────┐
    ┌───────────┐  ┌───────────┐  ┌───────────┐               │ Interactive Dashboard  │
    │ Executive │  │   POAM    │  │Compliance │               │  - Radar Maturity Chart│
    │ Briefing  │  │  Roadmap  │  │ Crosswalk │               │  - Owner Budget Bars   │
    │   (.md)   │  │   (.md)   │  │   (.md)   │               │  - Risk Register Table │
    └───────────┘  └───────────┘  └───────────┘               └────────────────────────┘
```

---

## 🏛️ The 6 Core Functions of NIST CSF 2.0

Unlike CSF 1.1, NIST CSF 2.0 introduces the critical **GOVERN (GV)** function to emphasize organizational risk strategy:

| Function ID | Function Name | Current Posture | Target Tier | Remediation Focus |
| :---: | :--- | :---: | :---: | :--- |
| **GV** | **GOVERN** | **Tier 2.00** | **Tier 3.50** | Formalizing Board risk appetite & third-party supply chain due diligence (`GV.SC`). |
| **ID** | **IDENTIFY** | **Tier 2.25** | **Tier 3.75** | Automated hardware/software asset discovery and CI/CD vulnerability scanning. |
| **PR** | **PROTECT** | **Tier 2.50** | **Tier 4.00** | Mandating FIDO2 MFA on all privileged AWS/cloud accounts; deploying endpoint DLP. |
| **DE** | **DETECT** | **Tier 2.00** | **Tier 3.50** | 100% EDR coverage on engineering laptops integrated into 24/7 MDR SOC. |
| **RS** | **RESPOND** | **Tier 1.50** | **Tier 3.50** | Revising IRP to support EU DORA 4-hour regulatory notification SLA; tabletop drills. |
| **RC** | **RECOVER** | **Tier 2.50** | **Tier 4.00** | Air-gapped AWS S3 Object Lock immutable backups & disaster recovery drill. |

---

## 📊 Assessment Summary: Apex Financial Technologies

```
Overall Maturity Progression:
Current: [████████████░░░░░░░░] Tier 2.17 (Risk-Informed / Partial Gaps)
Target:  [██████████████████░░] Tier 3.72 (Repeatable / Adaptive Posture)
Maturity Delta: +1.56 Tiers
Total Capital Expenditure Required: €185,000 (Allocated across Q4 2026 - Q1 2027)
```

### Top 5 Prioritized Enterprise Risks (Likelihood × Impact)

| Control ID | Subcategory Title | Risk Score (L×I) | Severity | Phased Budget | Lead Owner |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `PR.AA-01` | Credential & Identity Lifecycle Management | **25 / 25** | `CRITICAL` | €22,000 | Cloud Security Architect |
| `RS.MA-01` | Incident Response Plan & Execution | **20 / 25** | `CRITICAL` | €16,000 | CISO / Incident Commander |
| `GV.SC-04` | Third-Party Supplier Due Diligence | **16 / 25** | `HIGH` | €28,000 | Head of Procurement / CISO |
| `ID.RA-01` | Vulnerability Identification & Threat Modeling | **16 / 25** | `HIGH` | €12,000 | DevSecOps Lead |
| `DE.CM-01` | Network & Cloud Telemetry Monitoring | **16 / 25** | `HIGH` | €35,000 | SOC Lead |

---

## 📁 Repository Structure & Deliverables

```
nist-csf-assessment/
├── README.md                          # Comprehensive project documentation
├── requirements.txt                   # Dependencies (FastAPI, Uvicorn, Rich, PyYAML)
├── run_assessment.py                  # Master CLI & Web Assessment runner
├── data/
│   ├── nist_csf_2_schema.json         # Core NIST CSF 2.0 framework schema
│   └── apexfin_assessment.json        # Real-world enterprise evaluation dataset
├── engine/
│   ├── analyzer.py                    # Maturity calculator, risk ranking & POAM logic
│   └── reporter.py                    # Multi-format executive & technical report generator
├── policies/                          # Gold-standard production security policies
│   ├── Access_Control_and_Identity_Policy.md      (PR.AA)
│   ├── Incident_Response_Plan_and_Playbook.md     (RS.MA / DORA)
│   └── Third_Party_Cybersecurity_Risk_Policy.md   (GV.SC)
├── reports/                           # Generated assessment deliverables
│   ├── Executive_Briefing.md          # Board of Directors & CISO Briefing
│   ├── POAM_Remediation_Roadmap.md    # Phased engineering roadmap & budgets
│   ├── Compliance_Crosswalk.md        # NIST CSF 2.0 <-> ISO 27001 <-> DORA matrix
│   └── assessment_summary.json        # Raw telemetry JSON export
└── static/
    └── index.html                     # Interactive web dashboard (Tailwind + Chart.js)
```

---

## 🚀 Quickstart Guide

### 1. Installation

```bash
git clone https://github.com/your-username/nist-csf-assessment.git
cd nist-csf-assessment

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run CLI Assessment & Generate Deliverables

```bash
./run_assessment.py
```
This executes the analyzer, prints Rich terminal tables, and generates all 4 deliverable documents in `reports/`.

### 3. Launch Interactive Dashboard

```bash
./run_assessment.py --serve --port 8081
```
Open **`http://localhost:8081`** in your browser to view:
- NIST CSF 2.0 Function Maturity Spider/Radar Chart.
- Workstream Budget Breakdown Bar Chart.
- Interactive Prioritized Risk Register Table.

---

## 👤 Author

**Vasilis Tsiamouras**  
- LinkedIn: [linkedin.com/in/vasilis-tsiamouras](https://www.linkedin.com/in/vasilis-tsiamouras/)  
- Track: Offensive Security & Penetration Testing | Computer Science, University of Thessaly
