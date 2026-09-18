from __future__ import annotations

import json
from pathlib import Path


def assert_disjoint(splits: dict[str, list[str]]) -> None:
    train, val, test = set(splits["train"]), set(splits["val"]), set(splits["test"])
    if train & val or train & test or val & test:
        raise AssertionError("train/val/test ids overlap")


def main() -> None:
    raise NotImplementedError("chapter 02: write data/splits.json with a fixed seed")


def load_splits(path: str = "data/splits.json") -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))
