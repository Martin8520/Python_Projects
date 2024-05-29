def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        current_area = width * min(height[left], height[right])
        max_area = max(max_area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(maxArea([1, 1]))  # 1
print(maxArea([4, 3, 2, 1, 4]))  # 16
print(maxArea([1, 2, 1]))  # 2
print(maxArea([1, 3, 2, 5, 25, 24, 5]))  # 24
