def totalMaxFrequencies(nums):
    from collections import defaultdict

    frequency_count = defaultdict(int)
    for num in nums:
        frequency_count[num] += 1

    max_frequency = max(frequency_count.values())

    total_max_frequencies = sum(f for num, f in frequency_count.items() if f == max_frequency)

    return total_max_frequencies


nums1 = [1, 2, 2, 3, 1, 4]
print(totalMaxFrequencies(nums1))  # 4

nums2 = [1, 2, 3, 4, 5]
print(totalMaxFrequencies(nums2))  # 5
