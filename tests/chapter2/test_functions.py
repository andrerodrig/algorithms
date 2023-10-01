import pytest
from algorithms.chapter2.functions import find_value, binary_sum


def test_find_value() -> None:
    vector = [1, 10, 32, 35, 54, 32, 10, 100]

    assert find_value(vector, 10) == 1
    assert find_value(vector, 54) == 4
    assert find_value(vector, 1000) is None


@pytest.mark.parametrize(
    "a, b, c",
    [
        ([0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1, 0]),  # 5 + 5 = 10
        ([1, 1, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0, 0]),  # 15 + 5 = 20
        ([1, 1, 1, 1, 1], [0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 0]),  # 31 + 13 = 44
    ],
)
def test_binary_sum(a: list[int], b: list[int], c: list[int]) -> None:
    assert binary_sum(a, b) == c
