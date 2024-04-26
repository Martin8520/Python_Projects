def add_binary(a, b):
    result = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        sum_val = carry

        if i >= 0:
            sum_val += int(a[i])
            i -= 1
        if j >= 0:
            sum_val += int(b[j])
            j -= 1

        result.append(str(sum_val % 2))
        carry = sum_val // 2

    return ''.join(result[::-1])


print(add_binary("11", "1"))
print(add_binary("1010", "1011"))
