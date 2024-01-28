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


# def insertion_sort_with_bs(vector: list[int | float]) -> Sequence[int | float]:
#     '''
#     O(n) * (O(lg n) + O(n)) = O(nlg n) + O(n^2) = O(n^2)
#     # TODO: With bug. Fix later.
#     '''
#     for i in range(1, len(vector)):
#         key = vector[i]
#         j = i - 1
#         position_to_insert = _binary_search_for_insertion_sort(
#             vector[:j + 1], key, 0, j
#         )
#         if position_to_insert == 0:
#             for idx in range(i - 1, - 1, -1):
#                 vector[idx + 1] = vector[idx]
#                 j -= 1
#         elif key > vector[position_to_insert]:
#             for idx in range(i - 1, position_to_insert - 1, -1):
#                 vector[idx + 1] = vector[idx]
#                 j -= 1
#         vector[j + 1] = key
#         # else:
#         #     for idx in range(i - 1, position_to_insert - 1, -1):
#         #         vector[idx + 1] = vector[idx]
#         #         j -= 1
#         #     vector[j] = key

#     return vector


# def _binary_search_for_insertion_sort(
#     vector: list[int | float],
#     target: int | float,
#     initial_pos: int,
#     final_pos: int,
# ) -> int | None:
#     if initial_pos >= final_pos:
#         return initial_pos

#     half = initial_pos + math.floor((final_pos - initial_pos) / 2)

#     if vector[half] > target:
#         return _binary_search_for_insertion_sort(vector, target, initial_pos, half)
#     else:
#         return _binary_search_for_insertion_sort(vector, target, half + 1, final_pos)
