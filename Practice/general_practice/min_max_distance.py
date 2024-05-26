def can_place(stations, k, D):
    count = 0
    for i in range(1, len(stations)):
        dist = stations[i] - stations[i - 1]
        count += int(dist // D)
    return count <= k


def minimize_max_distance(stations, k):
    stations.sort()
    low, high = 1e-9, stations[-1] - stations[0]
    while high - low > 1e-6:
        mid = (low + high) / 2
        if can_place(stations, k, mid):
            high = mid
        else:
            low = mid
    return low


n = 6
stations = [1, 2, 3, 4, 5, 6]
k = 2
print(f"{minimize_max_distance(stations, k):.6f}")  # 1.000000
