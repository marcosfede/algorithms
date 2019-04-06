from dataclasses import dataclass
import re
from typing import List, Tuple


@dataclass
class Vector:
    x: int
    y: int


@dataclass
class Star:
    pos: Vector
    vel: Vector

    def position_at(self, time: int) -> Vector:
        return Vector(self.pos.x + time*self.vel.x, self.pos.y + time*self.vel.y)


stars = []
regex = r'position=<([-*| ]\d+), ([-*| ]\d+)> velocity=<([-*| ]\d+), ([-*| ]\d+)>'
with open('input') as f:
    for line in f:
        match = re.match(regex, line)
        x, y, vx, vy = map(int, match.groups())
        stars.append(Star(Vector(x, y), Vector(vx, vy)))


def bounds(positions: List[Vector]) -> Tuple[int]:
    minx = 10*10000000
    maxx = -10*10000000
    miny = 10*10000000
    maxy = -10*10000000
    for star in positions:
        if star.x < minx:
            minx = star.x
        if star.x > maxx:
            maxx = star.x
        if star.y < miny:
            miny = star.y
        if star.y > maxy:
            maxy = star.y
    return minx, maxx, miny, maxy


def print_sky(positions: List[Vector], minx, maxx, miny, maxy):
    matrix = [['.' for x in range(minx, maxx+1)] for y in range(miny, maxy+1)]
    for star in positions:
        matrix[star.y-miny][star.x-minx] = '#'
    print('\n'.join([''.join(x) for x in matrix]))


# tweak these so you find small area, message should be visible on a terminal...
mint = 10000
maxt = 11000
areas = []
for t in range(mint, maxt+1):
    positions = [star.position_at(t) for star in stars]
    minx, maxx, miny, maxy = bounds(positions)
    area = abs(maxx-minx)*abs(maxy-miny)
    areas.append((area, t))

t_min = min(areas, key=lambda x: x[0])[1]
positions = [star.position_at(t_min) for star in stars]
minx, maxx, miny, maxy = bounds(positions)
# p1
print_sky(positions, minx, maxx, miny, maxy)

# p2
print('t min at: ', t_min)
