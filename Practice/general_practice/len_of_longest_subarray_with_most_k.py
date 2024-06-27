def longestGoodSubarray(nums, k):
    freq = {}
    left = 0
    max_length = 0

    for right in range(len(nums)):
        if nums[right] in freq:
            freq[nums[right]] += 1
        else:
            freq[nums[right]] = 1

        while any(value > k for value in freq.values()):
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


print(longestGoodSubarray([1, 2, 3, 1, 2, 3, 1, 2], 2))  # 6
print(longestGoodSubarray([1, 2, 1, 2, 1, 2, 1, 2], 1))  # 2
print(longestGoodSubarray([5, 5, 5, 5, 5, 5, 5], 4))  # 4
