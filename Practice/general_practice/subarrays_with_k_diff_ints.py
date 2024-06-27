from collections import defaultdict


def at_most_k(nums, k):
    count = 0
    start = 0
    freq = defaultdict(int)

    for end in range(len(nums)):
        if freq[nums[end]] == 0:
            k -= 1
        freq[nums[end]] += 1

        while k < 0:
            freq[nums[start]] -= 1
            if freq[nums[start]] == 0:
                k += 1
            start += 1

        count += end - start + 1

    return count


def subarrays_with_k_distinct(nums, k):
    return at_most_k(nums, k) - at_most_k(nums, k - 1)


print(subarrays_with_k_distinct([1, 2, 1, 2, 3], 2))  # 7
print(subarrays_with_k_distinct([1, 2, 1, 3, 4], 3))  # 3
