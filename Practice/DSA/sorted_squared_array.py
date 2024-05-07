def sorted_squared(arr):
    n = len(arr)
    result = [0] * n
    left, right = 0, n - 1
    idx = n - 1

    while left <= right:
        left_squared = arr[left] * arr[left]
        right_squared = arr[right] * arr[right]

        if left_squared > right_squared:
            result[idx] = left_squared
            left += 1
        else:
            result[idx] = right_squared
            right -= 1
        idx -= 1

    return result
