from src.eval import require_split_metrics


def test_report_requires_both_kinds():
    require_split_metrics(
        {
            "text": {"text_only": 0.8, "multimodal": 0.82},
            "visual": {"text_only": 0.2, "multimodal": 0.7},
        }
    )


def test_flat_accuracy_is_rejected():
    try:
        require_split_metrics({"accuracy": 0.5})
    except AssertionError:
        return
    raise AssertionError("flat accuracy must be rejected")
