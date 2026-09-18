"""Semantic cache. Chapter 04 — student fills embeddings."""


def lookup(query: str, threshold: float) -> dict | None:
    raise NotImplementedError("chapter 04: embed, exclude self, return neighbor if score >= threshold")


def dump_scores(intents_path: str, out_path: str) -> None:
    raise NotImplementedError("chapter 04: write top-1 neighbor scores without applying a threshold")
