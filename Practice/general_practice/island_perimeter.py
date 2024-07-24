def islandPerimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 2

                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 2

    return perimeter


grid1 = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(islandPerimeter(grid1))

grid2 = [[1]]
print(islandPerimeter(grid2))

grid3 = [[1, 0]]
print(islandPerimeter(grid3))
