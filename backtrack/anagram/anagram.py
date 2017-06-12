# probably the most pythonic (and fastest) way
def perm(word):
    from itertools import permutations
    return permutations(word)


def perm(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for per in perm(elements[1:]):
            for i in range(len(elements)):
                yield per[:i] + elements[0:1] + per[i:]

# cute but slow oneliner
def perm(word):
    yield from (l + x for i, l in enumerate(word) for x in perm(word[:i] + word[i + 1:])) if len(word) > 1 else word


word = 'abcdefghi'
print(len(list(perm(word))))
