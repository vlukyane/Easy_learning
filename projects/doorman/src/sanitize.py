import re

INVISIBLE = re.compile(r"[\u200b\u200c\u200d\u2060\ufeff]")


def sanitize(text: str) -> str:
    """Drop zero-width characters; student extends with metadata stripping."""
    return INVISIBLE.sub("", text)
