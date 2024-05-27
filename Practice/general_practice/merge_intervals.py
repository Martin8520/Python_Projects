def merge(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged_intervals[-1]

        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged_intervals.append(current)

    return merged_intervals


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
print(merge([[1, 4], [4, 5]]))  # [[1,5]]
print(merge([[1, 4], [2, 3]]))  # [[1,4]]
print(merge([[1, 4], [0, 4]]))  # [[0,4]]
print(merge([[1, 4], [5, 6]]))  # [[1,4],[5,6]]
print(merge([]))  # []
