#!/usr/bin/env python3
import argparse
import os
import sys
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from engine.analyzer import GRCAnalyzer
from engine.reporter import GRCReporter

console = Console()

def create_app(analyzer: GRCAnalyzer) -> FastAPI:
    app = FastAPI(title="NIST CSF 2.0 Assessment Dashboard", version="1.0.0")
    analysis_cache = analyzer.analyze()

    static_dir = os.path.join(os.path.dirname(__file__), "static")
    if os.path.exists(static_dir):
        app.mount("/static", StaticFiles(directory=static_dir), name="static")

    @app.get("/", response_class=HTMLResponse)
    async def index():
        index_path = os.path.join(static_dir, "index.html")
        with open(index_path, "r", encoding="utf-8") as f:
            return f.read()

    @app.get("/api/assessment")
    async def get_assessment():
        return analysis_cache

    return app

def print_cli_summary(analysis: dict):
    org = analysis["organization"]
    mat = analysis["overall_maturity"]
    fns = analysis["function_scores"]
    risks = analysis["ranked_risks"]

    console.print()
    console.print(Panel.fit(
        f"[bold blue]NIST Cybersecurity Framework (CSF) 2.0 Assessment[/bold blue]\n"
        f"[bold white]Target:[/bold white] {org['name']} | [bold white]Lead Auditor:[/bold white] {org['lead_auditor']}\n"
        f"[dim]Scope: {', '.join(org['regulatory_scope'])}[/dim]",
        border_style="blue"
    ))

    m_table = Table(title="Enterprise Cybersecurity Maturity Overview", border_style="dim")
    m_table.add_column("Metric", style="bold white")
    m_table.add_column("Value", justify="center", style="bold cyan")
    m_table.add_column("Interpretation", style="dim")

    m_table.add_row("Current Maturity Tier", f"Tier {mat['current_score']} / 4.0", "Risk-Informed (Informal / Partial Gaps)")
    m_table.add_row("Target Maturity Tier", f"Tier {mat['target_score']} / 4.0", "Repeatable & Adaptive (Target Posture)")
    m_table.add_row("Overall Maturity Gap", f"+{mat['overall_gap']} Tiers", "Net maturity improvement required")
    m_table.add_row("Total Remediation Budget", f"€{mat['total_remediation_budget_eur']:,}", "Capital expenditure across Q4 2026 - Q1 2027")
    console.print(m_table)

    f_table = Table(title="NIST CSF 2.0 Core Functions Breakdown", border_style="dim")
    f_table.add_column("Function", style="bold white")
    f_table.add_column("Current Tier", justify="center", style="yellow")
    f_table.add_column("Target Tier", justify="center", style="green")
    f_table.add_column("Gap", justify="center", style="bold cyan")
    f_table.add_column("Status", justify="center")

    for fn, d in fns.items():
        status = "[bold red]ACTION REQ[/bold red]" if d["gap"] >= 1.5 else "[bold green]ON TRACK[/bold green]"
        f_table.add_row(f"{fn} - {d['name']}", str(d["current_tier"]), str(d["target_tier"]), f"+{d['gap']}", status)
    console.print(f_table)

    r_table = Table(title="Top Prioritized Enterprise Risks (Likelihood × Impact)", border_style="dim")
    r_table.add_column("ID", style="bold cyan")
    r_table.add_column("Initiative", style="bold white")
    r_table.add_column("Severity", justify="center")
    r_table.add_column("Score", justify="center", style="bold yellow")
    r_table.add_column("Remediation", style="dim")
    r_table.add_column("Owner", style="dim")
    r_table.add_column("Budget", justify="right", style="bold green")

    for r in risks[:5]:
        sev_badge = f"[bold red]{r['severity']}[/bold red]" if r["severity"] == "CRITICAL" else f"[bold yellow]{r['severity']}[/bold yellow]"
        r_table.add_row(
            r["id"],
            r["title"][:28] + "...",
            sev_badge,
            f"{r['risk_score']}/25",
            r["remediation"][:35] + "...",
            r["owner"],
            f"€{r['cost_eur']:,}"
        )
    console.print(r_table)
    console.print()

def main():
    parser = argparse.ArgumentParser(description="NIST CSF 2.0 GRC Assessment Platform")
    parser.add_argument("-d", "--data", default="data/apexfin_assessment.json", help="Path to assessment JSON")
    parser.add_argument("--serve", action="store_true", help="Launch interactive web dashboard")
    parser.add_argument("--port", type=int, default=8081, help="Web dashboard port (default: 8081)")
    args = parser.parse_args()

    analyzer = GRCAnalyzer(assessment_file=args.data)
    analysis = analyzer.analyze()

    reporter = GRCReporter(output_dir="reports")
    reporter.generate_all(analysis)

    print_cli_summary(analysis)
    console.print("[bold green]✓ Deliverables generated successfully:[/bold green]")
    console.print("  • [underline cyan]reports/Executive_Briefing.md[/underline cyan] (CISO & Board Presentation)")
    console.print("  • [underline cyan]reports/POAM_Remediation_Roadmap.md[/underline cyan] (Engineering Roadmap)")
    console.print("  • [underline cyan]reports/Compliance_Crosswalk.md[/underline cyan] (ISO 27001 & DORA Mapping)")
    console.print("  • [underline cyan]reports/assessment_summary.json[/underline cyan] (Raw Assessment Data)")

    if args.serve:
        console.print(f"\n[bold cyan]Starting Interactive GRC Dashboard on http://0.0.0.0:{args.port}...[/bold cyan]")
        app = create_app(analyzer)
        uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="warning")

if __name__ == "__main__":
    main()
