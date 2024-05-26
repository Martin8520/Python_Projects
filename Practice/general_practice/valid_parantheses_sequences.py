def count_valid_parentheses(n):
    catalan = [0] * (n + 1)

    catalan[0] = 1
    catalan[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]

    return catalan[n]


n = 3
print(count_valid_parentheses(n))  # 5
