"""PDF → page images + text layer. Chapter 04-ingestion."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Page:
    pdf_id: str
    page_num: int
    image_path: Path
    text: str
    width: int
    height: int


def render_pages(pdf_path: str | Path) -> list[Page]:
    raise NotImplementedError("chapter 04: implement pymupdf render + text layer")


def ingest_pdf(pdf_path: str | Path) -> list[Page]:
    return render_pages(pdf_path)
