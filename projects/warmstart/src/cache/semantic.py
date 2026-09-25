"""Семантический кэш (слой 3). Глава 04 — эмбеддинги пишешь ты.

Здесь появляются ложные попадания: два похожих по эмбеддингу запроса с РАЗНЫМИ
правильными ответами. Поэтому dump_scores выгружает соседей БЕЗ порога — порог и
false-hit меряются потом в metrics/eval_curve, а не угадываются.
"""


def lookup(query: str, threshold: float) -> dict | None:
    """Эмбеддинг запроса → ближайший сосед (исключая сам запрос); вернуть при score ≥ threshold.

    Возврат (dict) при попадании: {"answer","intent_id","score"}, иначе None.
    """
    raise NotImplementedError("глава 04: эмбеддинг, исключи self, верни соседа при score ≥ threshold")


def dump_scores(intents_path: str, out_path: str) -> None:
    """Выгрузить top-1 соседей БЕЗ порога — сырьё для кривой и false-hit. Глава 04.

    Каждая строка out_path: {"score", "query_intent", "neighbor_intent"} —
    ровно то, что ест metrics.false_hit_rate.
    """
    raise NotImplementedError("глава 04: выгрузи score top-1 соседа без применения порога")
