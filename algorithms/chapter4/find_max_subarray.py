from math import floor


def find_max_crossing_subarray(
    A: list, low: int, mid: int, high: int
) -> tuple[int, int, int | float]:
    """Find the maximum subarray that cross the mid of an array A[low..high]

    This algorithm works finding two subarrays A_1 and A_2 defined as:
        1. A_1 = A[i..mid], with low <= i <= mid. A_1 has the greatest sum of A[low..mid].
        2. A_2 = A[mid + 1..j], with mid + 1 <= j <= high. A_2 has the greatest sum of
        A[mid + 1..high].
    """

    left_sum = -float("inf")
    max_left = -1
    sum = 0
    for i in range(mid, low + -1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -float("inf")
    max_right = -1
    sum = 0
    for j in range(mid + 1, high + 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(A: list, low: int, high: int) -> tuple[int, int, int | float]:
    if high == low:
        return (low, high, A[low])
    else:
        mid = floor((low + high) / 2)
        left_low, left_high, left_max = find_max_subarray(A, low, mid)
        right_low, right_high, right_max = find_max_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_max = find_max_crossing_subarray(A, low, mid, high)

        if left_max >= right_max and left_max >= cross_max:
            return (left_low, left_high, left_max)
        elif right_max >= left_max and right_max >= cross_max:
            return (right_low, right_high, right_max)
        else:
            return (cross_low, cross_high, cross_max)
