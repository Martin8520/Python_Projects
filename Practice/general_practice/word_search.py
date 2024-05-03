def exist(board, word):
    def dfs(i, j, k):
        if k == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False

        temp = board[i][j]
        board[i][j] = '#'

        found = (dfs(i + 1, j, k + 1) or
                 dfs(i - 1, j, k + 1) or
                 dfs(i, j + 1, k + 1) or
                 dfs(i, j - 1, k + 1))

        board[i][j] = temp
        return found

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True

    return False


board1 = [["A", "B", "C", "E"],
          ["S", "F", "C", "S"],
          ["A", "D", "E", "E"]]
word1 = "ABCCED"
print(exist(board1, word1))

board2 = [["A", "B", "C", "E"],
          ["S", "F", "C", "S"],
          ["A", "D", "E", "E"]]
word2 = "SEE"
print(exist(board2, word2))

board3 = [["A", "B", "C", "E"],
          ["S", "F", "C", "S"],
          ["A", "D", "E", "E"]]
word3 = "ABCB"
print(exist(board3, word3))
