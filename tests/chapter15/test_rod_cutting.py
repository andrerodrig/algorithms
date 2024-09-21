import pytest
from algorithms.chapter15.rod_cutting import cut_rod, memoized_cut_rod


@pytest.mark.parametrize(
    "length, expected_max_rev",
    [
        (4, 10),
        (5, 13),
        (6, 17),
        (10, 30),
    ],
)
def test_cut_rod(length: int, expected_max_rev: int) -> None:
    prices_table = [1.0, 5.0, 8.0, 9.0, 10.0, 17.0, 17.0, 20.0, 24.0, 30.0]

    max_rev = cut_rod(prices_table, length)

    assert max_rev == expected_max_rev


@pytest.mark.parametrize(
    "length, expected_max_rev",
    [
        (4, 10),
        (5, 13),
        (6, 17),
        (10, 30),
    ],
)
def test_memoized_cut_rod(length: int, expected_max_rev: int) -> None:
    prices_table = [1.0, 5.0, 8.0, 9.0, 10.0, 17.0, 17.0, 20.0, 24.0, 30.0]

    max_rev = memoized_cut_rod(prices_table, length)

    assert max_rev == expected_max_rev
