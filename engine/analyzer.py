import json
import os
from typing import Dict, Any, List

FUNCTION_NAMES = {
    "GV": "GOVERN",
    "ID": "IDENTIFY",
    "PR": "PROTECT",
    "DE": "DETECT",
    "RS": "RESPOND",
    "RC": "RECOVER"
}

class GRCAnalyzer:
    def __init__(self, assessment_file: str = "data/apexfin_assessment.json"):
        self.assessment_file = assessment_file
        with open(assessment_file, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def analyze(self) -> Dict[str, Any]:
        org = self.data["organization"]
        controls = self.data["controls"]

        function_metrics = {fn: {"current_sum": 0.0, "target_sum": 0.0, "count": 0} for fn in FUNCTION_NAMES}
        all_subcategories = []
        total_budget = 0
        owner_costs = {}
        qtr_costs = {}

        for c in controls:
            fn = c["function_id"]
            for sub in c["subcategories"]:
                curr = sub["current_tier"]
                tgt = sub["target_tier"]
                function_metrics[fn]["current_sum"] += curr
                function_metrics[fn]["target_sum"] += tgt
                function_metrics[fn]["count"] += 1

                likelihood = sub.get("likelihood", 3)
                impact = sub.get("impact", 3)
                risk_score = likelihood * impact

                if risk_score >= 20:
                    severity = "CRITICAL"
                elif risk_score >= 12:
                    severity = "HIGH"
                elif risk_score >= 6:
                    severity = "MEDIUM"
                else:
                    severity = "LOW"

                cost = sub.get("estimated_cost_eur", 0)
                total_budget += cost

                owner = sub.get("owner", "Unassigned")
                owner_costs[owner] = owner_costs.get(owner, 0) + cost

                qtr = sub.get("target_qtr", "TBD")
                qtr_costs[qtr] = qtr_costs.get(qtr, 0) + cost

                item = {
                    "function_id": fn,
                    "function_name": FUNCTION_NAMES[fn],
                    "category_id": c["category_id"],
                    "id": sub["id"],
                    "title": sub["title"],
                    "current_tier": curr,
                    "target_tier": tgt,
                    "gap_tier": round(tgt - curr, 1),
                    "evidence": sub["evidence"],
                    "gap": sub["gap"],
                    "likelihood": likelihood,
                    "impact": impact,
                    "risk_score": risk_score,
                    "severity": severity,
                    "remediation": sub["remediation"],
                    "owner": owner,
                    "cost_eur": cost,
                    "target_qtr": qtr,
                    "compliance": sub.get("compliance_mappings", {})
                }
                all_subcategories.append(item)

        function_scores = {}
        overall_curr_sum = 0.0
        overall_tgt_sum = 0.0
        total_controls = 0

        for fn, metrics in function_metrics.items():
            cnt = metrics["count"]
            if cnt > 0:
                c_avg = round(metrics["current_sum"] / cnt, 2)
                t_avg = round(metrics["target_sum"] / cnt, 2)
            else:
                c_avg = 0.0
                t_avg = 0.0
            function_scores[fn] = {
                "name": FUNCTION_NAMES[fn],
                "current_tier": c_avg,
                "target_tier": t_avg,
                "gap": round(t_avg - c_avg, 2),
                "count": cnt
            }
            overall_curr_sum += metrics["current_sum"]
            overall_tgt_sum += metrics["target_sum"]
            total_controls += cnt

        overall_maturity = {
            "current_score": round(overall_curr_sum / total_controls, 2) if total_controls > 0 else 0.0,
            "target_score": round(overall_tgt_sum / total_controls, 2) if total_controls > 0 else 0.0,
            "overall_gap": round((overall_tgt_sum - overall_curr_sum) / total_controls, 2) if total_controls > 0 else 0.0,
            "total_evaluated_controls": total_controls,
            "total_remediation_budget_eur": total_budget
        }

        sorted_risks = sorted(all_subcategories, key=lambda x: x["risk_score"], reverse=True)

        return {
            "organization": org,
            "overall_maturity": overall_maturity,
            "function_scores": function_scores,
            "poam_by_owner": owner_costs,
            "poam_by_quarter": qtr_costs,
            "ranked_risks": sorted_risks
        }
