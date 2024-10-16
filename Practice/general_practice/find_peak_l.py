def find_peak_element(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


nums1 = [1, 2, 3, 1]
print(find_peak_element(nums1))  # 2

nums2 = [1, 2, 1, 3, 5, 6, 4]
print(find_peak_element(nums2))  # 5
