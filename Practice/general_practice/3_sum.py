def three_sum(nums):
    nums.sort()
    res = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return res


nums1 = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums1))  # [[-1, -1, 2], [-1, 0, 1]]

nums2 = []
print(three_sum(nums2))  # []

nums3 = [0]
print(three_sum(nums3))  # []
