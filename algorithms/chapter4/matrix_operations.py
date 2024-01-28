def square_matrix_multiply(A: list[list], B: list[list]) -> list[list]:
    length = len(A)
    c = [[0 for _ in range(length)] for _ in range(length)]
    return _square_matrix_multiply(A, B, c, length)


def _square_matrix_multiply(
    A: list[list], B: list[list], C: list[list], n: int
) -> list[list]:
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C


def square_matrix_multiply_recursive(A: list[list], B: list[list]) -> list[list]:
    length = len(A)
    return _square_matrix_multiply_recursive(A, B, length)


def _square_matrix_multiply_recursive(
    A: list[list], B: list[list], n: int
) -> list[list]:
    """
    Multiply two matrices A and B and return a new one called C.

    Recursion with:
    1. base case if n = 1: return the product of two numbers of A and B.
    2. recursive case if n > 1: The two matrices are divided partitioned into
    four smaller pieces. A C matrix is created and divided too, with equal length
    to A and B. After that the operations are executed, building the result matrix C.
    """

    if n == 1:
        # Base case
        return [[A[0][0] * B[0][0]]]

    # Otherwise divide
    mid = n // 2

    a11 = [a[:mid] for a in A[:mid]]
    a12 = [a[mid:] for a in A[:mid]]
    a21 = [a[:mid] for a in A[mid:]]
    a22 = [a[mid:] for a in A[mid:]]

    b11 = [b[:mid] for b in B[:mid]]
    b12 = [b[mid:] for b in B[:mid]]
    b21 = [b[:mid] for b in B[mid:]]
    b22 = [b[mid:] for b in B[mid:]]

    C = [[0 for _ in range(len(A))] for _ in range(len(A))]
    c11 = [c[:mid] for c in C[:mid]]
    c12 = [c[mid:] for c in C[:mid]]
    c21 = [c[:mid] for c in C[mid:]]
    c22 = [c[mid:] for c in C[mid:]]

    for i in range(len(c11)):
        for j in range(len(c11)):
            c11_a = _square_matrix_multiply_recursive(a11, b11, mid)
            c11_b = _square_matrix_multiply_recursive(a12, b21, mid)
            c11[i][j] = c11_a[i][j] + c11_b[i][j]

            c12_a = _square_matrix_multiply_recursive(a11, b12, mid)
            c12_b = _square_matrix_multiply_recursive(a12, b22, mid)
            c12[i][j] = c12_a[i][j] + c12_b[i][j]

            c21_a = _square_matrix_multiply_recursive(a21, b11, mid)
            c21_b = _square_matrix_multiply_recursive(a22, b21, mid)
            c21[i][j] = c21_a[i][j] + c21_b[i][j]

            c22_a = _square_matrix_multiply_recursive(a21, b12, mid)
            c22_b = _square_matrix_multiply_recursive(a22, b22, mid)
            c22[i][j] = c22_a[i][j] + c22_b[i][j]

            C[i][j] = c11[i][j]
            C[i][j + mid] = c12[i][j]
            C[i + mid][j] = c21[i][j]
            C[i + mid][j + mid] = c22[i][j]

    return C
