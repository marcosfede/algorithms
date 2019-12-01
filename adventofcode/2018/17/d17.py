from collections import namedtuple
import re


class Vector(namedtuple('Vector', 'x y')):
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


clay = set()
with open('./17/input.txt') as f:
    regex = r'(y)*(x)*=(\d+), (y)*(x)*=(\d+)..(\d+)'
    for line in f:
        m = re.match(regex, line)
        y1, x1, n1, y2, x2, n2, n3 = m.groups()
        n1, n2, n3 = int(n1), int(n2), int(n3)
        if y1:
            for x in range(n2, n3+1):
                clay.add(Vector(x, n1))
        else:
            for y in range(n2, n3+1):
                clay.add(Vector(n1, y))


SPRING = Vector(500, 0)
UP = Vector(0, -1)
DOWN = Vector(0, 1)
LEFT = Vector(-1, 0)
RIGHT = Vector(1, 0)


def simulate():
    maxy, miny = max(p.y for p in clay), min(p.y for p in clay)
    flowing, still, to_fall, to_spread = set(), set(), set(), set()

    to_fall.add(SPRING)
    while to_fall or to_spread:
        while to_fall:
            tf = to_fall.pop()
            res = fall(tf, maxy, clay, flowing)
            if res:
                to_spread.add(res)

        while to_spread:
            ts = to_spread.pop()
            rl, rr = spread(ts, clay, flowing, still)
            if not rr and not rl:
                to_spread.add(ts + UP)
            else:
                if rl:
                    to_fall.add(rl)
                if rr:
                    to_fall.add(rr)

    # Output
    print('Total Water = %d' %
          len([p for p in (flowing | still) if p.y >= miny]))
    print('Still Water = %d' % len([p for p in still if p.y >= miny]))


def fall(pos, maxy, clay, flowing):
    while pos.y < maxy:
        posd = pos + DOWN
        if posd not in clay:
            flowing.add(posd)
            pos = posd
        elif posd in clay:
            return pos
    return None


def spread(pos, clay, flowing, still):
    temp = set()
    pl = spread_r(pos, LEFT, clay, still, temp)
    pr = spread_r(pos, RIGHT, clay, still, temp)
    if not pl and not pr:
        still.update(temp)
    else:
        flowing.update(temp)
    return pl, pr


def spread_r(pos, off, clay, still, temp):
    pos1 = pos
    while pos1 not in clay:
        temp.add(pos1)
        pos2 = pos1 + DOWN
        if pos2 not in clay and pos2 not in still:
            return pos1
        pos1 = pos1 + off
    return None


if __name__ == '__main__':
    simulate()
