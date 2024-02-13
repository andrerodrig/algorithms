import pytest
import numpy as np
from algorithms.chapter4.matrix_operations import (
    square_matrix_multiply,
    square_matrix_multiply_recursive,
)


def test_matrix_multiply() -> None:
    a = [[1, 3], [2, 4]]
    b = [[5, 2], [2, 1]]

    c = square_matrix_multiply(a, b)

    #   [1, 3]  *  [5, 2]  =
    #   [2, 4]     [2, 1]
    #
    #   [1 * 5 + 3 * 2, 1 * 2 + 3 * 1]  =   [11, 5]
    #   [2 * 5 + 4 * 2, 2 * 2 + 4 * 1]      [18, 8]

    assert c == [[11, 5], [18, 8]]


@pytest.mark.parametrize(
    "a, b",
    (
        [[[1, 3], [2, 4]], [[5, 2], [2, 1]]],
        [
            [[1, 3, 1, 2], [2, 4, 1, 1], [2, 4, 5, 3], [2, 4, 9, 3]],
            [[3, 3, 1, 5], [10, 2, 21, 11], [2, 5, 3, 0], [2, 1, 6, 9]],
        ],
    ),
)
def test_square_matrix_multiply_recursive(a: list, b: list) -> None:
    c = square_matrix_multiply_recursive(a, b)

    assert np.all(c == np.matmul(a, b))
