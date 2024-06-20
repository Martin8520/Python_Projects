from collections import defaultdict, deque


def findAllPeople(n, meetings, firstPerson):
    meetings.sort(key=lambda x: x[2])

    know_secret = set([0, firstPerson])

    time_to_meetings = defaultdict(list)
    for x, y, time in meetings:
        time_to_meetings[time].append((x, y))

    for time in sorted(time_to_meetings.keys()):
        current_meetings = time_to_meetings[time]

        will_know_secret = set()
        for x, y in current_meetings:
            if x in know_secret or y in know_secret:
                will_know_secret.add(x)
                will_know_secret.add(y)

        for x, y in current_meetings:
            if x in will_know_secret or y in will_know_secret:
                know_secret.add(x)
                know_secret.add(y)

    return list(know_secret)


print(findAllPeople(6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1))  # [0,1,2,3,5]
print(findAllPeople(4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3))  # [0,1,3]
print(findAllPeople(5, [[3, 4, 2], [1, 2, 1], [2, 3, 1]], 1))  # [0,1,2,3,4]
