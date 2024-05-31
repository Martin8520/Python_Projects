def subarray_sum(nums, k):
    count = 0
    cumulative_sum = 0
    cumulative_sum_map = {0: 1}

    for num in nums:
        cumulative_sum += num

        if (cumulative_sum - k) in cumulative_sum_map:
            count += cumulative_sum_map[cumulative_sum - k]

        if cumulative_sum in cumulative_sum_map:
            cumulative_sum_map[cumulative_sum] += 1
        else:
            cumulative_sum_map[cumulative_sum] = 1

    return count


nums1 = [1, 1, 1]
k1 = 2
print(subarray_sum(nums1, k1))  # 2

nums2 = [1, 2, 3]
k2 = 3
print(subarray_sum(nums2, k2))  # 2
