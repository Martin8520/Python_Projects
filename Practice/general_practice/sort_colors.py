def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


nums1 = [2, 0, 2, 1, 1, 0]
sortColors(nums1)
print(nums1)

nums2 = [2, 0, 1]
sortColors(nums2)
print(nums2)
