import pytest
from algorithms.chapter2.functions import linear_search, binary_sum


def test_linear_search() -> None:
    vector = [1, 10, 32, 35, 54, 32, 10, 100]

    assert linear_search(vector, 10) == 1
    assert linear_search(vector, 54) == 4
    assert linear_search(vector, 1000) is None


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
