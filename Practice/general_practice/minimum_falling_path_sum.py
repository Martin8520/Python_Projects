def minFallingPathSum(matrix):
    n = len(matrix)

    for i in range(1, n):
        for j in range(n):
            above = matrix[i - 1][j]
            left = matrix[i - 1][j - 1] if j > 0 else float('inf')
            right = matrix[i - 1][j + 1] if j < n - 1 else float('inf')

            matrix[i][j] += min(above, left, right)

    return min(matrix[-1])


matrix1 = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(minFallingPathSum(matrix1))  # 13

matrix2 = [[-19, 57], [-40, -5]]
print(minFallingPathSum(matrix2))  # -59
