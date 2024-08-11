def minOperations(nums, k):
    initial_xor = 0
    for num in nums:
        initial_xor ^= num

    if initial_xor == k:
        return 0

    diff_xor = initial_xor ^ k
    operations = 0

    for num in nums:
        if diff_xor & num:
            diff_xor ^= num
            operations += 1

        if diff_xor == 0:
            break

    return operations if diff_xor == 0 else -1


nums1 = [2, 1, 3, 4]
k1 = 1
print(minOperations(nums1, k1))  # 2

nums2 = [2, 0, 2, 0]
k2 = 0
print(minOperations(nums2, k2))  # 0
