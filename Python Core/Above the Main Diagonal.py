def matrix_num(n):
    matrix_a = [[2 ** (x + y) for y in range(n)] for x in range(n)]
    return matrix_a


def sum_diagonal(matrix, n):
    total = 0
    for x in range(n):
        for y in range(x + 1, n):
            total += matrix[x][y]
    return total


num = int(input())

matrix_b = matrix_num(num)

result = sum_diagonal(matrix_b, num)

print(result)
