"""Normalized cache keys. Chapter 03."""

import re

_STOP = {"the", "a", "an", "please", "pls"}


def normalize(text: str) -> str:
    lowered = text.lower()
    stripped = re.sub(r"[^\w\s]", " ", lowered)
    tokens = [t for t in stripped.split() if t and t not in _STOP]
    return " ".join(tokens)
