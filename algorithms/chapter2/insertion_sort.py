from typing import Sequence


def insertion_sort(vector: list[int | float]) -> Sequence[int | float]:
    """The insertion sort algorihm. It gives a O(n^2) running time.

    :param vector: The unsorted vector.
    :returns: The given vector ascendingly sorted.
    """
    vector_ = vector.copy()

    for j in range(1, len(vector_)):
        key = vector_[j]
        i = j - 1
        while i > -1 and vector_[i] > key:
            vector_[i + 1] = vector_[i]
            i -= 1
        vector_[i + 1] = key

    return vector_


def rev_insertion_sort(vector: list[int | float]) -> Sequence[int | float]:
    vector_ = vector.copy()
    for j in range(len(vector_) - 2, -1, -1):
        key = vector_[j]
        i = j + 1
        while i < len(vector_) and vector_[i] > key:
            vector_[i - 1] = vector_[i]
            i += 1
        vector_[i - 1] = key
    return vector_


def recursive_insertion_sort(
    vector: list[int | float], size: int
) -> Sequence[int | float] | None:
    if size == 1:
        return None

    key = vector[size - 1]
    recursive_insertion_sort(vector, size - 1)
    if key > vector[size - 2]:
        return vector

    i = size - 2
    while i > -1 and vector[i] >= key:
        vector[i + 1] = vector[i]
        i -= 1

    vector[i + 1] = key
    return vector
