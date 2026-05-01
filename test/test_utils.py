import pytest
from app.utils import clean_data, compute_statistics

def test_clean_data():
    data = [1, -2, None, 5]
    assert clean_data(data) == [1, 5]


def test_compute_statistics():
    data = [1, 2, 3]
    stats = compute_statistics(data)

    assert stats["mean"] == 2
    assert stats["min"] == 1
    assert stats["max"] == 3


def test_empty_statistics():
    with pytest.raises(ValueError):
        compute_statistics([])