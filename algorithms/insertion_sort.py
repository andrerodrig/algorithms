from typing import Sequence


def insertion_sort(vector: list[int | float]) -> Sequence[int | float]:
    vector_ = vector.copy()

    for j in range(1, len(vector_)):
        key = vector_[j]
        i = j - 1
        while i > -1 and vector_[i] > key:
            vector_[i + 1] = vector_[i]
            i = i - 1
        vector_[i + 1] = key

    return vector_


def merge_sort(vector: list[int | float]) -> None:
    ...
