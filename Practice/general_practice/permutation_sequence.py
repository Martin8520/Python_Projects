def getPermutation(n, k):
    factorials = [1] * (n + 1)
    for i in range(1, n + 1):
        factorials[i] = factorials[i - 1] * i

    digits = [str(i) for i in range(1, n + 1)]
    k -= 1

    result = ''
    for i in range(n):
        index = k // factorials[n - 1 - i]
        result += digits[index]
        digits.pop(index)
        k %= factorials[n - 1 - i]

    return result


print(getPermutation(3, 3))
print(getPermutation(4, 9))
print(getPermutation(3, 1))
