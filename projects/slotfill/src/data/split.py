"""Разбиение train/val/test. Глава 02.

test не трогаем до самого конца. Утечка test в train на синтетике особенно легка —
assert_disjoint защищает от неё (тест test_split зелёный из коробки).
"""

from __future__ import annotations

import json
from pathlib import Path


def assert_disjoint(splits: dict[str, list[str]]) -> None:
    """Кинуть AssertionError, если id пересекаются между train/val/test."""
    train, val, test = set(splits["train"]), set(splits["val"]), set(splits["test"])
    if train & val or train & test or val & test:
        raise AssertionError("train/val/test ids overlap")


def main() -> None:
    """Записать data/splits.json с фиксированным seed (воспроизводимое разбиение). Глава 02."""
    raise NotImplementedError("глава 02: запиши data/splits.json с фиксированным seed")


def load_splits(path: str = "data/splits.json") -> dict:
    """Прочитать splits.json → {"train":[...], "val":[...], "test":[...]}."""
    return json.loads(Path(path).read_text(encoding="utf-8"))
