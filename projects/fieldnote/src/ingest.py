"""PDF → изображения страниц + текстовый слой. Глава 04-ingestion.

Ingestion сохраняет ДВА представления одной страницы: пиксели (PNG) и текст,
если он есть. Правило главы: не звать VLM «опиши страницу», не выкидывать
страницы без текста, не склеивать PDF в один чанк.

Как (pymupdf, это подсказка, не решение целиком):

    import fitz                      # пакет называется pymupdf, модуль — fitz
    doc = fitz.open(pdf_path)
    page = doc[i]
    pix = page.get_pixmap(dpi=150)   # растр страницы
    pix.save(image_path)             # -> PNG
    text = page.get_text("text")     # текстовый слой, может быть ""
    w, h = page.rect.width, page.rect.height
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Page:
    """Одна страница в двух представлениях. Контракт для index/retrieve/цитат.

    Поля: pdf_id — стабильный id документа; page_num — с 1; image_path — путь к
    PNG; text — текстовый слой ("" допустимо для скана/схемы); width/height — px.
    """

    pdf_id: str
    page_num: int
    image_path: Path
    text: str
    width: int
    height: int


def render_pages(pdf_path: str | Path) -> list[Page]:
    """PDF → список Page. Каждой странице: PNG на диске + текстовый слой.

    Возврат: list[Page]. Страницы без текста тоже включай (text="").
    """
    raise NotImplementedError("глава 04: рендер через pymupdf + текстовый слой; верни list[Page]")


def ingest_pdf(pdf_path: str | Path) -> list[Page]:
    """Обёртка над render_pages (сюда позже добавишь запись sidecar-метаданных)."""
    return render_pages(pdf_path)
