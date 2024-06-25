def findMinArrowShots(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])

    arrows = 1
    current_end = points[0][1]

    for xstart, xend in points[1:]:
        if xstart > current_end:
            arrows += 1
            current_end = xend

    return arrows


# Test cases
print(findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))  # 2
print(findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))  # 4
print(findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))  # 2
