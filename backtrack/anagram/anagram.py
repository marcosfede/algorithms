def perm(word):
    from itertools import permutations
    return permutations(word)


def perm(word):
    yield from (l + x for i, l in enumerate(word) for x in perm(word[:i] + word[i + 1:])) if len(word) > 1 else word

