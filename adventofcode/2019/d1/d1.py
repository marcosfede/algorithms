masses = []
with open('./input.txt') as f:
    for i, line in enumerate(f):
        masses.append(int(line))


def calc_fuel(mass):
    return mass//3 - 2


def calc_true_fuel(mass):
    fuel = calc_fuel(mass)
    return 0 if fuel <= 0 else fuel + calc_true_fuel(fuel)


# p1
print(sum(map(calc_fuel, masses)))

# p2
print(sum(map(calc_true_fuel, masses)))
