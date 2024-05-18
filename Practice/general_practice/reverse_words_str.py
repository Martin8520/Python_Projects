def reverseWords(s: str) -> str:
    words = s.strip().split()

    words.reverse()

    return ' '.join(words)


s1 = "the sky is blue"
print(reverseWords(s1))  # "blue is sky the"

s2 = "  hello world  "
print(reverseWords(s2))  # "world hello"

s3 = "a good   example"
print(reverseWords(s3))  # "example good a"
