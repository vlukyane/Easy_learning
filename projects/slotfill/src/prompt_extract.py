"""Система A: извлечение полей промптом. Глава 03.

Промпт few-shot (примеры берём ТОЛЬКО из train) → parse в Pydantic InvoiceFields
→ log_call для учёта стоимости. Выход обязан быть тем же объектом, что у системы B
(LoRA), иначе бенчмарк несравним. baselines/prompt.py вызывает это.
"""

from src.schema import InvoiceFields


def extract(document: str, examples: list | None = None) -> InvoiceFields:
    """Документ → InvoiceFields через few-shot Claude. examples — из train. Глава 03.

    Спарси ответ модели строго в InvoiceFields; залогируй токены/стоимость (log_call).
    """
    raise NotImplementedError("глава 03: few-shot Claude → InvoiceFields; примеры только из train")
