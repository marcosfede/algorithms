from dataclasses import dataclass
from collections import Counter

points = []


@dataclass
class Point:
    id: int
    x: int
    y: int

    def dist_to(self, x, y):
        return abs(self.x - x) + abs(self.y - y)


@dataclass
class Neighbour:
    distance: int
    to: int


with open('input') as f:
    for i, line in enumerate(f):
        coords = tuple(map(int, line.split(", ")))
        points.append(Point(i, coords[0], coords[1]))


maxx = max(point.x for point in points)
maxy = max(point.y for point in points)


# p1
matrix = []
for y in range(maxy):
    row = []
    for x in range(maxx):
        min_dist = maxx + maxy
        best = None
        for point in points:
            dist = point.dist_to(x, y)
            if dist < min_dist:
                min_dist = dist
                best = point
        row.append(Neighbour(min_dist, best))
    matrix.append(row)

infinite = set(n.to.id for n in matrix[0]) | set(
    n.to.id for n in matrix[-1]) | set(y[0].to.id for y in matrix) | set(y[-1].to.id for y in matrix)
counter = Counter(
    n.to.id for y in matrix for n in y if n.to.id not in infinite)
print(max(counter.values()))

# p2
blocks = 0
for y in range(maxy):
    for x in range(maxx):
        total_dist = sum(p.dist_to(x, y) for p in points)
        if total_dist < 10000:
            blocks += 1
print(blocks)
