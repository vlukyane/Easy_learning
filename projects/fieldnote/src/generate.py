"""Generation. Chapters 05 and 07."""


def answer_text_only(question: str, chunks: list[dict]) -> dict:
    raise NotImplementedError("chapter 05: Claude without vision")


def answer_multimodal(question: str, hits: list[dict]) -> dict:
    raise NotImplementedError("chapter 07: send crop bytes to Claude vision; return citation bbox")


def demo(question: str) -> None:
    raise NotImplementedError("chapter 07: retrieve_hybrid + answer_multimodal + print crop path")
