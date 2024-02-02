def is_triangle(a, b, c):
    sides = sorted([a, b, c])

    return sides[0] + sides[1] > sides[2]


x1 = is_triangle(3, 4, 5)
print(x1)

x2 = is_triangle(3, 6, 3)
print(x2)
