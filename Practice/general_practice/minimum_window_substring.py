from collections import Counter


def minWindow(s, t):
    if not s or not t or len(s) < len(t):
        return ""

    target_counts = Counter(t)
    required_chars = len(target_counts)

    left, right = 0, 0
    formed = 0
    window_counts = {}

    min_length = float("inf")
    min_window = ""

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in target_counts and window_counts[char] == target_counts[char]:
            formed += 1

        while formed == required_chars and left <= right:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window = s[left:right + 1]

            char = s[left]
            window_counts[char] -= 1

            if char in target_counts and window_counts[char] < target_counts[char]:
                formed -= 1

            left += 1

        right += 1

    return min_window


print(minWindow("ADOBECODEBANC", "ABC"))
print(minWindow("a", "a"))
print(minWindow("a", "aa"))
