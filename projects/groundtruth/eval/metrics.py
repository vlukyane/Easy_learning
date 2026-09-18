"""Metrics and gold validation. Chapters 03–05."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.constants import K


def recall_at_k(relevant: list[str], retrieved: list[str], k: int = K) -> float:
    if not relevant:
        return 0.0
    top = set(retrieved[:k])
    return len(set(relevant) & top) / len(set(relevant))


def precision_at_k(relevant: list[str], retrieved: list[str], k: int = K) -> float:
    top = retrieved[:k]
    if not top:
        return 0.0
    hits = len(set(relevant) & set(top))
    return hits / len(top)


def mrr(relevant: list[str], retrieved: list[str]) -> float:
    rel = set(relevant)
    for i, doc_id in enumerate(retrieved, start=1):
        if doc_id in rel:
            return 1.0 / i
    return 0.0


def validate_gold(path: str) -> None:
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
    raise NotImplementedError("chapter 04: mean recall@k / precision@k / MRR on split")


def write_baseline(gold_path: str, out_path: str) -> None:
    raise NotImplementedError("chapter 05: script-only write of eval/baseline.json")
