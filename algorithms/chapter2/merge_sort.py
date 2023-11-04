import math


def merge_sort(vector: list[int]) -> list[int] | None:
    vector_ = vector.copy()
    p = 0
    r = len(vector) - 1
    return run_merge_sort(vector_, p, r)


def run_merge_sort(vector: list[int], p: int, r: int) -> list[int] | None:
    if p == r:
        return None

    q = math.floor((p + r) / 2)  # Midpoint of vector[p:r]
    run_merge_sort(vector, p, q)
    run_merge_sort(vector, q + 1, r)
    return merge(vector, p, q, r)


def merge(vector: list[int], p: int, q: int, r: int) -> list[int]:
    n_l = q - p + 1
    n_r = r - q

    left: list[int] = [0] * (n_l)
    right: list[int] = [0] * (n_r)

    for i in range(n_l):
        left[i] = vector[p + i]

    for j in range(n_r):
        right[j] = vector[q + j + 1]

    i = 0
    j = 0
    k = p

    while i < n_l and j < n_r:
        if left[i] is None or right[j] is None:
            raise ValueError("List with None items cannot be sorted.")
        else:
            if left[i] <= right[j]:  # type: ignore
                vector[k] = left[i]
                i += 1
            else:
                vector[k] = right[j]
                j += 1
            k += 1

    # Loop has finished.
    while i < n_l:
        vector[k] = left[i]
        i += 1
        k += 1
    while j < n_r:
        vector[k] = right[j]
        j += 1
        k += 1

    return vector
