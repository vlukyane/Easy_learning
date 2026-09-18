from src.contracts import Handoff, PayoutDecision


def test_invalid_handoff_raises():
    try:
        Handoff.model_validate({"from_agent": "intake"})
    except Exception:
        return
    raise AssertionError("invalid handoff must not pass")


def test_valid_handoff():
    Handoff(
        from_agent="intake",
        to_agent="classifier",
        payload={"claim_id": "CLM-001"},
        tokens_used=10,
        cost_usd=0.001,
    )


def test_payout_decision_requires_fields():
    PayoutDecision(claim_id="CLM-001", amount=10.0, approved=False, approver=None)
