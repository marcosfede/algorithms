import os
from time import sleep


class Acre:

    @classmethod
    def from_char(cls, char):
        for subclass in cls.__subclasses__():
            if subclass.char == char:
                return subclass()

    def evolve(neighbours):
        pass


class Open(Acre):
    char = '.'

    def evolve(self, neighbours):
        ntrees = sum(isinstance(n, Tree) for n in neighbours)
        return Tree() if ntrees >= 3 else self


class Tree(Acre):
    char = '|'

    def evolve(self, neighbours):
        nlumberyards = sum(isinstance(n, Lumberyard) for n in neighbours)
        return Lumberyard() if nlumberyards >= 3 else self


class Lumberyard(Acre):
    char = '#'

    def evolve(self, neighbours):
        ntrees = sum(isinstance(n, Tree) for n in neighbours)
        nlumberyards = sum(isinstance(n, Lumberyard) for n in neighbours)
        return self if (ntrees >= 1 and nlumberyards >= 1) else Open()


# def transition_open(ntrees, nlumberyards):
#     return '|' if ntrees >= 3 else '.'


# def transition_tree(ntrees, nlumberyards):
#     return '#' if nlumberyards >= 3 else '|'


# def transition_lumberyard(ntrees, nlumberyards):
#     return '|' if (ntrees >= 1 and nlumberyards >= 1) else '.'


class Forest:
    @classmethod
    def from_file(cls, f):
        forest = []
        for line in f:
            row = []
            for char in line.strip():
                row.append(Acre.from_char(char))
            forest.append(row)

        return cls(forest)

    def __init__(self, forest):
        self.forest = forest

    def get_neighbours(self, x, y):
        neighbours = []
        for points in (x-1, y+1), (x, y+1), (x+1, y+1), (x-1, y), (x+1, y), (x-1, y-1),  (x, y-1), (x+1, y-1):
            px, py = points
            if not (0 <= px < len(self.forest[0])) or not (0 <= py < len(self.forest)):
                continue
            neighbours.append(self.forest[py][px])
        return neighbours

    def step(self):
        nextstate = []
        for y, col in enumerate(self.forest):
            newcol = []
            for x, acre in enumerate(col):
                neigh = self.get_neighbours(x, y)
                next_acre = acre.evolve(neigh)
                newcol.append(next_acre)
            nextstate.append(newcol)

        self.forest = nextstate
        # os.system('clear')
        # print(self)
        # sleep(0.01)

    def run_generations(self, number):
        for gen in range(number):
            self.step()

    @property
    def resource_value(self):
        trees = sum(isinstance(x, Tree) for row in self.forest for x in row)
        lumbs = sum(isinstance(x, Lumberyard)
                    for row in self.forest for x in row)
        return trees * lumbs

    def __repr__(self):
        return '\n'.join([''.join(x.char for x in line) for line in self.forest])


with open('./18/input.txt') as f:
    # p1
    forest = Forest.from_file(f)
    forest.run_generations(10)
    print(forest.resource_value)

with open('./18/input.txt') as f:
    # p2
    forest = Forest.from_file(f)
    # pattern repeats every 28 minutes, after the first 476 or so minutes
    forest.run_generations(17*28 + 1000000000 % 28)
    print(forest.resource_value)
