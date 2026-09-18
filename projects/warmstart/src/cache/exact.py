"""Exact cache. Chapters 03 and 07 (TTL)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class CacheEntry:
    answer: str
    intent_id: str
    cached_at: datetime
    ttl_seconds: int = 7 * 24 * 3600


_STORE: dict[str, CacheEntry] = {}


def lookup(key: str, now: datetime | None = None) -> CacheEntry | None:
    now = now or datetime.now(timezone.utc)
    entry = _STORE.get(key)
    if entry is None:
        return None
    age = (now - entry.cached_at).total_seconds()
    if age > entry.ttl_seconds:
        return None
    return entry


def put(key: str, entry: CacheEntry) -> None:
    _STORE[key] = entry
