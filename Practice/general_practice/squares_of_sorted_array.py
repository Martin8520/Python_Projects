def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1

        pos -= 1

    return result


print(sortedSquares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
print(sortedSquares([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]
