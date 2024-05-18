from collections import defaultdict
from math import gcd


def maxPoints(points):
    def get_slope(p1, p2):
        dy = p2[1] - p1[1]
        dx = p2[0] - p1[0]
        if dx == 0:
            return 1, 0
        if dy == 0:
            return 0, 1
        g = gcd(dx, dy)
        return dy // g, dx // g

    n = len(points)
    if n <= 2:
        return n

    max_points = 1

    for i in range(n):
        slopes = defaultdict(int)
        for j in range(i + 1, n):
            slope = get_slope(points[i], points[j])
            slopes[slope] += 1
        current_max = max(slopes.values(), default=0) + 1
        max_points = max(max_points, current_max)

    return max_points


points1 = [[1, 1], [2, 2], [3, 3]]
print(maxPoints(points1))  # 3

points2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
print(maxPoints(points2))  # 4
