def solve(board):
    if not board:
        return

    m, n = len(board), len(board[0])

    def dfs(row, col):
        if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != 'O':
            return
        board[row][col] = 'S'
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for i in range(m):
        dfs(i, 0)
        dfs(i, n - 1)
    for j in range(n):
        dfs(0, j)
        dfs(m - 1, j)

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'S':
                board[i][j] = 'O'


board1 = [["X", "X", "X", "X"],
          ["X", "O", "O", "X"],
          ["X", "X", "O", "X"],
          ["X", "O", "X", "X"]]
solve(board1)
for row in board1:
    print(row)
# [["X","X","X","X"],
#  ["X","X","X","X"],
#  ["X","X","X","X"],
#  ["X","O","X","X"]]

board2 = [["X"]]
solve(board2)
for row in board2:
    print(row)
# [["X"]]
