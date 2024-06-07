from collections import Counter


def areClose(word1, word2):

    if len(word1) != len(word2):
        return False

    freq1 = Counter(word1)
    freq2 = Counter(word2)

    if set(freq1.keys()) != set(freq2.keys()):
        return False

    if sorted(freq1.values()) != sorted(freq2.values()):
        return False

    return True


word1 = "abc"
word2 = "bca"
print(areClose(word1, word2))  # true

word1 = "a"
word2 = "aa"
print(areClose(word1, word2))  # false

word1 = "cabbba"
word2 = "abbccc"
print(areClose(word1, word2))  # true
