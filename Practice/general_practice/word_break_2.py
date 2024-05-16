def wordBreak(s, wordDict):
    wordset = set(wordDict)
    memo = {}

    def backtrack(start):
        if start == len(s):
            return [""]

        if start in memo:
            return memo[start]

        result = []
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordset:
                rest_sentences = backtrack(end)
                for sentence in rest_sentences:
                    if sentence:
                        result.append(s[start:end] + " " + sentence)
                    else:
                        result.append(s[start:end])

        memo[start] = result
        return result

    return backtrack(0)


# Test cases
print(wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))  # ["cats and dog","cat sand dog"]
print(wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine",
                                      "pineapple"]))  # ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # []
