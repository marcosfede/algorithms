def split(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]


def count(l, v):
    return sum(map(lambda x: 1 if x == v else 0, l))


def collapse(layers):
    return [next(filter(lambda v: v != 2, lay)) for lay in zip(*layers)]


def draw(img):
    for r in img:
        print(*['#' if x == 1 else ' ' for x in r])


lenx, leny = 25, 6
size = lenx * leny

data = [int(x) for x in open('./input.txt').read().strip('\n')]
layers = split(data, size)

# Part 1
best = min(layers, key=lambda l: count(l, 0))
print(count(best, 1) * count(best, 2))

# Part 2
img = split(collapse(layers), lenx)
draw(img)
