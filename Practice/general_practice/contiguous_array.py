def findMaxLength(nums):
    transformed = [-1 if num == 0 else 1 for num in nums]

    prefix_sum = 0
    max_length = 0
    prefix_sum_map = {0: -1}

    for i, num in enumerate(transformed):
        prefix_sum += num

        if prefix_sum in prefix_sum_map:
            length = i - prefix_sum_map[prefix_sum]
            max_length = max(max_length, length)
        else:
            prefix_sum_map[prefix_sum] = i

    return max_length


print(findMaxLength([0, 1]))  # 2
print(findMaxLength([0, 1, 0]))  # 2
print(findMaxLength([0, 1, 0, 1, 1, 0]))  # 6
