"""Eval harness. Chapters 03, 05, 08."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REQUIRED_GOLD_FIELDS = {"id", "question", "kind", "pdf", "page", "answer"}


def validate_gold(path: str | Path) -> None:
    kinds: set[str] = set()
    n = 0
    with Path(path).open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            missing = REQUIRED_GOLD_FIELDS - set(row)
            if missing:
                raise ValueError(f"gold row missing {missing}: {row.get('id')}")
            if row["kind"] not in {"text", "visual"}:
                raise ValueError(f"bad kind for {row['id']}")
            if int(row["page"]) < 1:
                raise ValueError(f"page must be >= 1 for {row['id']}")
            kinds.add(row["kind"])
            n += 1
    if n == 0:
        raise ValueError("empty gold file")
    if kinds != {"text", "visual"}:
        raise ValueError(f"gold must include both kinds, got {kinds}")
    print(f"gold ok: {n} rows, kinds={sorted(kinds)}")


def require_split_metrics(report: dict[str, Any]) -> None:
    """Flat accuracy is forbidden — both question kinds must be present."""
    if "accuracy" in report and "text" not in report:
        raise AssertionError("do not collapse text/visual into a single accuracy")
    for kind in ("text", "visual"):
        if kind not in report:
            raise AssertionError(f"missing kind {kind}")
        block = report[kind]
        for system in ("text_only", "multimodal"):
            if system not in block:
                raise AssertionError(f"missing {system} for {kind}")


def run_text_only(gold_path: str) -> dict[str, Any]:
    raise NotImplementedError("chapter 05: accuracy_text and accuracy_visual for text-only RAG")


def run_all(gold_path: str) -> dict[str, Any]:
    raise NotImplementedError("chapter 08: write logs/eval-report.json with four cells + visual ratio")
