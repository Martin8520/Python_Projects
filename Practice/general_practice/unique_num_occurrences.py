def uniqueOccurrences(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    occurrence_set = set()
    for occurrence in count.values():
        if occurrence in occurrence_set:
            return False
        occurrence_set.add(occurrence)

    return True


arr1 = [1, 2, 2, 1, 1, 3]
print(uniqueOccurrences(arr1))  # True

arr2 = [1, 2]
print(uniqueOccurrences(arr2))  # False

arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
print(uniqueOccurrences(arr3))  # True
