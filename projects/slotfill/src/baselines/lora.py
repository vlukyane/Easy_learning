"""Система B: инференс LoRA-адаптера в InvoiceFields. Глава 04.

Тот же выходной объект, что у системы A. Адаптер обучается в train.py на train-срезе.
"""


def run(split: str = "val", limit: int | None = None) -> dict:
    """Прогнать систему B (LoRA) по срезу split. Верни метрики/предсказания. Глава 04."""
    raise NotImplementedError("глава 04: инференс LoRA-адаптера в InvoiceFields")
