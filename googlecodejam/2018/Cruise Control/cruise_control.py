from collections import namedtuple
from functools import partial

Horse = namedtuple('Horse', ['x', 'v'])


def time_to_target(target, horse):
    return (target - horse.x) / horse.v


def solve(horses, target):
    time_horse = partial(time_to_target, target)
    slowest = max(horses, key=time_horse)
    time = time_horse(slowest)
    return target / time


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        dist, horses = map(int, input().split(" "))
        horse_list = []
        for horse in range(horses):
            info = Horse(*map(int, input().split(" ")))
            horse_list.append(info)
        solution = solve(horse_list, dist)
        print('CASE #{}: {}'.format(case, solution))


read_input()
