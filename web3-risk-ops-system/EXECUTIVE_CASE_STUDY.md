# Executive Case Study - Web3 Risk Operations System

## Business Problem

Crypto-facing platforms do not see risk as one clean stream. A weekly operations queue can contain account takeover signals, stale KYC/KYB records, high-risk wallet exposure, payment fraud, market-conduct anomalies and customer-support escalations at the same time.

This project shows how I would turn those mixed signals into a practical risk operations view.

## What The System Does

The Python pipeline generates 240 synthetic weekly events and converts them into a unified case queue. Each case receives:

- scenario classification
- explainable score
- priority level
- review queue
- signal list
- recommended action
- bounded reviewer note

The workflow then writes the results to SQLite and generates:

- `dashboard.html` for manager review
- `weekly_risk_report.md` for narrative reporting
- `weekly_risk_report.html` for browser review
- `risk_ops_review_queries.sql` for analyst follow-up queries
- `data/events.csv` as synthetic source evidence

## Scenarios Covered

| Scenario | Example signals | Review queue |
|---|---|---|
| Account takeover | new device, geo velocity, repeated failed login | ATO / account security |
| KYC/KYB review | stale profile, high-value activity | KYC / KYB operations |
| Wallet exposure | high wallet risk, large outflow | Blockchain risk review |
| Payment fraud | chargeback cluster, payment loss pattern | Payments fraud |
| Market conduct | large value, price deviation | Market surveillance |
| Support escalation | confusion, complaint risk, Mandarin support need | Customer risk education |

## Why This Is Useful For Target Roles

For Binance/Web3 risk roles, this is evidence of practical queue review, escalation discipline and crypto risk awareness.

For AI/KYC/KYB roles, it shows human-review boundaries, structured reviewer notes and repeatable case logic.

For payments/fraud/identity roles, it shows how payment abuse and account-security signals can be separated from ordinary customer friction.

For analyst roles more broadly, it shows Python, SQL, dashboard reporting and written risk communication in one connected workflow.

## Truth Boundary

All data is synthetic. This project does not claim formal exchange, broker, AML/CTF, sanctions, market-surveillance, law-enforcement or professional trading employment. It is proof-of-work for entry-level or early-career risk operations applications.
