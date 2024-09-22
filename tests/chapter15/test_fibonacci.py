import pytest
from algorithms.chapter15.fibonacci import fib, fib_memoized, fib_bottom_up


@pytest.mark.parametrize(
    "n, exp_result",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55),
    ],
)
def test_fib(n: int, exp_result: int) -> None:
    result = fib(n)
    assert result == exp_result


@pytest.mark.parametrize(
    "n, exp_result",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55),
    ],
)
def test_fib_memoized(n: int, exp_result: int) -> None:
    result = fib_memoized(n)
    assert result == exp_result


@pytest.mark.parametrize(
    "n, exp_result",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55),
    ],
)
def test_fib_bottom_up(n: int, exp_result: int) -> None:
    result = fib_bottom_up(n)
    assert result == exp_result
