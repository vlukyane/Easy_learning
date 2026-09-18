"""Retrieval. Chapters 05 and 07."""

from typing import Any


def retrieve_text(question: str, k: int = 5) -> list[dict[str, Any]]:
    raise NotImplementedError("chapter 05: text-only retrieval")


def retrieve_hybrid(question: str, k: int = 5) -> list[dict[str, Any]]:
    raise NotImplementedError("chapter 07: RRF fusion of text + image hits")
