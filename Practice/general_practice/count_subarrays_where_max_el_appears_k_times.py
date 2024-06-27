def count_valid_subarrays(nums, k):
    n = len(nums)
    count = 0
    start = 0
    freq = {}
    max_freq = 0

    for end in range(n):
        num = nums[end]
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

        max_freq = max(max_freq, freq[num])

        while max_freq >= k:
            count += n - end

            freq[nums[start]] -= 1
            if freq[nums[start]] == 0:
                del freq[nums[start]]
            start += 1

            max_freq = max(freq.values(), default=0)

    return count


print(count_valid_subarrays([1, 3, 2, 3, 3], 2))  # 6
print(count_valid_subarrays([1, 4, 2, 1], 3))  # 0
