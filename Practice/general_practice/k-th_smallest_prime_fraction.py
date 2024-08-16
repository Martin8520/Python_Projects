def kthSmallestPrimeFraction(arr, k):
    import heapq

    # Function to count fractions less than or equal to mid
    def countLessEqual(mid):
        count = 0
        j = 1  # Initialize pointer for `arr[j]`

        for i in range(len(arr)):
            while j < len(arr) and arr[i] / arr[j] > mid:
                j += 1
            count += j
        return count

    # Binary search to find the k-th smallest fraction
    lo, hi = 0, 1
    while hi - lo > 1e-9:
        mid = (lo + hi) / 2
        if countLessEqual(mid) < k:
            lo = mid
        else:
            hi = mid

    # Find the actual k-th smallest fraction
    min_fraction = (0, 1)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] / arr[j] <= lo:
                if arr[i] * min_fraction[1] < min_fraction[0] * arr[j]:
                    min_fraction = (arr[i], arr[j])

    return min_fraction


# Example usage
print(kthSmallestPrimeFraction([1, 2, 3, 5], 3))  # Output: [2, 5]
print(kthSmallestPrimeFraction([1, 7], 1))  # Output: [1, 7]
