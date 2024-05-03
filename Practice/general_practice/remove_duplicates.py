def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    k = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[k - 1] or nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1

    return k


nums1 = [1, 1, 1, 2, 2, 3]
print(removeDuplicates(nums1))
nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(removeDuplicates(nums2))
