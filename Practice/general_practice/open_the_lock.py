from collections import deque


def openLock(deadends, target):
    dead_set = set(deadends)
    visited = set("0000")
    if "0000" in dead_set:
        return -1

    queue = deque([("0000", 0)])

    while queue:
        current, steps = queue.popleft()

        if current == target:
            return steps

        for i in range(4):
            for move in [-1, 1]:
                new_digit = (int(current[i]) + move) % 10
                new_state = current[:i] + str(new_digit) + current[i + 1:]

                if new_state not in visited and new_state not in dead_set:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))

    return -1


deadends1 = ["0201", "0101", "0102", "1212", "2002"]
target1 = "0202"
print(openLock(deadends1, target1))  # 6

deadends2 = ["8888"]
target2 = "0009"
print(openLock(deadends2, target2))  # 1

deadends3 = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
target3 = "8888"
print(openLock(deadends3, target3))  # -1
