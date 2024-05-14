def minCut(s):
    n = len(s)

    def is_palindrome(sub):
        return sub == sub[::-1]

    palindrome_matrix = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            palindrome_matrix[i][j] = palindrome_matrix[j][i] = is_palindrome(s[i:j + 1])

    dp = [i for i in range(n)]

    for i in range(n):
        for j in range(i, -1, -1):
            if palindrome_matrix[j][i]:
                dp[i] = min(dp[i], dp[j - 1] + 1 if j > 0 else 0)

    return dp[n - 1]


s1 = "aab"
print(minCut(s1))  # 1

s2 = "a"
print(minCut(s2))  # 0

s3 = "ab"
print(minCut(s3))  # 1
