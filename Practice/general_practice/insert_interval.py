def insert(intervals, newInterval):
    result = []
    new_start, new_end = newInterval
    placed = False

    for interval in intervals:
        if interval[1] < new_start:
            result.append(interval)
        elif interval[0] > new_end:
            if not placed:
                result.append([new_start, new_end])
                placed = True
            result.append(interval)
        else:
            new_start = min(new_start, interval[0])
            new_end = max(new_end, interval[1])

    if not placed:
        result.append([new_start, new_end])

    return result


print(insert([[1, 3], [6, 9]], [2, 5]))  # [[1,5],[6,9]]
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # [[1,2],[3,10],[12,16]]
