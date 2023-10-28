import pytest
from random import randint
from algorithms.chapter2.merge_sort import merge_sort


@pytest.mark.parametrize(
    "vector",
    (
        [randint(0, 1000) for _ in range(10)],
        [randint(0, 120) for _ in range(100)],
        [randint(0, 5550) for _ in range(10000)],
    ),
)
def test_merge_sort(vector: list[int]) -> None:
    assert merge_sort(vector) == sorted(vector)
