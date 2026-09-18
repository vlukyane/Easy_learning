from eval.metrics import recall_at_k


def test_recall_partial():
    assert recall_at_k(["a", "b", "c", "d"], ["a", "x", "b", "y"], k=10) == 0.5


def test_recall_none():
    assert recall_at_k(["a"], ["z", "y"], k=5) == 0.0
