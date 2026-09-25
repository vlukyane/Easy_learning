"""Retrieval. Глава 02.

Возврат — ранжированный список doc_id. Детерминизм обязателен: гейт сравнивает
recall с baseline, а недетерминированный retrieve делает гейт флаки (ложные падения PR).
"""

from src.constants import K


def retrieve(query: str, k: int = K) -> list[str]:
    """Вернуть ранжированный список doc_id по запросу. Должен быть детерминированным. Глава 02."""
    raise NotImplementedError("глава 02: верни ранжированные doc_id; строго детерминированно")
