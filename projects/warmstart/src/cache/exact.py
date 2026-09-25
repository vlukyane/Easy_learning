"""Точный кэш (слой 1). Главы 03 и 07 (TTL).

Ключ — сырой запрос. Безопасный слой без ложных попаданий, но и хит-рейт низкий.
TTL защищает от устаревших ответов (устаревший ответ = ложное попадание во времени).
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class CacheEntry:
    """Запись кэша: ответ, к какому интенту он относится, когда закэширован, TTL."""

    answer: str
    intent_id: str
    cached_at: datetime
    ttl_seconds: int = 7 * 24 * 3600


_STORE: dict[str, CacheEntry] = {}


def lookup(key: str, now: datetime | None = None) -> CacheEntry | None:
    """Вернуть живую запись по точному ключу или None (протухшую считаем промахом)."""
    now = now or datetime.now(timezone.utc)
    entry = _STORE.get(key)
    if entry is None:
        return None
    age = (now - entry.cached_at).total_seconds()
    if age > entry.ttl_seconds:
        return None
    return entry


def put(key: str, entry: CacheEntry) -> None:
    """Положить запись по точному ключу."""
    _STORE[key] = entry
