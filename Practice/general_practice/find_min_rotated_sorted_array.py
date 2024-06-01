def find_min(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


nums1 = [3, 4, 5, 1, 2]
print(find_min(nums1))  # 1

nums2 = [4, 5, 6, 7, 0, 1, 2]
print(find_min(nums2))  # 0

nums3 = [11, 13, 15, 17]
print(find_min(nums3))  # 11
