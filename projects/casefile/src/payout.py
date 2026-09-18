"""Payout is not an LLM step. Chapter 06-hitl."""

from src.contracts import PayoutDecision


def execute_payout(decision: PayoutDecision) -> None:
    if not decision.approved:
        raise PermissionError("payout requires human approval")
    raise NotImplementedError("chapter 06: wire ledger after approval flag is set")
