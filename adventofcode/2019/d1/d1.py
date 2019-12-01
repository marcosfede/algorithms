import math

masses = []
with open('./input.txt') as f:
    for i, line in enumerate(f):
        masses.append(int(line))


def calc_fuel(mass):
    return math.floor(mass/3) - 2


def calc_true_fuel(mass):
    fuel = calc_fuel(mass)
    next_cost = calc_fuel(fuel)
    while next_cost > 0:
        fuel += next_cost
        next_cost = calc_fuel(next_cost)
    return fuel


# p1
print(sum(map(calc_fuel, masses)))

# p2
print(sum(map(calc_true_fuel, masses)))
