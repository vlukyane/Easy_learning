import re

INVISIBLE = re.compile(r"[\u200b\u200c\u200d\u2060\ufeff]")


def sanitize(text: str) -> str:
    """Вычистить невидимые символы (нулевой ширины). Глава 04.

    Один слой защиты. Ученик расширяет: метаданные PDF, alt-тексты, unicode-трюки —
    именно там прячут инъекции, которые человек в превью не увидит.
    """
    return INVISIBLE.sub("", text)
