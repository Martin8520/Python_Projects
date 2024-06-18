import heapq


def mostBooked(n, meetings):
    meetings.sort()

    free_rooms = list(range(n))
    heapq.heapify(free_rooms)

    ongoing_meetings = []

    room_meetings_count = [0] * n

    for start, end in meetings:
        while ongoing_meetings and ongoing_meetings[0][0] <= start:
            _, room = heapq.heappop(ongoing_meetings)
            heapq.heappush(free_rooms, room)

        if free_rooms:
            room = heapq.heappop(free_rooms)
            room_meetings_count[room] += 1
            heapq.heappush(ongoing_meetings, (end, room))
        else:
            end_time, room = heapq.heappop(ongoing_meetings)
            new_end = end_time + (end - start)
            room_meetings_count[room] += 1
            heapq.heappush(ongoing_meetings, (new_end, room))

    max_meetings = max(room_meetings_count)
    for i in range(n):
        if room_meetings_count[i] == max_meetings:
            return i


print(mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))  # 0
print(mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))  # 1
