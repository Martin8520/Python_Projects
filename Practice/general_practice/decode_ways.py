def numDecodings(s):
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(2, n + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]

        two_digits = int(s[i - 2:i])
        if 10 <= two_digits <= 26:
            dp[i] += dp[i - 2]

    return dp[n]


s1 = "12"
s2 = "226"
s3 = "06"

print("Number of ways to decode", s1, ":", numDecodings(s1))
print("Number of ways to decode", s2, ":", numDecodings(s2))
print("Number of ways to decode", s3, ":", numDecodings(s3))
