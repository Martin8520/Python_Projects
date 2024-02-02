def num_grid(N, M):
    matrix = [[2 ** (i + j) for j in range(M)] for i in range(N)]

    total_sum = 0
    current_row, current_col = 0, 0
    dir_row, dir_col = 1, 1

    while 0 <= current_row < N and 0 <= current_col < M:
        total_sum += matrix[current_row][current_col]

        if current_row + dir_row < 0 or current_row + dir_row == N:
            dir_row *= -1
        elif current_col + dir_col < 0 or current_col + dir_col == M:
            dir_col *= -1

        current_row += dir_row
        current_col += dir_col

    return total_sum


N, M = map(int, input().split())

result = num_grid(N, M)
print(result)
