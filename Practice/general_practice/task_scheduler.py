from collections import Counter


def leastInterval(tasks, n):
    if n == 0:
        return len(tasks)

    task_counts = Counter(tasks)
    max_freq = max(task_counts.values())

    num_max_freq = sum(1 for task, count in task_counts.items() if count == max_freq)

    part_count = max_freq - 1
    part_length = n - (num_max_freq - 1)
    empty_slots = part_count * part_length
    available_tasks = len(tasks) - max_freq * num_max_freq

    idles = max(0, empty_slots - available_tasks)

    return len(tasks) + idles


print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # 8
print(leastInterval(["A", "C", "A", "B", "D", "B"], 1))  # 6
print(leastInterval(["A", "A", "A", "B", "B", "B"], 3))  # 10
