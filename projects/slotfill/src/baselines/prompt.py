"""Система A (baseline): извлечение полей промптом. Глава 03.

Тонкая обёртка над prompt_extract.extract по срезу данных. few-shot примеры —
только из train. Test не трогаем до harness (глава 05).
"""


def run(split: str = "val", limit: int | None = None) -> dict:
    """Прогнать систему A по срезу split (обычно val). Верни метрики/предсказания. Глава 03.

    Используй src.prompt_extract.extract; few-shot из train; логируй стоимость.
    """
    raise NotImplementedError("глава 03: few-shot Claude → InvoiceFields; примеры только из train")
