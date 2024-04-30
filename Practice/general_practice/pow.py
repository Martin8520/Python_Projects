def pow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / pow(x, -n)
    elif n % 2 == 0:
        return pow(x * x, n // 2)
    else:
        return x * pow(x, n - 1)


print(pow(2.00000, 10))
print(pow(2.10000, 3))
print(pow(2.00000, -2))
