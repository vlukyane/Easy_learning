"""Retrieval. Главы 05 и 07.

retrieve_text — по текстовому индексу (baseline). retrieve_hybrid — слияние
text- и image-хитов (например, Reciprocal Rank Fusion) для multimodal-ветки.

Формат хита (dict): {"pdf_id", "page_num", "score", "modality", "image_path"?, "text"?}.
"""

from typing import Any


def retrieve_text(question: str, k: int = 5) -> list[dict[str, Any]]:
    """Топ-k по текстовому индексу. Глава 05."""
    raise NotImplementedError("глава 05: text-only retrieval, верни list хитов")


def retrieve_hybrid(question: str, k: int = 5) -> list[dict[str, Any]]:
    """Слияние text + image хитов (RRF). Глава 07.

    RRF: score = sum(1 / (k0 + rank_i)) по спискам, k0≈60. Возврат — единый
    ранжированный список хитов обеих модальностей.
    """
    raise NotImplementedError("глава 07: RRF-слияние text + image хитов")
