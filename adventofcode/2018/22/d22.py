import networkx as nx

depth = 3066
target = (13, 726)
mod = 20183

offsetx = 20
offsety = 50
maxy = target[1]+1 + offsety
maxx = target[0]+1 + offsetx

geo_index = [[0]*maxx for _ in range(maxy)]
erosion = [[0]*maxx for _ in range(maxy)]

for y in range(maxy):
    geo = (y*48271)
    geo_index[y][0] = geo
    erosion[y][0] = (geo + depth) % mod

for x in range(maxx):
    geo = (x*16807)
    geo_index[0][x] = geo
    erosion[0][x] = (geo + depth) % mod

for y in range(1, maxy):
    for x in range(1, maxx):
        geo = (erosion[y-1][x]*erosion[y][x-1])
        geo_index[y][x] = geo
        erosion[y][x] = (geo + depth) % mod

geo_index[target[1]][target[0]] = 0
erosion[target[1]][target[0]] = 510
types = [[col % 3 for col in row] for row in erosion]


def print_cave(types):
    type_map = {0: '.', 1: '=', 2: '|'}
    cave = [[type_map[col] for col in row] for row in types]
    cave[0][0] = 'M'
    cave[target[1]][target[0]] = 'T'
    print('\n'.join([''.join(row) for row in cave]))


# print_cave(types)

# p1
print(sum(sum(row) for row in types))


# p2
allowed_jumps = {
    (0, 0): 'CT',
    (0, 1): 'C',
    (0, 2): 'T',
    (1, 0): 'C',
    (1, 1): 'CN',
    (1, 2): 'N',
    (2, 0): 'T',
    (2, 1): 'N',
    (2, 2): 'TN'
}

G = nx.Graph()

for tool in 'TCN':
    for y, row in enumerate(types):
        for x, type in enumerate(row):
            # skip if can't be reached with current tool
            if tool not in allowed_jumps[(type, type)]:
                continue
            # connect with neighbours
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                xp, yp = x+dx, y+dy
                # check out of bounds
                if xp < 0 or xp >= maxx or yp < 0 or yp >= maxy:
                    continue
                type2 = types[yp][xp]
                # check if can be crossed with current tool
                if tool in allowed_jumps[(type, type2)]:
                    G.add_edge((tool, (x, y)), (tool, (xp, yp)), weight=1)
            # connect node with parallel map using other tool
            for nexttool in allowed_jumps[(type, type)]:
                if nexttool != tool:
                    G.add_edge((tool, (x, y)), (nexttool, (x, y)), weight=7)


source = ('T', (0, 0))
destination = ('T', target)
print(nx.shortest_path_length(G, source, destination, weight='weight'))
