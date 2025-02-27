def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False

    for j in range(n):
        if matrix[0][j] == 0:
            first_row_zero = True
            break

    for i in range(m):
        if matrix[i][0] == 0:
            first_col_zero = True
            break

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0


matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
setZeroes(matrix1)
print(matrix1)

matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
setZeroes(matrix2)
print(matrix2)
