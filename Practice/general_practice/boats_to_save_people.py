def numRescueBoats(people, limit):
    people.sort()

    left = 0
    right = len(people) - 1

    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boats += 1

    return boats


print(numRescueBoats([1, 2], 3))  # 1
print(numRescueBoats([3, 2, 2, 1], 3))  # 3
print(numRescueBoats([3, 5, 3, 4], 5))  # 4
