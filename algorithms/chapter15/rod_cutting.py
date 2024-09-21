"""
Dynamic Programming: Rod-cutting problem

"""


def cut_rod(prices: list[float], length: int) -> float:
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

    rev = -float("inf")
    for i in range(length):
        rev = max(rev, prices[i] + cut_rod(prices, length - i - 1))
    return rev


def memoized_cut_rod(prices: list[float], length: int) -> float:
    cache: dict[int, float] = {}
    for i in range(length + 1):
        cache[i] = -float("inf")

    return _call_memoized_cut_rod(prices, length, cache)


def _call_memoized_cut_rod(
    prices: list[float], length: int, cache: dict[int, float]
) -> float:
    if cache[length] >= 0:
        return cache[length]
    if length == 0:
        rev: float = 0.0
    else:
        rev = -float("inf")
        for i in range(length):
            rev = max(
                rev, prices[i] + _call_memoized_cut_rod(prices, length - i - 1, cache)
            )

    cache[length] = rev
    return rev
