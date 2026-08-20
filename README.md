# AI + Web3 Risk Portfolio - George Yu

This portfolio supports applications for AI/Data/Web3 risk operations roles.

It focuses on practical analyst workflows rather than abstract machine-learning theory:

- define messy data clearly
- classify cases into useful typologies
- use Python/SQL-style processing
- create dashboards that a reviewer or manager can act on
- keep AI-assisted notes auditable and bounded

## Projects

1. `crypto-risk-dashboard` - synthetic transaction risk scoring and KRI dashboard.
2. `ai-ops-workflow-agent` - case classification and reviewer-note generation demo.
3. `operations-data-dashboard` - operational service data dashboard showing issue mix and turnaround patterns.

## Current Application Mapping

The portfolio is now mapped directly to the current target queue:

- Binance risk / AI-KYB-KYC roles: transaction review, KRI reporting, AI workflow testing and reviewer-note discipline.
- PointsBet payments / fraud / identity: payment-risk signals, behavioural anomaly review and issue escalation.
- DigiCert authentication analyst: document/process review, suspicious-case escalation and bilingual customer explanation.
- Airwallex credit risk operations: client monitoring, account-history review, exception lists and SQL-style analysis.
- AustralianSuper AML/CTF & fraud: transaction monitoring, EDD-style review, fraud trend analysis and control reporting mindset.

See `ROLE_MAPPING.md` and `INTERVIEW_PLAYBOOK.md` for the recruiter-facing explanation and interview defence.

## Recruiter Readme

For a risk, fraud, compliance operations, or AI workflow reviewer, the useful signal is not that this repo uses complicated tooling. The signal is that each demo follows a practical analyst loop:

1. turn raw events into a reviewable case queue
2. define explainable risk signals
3. separate case typologies instead of treating every issue as the same
4. create concise reviewer notes
5. expose KRIs in a dashboard so a manager can see where risk is building

The crypto demo is synthetic, but the workflow mirrors real entry-level risk work: review queues, abnormal activity indicators, account and transaction context, documentation quality, and escalation logic.

## Positioning

These projects are intentionally small and readable. They show how I approach Binance-style risk analyst work: queue review, abnormal activity signals, data aggregation, risk typology, clear notes and responsible use of AI.

No real customer, exchange, banking or employer data is included.

## Quick Run

```bash
python3 crypto-risk-dashboard/risk_pipeline.py
sqlite3 crypto-risk-dashboard/risk_cases.sqlite < crypto-risk-dashboard/risk_review_queries.sql
python3 ai-ops-workflow-agent/workflow_agent.py
python3 operations-data-dashboard/operations_dashboard.py
```

Generated HTML dashboards are committed so a reviewer can inspect the output without running the scripts.

The SQL file is included to show the review questions an analyst would ask after the Python pipeline creates the case table.

## Static Portfolio Page

Open `index.html` or `portfolio.html` for a recruiter-facing summary of the proof-of-work. This is ready for GitHub Pages or any static host once the repository is published.
