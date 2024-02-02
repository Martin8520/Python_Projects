def shooting(board, row, col):
    if board[row][col] == 1:
        board[row][col] = -1
        return "Booom"
    elif board[row][col] == 0:
        return "Missed"
    else:
        return "You already shot there!"


def count_boats(board):
    return sum(row.count(1) for row in board)


def create_board():
    R, C = map(int, input().split())
    player1 = [list(map(int, input().split())) for i in range(R)]
    player2 = [list(map(int, input().split())) for i in range(R)]

    results = []

    player_turn = 1

    while True:
        command = input().split()
        if command[0] == "END":
            break

        if command[0] == "Shoot":
            row = int(command[1])
            col = int(command[2])

            if player_turn == 1:
                result = shooting(player2, row, col)
            else:
                result = shooting(player1, row, col)

            results.append(result)
            player_turn = 3 - player_turn

    for result in results:
        print(result)

    boats_boats_p1 = count_boats(player1)
    boats_boats_p2 = count_boats(player2)

    print(f"{boats_boats_p1}:{boats_boats_p2}")


create_board()
