import pytest
from random import randint
from algorithms.chapter2.selection_sort import selection_sort


@pytest.mark.parametrize(
    "vector",
    (
        [randint(0, 1000) for _ in range(10)],
        [randint(0, 120) for _ in range(100)],
        [randint(0, 5550) for _ in range(10000)],
    ),
)
def test_selection_sort(vector: list[int]) -> None:
    assert selection_sort(vector) == sorted(vector)
