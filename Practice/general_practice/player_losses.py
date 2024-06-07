def findWinners(matches):
    from collections import defaultdict

    loss_count = defaultdict(int)
    players = set()

    for winner, loser in matches:
        loss_count[loser] += 1
        players.add(winner)
        players.add(loser)

    no_loss = []
    one_loss = []

    for player in players:
        if loss_count[player] == 0:
            no_loss.append(player)
        elif loss_count[player] == 1:
            one_loss.append(player)

    return [sorted(no_loss), sorted(one_loss)]


matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
print(findWinners(matches))  # [[1,2,10],[4,5,7,8]]

matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
print(findWinners(matches))  # [[1,2,5,6],[]]
