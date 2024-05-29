def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merged_intervals = []
    for interval in intervals:
        if not merged_intervals or merged_intervals[-1][1] < interval[0]:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

    return merged_intervals


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1, 6], [8, 10], [15, 18]]
print(merge([[1, 4], [4, 5]]))  # [[1, 5]]
print(merge([[1, 10], [2, 6], [8, 10], [15, 18]]))  # [[1, 10], [15, 18]]
print(merge([[1, 4], [0, 4]]))  # [[0, 4]]
print(merge([[1, 4], [0, 0]]))  # [[0, 0], [1, 4]]
