def firstUniqChar(s):
    from collections import Counter
    char_count = Counter(s)

    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index

    return -1


print(firstUniqChar("leetcode"))  # 0
print(firstUniqChar("loveleetcode"))  # 2
print(firstUniqChar("aabb"))  # -1
