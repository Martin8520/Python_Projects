def customSortString(order, s):
    priority = {char: i for i, char in enumerate(order)}

    sorted_s = sorted(s, key=lambda x: priority.get(x, len(order)))

    return ''.join(sorted_s)


order = "cba"
s = "abcd"
print(customSortString(order, s))  # "cbad"

order = "bcafg"
s = "abcd"
print(customSortString(order, s))  # "bcad"
