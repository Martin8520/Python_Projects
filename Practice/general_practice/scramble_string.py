class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def scramble(s1, s2):
            if (s1, s2) in memo:
                return memo[(s1, s2)]

            if s1 == s2:
                memo[(s1, s2)] = True
                return True
            if sorted(s1) != sorted(s2):
                memo[(s1, s2)] = False
                return False

            length = len(s1)
            for i in range(1, length):
                if scramble(s1[:i], s2[:i]) and scramble(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True
                if scramble(s1[:i], s2[length - i:]) and scramble(s1[i:], s2[:length - i]):
                    memo[(s1, s2)] = True
                    return True

            memo[(s1, s2)] = False
            return False

        return scramble(s1, s2)


solution = Solution()
print(solution.isScramble("great", "rgeat"))
print(solution.isScramble("abcde", "caebd"))
print(solution.isScramble("a", "a"))
