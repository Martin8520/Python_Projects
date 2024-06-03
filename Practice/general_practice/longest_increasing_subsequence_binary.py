def length_of_longest_substring(s):
    char_index_map = {}
    max_length = 0
    left = 0

    for right in range(len(s)):
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1

        char_index_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length


s1 = "abcabcbb"
print(length_of_longest_substring(s1))  # 3

s2 = "bbbbb"
print(length_of_longest_substring(s2))  # 1

s3 = "pwwkew"
print(length_of_longest_substring(s3))  # 3
