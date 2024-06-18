from collections import Counter


def findLeastNumOfUniqueInts(arr, k):
    freq = Counter(arr)

    freq_list = sorted(freq.values())

    for count in freq_list:
        if k >= count:
            k -= count
        else:
            break

    unique_count = len(freq_list) - (freq_list.index(count) if k < count else len(freq_list))

    return unique_count


print(findLeastNumOfUniqueInts([5, 5, 4], 1))  # 1
print(findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))  # 2
