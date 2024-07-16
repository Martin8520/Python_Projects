from collections import deque


def deckRevealedIncreasing(deck):
    sorted_deck = sorted(deck)

    q = deque()

    for card in reversed(sorted_deck):
        if q:
            q.appendleft(q.pop())
        q.appendleft(card)

    return list(q)


print(deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))  # [2, 13, 3, 11, 5, 17, 7]
print(deckRevealedIncreasing([1, 1000]))  # [1, 1000]
