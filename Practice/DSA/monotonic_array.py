def monotonic_array(array):
    increasing = True
    decreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            increasing = False
            break

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            decreasing = False
            break

    return increasing or decreasing
