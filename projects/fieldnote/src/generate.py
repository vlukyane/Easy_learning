"""Генерация ответа. Главы 05 и 07.

Ключ проекта: в multimodal-ветке источник-картинка уходит в Claude как image-блок,
а не строкой «см. стр. 12». Возврат содержит путь к кропу-источнику.

Как (vision, подсказка формы):

    import anthropic, base64
    client = anthropic.Anthropic()
    b64 = base64.standard_b64encode(open(crop_path, "rb").read()).decode()
    client.messages.create(model=MODEL, max_tokens=512, messages=[{"role":"user",
        "content":[{"type":"image","source":{"type":"base64",
                    "media_type":"image/png","data":b64}},
                   {"type":"text","text":question}]}])
"""


def answer_text_only(question: str, chunks: list[dict]) -> dict:
    """Ответ без vision, только по текстовым чанкам. Глава 05 (baseline)."""
    raise NotImplementedError("глава 05: Claude без vision по текстовым чанкам")


def answer_multimodal(question: str, hits: list[dict]) -> dict:
    """Ответ по кропу-источнику через Claude vision; вернуть citation bbox. Глава 07."""
    raise NotImplementedError("глава 07: отправь байты кропа в Claude vision; верни citation bbox")


def demo(question: str) -> None:
    """Полный путь: retrieve_hybrid → answer_multimodal → печать пути к кропу. Глава 07."""
    raise NotImplementedError("глава 07: retrieve_hybrid + answer_multimodal + печать пути кропа")
