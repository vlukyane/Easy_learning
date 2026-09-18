#!/usr/bin/env python3
"""Fail the process if recall dropped below baseline - epsilon. Chapter 06."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.constants import EPSILON, GATE_SPLIT  # noqa: E402

BASELINE_PATH = ROOT / "eval" / "baseline.json"


def main() -> int:
    baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    try:
        from eval.metrics import evaluate

        current = evaluate(str(ROOT / "eval" / "gold.jsonl"), split=GATE_SPLIT)
    except FileNotFoundError:
        print("GATE_FAIL missing eval/gold.jsonl — copy from gold.jsonl.example and label it")
        return 1
    except NotImplementedError as exc:
        print(f"GATE_FAIL {exc}")
        return 1

    recall = float(current["recall"])
    base = float(baseline["recall"])
    if recall < base - EPSILON:
        print(f"GATE_FAIL recall={recall:.3f} baseline={base:.3f} eps={EPSILON} split={GATE_SPLIT}")
        return 1
    print(f"GATE_OK recall={recall:.3f} baseline={base:.3f} eps={EPSILON} split={GATE_SPLIT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
