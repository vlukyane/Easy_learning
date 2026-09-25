"""Оркестратор-FSM. Глава 04.

Путь: intake → classify → fraud → (send_to_human? request_approval) → assess →
payout_gate. На каждом шаге CostClock.add(...) и проверка would_exceed ДО
следующего вызова; пробили потолок — graceful stop с частичным результатом.
Выплата — только через payout.execute_payout.
"""


def run_claim(claim_id: str) -> dict:
    """Провести одну заявку по FSM: сначала линейно, потом ветка high-fraud. Глава 04.

    Возврат: трасса (шаги, стоимость, send_to_human, approved, итог).
    """
    raise NotImplementedError("глава 04: линейный FSM, затем ветка high-fraud")


def run_batch(claims_path: str = "data/claims.jsonl", limit_usd: float = 0.15) -> dict:
    """Прогнать пачку под общим потолком; собрать числа. Глава 07.

    Возврат: 50–100 заявок, инварианты (0 выплат без approval), ¢/claim, доля ceiling-stop.
    """
    raise NotImplementedError("глава 07: 50–100 заявок, инварианты, ¢/claim")
