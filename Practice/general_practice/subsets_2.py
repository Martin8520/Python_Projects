def subsetsWithDup(nums):
    def backtrack(start, path):
        subsets.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    nums.sort()
    subsets = []
    backtrack(0, [])
    return subsets


nums1 = [1, 2, 2]
nums2 = [0]

print("Subsets for nums1:", subsetsWithDup(nums1))
print("Subsets for nums2:", subsetsWithDup(nums2))
