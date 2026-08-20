from __future__ import annotations

CASES = [
    {"id": "C001", "text": "User reports a withdrawal after a login from a new country and cannot access account."},
    {"id": "C002", "text": "Customer asks why KYC review is taking longer after submitting address proof."},
    {"id": "C003", "text": "Multiple failed card attempts followed by a high value crypto purchase."},
    {"id": "C004", "text": "Mandarin-speaking user asks how to understand risk warning before transfer."},
]


def classify(text: str) -> tuple[str, str, list[str]]:
    lower = text.lower()
    reasons = []
    if "new country" in lower or "cannot access" in lower:
        reasons.append("possible account takeover")
    if "failed card" in lower or "high value" in lower:
        reasons.append("payment abuse / high value risk")
    if "kyc" in lower or "address proof" in lower:
        reasons.append("kyc queue delay")
    if "mandarin" in lower or "risk warning" in lower:
        reasons.append("bilingual education need")
    priority = "high" if any("takeover" in r or "high value" in r for r in reasons) else "normal"
    queue = "risk_review" if priority == "high" else "customer_operations"
    return queue, priority, reasons or ["standard enquiry"]


def reviewer_note(case: dict[str, str]) -> str:
    queue, priority, reasons = classify(case["text"])
    return (
        f"{case['id']} -> queue={queue}, priority={priority}. "
        f"Rationale: {', '.join(reasons)}. "
        "Next step: verify account/customer facts, document evidence, avoid over-promising, and escalate if risk remains unresolved."
    )


if __name__ == "__main__":
    for case in CASES:
        print(reviewer_note(case))
