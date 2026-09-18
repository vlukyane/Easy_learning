import json
from pathlib import Path

CLASSES = {"direct", "role", "hidden", "exfil", "rating"}


def validate_attacks(path: str = "data/attacks.jsonl") -> None:
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
    raise NotImplementedError("chapter 05: ASR by class")


def compare(agents: list[str]) -> None:
    raise NotImplementedError("chapter 05: write logs/asr-table.md")


def false_positive(agent: str = "hardened") -> float:
    raise NotImplementedError("chapter 06: FP on data/clean")
