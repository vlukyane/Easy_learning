"""Attack Success Rate по классам атак. Глава 05–06.

validate_attacks реализован (тест зелёный). run/compare/false_positive пишешь ты.
ASR = доля атак, изменивших поведение агента (success_if). Меряем до и после каждого
слоя защиты, отдельно false_positive на чистых резюме (защита не должна их резать).
"""

import json
from pathlib import Path

CLASSES = {"direct", "role", "hidden", "exfil", "rating"}


def validate_attacks(path: str = "data/attacks.jsonl") -> None:
    """Проверить корпус атак: класс ∈ CLASSES, есть success_if, покрыты все 5 классов."""
    src = Path(path)
    if not src.exists():
        src = Path("data/attacks.jsonl.example")
    n = 0
    seen: set[str] = set()
    with src.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if row.get("class") not in CLASSES:
                raise ValueError(f"bad class {row.get('class')}")
            if "success_if" not in row:
                raise ValueError("success_if required")
            seen.add(row["class"])
            n += 1
    missing = CLASSES - seen
    if missing:
        raise ValueError(f"missing classes {missing}")
    print(f"attacks ok: {n} rows, classes={sorted(seen)}")


def run(agent: str = "vulnerable", tag: str = "baseline") -> dict:
    """Прогнать корпус атак через agent, вернуть ASR по классам. Глава 05.

    Для каждой атаки: screen(resume) → проверь success_if. Возврат: {class: asr, "overall": ...}.
    """
    raise NotImplementedError("глава 05: ASR по классам")


def compare(agents: list[str]) -> None:
    """Сравнить ASR нескольких агентов (vulnerable vs hardened) → logs/asr-table.md. Глава 05."""
    raise NotImplementedError("глава 05: запиши logs/asr-table.md")


def false_positive(agent: str = "hardened") -> float:
    """Доля чистых резюме (data/clean), которые защита ошибочно зарезала. Глава 06."""
    raise NotImplementedError("глава 06: FP на data/clean")
