"""Часы стоимости. Глава 05-cost-ceiling.

Агенты зацикливаются и жгут токены — CostClock копит стоимость и даёт
оркестратору решить, не пора ли остановиться (would_exceed) до следующего вызова.
Цены — примерные, USD за 1M токенов; поправь под актуальный прайс.
"""

from __future__ import annotations

PRICE_PER_MTOK = {
    "claude-haiku-4-5-20251001": {"in": 0.8, "out": 4.0},
}


class CostClock:
    """Накопитель стоимости с потолком limit_usd."""

    def __init__(self, limit_usd: float) -> None:
        self.limit_usd = limit_usd
        self.spent = 0.0

    def add(self, tokens_in: int, tokens_out: int, model: str) -> float:
        """Учесть вызов, вернуть его стоимость. Неизвестная модель → цена Haiku."""
        table = PRICE_PER_MTOK.get(model, PRICE_PER_MTOK["claude-haiku-4-5-20251001"])
        delta = tokens_in / 1_000_000 * table["in"] + tokens_out / 1_000_000 * table["out"]
        self.spent += delta
        return delta

    def would_exceed(self, extra: float = 0.0) -> bool:
        """Пробьёт ли потолок следующий вызов ценой extra. Проверяй ДО вызова."""
        return self.spent + extra > self.limit_usd
