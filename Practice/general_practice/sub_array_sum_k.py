def subarray_sum(nums, k):
    prefix_sum_count = {0: 1}
    prefix_sum = 0
    total_count = 0

    for num in nums:
        prefix_sum += num
        total_count += prefix_sum_count.get(prefix_sum - k, 0)
        prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

    return total_count


nums1 = [1, 1, 1]
k1 = 2
print(subarray_sum(nums1, k1))  # 2

nums2 = [1, 2, 3]
k2 = 3
print(subarray_sum(nums2, k2))  # 2
