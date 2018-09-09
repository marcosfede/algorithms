"""
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands.
An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""


# O(n*m) recursive
def num_islands(grid):
    count = 0
    for y, row in enumerate(grid):
        for x, col in enumerate(grid[y]):
            if col == 1:
                DFS(grid, x, y)
                count += 1
    return count


def DFS(grid, x, y):
    grid[y][x] = 0
    for neigh in neighbours((x, y), grid):
        DFS(grid, neigh[0], neigh[1])


def neighbours(coord, grid):
    for delta in (0, 1), (0, -1), (1, 0), (-1, 0):
        newcoords = (coord[0] + delta[0], coord[1] + delta[1])
        if 0 <= newcoords[0] < len(grid[0]) and 0 <= newcoords[1] < len(grid):
            if grid[newcoords[1]][newcoords[0]] == 1:
                yield newcoords


# O(n*m) iterative
def num_islands2(grid):
    q = set((x, y) for y in range(len(grid))
            for x in range(len(grid[0])) if grid[y][x] == 1)
    count = 0
    while q:
        current = q.pop()
        q2 = set()
        q2.add(current)
        visited = set()
        while q2:
            next = q2.pop()
            visited.add(next)
            for n in neighbours(next, grid):
                if n not in visited:
                    q2.add(n)
        # remove from q all the nodes in this island
        q -= visited
        count += 1
    return count


assert num_islands([[1, 1, 0], [0, 0, 1], [0, 1, 0]]) == 3
assert num_islands([[1, 0, 0], [0, 0, 1], [0, 0, 0]]) == 2
assert num_islands([[1, 1, 0], [1, 1, 1], [0, 0, 1]]) == 1
