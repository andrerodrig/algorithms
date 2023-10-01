import pytest
from algorithms.chapter2.insertion_sort import insertion_sort, rev_insertion_sort
from random import randint


@pytest.mark.parametrize(
    "vector",
    (
        [randint(0, 1000) for _ in range(10)],
        [randint(0, 120) for _ in range(100)],
        [randint(0, 5550) for _ in range(10000)],
    ),
)
def test_insertion_sort(vector: list[int | float]) -> None:
    ordered_vect = insertion_sort(vector)

    assert ordered_vect == sorted(vector)


@pytest.mark.parametrize(
    "vector",
    (
        [randint(0, 1000) for _ in range(10)],
        [randint(0, 120) for _ in range(100)],
        [randint(0, 5550) for _ in range(10000)],
    ),
)
def test_rev_insertion_sort(vector: list[int | float]) -> None:
    ordered_vect = rev_insertion_sort(vector)

    assert ordered_vect == sorted(vector, reverse=True)
