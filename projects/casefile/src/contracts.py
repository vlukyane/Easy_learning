"""Typed handoffs. Chapter 02-contracts."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class ClaimIntake(BaseModel):
    claim_id: str
    narrative: str
    claimed_amount: float
    incident_date: str
    attachments_meta: list[str] = Field(default_factory=list)


class IntakeResult(BaseModel):
    claim_id: str
    narrative: str
    claimed_amount: float
    incident_date: str
    facts: list[str]


class ClassifierResult(BaseModel):
    claim_id: str
    claim_type: str
    priority: Literal["low", "medium", "high"]
    confidence: float


class FraudResult(BaseModel):
    claim_id: str
    risk: Literal["low", "medium", "high"]
    flags: list[str]
    send_to_human: bool


class Assessment(BaseModel):
    claim_id: str
    recommended_payout: float
    rationale_facts: list[str]


class Handoff(BaseModel):
    from_agent: str
    to_agent: str
    payload: dict[str, Any]
    tokens_used: int = 0
    cost_usd: float = 0.0


class PayoutDecision(BaseModel):
    claim_id: str
    amount: float
    approved: bool
    approver: str | None = None
