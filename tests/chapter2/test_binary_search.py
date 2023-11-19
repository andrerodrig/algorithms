import random
import pytest

from algorithms.chapter2.binary_search import binary_search


@pytest.mark.parametrize(
    "vector",
    (
        [random.randint(0, 1000) for _ in range(10)],
        [random.randint(0, 120) for _ in range(100)],
        [random.randint(0, 5550) for _ in range(10000)],
        [random.randint(0, 50_000) for _ in range(100_000)],
        [random.randint(0, 800_000) for _ in range(1_000_000)],
    ),
)
def test_binary_search(vector: list[int | float]) -> None:
    sorted_vector = sorted(vector)
    target = random.choice(sorted_vector)

    target_indexes = [
        i for i, _ in enumerate(sorted_vector) if sorted_vector[i] == target
    ]

    assert binary_search(sorted_vector, target, 0, len(vector)) in target_indexes
