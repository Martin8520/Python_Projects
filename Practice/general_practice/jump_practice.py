def jump(nums):
    n = len(nums)
    if n == 1:
        return 0

    jumps = 0
    max_reach = 0
    curr_end = 0
    for i in range(n - 1):
        max_reach = max(max_reach, i + nums[i])

        if i == curr_end:
            jumps += 1
            curr_end = max_reach

    return jumps


nums1 = [2, 3, 1, 1, 4]
print(jump(nums1))

nums2 = [2, 3, 0, 1, 4]
print(jump(nums2))
