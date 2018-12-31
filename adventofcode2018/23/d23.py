from collections import namedtuple
import re
from z3 import Int, If, Optimize


def l1(v1, v2):
    return abs(v1.x-v2.x) + abs(v1.y-v2.y) + abs(v1.z-v2.z)


class Vector3(namedtuple('Vector3', ['x', 'y', 'z'])):
    def __add__(self, other):
        return Vector3(self.x+other.x, self.y+other.y, self.z+other.z)


Bot = namedtuple('Bot', ['pos', 'r'])

bots = []
regex = r'pos=\<(-*\d+),(-*\d+),(-*\d+)\>, r=(\d+)$'
with open('./23/input.txt') as f:
    for line in f:
        match = re.match(regex, line)
        x, y, z, r = [int(v) for v in match.groups()]
        bots.append(Bot(pos=Vector3(x, y, z), r=r))

# p1
strongest = max(bots, key=lambda b: b.r)
inrange = [b for b in bots if l1(strongest.pos, b.pos) <= strongest.r]
print(len(inrange))

# p2


def z3_abs(x):
    return If(x >= 0, x, -x)


def z3_dist(v1, v2):
    return z3_abs(v1.x-v2.x) + z3_abs(v1.y-v2.y) + z3_abs(v1.z-v2.z)


x = Int('x')
y = Int('y')
z = Int('z')
orig = (x, y, z)
cost = Int('cost')
cost_expr = 0
for bot in bots:
    cost_expr += If(z3_dist(Vector3(*orig), bot.pos) <= bot.r, 1, 0)
opt = Optimize()

print("let's go")
opt.add(cost == cost_expr)
opt.maximize(cost)
opt.minimize(z3_dist(Vector3(0, 0, 0), Vector3(x, y, z)))

opt.check()

model = opt.model()
print(model)
pos = (model[x].as_long(), model[y].as_long(), model[z].as_long())
print("position:", pos)
print("num in range:", model[cost].as_long())
print("distance:", l1(Vector3(0, 0, 0), Vector3(*pos)))
