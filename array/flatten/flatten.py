from functools import reduce


def list_flatten(l):
    def flatten(pv, cv):
        if not isinstance(cv, list):
            return pv + [cv]
        else:
            return pv + list_flatten(cv)
    return reduce(flatten, l, [])


print(list_flatten([2, 1, [3, [4, 5], 6], 7, [8]]))
print('output should be [2, 1, 3, 4, 5, 6, 7, 8]')
