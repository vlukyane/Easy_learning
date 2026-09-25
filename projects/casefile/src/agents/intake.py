"""Intake-агент. Глава 03.

Узкая роль: прочитать заявку и извлечь факты. Возвращает структуру (IntakeResult
в payload), НИКОГДА свободный текст следующему шагу.
"""


def run(claims_path: str) -> dict:
    """Прочитать заявку из claims_path, извлечь факты через LLM. Верни dict-payload IntakeResult."""
    raise NotImplementedError("глава 03: верни IntakeResult, не свободный текст")
