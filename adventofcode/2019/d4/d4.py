from itertools import groupby


def valid(code, pred):
    # 599922 => ('5', '9', '2'), (1, 3, 2)
    keys, counts = zip(*[(k, len(list(g))) for k, g in groupby(str(code))])
    return all(b >= a for a, b in zip(keys, keys[1:])) and pred(counts)


a, b = 284639, 748759
# p1
print(sum(valid(code, lambda counts: any(count > 1 for count in counts))
          for code in range(a, b)))
# p2
print(sum(valid(code, lambda counts: any(count == 2 for count in counts)) for code in range(a, b)))
