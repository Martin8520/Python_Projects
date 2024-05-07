def sorted_squared(array):
    n = len(array)
    i, j = 0, n-1
    res = [0] * n
    for k in reversed(range(n)):
        if array[i] ** 2 > array[j] ** 2:
            res[k] = array[j] ** 2
            i += 1
        else:
            res[k] = array[j] ** 2
            j -= 1
    return res
