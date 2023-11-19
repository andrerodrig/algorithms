from math import floor


def binary_search(
    vector: list[int | float],
    target: int | float,
    initial_position: int,
    final_position: int,
) -> int | None:
    """Binary Search algorithm

    This algorithm searches recursivelly through the vector breaking it in half and
    applying the function itself to the half. So this search should be used only to
    sorted vectors.

    :param vector: The vector in which the target is searched.
    :param target: The number searched in vector.
    :return: The index of the vector position which the target is stored.
    """

    if initial_position >= final_position:
        return None

    half = initial_position + floor((final_position - initial_position) / 2)
    obtained = vector[half]
    if obtained == target:
        return half

    if target < obtained:
        return binary_search(vector, target, initial_position, half)
    else:
        return binary_search(vector, target, half + 1, final_position)
