def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid + 1
        else:
            right -= 1

    return nums[left]


nums1 = [1, 3, 5]
print(findMin(nums1))  # 1

nums2 = [2, 2, 2, 0, 1]
print(findMin(nums2))  # 0
