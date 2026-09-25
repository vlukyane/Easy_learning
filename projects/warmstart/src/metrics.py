"""False-hit и экономия. Главы 05 и 08.

false_hit_rate реализован (чистая логика, тест зелёный). eval_layers и
monthly_savings пишешь ты. Формула false-hit не меняется молча: false_hits / semantic_hits.
"""

from __future__ import annotations

from typing import Any


def false_hit_rate(rows: list[dict[str, Any]] | str, threshold: float) -> float:
    """false_hits / semantic_hits при данном пороге.

    Строка: {score, query_intent, neighbor_intent}. Хит, если score >= threshold.
    Ложное попадание — хит, у которого интенты различаются. rows может быть путём
    к JSONL или уже загруженным списком.
    """
    if isinstance(rows, str):
        import json
        from pathlib import Path

        path = Path(rows)
        loaded: list[dict[str, Any]] = []
        with path.open(encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    loaded.append(json.loads(line))
        rows = loaded
    hits = [r for r in rows if r["score"] >= threshold]
    if not hits:
        return 0.0
    false_hits = [r for r in hits if r["query_intent"] != r["neighbor_intent"]]
    return len(false_hits) / len(hits)


def eval_layers(layers: list[str]) -> dict:
    """Hit-rate по каждому слою (exact/normalized/...) на корпусе фраз. Глава 03.

    Возврат: {layer: hit_rate}. Слои exact/normalized считаются без эмбеддингов.
    """
    raise NotImplementedError("глава 03: hit-rate по слоям на корпусе фраз")


def monthly_savings(operating_point: dict | None = None, calls: int = 400_000) -> dict:
    """$ сэкономлено и ожидаемое число ошибок при 400k вызовов/мес. Глава 08.

    Возьми hit-rate и false-hit из рабочей точки: экономия ≈ calls·hit_rate·цена_вызова,
    ошибки ≈ calls·hit_rate·false_hit_rate. Верни оба числа рядом — экономия vs цена ошибок.
    """
    raise NotImplementedError("глава 08: $ экономии и ожидаемые ошибки при 400k/мес")
