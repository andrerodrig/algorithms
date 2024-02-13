import pytest
from algorithms.chapter4.find_max_subarray import (
    find_max_crossing_subarray,
    find_max_subarray,
)


@pytest.mark.parametrize(
    ["array", "expected_result"],
    (
        ([1, 32, -3, 4, -33, -34, 23, 6, 18, -10, -2, -15, 18, 8], (6, 8, 47)),
        (
            [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7],
            (7, 10, 43),
        ),
    ),
)
def test_find_max_crossing_subarray(
    array: list, expected_result: tuple[int, int, int]
) -> None:
    left_index, right_index, max_value = find_max_crossing_subarray(
        array, 0, (len(array) // 2) - 1, len(array) - 1
    )

    assert (left_index, right_index, max_value) == expected_result


@pytest.mark.parametrize(
    ["array", "expected_result"],
    (
        ([1, 32, -3, 4, -33, -34, 23, 6, 18, -10, -2, -15, 18, 8], (6, 8, 47)),
        (
            [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7],
            (7, 10, 43),
        ),
    ),
)
def test_find_max_subarray(array: list, expected_result: tuple[int, int, int]) -> None:
    left_index, right_index, max_value = find_max_subarray(array, 0, len(array) - 1)

    assert (left_index, right_index, max_value) == expected_result
