from src.metrics import false_hit_rate


def test_false_hit_on_fixture():
    rows = [
        {"score": 0.95, "query_intent": "password", "neighbor_intent": "password"},
        {"score": 0.94, "query_intent": "password", "neighbor_intent": "mfa"},
        {"score": 0.40, "query_intent": "refund", "neighbor_intent": "billing"},
    ]
    rate = false_hit_rate(rows, threshold=0.86)
    assert abs(rate - 0.5) < 1e-9
