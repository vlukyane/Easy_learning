"""Ingestion корпуса. Глава 02.

Загрузить корпус юридических текстов в стабильные (doc_id, text). Стабильный
doc_id критичен: на него ссылаются relevant_ids в золоте — иначе recall не сойдётся.
"""


def build() -> None:
    """Разобрать корпус из data/corpus/ в стабильные doc_id + text. Глава 02."""
    raise NotImplementedError("глава 02: загрузи корпус в стабильные doc_id + text")
