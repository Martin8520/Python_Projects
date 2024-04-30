def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals1))

intervals2 = [[1, 4], [4, 5]]
print(merge(intervals2))
