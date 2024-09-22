def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def fib_memoized(n: int) -> int:
    memo: dict[int, int] = {}
    return _fib_memoized(n, memo)


def _fib_memoized(n: int, memo: dict[int, int]) -> int:
    if n < 0:
        raise ValueError("n can not be < 0.")
    if memo.get(n) is not None:
        return memo[0]
    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


def fib_bottom_up(n: int) -> int:
    if n < 0:
        raise ValueError("n can not be < 0.")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        result = 0
        for _ in range(2, n + 1):
            result = a + b
            a = b
            b = result

        return result
