"""HITL-гейт перед необратимым действием. Глава 06.

request_approval превращает Assessment в PayoutDecision через решение человека.
В проде это внешний шаг; в курсе достаточно CLI input(). Безопасный дефолт:
всё, кроме явного согласия, → approved=False.
"""

from src.contracts import Assessment, PayoutDecision


def request_approval(assessment: Assessment) -> PayoutDecision:
    """Спросить человека и вернуть PayoutDecision. Глава 06.

    Пример: ответ 'y' → approved=True, approver="cli"; иначе approved=False.
    """
    raise NotImplementedError("глава 06: CLI input() → PayoutDecision(approved=...)")
