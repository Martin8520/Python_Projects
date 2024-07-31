def findRotateSteps(ring, key):
    from collections import defaultdict
    import sys

    n = len(ring)
    m = len(key)

    char_indices = defaultdict(list)
    for i, ch in enumerate(ring):
        char_indices[ch].append(i)

    dp = [[sys.maxsize] * n for _ in range(m + 1)]
    dp[0][0] = 0

    for i in range(m):
        for j in range(n):
            if dp[i][j] == sys.maxsize:
                continue
            cur_char = key[i]
            for k in char_indices[cur_char]:
                dist = min(abs(j - k), n - abs(j - k))
                dp[i + 1][k] = min(dp[i + 1][k], dp[i][j] + dist + 1)

    return min(dp[m])


ring = "godding"
key = "gd"
print(findRotateSteps(ring, key))  # 4

ring = "godding"
key = "godding"
print(findRotateSteps(ring, key))  # 13
