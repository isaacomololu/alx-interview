#!/usr/bin/python3
''' Island perimeter computing module.
'''


def island_perimeter(grid):
    '''
    Returns the perimeter of the island described in grid with no lakes.
    '''
    visit = set()

    def dfs(i, j):
        if i >= len(grid) or j >= len(grid[0]) or\
              i < 0 or j < 0 or grid[i][j] == 0:
            return 1

        if (i, j) in visit:
            return 0

        visit.add((i, j))
        perim = dfs(i, j + 1)
        perim += dfs(i, j - 1)
        perim += dfs(i + 1, j)
        perim += dfs(i - 1, j)
        return perim

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                return dfs(row, col)
