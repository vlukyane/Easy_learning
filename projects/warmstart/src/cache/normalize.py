"""Нормализованный ключ кэша (слой 2). Глава 03.

Приводит запросы к одной форме (регистр, пунктуация, стоп-слова) — ловит больше
попаданий, чем точный слой, всё ещё без семантического риска.
"""

import re

_STOP = {"the", "a", "an", "please", "pls"}


def normalize(text: str) -> str:
    """Lowercase → убрать пунктуацию → выкинуть стоп-слова → склеить токены пробелом.

    Пример: "Please, how do I RESET the password?" → "how do i reset password".
    """
    lowered = text.lower()
    stripped = re.sub(r"[^\w\s]", " ", lowered)
    tokens = [t for t in stripped.split() if t and t not in _STOP]
    return " ".join(tokens)
