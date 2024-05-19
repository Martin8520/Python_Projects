def maxProduct(nums):
    if not nums:
        return 0

    max_product = nums[0]
    current_max = nums[0]
    current_min = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        temp_max = current_max

        current_max = max(num, num * current_max, num * current_min)
        current_min = min(num, num * temp_max, num * current_min)

        max_product = max(max_product, current_max)

    return max_product


test_cases = [
    [2, 3, -2, 4],
    [-2, 0, -1],
    [-2, 3, -4],
    [0, 2],
    [-2, -3, 7],
    [1, -2, -3, 0, 7, -8, -2]
]

for i, nums in enumerate(test_cases):
    print(f"Example {i + 1}: {nums} => Output: {maxProduct(nums)}")
