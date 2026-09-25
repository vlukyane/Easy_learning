"""Единый harness скоринга. Глава 05.

Одно правило успеха для A и B — формулы живут ЗДЕСЬ, их не копипастят в train.py
и не «чуть-чуть» меняют между системами. field_level_accuracy и exact_doc_match
реализованы (чистая логика); run_test — оркестрация, пишешь ты.

Поля сравниваются как dict {имя_поля: значение}; приведи предсказание и золото к
такому виду (например InvoiceFields.model_dump()) перед скорингом.
"""

from __future__ import annotations

from typing import Any


def field_level_accuracy(pred: dict[str, Any], gold: dict[str, Any]) -> float:
    """Доля полей золота, совпавших с предсказанием (по значению, точное сравнение)."""
    if not gold:
        return 0.0
    hits = sum(1 for k, v in gold.items() if pred.get(k) == v)
    return hits / len(gold)


def exact_doc_match(pred: dict[str, Any], gold: dict[str, Any]) -> bool:
    """True, только если ВСЕ поля золота совпали (документ верен целиком)."""
    return all(pred.get(k) == v for k, v in gold.items())


def run_test(backends: list[str]) -> dict:
    """Загрузить test id → прогнать A/B → parse → метрики → JSON. Глава 05.

    Один и тот же test-набор и один и тот же parse для обеих систем.
    """
    raise NotImplementedError("глава 05: один harness, те же test id и parser для A и B")
