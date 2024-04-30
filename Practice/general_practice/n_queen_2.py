def totalNQueens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False

        return True

    def backtrack(board, row):
        nonlocal count
        if row == n:
            count += 1
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'

    count = 0
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    return count


print(totalNQueens(4))
print(totalNQueens(1))
