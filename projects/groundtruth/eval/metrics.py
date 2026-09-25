"""Метрики и валидация золота. Главы 03–05.

recall@k / precision@k / MRR и validate_gold реализованы (тесты зелёные).
evaluate и write_baseline пишешь ты. Главная метрика проекта — recall@k:
пропустить релевантный прецедент хуже, чем показать лишний.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.constants import K


def recall_at_k(relevant: list[str], retrieved: list[str], k: int = K) -> float:
    """Доля релевантных, попавших в топ-k. Главная метрика проекта."""
    if not relevant:
        return 0.0
    top = set(retrieved[:k])
    return len(set(relevant) & top) / len(set(relevant))


def precision_at_k(relevant: list[str], retrieved: list[str], k: int = K) -> float:
    """Доля топ-k, оказавшихся релевантными."""
    top = retrieved[:k]
    if not top:
        return 0.0
    hits = len(set(relevant) & set(top))
    return hits / len(top)


def mrr(relevant: list[str], retrieved: list[str]) -> float:
    """Mean reciprocal rank: 1/позиция первого релевантного (0, если его нет)."""
    rel = set(relevant)
    for i, doc_id in enumerate(retrieved, start=1):
        if doc_id in rel:
            return 1.0 / i
    return 0.0


def validate_gold(path: str) -> None:
    """Проверить формат золота: поля qid/query/relevant_ids/split, split ∈ {dev, heldout}."""
    n = 0
    with Path(path).open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            for key in ("qid", "query", "relevant_ids", "split"):
                if key not in row:
                    raise ValueError(f"missing {key}")
            if row["split"] not in {"dev", "heldout"}:
                raise ValueError(f"bad split {row['split']}")
            n += 1
    if n == 0:
        raise ValueError("empty gold")
    print(f"gold ok: {n} queries")


def evaluate(gold_path: str, split: str = "dev") -> dict[str, Any]:
    """Средние recall@k / precision@k / MRR по сплиту. Глава 04.

    Для каждого запроса сплита: retrieve(query) → сравни с relevant_ids. Возврат
    (dict): {"recall","precision","mrr","n_queries","k"} — эту форму читает ci_eval.
    """
    raise NotImplementedError("глава 04: средние recall@k / precision@k / MRR по сплиту")


def write_baseline(gold_path: str, out_path: str) -> None:
    """Записать eval/baseline.json из evaluate(). Глава 05.

    Только скриптом (числа руками не правят). Гейт сравнивает текущий recall с этим baseline.
    """
    raise NotImplementedError("глава 05: запись eval/baseline.json только скриптом")
