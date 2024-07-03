def count_fixed_bound_subarrays(nums, minK, maxK):
    n = len(nums)
    last_minK, last_maxK = -1, -1
    start = 0
    count = 0

    for end in range(n):
        if nums[end] < minK or nums[end] > maxK:
            start = end + 1
            last_minK = last_maxK = -1
        if nums[end] == minK:
            last_minK = end
        if nums[end] == maxK:
            last_maxK = end

        if last_minK != -1 and last_maxK != -1:
            count += max(0, min(last_minK, last_maxK) - start + 1)

    return count


print(count_fixed_bound_subarrays([1, 3, 5, 2, 7, 5], 1, 5))  # 2
print(count_fixed_bound_subarrays([1, 1, 1, 1], 1, 1))  # 10
