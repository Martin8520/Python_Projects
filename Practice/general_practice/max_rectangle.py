def maximalRectangle(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_area = 0

    heights = [0] * (cols + 1)

    for row in range(rows):
        stack = []
        for col in range(cols + 1):
            if col < cols:
                if matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            while stack and heights[col] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = col if not stack else col - stack[-1] - 1
                max_area = max(max_area, h * w)

            stack.append(col)

    return max_area


matrix1 = [["1", "0", "1", "0", "0"],
           ["1", "0", "1", "1", "1"],
           ["1", "1", "1", "1", "1"],
           ["1", "0", "0", "1", "0"]]
print(maximalRectangle(matrix1))

matrix2 = [["0"]]
print(maximalRectangle(matrix2))

matrix3 = [["1"]]
print(maximalRectangle(matrix3))
