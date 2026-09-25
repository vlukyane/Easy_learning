"""Текстовый и image индексы. Главы 05–06.

Ради честного baseline image-индекс эмбеддит САМ регион/страницу, а не
VLM-подпись к ней (подпись — это text-only в маске, см. ловушку caption).

Как (chromadb, подсказка формы):

    import chromadb
    client = chromadb.PersistentClient(path="data/chroma")
    col = client.get_or_create_collection("fieldnote_text")
    col.add(ids=[page_id], documents=[chunk_text],
            metadatas=[{"pdf_id": ..., "page_num": ...}])
"""


def build_text_index(pages_dir: str = "data/pages") -> None:
    """Нарезать sidecar-текст страниц в чанки и сложить в Chroma/LanceDB.

    Глава 05. Это опора text-only baseline.
    """
    raise NotImplementedError("глава 05: индексируй текст страниц в Chroma/LanceDB")


def build_image_index(pages_dir: str = "data/pages") -> None:
    """Проиндексировать изображения страниц (эмбеддинг пикселей, НЕ подписи).

    Глава 06. Если эмбеддишь VLM-подпись — это caption-ловушка, не image-индекс.
    """
    raise NotImplementedError("глава 06: эмбеддь изображения страниц, не заменяй их подписями")
