def singleNumber(nums):
    count = [0] * 32

    for num in nums:
        for i in range(32):
            if num & (1 << i):
                count[i] = (count[i] + 1) % 3

    result = 0
    for i in range(32):
        if count[i] != 0:
            result |= (1 << i)

    if result >= 2 ** 31:
        result -= 2 ** 32

    return result


nums1 = [2, 2, 3, 2]
print(singleNumber(nums1))  # 3

nums2 = [0, 1, 0, 1, 0, 1, 99]
print(singleNumber(nums2))  # 99
