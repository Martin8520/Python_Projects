n = input()

digit_1 = int(n[0])
digit_2 = int(n[1])
digit_3 = int(n[2])

result1 = digit_1 + digit_2 + digit_3
result2 = digit_1 * digit_2 * digit_3
result3 = (digit_2 * digit_3) + digit_1

maximum_result = max(result1, result2, result3)
print(maximum_result)
