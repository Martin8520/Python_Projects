def findMaxK(nums):
    num_set = set(nums)
    max_k = -1

    for num in nums:
        if num > 0 and -num in num_set:
            max_k = max(max_k, num)

    return max_k


print(findMaxK([-1, 2, -3, 3]))  # 3
print(findMaxK([-1, 10, 6, 7, -7, 1]))  # 7
print(findMaxK([-10, 8, 6, 7, -2, -3]))  # -1
