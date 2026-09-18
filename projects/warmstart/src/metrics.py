"""False-hit and savings. Chapters 05 and 08."""

from __future__ import annotations

from typing import Any


def false_hit_rate(rows: list[dict[str, Any]] | str, threshold: float) -> float:
    """false_hits / semantic_hits at this threshold.

    Each row: {score, query_intent, neighbor_intent}.
    Hit if score >= threshold. False-hit if hit and intents differ.
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
    raise NotImplementedError("chapter 03: hit-rate per layer on the phrase corpus")


def monthly_savings(operating_point: dict | None = None, calls: int = 400_000) -> dict:
    raise NotImplementedError("chapter 08: $ saved and expected errors at 400k/month")
