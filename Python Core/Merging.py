def merge(num1, num2):
    result = 0
    multiplier = 1

    while num1 > 0 or num2 > 0:
        digit_sum = (num1 + num2) % 10
        result += digit_sum * multiplier

        num1 //= 10
        num2 //= 10
        multiplier *= 10

    return result


x1 = merge(123, 123)
print(x1)

x2 = merge(789, 123)
print(x2)
