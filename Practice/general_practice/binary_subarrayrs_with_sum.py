def num_subarrays_with_sum(nums, goal):
    from collections import defaultdict

    prefix_sum = 0
    prefix_sums_count = defaultdict(int)
    prefix_sums_count[0] = 1

    count = 0

    for num in nums:
        prefix_sum += num

        if (prefix_sum - goal) in prefix_sums_count:
            count += prefix_sums_count[prefix_sum - goal]

        prefix_sums_count[prefix_sum] += 1

    return count


print(num_subarrays_with_sum([1, 0, 1, 0, 1], 2))  # 4
print(num_subarrays_with_sum([0, 0, 0, 0, 0], 0))  # 15
