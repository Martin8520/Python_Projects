def partition(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    def partition_helper(start, current_partition):
        if start == len(s):
            result.append(current_partition[:])
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                current_partition.append(substring)
                partition_helper(end, current_partition)
                current_partition.pop()

    result = []
    partition_helper(0, [])
    return result


s1 = "aab"
print(partition(s1))  # [["a","a","b"],["aa","b"]]

s2 = "a"
print(partition(s2))  # [["a"]]
