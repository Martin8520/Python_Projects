def isScramble(s1, s2):
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False

    length = len(s1)
    for i in range(1, length):
        if isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]):
            return True
        if isScramble(s1[:i], s2[length - i:]) and isScramble(s1[i:], s2[:length - i]):
            return True

    return False


print(isScramble("great", "rgeat"))
print(isScramble("abcde", "caebd"))
print(isScramble("a", "a"))
