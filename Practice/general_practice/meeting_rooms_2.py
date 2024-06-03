import heapq


def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    heap = []

    for interval in intervals:
        if heap and heap[0] <= interval[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, interval[1])

    return len(heap)


intervals1 = [[0, 30], [5, 10], [15, 20]]
print(min_meeting_rooms(intervals1))  # 2

intervals2 = [[7, 10], [2, 4]]
print(min_meeting_rooms(intervals2))  # 1
