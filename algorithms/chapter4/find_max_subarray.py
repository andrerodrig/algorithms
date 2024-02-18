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
    for i in range(mid, low - 1, -1):
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
    """Recursive form of find maximum subarray algorithm.

    Applies itself to the left side, right side, and the subarray that crosses the
    middle.

    :param A: The array in which is searched the subarray.
    :param low: The first index of the array.
    :param high: The last index of the array.
    """
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


def find_max_subarray_iterative(A: list) -> tuple[int, int, int | float]:
    """Iterative form of find maximum subarray.

    Finds the max subarray by brute force, comparing each subarray iteratively.

    :param A: The array used to find the max subarray.
    :returns: The left and right indexes of the subarray and it's value.
    """
    max_value = -float("inf")
    max_index_left = max_index_right = -1
    sum_value = 0

    for i in range(len(A)):
        sum_value = A[i]

        if sum_value >= max_value:
            max_value = sum_value
            max_index_left = max_index_right = i

        for j in range(i, len(A)):
            if i == j:
                continue

            sum_value += A[j]
            if sum_value >= max_value:
                max_value = sum_value
                max_index_left = i
                max_index_right = j

    return (max_index_left, max_index_right, max_value)
