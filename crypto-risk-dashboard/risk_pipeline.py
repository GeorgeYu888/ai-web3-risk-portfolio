from __future__ import annotations

import csv
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DB = ROOT / "risk_cases.sqlite"
CSV_PATH = ROOT / "data" / "sample_transactions.csv"


def boolish(value: str) -> bool:
    return value.lower() == "true"


def score(row: dict[str, str]) -> tuple[int, list[str]]:
    amount = float(row["amount_usd"])
    reasons = []
    points = 0
    if amount >= 10000:
        points += 35
        reasons.append("large_value_transfer")
    if boolish(row["new_device"]):
        points += 18
        reasons.append("new_device")
    if boolish(row["failed_attempt"]):
        points += 22
        reasons.append("failed_attempt")
    if boolish(row["country_change"]):
        points += 20
        reasons.append("country_change")
    if boolish(row["withdrawal"]) and amount >= 5000:
        points += 15
        reasons.append("high_value_withdrawal")
    return min(points, 100), reasons


def typology(reasons: list[str]) -> str:
    if "country_change" in reasons and "new_device" in reasons:
        return "account_takeover_signal"
    if "large_value_transfer" in reasons and "high_value_withdrawal" in reasons:
        return "high_value_outflow"
    if "failed_attempt" in reasons:
        return "authentication_or_payment_friction"
    return "standard_review"


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open()))
    with sqlite3.connect(DB) as db:
        db.execute("drop table if exists risk_cases")
        db.execute(
            """
            create table risk_cases (
                tx_id text primary key,
                user_id text,
                timestamp text,
                asset text,
                amount_usd real,
                country text,
                risk_score integer,
                typology text,
                reasons text,
                reviewer_note text
            )
            """
        )
        for row in rows:
            risk_score, reasons = score(row)
            case_type = typology(reasons)
            note = f"Review {row['tx_id']} for {case_type}: {', '.join(reasons) or 'no major flags'}."
            db.execute(
                "insert into risk_cases values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    row["tx_id"],
                    row["user_id"],
                    row["timestamp"],
                    row["asset"],
                    float(row["amount_usd"]),
                    row["country"],
                    risk_score,
                    case_type,
                    ",".join(reasons),
                    note,
                ),
            )
        top_cases = db.execute(
            "select tx_id, user_id, asset, amount_usd, risk_score, typology, reviewer_note from risk_cases order by risk_score desc, amount_usd desc limit 20"
        ).fetchall()
        summary = db.execute(
            "select typology, count(*), round(avg(risk_score), 1), round(sum(amount_usd), 2) from risk_cases group by typology order by count(*) desc"
        ).fetchall()

    html_rows = "\n".join(
        f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>${d:,.0f}</td><td>{e}</td><td>{f}</td><td>{g}</td></tr>"
        for a, b, c, d, e, f, g in top_cases
    )
    summary_rows = "\n".join(
        f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>${d:,.0f}</td></tr>" for a, b, c, d in summary
    )
    (ROOT / "dashboard.html").write_text(
        f"""<!doctype html>
<html><head><meta charset='utf-8'><title>Crypto Risk Dashboard</title>
<style>
body{{font-family:Arial,sans-serif;margin:32px;color:#172033;background:#f6f7f9}}
h1{{margin-bottom:4px}} table{{border-collapse:collapse;width:100%;background:white;margin:16px 0}}
td,th{{border:1px solid #d8dde6;padding:8px;text-align:left;font-size:13px}} th{{background:#101827;color:white}}
.grid{{display:grid;grid-template-columns:1fr 2fr;gap:20px}} .card{{background:white;padding:16px;border:1px solid #d8dde6;border-radius:6px}}
</style></head><body>
<h1>Crypto Risk Dashboard</h1>
<p>Synthetic Binance-style transaction review demo: SQL/Python scoring, typology classification and reviewer notes.</p>
<div class='grid'><div class='card'><h2>KRI Summary</h2><table><tr><th>Typology</th><th>Cases</th><th>Avg score</th><th>Value</th></tr>{summary_rows}</table></div>
<div class='card'><h2>Top Review Queue</h2><table><tr><th>TX</th><th>User</th><th>Asset</th><th>Amount</th><th>Score</th><th>Typology</th><th>Reviewer note</th></tr>{html_rows}</table></div></div>
</body></html>""",
        encoding="utf-8",
    )
    print(f"Wrote {DB} and dashboard.html")


if __name__ == "__main__":
    main()
