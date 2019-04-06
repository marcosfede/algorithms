from dataclasses import dataclass
from typing import Optional, List, Any

with open('./13/input') as f:
    lines = [list(row.rstrip('\n')) for row in f]


@dataclass
class Vector:
    x: int
    y: int

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


@dataclass
class Direction:
    vector: Vector
    next: Optional['Direction'] = None

    def __hash__(self):
        return hash(self.vector)

    def __eq__(self, other):
        return self.vector == other.vector

    def __repr__(self):
        return str(self.vector)


left = Direction(Vector(-1, 0))
right = Direction(Vector(1, 0))
up = Direction(Vector(0, -1))
down = Direction(Vector(0, 1))
left.next = up
up.next = right
right.next = down
down.next = left


@dataclass
class Cart:
    id: int
    position: Vector
    direction: Direction
    crashed = False
    _turns = 0

    def turn(self, rail):
        if rail not in rail_turns:
            return
        if rail == '+':
            turns = self._turns % 3
            if turns == 0:
                self.direction = self.direction.next.next.next  # turn left
            if turns == 1:
                pass  # continue
            if turns == 2:
                self.direction = self.direction.next  # turn right
            self._turns += 1
        else:
            self.direction = corner_turns[(self.direction, rail)]

    def move(self):
        self.position = self.position + self.direction.vector


arrows_to_directions = {
    'v': down,
    '^': up,
    '<': left,
    '>': right,
}
directions_to_arrows = {v: k for k, v in arrows_to_directions.items()}
arrows = set(arrows_to_directions.keys())
track_beneath_cart: Any = {
    'v': '|',
    '^': '|',
    '<': '-',
    '>': '-',
}
corner_turns = {
    (left, '\\'): up,
    (left, '/'): down,
    (right, '\\'): down,
    (right, '/'): up,
    (up, '\\'): left,
    (up, '/'): right,
    (down, '\\'): right,
    (down, '/'): left,
}
# track_beneath_cart = {
#     arrows_to_directions[k]: v for k, v in track_beneath_cart.items()}
rail_turns = set(['\\', '/', '+'])


class Mine:
    def __init__(self, track: List[List[str]]):
        id = 1
        self.track = [[t for t in row] for row in track]
        carts: List[Cart] = []
        for y, row in enumerate(self.track):
            for x, val in enumerate(row):
                if val in arrows:
                    carts.append(
                        Cart(id, Vector(x, y), arrows_to_directions[val]))
                    id += 1
                    self.track[y][x] = track_beneath_cart[val]
        self.carts = carts

    def __repr__(self):
        return '\n'.join(''.join(t) for t in self.track)

    def run(self):
        while True:
            if len(self.carts) == 1:
                print('last cart at: ', self.carts[0].position)
                return

            for cart in self.carts:
                if cart.crashed:
                    continue
                cart.move()
                nextpos = cart.position
                for k in self.carts:
                    if k.position == nextpos and k.id != cart.id:
                        print(f'{k.id} has crashed with {cart.id} at {nextpos}')
                        k.crashed = True
                        cart.crashed = True

                rail = self.track[nextpos.y][nextpos.x]
                cart.turn(rail)

            self.carts = sorted([k for k in self.carts if k.crashed is False], key=lambda c: (
                c.position.y, c.position.x))


mine = Mine(lines)
mine.run()
