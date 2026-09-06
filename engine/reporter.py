import json
import os
from datetime import datetime, timezone
from typing import Dict, Any

class GRCReporter:
    def __init__(self, output_dir: str = "reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_all(self, analysis: Dict[str, Any]):
        self.generate_executive_briefing(analysis)
        self.generate_poam_roadmap(analysis)
        self.generate_compliance_crosswalk(analysis)
        self.generate_json_summary(analysis)

    def generate_executive_briefing(self, analysis: Dict[str, Any]) -> str:
        org = analysis["organization"]
        mat = analysis["overall_maturity"]
        fns = analysis["function_scores"]
        risks = analysis["ranked_risks"]

        md = f"""# Executive Cybersecurity Maturity & Risk Assessment
## NIST Cybersecurity Framework (CSF) 2.0 Briefing

**Client Organization:** {org['name']}  
**Industry Vertical:** {org['industry']} ({org['headcount']} employees)  
**Lead Cybersecurity Auditor:** {org['lead_auditor']}  
**Assessment Date:** {org['assessment_date']}  
**Applicable Regulations:** {', '.join(org['regulatory_scope'])}  

---

## 1. Executive Summary

Apex Financial Technologies underwent a formal cybersecurity posture evaluation benchmarked against the **NIST Cybersecurity Framework (CSF) 2.0**. 

The current enterprise maturity is evaluated at **Tier {mat['current_score']} / 4.0** (Risk-Informed with Significant Control Gaps), against a defined Board target of **Tier {mat['target_score']} / 4.0** (Repeatable & Adaptive).

To achieve regulatory compliance under the impending **EU Digital Operational Resilience Act (DORA)** and satisfy **PCI-DSS v4.0** merchant obligations, an estimated total remediation capital investment of **€{mat['total_remediation_budget_eur']:,}** across Q4 2026 and Q1 2027 is required.

```
Maturity Progression:
Current: [████████████░░░░░░░░] Tier 2.17 (Partial / Risk-Informed)
Target:  [██████████████████░░] Tier 3.72 (Repeatable / Adaptive)
```

---

## 2. NIST CSF 2.0 Function Breakdown

| Function Code | Core Function Name | Current Tier | Target Tier | Maturity Gap | Status |
| :---: | :--- | :---: | :---: | :---: | :---: |
"""
        for fn_code, data in fns.items():
            status = "⚠️ Action Required" if data["gap"] >= 1.5 else "⚡ Moderate Gap"
            md += f"| **{fn_code}** | {data['name']} | **{data['current_tier']}** | **{data['target_tier']}** | +{data['gap']} | {status} |\n"

        md += f"""
---

## 3. Top Strategic Enterprise Risks (Prioritized POAM)

The following vulnerabilities present immediate operational disruption or regulatory penalty exposure:

| Risk ID | Category | Threat / Control Deficiency | Risk Score (L×I) | Severity | Required Investment | Owner |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
"""
        for r in risks[:5]:
            md += f"| `{r['id']}` | **{r['title']}** | {r['gap']} | **{r['risk_score']} / 25** | `{r['severity']}` | €{r['cost_eur']:,} | {r['owner']} |\n"

        md += f"""
---

## 4. Board Recommendations & Next Steps

1. **Mandate FIDO2 MFA for Privileged Accounts (`PR.AA-01`):** Eliminate SMS authentication and non-expiring cloud IAM credentials immediately.
2. **Standardize DORA-Compliant Incident Response (`RS.MA-01`):** Upgrade 2023 IRP to support 4-hour regulatory notification SLA and conduct an executive tabletop exercise.
3. **Automate Third-Party Risk Management (`GV.SC-04`):** Ensure all external payment and cloud API vendors maintain active SOC 2 Type II certifications.
4. **Approve Capital Budget (€{mat['total_remediation_budget_eur']:,}):** Allocate phased spending across Q4 2026 (€{analysis['poam_by_quarter'].get('Q4 2026', 0):,}) and Q1 2027 (€{analysis['poam_by_quarter'].get('Q1 2027', 0):,}).
"""

        path = os.path.join(self.output_dir, "Executive_Briefing.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(md)
        return path

    def generate_poam_roadmap(self, analysis: Dict[str, Any]) -> str:
        risks = analysis["ranked_risks"]
        md = f"""# Plan of Action & Milestones (POAM) Remediation Roadmap
**Framework:** NIST CSF 2.0 | **Organization:** {analysis['organization']['name']}  

---

## Phased Remediation Workstreams

"""
        for qtr, budget in analysis["poam_by_quarter"].items():
            md += f"### Phase: {qtr} (Allocated Budget: €{budget:,})\n\n"
            md += "| Control ID | Initiative | Remediation Engineering Action | Lead Owner | Investment |\n"
            md += "| :--- | :--- | :--- | :--- | :---: |\n"
            for r in risks:
                if r["target_qtr"] == qtr:
                    md += f"| `{r['id']}` | **{r['title']}** | {r['remediation']} | {r['owner']} | €{r['cost_eur']:,} |\n"
            md += "\n"

        path = os.path.join(self.output_dir, "POAM_Remediation_Roadmap.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(md)
        return path

    def generate_compliance_crosswalk(self, analysis: Dict[str, Any]) -> str:
        risks = analysis["ranked_risks"]
        md = f"""# Regulatory Compliance Crosswalk
**Mapping:** NIST CSF 2.0 ⟷ ISO/IEC 27001:2022 ⟷ EU DORA (Digital Operational Resilience Act)

| NIST CSF 2.0 Subcategory | Title | ISO 27001:2022 Mapping | EU DORA Article Mapping |
| :--- | :--- | :--- | :--- |
"""
        for r in risks:
            iso = r["compliance"].get("iso27001", "N/A")
            dora = r["compliance"].get("dora", "N/A")
            md += f"| `{r['id']}` | {r['title']} | `{iso}` | `{dora}` |\n"

        path = os.path.join(self.output_dir, "Compliance_Crosswalk.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(md)
        return path

    def generate_json_summary(self, analysis: Dict[str, Any]) -> str:
        path = os.path.join(self.output_dir, "assessment_summary.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(analysis, f, indent=2)
        return path
