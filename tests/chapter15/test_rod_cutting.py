import pytest
from algorithms.chapter15.rod_cutting import (
    cut_rod,
    memoized_cut_rod,
    cut_rod_bottom_up,
    cut_rod_bottom_up_extended,
    get_cut_rod_optimal_values,
    cut_rod_with_cost,
)


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


@pytest.mark.parametrize(
    "length, expected_max_rev",
    [
        (4, 10),
        (5, 13),
        (6, 17),
        (10, 30),
    ],
)
def test_cut_rod_bottom_up(length: int, expected_max_rev: int) -> None:
    prices_table = [1.0, 5.0, 8.0, 9.0, 10.0, 17.0, 17.0, 20.0, 24.0, 30.0]

    max_rev = cut_rod_bottom_up(prices_table, length)

    assert max_rev == expected_max_rev


@pytest.mark.parametrize(
    "length, expected_values",
    [
        (4, (10, 2)),
        (5, (13, 2)),
        (6, (17, 6)),
        (10, (30, 10)),
    ],
)
def test_cut_rod_optimal_values(length: int, expected_values: tuple[float, int]) -> None:
    prices_table = [1.0, 5.0, 8.0, 9.0, 10.0, 17.0, 17.0, 20.0, 24.0, 30.0]

    max_rev = get_cut_rod_optimal_values(prices_table, length)

    assert max_rev == expected_values


@pytest.mark.parametrize(
    "length, expected_values",
    [
        (4, ({0: 0, 1: 1.0, 2: 5.0, 3: 8.0, 4: 10.0}, {1: 1, 2: 2, 3: 3, 4: 2})),
        (
            5,
            (
                {0: 0, 1: 1.0, 2: 5.0, 3: 8.0, 4: 10.0, 5: 13.0},
                {1: 1, 2: 2, 3: 3, 4: 2, 5: 2},
            ),
        ),
        (
            6,
            (
                {0: 0, 1: 1.0, 2: 5.0, 3: 8.0, 4: 10.0, 5: 13.0, 6: 17.0},
                {1: 1, 2: 2, 3: 3, 4: 2, 5: 2, 6: 6},
            ),
        ),
        (
            10,
            (
                {
                    0: 0,
                    1: 1.0,
                    2: 5.0,
                    3: 8.0,
                    4: 10.0,
                    5: 13.0,
                    6: 17.0,
                    7: 18.0,
                    8: 22.0,
                    9: 25.0,
                    10: 30.0,
                },
                {1: 1, 2: 2, 3: 3, 4: 2, 5: 2, 6: 6, 7: 1, 8: 2, 9: 3, 10: 10},
            ),
        ),
    ],
)
def test_cut_rod_bottom_up_extended(
    length: int, expected_values: tuple[float, int]
) -> None:
    prices_table = [1.0, 5.0, 8.0, 9.0, 10.0, 17.0, 17.0, 20.0, 24.0, 30.0]

    prices_and_lengths = cut_rod_bottom_up_extended(prices_table, length)

    assert prices_and_lengths == expected_values


@pytest.mark.parametrize(
    "length, expected_values",
    [
        (4, ({0: 0.0, 1: -0.2, 2: 3.8, 3: 6.8, 4: 7.8}, {1: 1, 2: 2, 3: 3, 4: 4})),
        (
            5,
            (
                {0: 0.0, 1: -0.2, 2: 3.8, 3: 6.8, 4: 7.8, 5: 10.6},
                {1: 1, 2: 2, 3: 3, 4: 4, 5: 2},
            ),
        ),
        (
            6,
            (
                {0: 0.0, 1: -0.2, 2: 3.8, 3: 6.8, 4: 7.8, 5: 10.6, 6: 15.8},
                {1: 1, 2: 2, 3: 3, 4: 4, 5: 2, 6: 6},
            ),
        ),
        (
            10,
            (
                {
                    0: 0.0,
                    1: -0.2,
                    2: 3.8,
                    3: 6.8,
                    4: 7.8,
                    5: 10.6,
                    6: 15.8,
                    7: 15.8,
                    8: 19.6,
                    9: 22.8,
                    10: 28.8,
                },
                {1: 1, 2: 2, 3: 3, 4: 4, 5: 2, 6: 6, 7: 7, 8: 2, 9: 9, 10: 10},
            ),
        ),
    ],
)
def test_cut_rod_with_cost(
    length: int, expected_values: tuple[dict[int, float | int], dict[int, int]]
) -> None:
    import numpy as np

    prices_table: list[float | int] = [
        1.0,
        5.0,
        8.0,
        9.0,
        10.0,
        17.0,
        17.0,
        20.0,
        24.0,
        30.0,
    ]
    cost = 1.2

    revs, opt_sizes = cut_rod_with_cost(prices_table, length, cost)

    for r, exp_r in zip(revs.values(), expected_values[0].values()):
        assert np.isclose(r, exp_r, rtol=1e-07)

    for opt, exp_opt in zip(opt_sizes.values(), expected_values[1].values()):
        assert opt == exp_opt
