def minWindow(s, t):
    from collections import Counter

    dict_t = Counter(t)

    required = len(dict_t)

    l, r = 0, 0

    formed = 0

    window_counts = {}

    ans = float("inf"), None, None

    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        while l <= r and formed == required:
            character = s[l]

            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            l += 1

        r += 1

    return "" if ans[1] is None else s[ans[1]: ans[2] + 1]


print(minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
print(minWindow("a", "a"))  # "a"
print(minWindow("a", "aa"))  # ""
