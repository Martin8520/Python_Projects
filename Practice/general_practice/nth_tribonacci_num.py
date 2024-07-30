def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    T0, T1, T2 = 0, 1, 1
    for i in range(3, n + 1):
        Tn = T0 + T1 + T2
        T0, T1, T2 = T1, T2, Tn

    return T2


print(tribonacci(4))  # 4
print(tribonacci(25))  # 1389537
