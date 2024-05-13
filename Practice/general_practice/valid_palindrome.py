def isPalindrome(s):

    def isAlphanumeric(c):
        return c.isalnum()

    s = ''.join(c.lower() for c in s if isAlphanumeric(c))

    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not isAlphanumeric(s[left]):
            left += 1
        while left < right and not isAlphanumeric(s[right]):
            right -= 1
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


s1 = "A man, a plan, a canal: Panama"
print(isPalindrome(s1))  # True

s2 = "race a car"
print(isPalindrome(s2))  # False

s3 = " "
print(isPalindrome(s3))  # True
