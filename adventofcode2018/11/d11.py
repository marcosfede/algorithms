

def power(snumber, x, y):
    return ((((((x + 10) * y) + snumber)*(x+10))//100) % 10)-5


def build_grid_sum(grid):
    grid_sums = [[0]*300 for _ in range(300)]
    for y, vy in enumerate(grid):
        for x, vx in enumerate(vy):
            B = grid_sums[y-1][x] if y > 0 else 0
            C = grid_sums[y][x-1] if x > 0 else 0
            A = grid_sums[y-1][x-1] if y > 0 and x > 0 else 0
            grid_sums[y][x] = C + B - A + vx
    return grid_sums


snumber = 2694
grid = [[power(snumber, x, y) for x in range(0, 300)] for y in range(0, 300)]
grid_sums = build_grid_sum(grid)


def power_between(grid_sums, x1, y1, x2, y2):
    return grid_sums[y2][x2] + grid_sums[y1][x1] - grid_sums[y2][x1] - grid_sums[y1][x2]


# p1
max_power = 0
best_coords = None
block_size = 3
for y in range(300 - block_size):
    for x in range(300 - block_size):
        total_power = power_between(
            grid_sums, x, y, x+block_size, y+block_size)
        if total_power > max_power:
            best_coords = (x, y)
            max_power = total_power

# coords are 0-based...
print(best_coords[0]+1, best_coords[1]+1)

# p2
max_power = 0
best_coords = None
best_block_size = None
for block_size in range(1, 301):
    for y in range(300 - block_size):
        for x in range(300 - block_size):
            total_power = power_between(
                grid_sums, x, y, x+block_size, y+block_size)
            if total_power > max_power:
                best_coords = (x, y)
                max_power = total_power
                best_block_size = block_size

# coords are 0-based...
print(best_coords[0]+1, best_coords[1]+1, best_block_size)
