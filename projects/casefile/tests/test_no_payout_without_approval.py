from src.contracts import PayoutDecision
from src.payout import execute_payout


def test_no_payout_without_approval():
    decision = PayoutDecision(claim_id="CLM-001", amount=500.0, approved=False)
    try:
        execute_payout(decision)
    except PermissionError:
        return
    raise AssertionError("payout without approval must fail")
