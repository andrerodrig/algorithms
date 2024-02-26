from plotly import express as px
from plotly import graph_objects as go
from collections.abc import Callable
import random
from time import time

from algorithms.chapter4.find_max_subarray import (
    find_max_subarray_recursive,
    find_max_subarray_iterative,
    find_max_subarray_hybrid,
)

RECURSIVE = "recursive"
ITERATIVE = "iterative"
HYBRID = "hybrid"


def get_running_time_of_fms_algorithms(
    rec_func: Callable[[list[int]], tuple[int, int, int | float]],
    iter_func: Callable[[list[int]], tuple[int, int, int | float]],
    hybrid_func: Callable[[list[int]], tuple[int, int, int | float]],
    n: int,
) -> list[dict[str, int | float]]:
    """Get the running time of the two types of algorithms for find max subarray
    (recursive and iterative). Both functions must have same inputs.

    :param rec_func: Algorithm 1.
    :param iter_func: Algorithm 2.
    :param hybrid_func: Algorithm 3.
    :param n: The max length of the input array.

    This algorithm calculate the time of all algorithms applyed each to arrays
    of size {1, 2, ..., n}. Return a dict mapping each running time for
    recursive / iterative / hybrid approach.
    """
    random_arrays = []
    for i in range(1, n + 1):
        array = [random.randrange(-50, 80) for _ in range(1, i + 1)]
        random_arrays.append(array)

    running_times: list[dict[str, int | float]] = []

    for arr in random_arrays:
        times_mapping: dict[str, int | float] = {}

        t_01 = time()
        _, _, _ = rec_func(arr)
        t_11 = time() - t_01

        t_02 = time()
        _, _, _ = iter_func(arr)
        t_12 = time() - t_02

        t_03 = time()
        _, _, _ = hybrid_func(arr)
        t_13 = time() - t_03

        times_mapping[RECURSIVE] = t_11
        times_mapping[ITERATIVE] = t_12
        times_mapping[HYBRID] = t_13

        running_times.append(times_mapping)

    return running_times


def convert_running_time_data(
    time_mapping_list: list[dict[str, float]]
) -> dict[str, list[int] | list[float]]:
    result_dict: dict[str, list[int] | list[float]] = {}
    domain = list(range(1, len(time_mapping_list) + 1))
    recursive_list = [mapping[RECURSIVE] for mapping in time_mapping_list]
    iterative_list = [mapping[ITERATIVE] for mapping in time_mapping_list]
    hybrid_list = [mapping[HYBRID] for mapping in time_mapping_list]

    result_dict[RECURSIVE] = recursive_list
    result_dict[ITERATIVE] = iterative_list
    result_dict[HYBRID] = hybrid_list
    result_dict["domain"] = domain
    return result_dict


def print_mapping(time_mapping: dict[str, list[int | float]]) -> None:
    print(f"\n{RECURSIVE}\t\t{ITERATIVE}")
    for value1, value2 in zip(time_mapping[RECURSIVE], time_mapping[ITERATIVE]):
        print(f"{value1}\t{value2}")


def plot_comparison(number_of_arrays: int) -> go.Figure:
    """Plot the comparison of both find maximum subarray algorithms

    :param number_of_arrays: Number of arrays that will be analyzed.
    :return: The plotly Figure object.
    """
    mapping_list = get_running_time_of_fms_algorithms(
        find_max_subarray_recursive,
        find_max_subarray_iterative,
        find_max_subarray_hybrid,
        number_of_arrays,
    )
    time_mapping = convert_running_time_data(mapping_list)

    figure = px.line(
        time_mapping,
        x="domain",
        y=[RECURSIVE, ITERATIVE, HYBRID],
        labels={"domain": "input size (n)", "value": "time (s)"},
    )
    return figure


if __name__ == "__main__":
    fig = plot_comparison(number_of_arrays=100)
    fig.show()
