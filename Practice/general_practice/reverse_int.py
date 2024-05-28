def reverse(x):
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    sign = 1 if x >= 0 else -1
    x = abs(x)

    result = 0
    while x != 0:
        digit = x % 10
        x //= 10

        if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
            return 0
        if result < INT_MIN // 10 or (result == INT_MIN // 10 and digit > 8):
            return 0

        result = result * 10 + digit

    return sign * result


print(reverse(123))  # 321
print(reverse(-123))  # -321
print(reverse(120))  # 21
print(reverse(0))  # 0
print(reverse(1534236469))  # 0 (Overflow)
