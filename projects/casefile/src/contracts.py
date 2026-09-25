"""Типизированные хендоффы. Глава 02-contracts.

Смысл проекта: агенты обмениваются НЕ свободным текстом, а валидируемыми
моделями отсюда. Кривой payload → падение на шаге, а не «молча поехало дальше».
Каждый агент кладёт результат в Handoff.payload и передаёт следующему.
"""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class ClaimIntake(BaseModel):
    """Сырьё из data/claims.jsonl — входная заявка до обработки."""

    claim_id: str
    narrative: str
    claimed_amount: float
    incident_date: str
    attachments_meta: list[str] = Field(default_factory=list)


class IntakeResult(BaseModel):
    """Выход intake-агента: заявка + извлечённые факты."""

    claim_id: str
    narrative: str
    claimed_amount: float
    incident_date: str
    facts: list[str]


class ClassifierResult(BaseModel):
    """Выход classifier-агента: тип, приоритет, уверенность."""

    claim_id: str
    claim_type: str
    priority: Literal["low", "medium", "high"]
    confidence: float


class FraudResult(BaseModel):
    """Выход fraud-агента. send_to_human=True уводит заявку к человеку."""

    claim_id: str
    risk: Literal["low", "medium", "high"]
    flags: list[str]
    send_to_human: bool


class Assessment(BaseModel):
    """Выход assessor-агента: рекомендованная сумма + факты-обоснование (не выплата)."""

    claim_id: str
    recommended_payout: float
    rationale_facts: list[str]


class Handoff(BaseModel):
    """Конверт хендоффа между агентами: кто→кому, payload и учтённая стоимость."""

    from_agent: str
    to_agent: str
    payload: dict[str, Any]
    tokens_used: int = 0
    cost_usd: float = 0.0


class PayoutDecision(BaseModel):
    """Решение о выплате — единственное, на основании чего payout.execute_payout платит.

    approved=False обязано блокировать выплату (см. tests/test_no_payout_without_approval).
    """

    claim_id: str
    amount: float
    approved: bool
    approver: str | None = None
