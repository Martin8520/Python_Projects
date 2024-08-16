import heapq


def kthSmallestPrimeFraction(arr, k):
    def countLessEqual(x):
        """Count fractions <= x using two pointers."""
        count = 0
        j = 1
        for i in range(len(arr)):
            while j < len(arr) and arr[i] / arr[j] > x:
                j += 1
            count += j
        return count

    lo, hi = 0.0, 1.0
    while hi - lo > 1e-9:
        mid = (lo + hi) / 2
        if countLessEqual(mid) < k:
            lo = mid
        else:
            hi = mid

    min_heap = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            heapq.heappush(min_heap, (arr[i] / arr[j], arr[i], arr[j]))

    for _ in range(k):
        fraction = heapq.heappop(min_heap)

    return [fraction[1], fraction[2]]


print(kthSmallestPrimeFraction([1, 2, 3, 5], 3))  # [2, 5]
print(kthSmallestPrimeFraction([1, 7], 1))  # [1, 7]
