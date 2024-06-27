def firstMissingPositive(nums):
    n = len(nums)

    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap nums[i] with nums[nums[i] - 1]
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


print(firstMissingPositive([1, 2, 0]))  # 3
print(firstMissingPositive([3, 4, -1, 1]))  # 2
print(firstMissingPositive([7, 8, 9, 11, 12]))  # 1
