"""
Dynamic Programming: Rod-cutting problem

"""


def cut_rod(prices: list[float | int], length: int) -> float:
    """Top-down recursive implementation of Rod-cutting algorithm.

    :param prices:
        The prices table for length i of a Rod.
    :param length:
        Total Rod's length.
    :return:
        The maximum revenue gotten.
    """
    if length == 0:
        return 0

    rev = -1.0
    for i in range(length):
        rev = max(rev, prices[i] + cut_rod(prices, length - i - 1))
    return rev


def memoized_cut_rod(prices: list[float | int], length: int) -> float:
    cache: dict[int, float] = {}
    for i in range(length + 1):
        cache[i] = -1

    return _call_memoized_cut_rod(prices, length, cache)


def _call_memoized_cut_rod(
    prices: list[float | int], length: int, cache: dict[int, float]
) -> float:
    if cache[length] >= 0:
        return cache[length]
    if length == 0:
        rev = 0.0
    else:
        rev = -1
        for i in range(length):
            rev = max(
                rev, prices[i] + _call_memoized_cut_rod(prices, length - i - 1, cache)
            )

    cache[length] = rev
    return rev


def cut_rod_bottom_up(prices: list[float | int], length: int) -> float:
    # Initialize cache as a mapping length: price
    cache: dict[int, float | int] = {}
    cache[0] = 0

    for i in range(length):
        rev = -1.0
        for j in range(i + 1):
            rev = max(rev, prices[j] + cache[i - j])
        cache[i + 1] = rev

    return cache[length]


def cut_rod_bottom_up_extended(
    prices: list[float | int], length: int
) -> tuple[dict[int, float | int], dict[int, int]]:
    revenue_cache: dict[int, float | int] = {}
    optimal_size_cache: dict[int, int] = {}
    revenue_cache[0] = 0

    for i in range(length):
        rev = -1.0
        for j in range(i + 1):
            new_rev = prices[j] + revenue_cache[i - j]
            if rev < new_rev:
                rev = new_rev
                optimal_size_cache[i + 1] = j + 1

        revenue_cache[i + 1] = rev
    return revenue_cache, optimal_size_cache


def print_cut_rod_solution(prices: list[float | int], length: int) -> None:
    _, optimal_size_cache = cut_rod_bottom_up_extended(prices, length)
    while length > 0:
        print(f"optimal_size_cache[{length}]={optimal_size_cache[length]}")
        length = length - optimal_size_cache[length]


def get_cut_rod_optimal_values(
    prices: list[float | int], length: int
) -> tuple[float, int]:
    rev_cache, optimal_size_cache = cut_rod_bottom_up_extended(prices, length)
    return rev_cache[length], optimal_size_cache[length]


# 15.1-3) Consider a modification of the rod-cutting problem in which, in addition to a
# price p_i for each rod, each cut incurs a fixed cost of c. The revenue associated with
# a solution is now the sum of the prices of the pieces minus the costs of making the
# cuts. Give a dynamic-programming algorithm to solve this modified problem.
def cut_rod_with_cost(
    prices: list[float | int], length: int, cut_cost: float
) -> tuple[dict[int, float | int], dict[int, int]]:
    rev_cache = {}
    rev_cache[0] = 0.0
    optimal_size_map = {}

    for i in range(length):
        rev = -float("inf")
        for j in range(i + 1):
            new_rev = prices[j] + rev_cache[i - j] - cut_cost
            if rev < new_rev:
                rev = new_rev
                optimal_size_map[i + 1] = j + 1

        rev_cache[i + 1] = rev

    return rev_cache, optimal_size_map
