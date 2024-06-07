from collections import Counter


def minSteps(s, t):
    count_s = Counter(s)
    count_t = Counter(t)

    steps = 0
    for char in count_s:
        if count_s[char] > count_t[char]:
            steps += count_s[char] - count_t[char]

    return steps


s = "bab"
t = "aba"
print(minSteps(s, t))  # 1

s = "leetcode"
t = "practice"
print(minSteps(s, t))  # 5

s = "anagram"
t = "mangaar"
print(minSteps(s, t))  # 0
