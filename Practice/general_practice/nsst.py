def numSubmatrixSumTarget(matrix, target):
    from collections import defaultdict

    rows, cols = len(matrix), len(matrix[0])

    prefix_sum = [[0] * (cols + 1) for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            prefix_sum[r][c + 1] = prefix_sum[r][c] + matrix[r][c]

    count = 0

    for start_col in range(cols):
        for end_col in range(start_col, cols):
            sum_dict = defaultdict(int)
            sum_dict[0] = 1
            curr_sum = 0

            for r in range(rows):
                curr_sum += prefix_sum[r][end_col + 1] - prefix_sum[r][start_col]
                count += sum_dict[curr_sum - target]
                sum_dict[curr_sum] += 1

    return count


matrix1 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
target1 = 0
print(numSubmatrixSumTarget(matrix1, target1))  # Output: 4

matrix2 = [[1, -1], [-1, 1]]
target2 = 0
print(numSubmatrixSumTarget(matrix2, target2))  # Output: 5

matrix3 = [[904]]
target3 = 0
print(numSubmatrixSumTarget(matrix3, target3))  # Output: 0
