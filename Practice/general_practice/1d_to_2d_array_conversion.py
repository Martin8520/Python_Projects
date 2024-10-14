def construct2DArray(original, m, n):
    if m * n != len(original):
        return []
    return [original[i * n:(i + 1) * n] for i in range(m)]

original = [1, 2, 3, 4]
m = 2
n = 2
print(construct2DArray(original, m, n))

original = [1, 2, 3]
m = 1
n = 3
print(construct2DArray(original, m, n))

original = [1, 2]
m = 1
n = 1
print(construct2DArray(original, m, n))
