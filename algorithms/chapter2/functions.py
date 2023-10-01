def find_value(vector: list[int], value: int) -> int | None:
    for index, v in enumerate(vector):
        if v == value:
            return index

    return None


def binary_sum(binary_a: list[int], binary_b: list[int]) -> list[int]:
    n = len(binary_a)
    carry = 0
    binary_c = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        binary_c[i + 1] = (binary_a[i] + binary_b[i] + carry) % 2
        carry = (binary_a[i] + binary_b[i] + carry) // 2
    binary_c[0] = carry

    return binary_c
