from src.eval.asr import CLASSES, validate_attacks


def test_example_corpus_valid():
    validate_attacks("data/attacks.jsonl.example")
    assert CLASSES == {"direct", "role", "hidden", "exfil", "rating"}
