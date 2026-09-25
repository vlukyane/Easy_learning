"""Кривая порогов. Глава 06.

Из выгрузки semantic.dump_scores строит зависимость hit-rate и false-hit-rate от
порога similarity. По этой кривой выбирается рабочая точка (не угадывается).
"""


def main() -> None:
    """Пройти пороги 0.70–0.98, посчитать hit-rate и false-hit, записать logs/curve.json.

    Глава 06. На каждый порог: доля запросов с хитом (hit-rate) и
    metrics.false_hit_rate(...) на той же выгрузке. Печатай таблицу, чтобы выбрать точку.
    """
    raise NotImplementedError("глава 06: запиши logs/curve.json по порогам 0.70–0.98")
