from __future__ import annotations

import random
from collections import Counter, defaultdict
from pathlib import Path

random.seed(21)
ROOT = Path(__file__).resolve().parent
sources = ["front_counter", "collection_box", "commercial_client", "phone_request"]
issues = ["on_time", "delayed", "complaint", "rework", "inventory_needed"]
owners = ["site_manager", "front_counter", "supplier_followup", "driver", "operations"]

rows = []
for i in range(180):
    source = random.choice(sources)
    issue = random.choices(issues, weights=[52, 18, 10, 8, 12])[0]
    rows.append({
        "order_id": f"O{i+1:04d}",
        "source": source,
        "issue": issue,
        "turnaround_days": random.randint(1, 6) + (2 if issue in {"delayed", "rework"} else 0),
        "owner": random.choice(owners),
    })

by_issue = Counter(r["issue"] for r in rows)
avg_by_source = defaultdict(list)
for r in rows:
    avg_by_source[r["source"]].append(r["turnaround_days"])

issue_rows = "\n".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in by_issue.most_common())
source_rows = "\n".join(
    f"<tr><td>{k}</td><td>{sum(v)/len(v):.1f}</td><td>{len(v)}</td></tr>" for k, v in sorted(avg_by_source.items())
)
html = f"""<!doctype html><html><head><meta charset='utf-8'><title>Operations Data Dashboard</title>
<style>body{{font-family:Arial,sans-serif;margin:32px;background:#f6f7f9;color:#172033}}table{{border-collapse:collapse;width:100%;background:white}}td,th{{border:1px solid #d8dde6;padding:8px}}th{{background:#172033;color:white}}.grid{{display:grid;grid-template-columns:1fr 1fr;gap:20px}}</style>
</head><body><h1>Operations Data Dashboard</h1><p>Synthetic service data: source, issue type, turnaround and action ownership.</p>
<div class='grid'><section><h2>Issue mix</h2><table><tr><th>Issue</th><th>Count</th></tr>{issue_rows}</table></section>
<section><h2>Turnaround by source</h2><table><tr><th>Source</th><th>Avg days</th><th>Orders</th></tr>{source_rows}</table></section></div>
</body></html>"""
Path(ROOT / "operations_dashboard.html").write_text(html, encoding="utf-8")
print("Wrote operations_dashboard.html")
