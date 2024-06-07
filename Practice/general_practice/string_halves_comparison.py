def halvesAreAlike(s):
    vowels = set('aeiouAEIOU')
    n = len(s)
    a, b = s[:n // 2], s[n // 2:]

    count_vowels = lambda x: sum(1 for char in x if char in vowels)

    return count_vowels(a) == count_vowels(b)


s = "book"
print(halvesAreAlike(s))  # true

s = "textbook"
print(halvesAreAlike(s))  # false
