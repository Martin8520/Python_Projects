def wordBreak(s, wordDict):
    wordset = set(wordDict)

    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordset:
                dp[i] = True
                break

    return dp[-1]


print(wordBreak("leetcode", ["leet", "code"]))  # True
print(wordBreak("applepenapple", ["apple", "pen"]))  # True
print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False
