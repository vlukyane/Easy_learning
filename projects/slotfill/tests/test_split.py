from src.data.split import assert_disjoint


def test_no_overlap():
    assert_disjoint(
        {
            "train": ["a", "b"],
            "val": ["c"],
            "test": ["d"],
        }
    )


def test_overlap_rejected():
    try:
        assert_disjoint({"train": ["a"], "val": ["a"], "test": ["b"]})
    except AssertionError:
        return
    raise AssertionError("overlap must be rejected")
