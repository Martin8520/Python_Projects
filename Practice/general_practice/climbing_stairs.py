def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2

    for _ in range(3, n + 1):
        a, b = b, a + b

    return b


n1 = 2
print(climbStairs(n1))  # 2

n2 = 3
print(climbStairs(n2))  # 3
