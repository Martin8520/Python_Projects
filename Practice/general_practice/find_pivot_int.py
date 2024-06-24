def find_pivot_integer(n):
    total_sum = (n * (n + 1)) // 2

    for x in range(1, n + 1):
        left_sum = (x * (x + 1)) // 2
        right_sum = total_sum - left_sum + x
        if left_sum == right_sum:
            return x
    return -1


print(find_pivot_integer(8))  # 6
print(find_pivot_integer(1))  # 1
print(find_pivot_integer(4))  # -1
