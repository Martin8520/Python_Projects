def sequentialDigits(low, high):
    result = []

    for start in range(1, 10):
        num = start
        next_digit = start
        while num <= high and next_digit < 10:
            if num >= low:
                result.append(num)
            next_digit += 1
            num = num * 10 + next_digit

    return sorted(result)


low1, high1 = 100, 300
print(sequentialDigits(low1, high1))  # [123, 234]

low2, high2 = 1000, 13000
print(sequentialDigits(low2, high2))  # [1234, 2345, 3456, 4567, 5678, 6789, 12345]
