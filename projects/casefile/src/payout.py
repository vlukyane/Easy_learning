"""Выплата — не LLM-шаг. Глава 06-hitl.

Единственная дверь к выплате. Инвариант проекта: без approved=True выплата
физически невозможна (кидает PermissionError). Оркестратор обязан платить ТОЛЬКО
через эту функцию — тогда инвариант держит всю систему.
"""

from src.contracts import PayoutDecision


def execute_payout(decision: PayoutDecision) -> None:
    """Провести выплату. PermissionError, если решение не одобрено человеком.

    Проверку approved НЕ снимай — на ней стоит tests/test_no_payout_without_approval.
    """
    if not decision.approved:
        raise PermissionError("payout requires human approval")
    raise NotImplementedError("глава 06: проведи выплату в ledger после установки approved")
