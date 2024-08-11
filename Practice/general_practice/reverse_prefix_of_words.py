def reversePrefix(word, ch):
    idx = word.find(ch)

    if idx != -1:
        return word[:idx + 1][::-1] + word[idx + 1:]
    else:
        return word


word1 = "abcdefd"
ch1 = "d"
print(reversePrefix(word1, ch1))  # "dcbaefd"

word2 = "xyxzxe"
ch2 = "z"
print(reversePrefix(word2, ch2))  # "zxyxxe"

word3 = "abcd"
ch3 = "z"
print(reversePrefix(word3, ch3))  # "abcd"
