def timeRequiredToBuy(tickets, k):
    time = 0
    n = len(tickets)

    while tickets[k] > 0:
        for i in range(n):
            if tickets[i] > 0:
                tickets[i] -= 1
                time += 1
                if tickets[k] == 0:
                    return time


print(timeRequiredToBuy([2, 3, 2], 2))  # 6
print(timeRequiredToBuy([5, 1, 1, 1], 0))  # 8
