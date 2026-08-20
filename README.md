# AI + Web3 Risk Portfolio - George Yu

This portfolio supports applications for AI, Web3, fraud, payments, KYC/KYB, identity and risk operations roles.

The main project is a connected Web3 risk operations system, not a single student-style demo. It creates synthetic events across six realistic crypto/platform-risk scenarios, turns them into a unified review queue, stores them in SQLite, generates a manager dashboard, and writes a weekly risk report.

## Main Project

`web3-risk-ops-system` is the primary proof-of-work.

It covers:

- account takeover and login anomalies
- KYC/KYB review and enhanced due diligence triggers
- wallet exposure and high-risk transfer review
- card/payment abuse and chargeback clusters
- market-conduct anomaly review
- customer support escalation and bilingual education needs

Generated outputs:

- `web3-risk-ops-system/dashboard.html` - operational risk dashboard
- `web3-risk-ops-system/weekly_risk_report.md` - weekly risk report
- `web3-risk-ops-system/weekly_risk_report.html` - browser-readable report
- `web3-risk-ops-system/EXECUTIVE_CASE_STUDY.md` - recruiter-facing case study
- `web3-risk-ops-system/web3_risk_ops.sqlite` - case queue database
- `web3-risk-ops-system/risk_ops_review_queries.sql` - analyst review query pack
- `web3-risk-ops-system/data/events.csv` - synthetic source events

## Supporting Projects

1. `crypto-risk-dashboard` - focused synthetic transaction monitoring and KRI dashboard.
2. `ai-ops-workflow-agent` - case classification and bounded reviewer-note generation.
3. `operations-data-dashboard` - operational service dashboard showing issue mix, turnaround and follow-up patterns.

## Current Application Mapping

The portfolio is mapped directly to the current target queue:

- Binance risk / AI-KYB-KYC roles: account security, KYC/KYB triggers, wallet exposure review, market-conduct signals, AI workflow testing and reviewer-note discipline.
- PointsBet payments / fraud / identity: payment-risk signals, chargeback clusters, behavioural anomaly review and issue escalation.
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

The data is synthetic, but the workflow mirrors real entry-level risk work: review queues, abnormal activity indicators, account and transaction context, documentation quality, escalation logic, management reporting and evidence boundaries.

## Positioning

The main system is intentionally practical and readable. It shows how I approach Binance-style risk analyst work: queue review, abnormal activity signals, data aggregation, risk typology, clear notes, operational reporting and responsible use of AI.

No real customer, exchange, banking or employer data is included.

## Quick Run

```bash
python3 web3-risk-ops-system/web3_risk_ops_pipeline.py
sqlite3 web3-risk-ops-system/web3_risk_ops.sqlite < web3-risk-ops-system/risk_ops_review_queries.sql
python3 crypto-risk-dashboard/risk_pipeline.py
sqlite3 crypto-risk-dashboard/risk_cases.sqlite < crypto-risk-dashboard/risk_review_queries.sql
python3 ai-ops-workflow-agent/workflow_agent.py
python3 operations-data-dashboard/operations_dashboard.py
```

Generated HTML dashboards are committed so a reviewer can inspect the output without running the scripts.

The SQL file is included to show the review questions an analyst would ask after the Python pipeline creates the case table.

## Static Portfolio Page

Open `index.html` or `portfolio.html` for a recruiter-facing summary of the proof-of-work. This is ready for GitHub Pages or any static host once the repository is published.
