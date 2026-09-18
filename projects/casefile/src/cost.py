"""Cost clock. Chapter 05-cost-ceiling."""

from __future__ import annotations

PRICE_PER_MTOK = {
    "claude-haiku-4-5-20251001": {"in": 0.8, "out": 4.0},
}


class CostClock:
    def __init__(self, limit_usd: float) -> None:
        self.limit_usd = limit_usd
        self.spent = 0.0

    def add(self, tokens_in: int, tokens_out: int, model: str) -> float:
        table = PRICE_PER_MTOK.get(model, PRICE_PER_MTOK["claude-haiku-4-5-20251001"])
        delta = tokens_in / 1_000_000 * table["in"] + tokens_out / 1_000_000 * table["out"]
        self.spent += delta
        return delta

    def would_exceed(self, extra: float = 0.0) -> bool:
        return self.spent + extra > self.limit_usd
