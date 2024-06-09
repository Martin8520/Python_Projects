def findErrorNums(nums):
    n = len(nums)
    S = n * (n + 1) // 2
    P = n * (n + 1) * (2 * n + 1) // 6
    sum_nums = sum(nums)
    sum_squares_nums = sum(x * x for x in nums)
    sum_diff = S - sum_nums
    square_diff = P - sum_squares_nums
    sum_xy = square_diff // sum_diff
    x = (sum_xy + sum_diff) // 2
    y = sum_xy - x
    return [y, x]


nums1 = [1, 2, 2, 4]
print(findErrorNums(nums1))  # [2, 3]

nums2 = [1, 1]
print(findErrorNums(nums2))  # [1, 2]
