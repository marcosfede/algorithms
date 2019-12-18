import itertools

inpt = [int(x) for x in open('./input.txt').read().strip()]


def dot(a, b):
    return sum((x*y) for x, y in zip(a, b))


def calc_for_idx(inpt, i):
    pattern = itertools.cycle(itertools.chain(itertools.repeat(
        0, i+1), itertools.repeat(1, i+1), itertools.repeat(0, i+1), itertools.repeat(-1, i+1)))
    next(pattern)
    return abs(dot(inpt, pattern)) % 10


def step(inpt):
    return [calc_for_idx(inpt, i) for i, x in enumerate(inpt)]


def fft(inpt, times):
    for times in range(times):
        out = step(inpt)
        inpt = out
    return out


def part1(inpt):
    offset = 0
    return ''.join(map(str, fft(inpt, 100)[:8]))


print(f'part1: {part1(inpt)}')


def part2(inpt, offset):
    off = offset % len(inpt)
    out = inpt[off:] + inpt * ((len(inpt)*10000 - offset)//len(inpt))

    for iter in range(100):
        accum = 0
        for idx in range(len(out)-1, -1, -1):
            accum += out[idx]
            out[idx] = abs(accum) % 10
    return ''.join(map(str, out[:8]))


offset = int(''.join(map(str, inpt[:7])))
print(f'part2: {part2(inpt,offset)}')
