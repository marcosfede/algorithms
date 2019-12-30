
from functools import lru_cache
shuffles = []
with open('input.txt') as f:
    for line in f:
        if line.startswith('deal with'):
            inc = int(line.strip().split(' ')[-1])
            shuffles.append((2, inc))
        elif line.startswith('cut'):
            d = int(line.strip().split(' ')[-1])
            shuffles.append((1, d))
        elif line.startswith('deal into'):
            shuffles.append((0,))
        else:
            assert False


def deal_with(inc, arr):
    ans = arr[:]
    for idx, card in enumerate(arr):
        idx_new = (idx * inc) % len(arr)
        ans[idx_new] = card
    return ans


def cut(n, arr):
    return arr[n:] + arr[:n]


def deal_into(arr):
    return list(reversed(arr))


def reverse_deal_into(ncards, idx):
    return ncards - idx - 1


assert reverse_deal_into(10, 0) == 9
assert reverse_deal_into(10, 9) == 0


def reverse_cut(ncards, n, idx):
    n = n % ncards
    if idx < ncards - n:
        return n + idx
    else:
        return idx - (ncards - n)


assert reverse_cut(10, 3, 0) == 3
assert reverse_cut(10, 3, 6) == 9
assert reverse_cut(10, 3, 7) == 0
assert reverse_cut(10, 3, 9) == 2
assert reverse_cut(10, -4, 4) == 0
assert reverse_cut(10, -4, 0) == 6
assert reverse_cut(10, -4, 9) == 5


def reverse_deal_with(ncards, inc, idx):
    return ((ncards - inc)*idx) % ncards


assert reverse_deal_with(10, 3, 0) == 0
assert reverse_deal_with(10, 3, 1) == 7
assert reverse_deal_with(10, 3, 3) == 1
assert reverse_deal_with(10, 3, 2) == 4
assert reverse_deal_with(10, 3, 4) == 8
assert reverse_deal_with(10007, 31, 1) == 8393


def shuffle_many(deck, shuffles):
    for shuffle in shuffles:
        if shuffle[0] == 0:
            new_deck = deal_into(deck)
            for idx in range(len(deck)):
                prev_idx = reverse_deal_into(len(deck), idx)
                assert deck[prev_idx] == new_deck[idx]
            deck = deal_into(deck)
        elif shuffle[0] == 1:
            new_deck = cut(shuffle[1], deck)
            for idx in range(len(deck)):
                prev_idx = reverse_cut(len(deck), shuffle[1], idx)
                assert deck[prev_idx] == new_deck[idx]
            deck = cut(shuffle[1], deck)
        elif shuffle[0] == 2:
            new_deck = deal_with(shuffle[1], deck)
            for idx in range(len(deck)):
                prev_idx = reverse_deal_with(len(deck), shuffle[1], idx)
                print(shuffle)
                print(prev_idx, idx)
                assert deck[prev_idx] == new_deck[idx]
            deck = deal_with(shuffle[1], deck)
    return deck


print('part1: ', shuffle_many(list(range(10007)), shuffles).index(2019))


@lru_cache()
def reverse_shuffle(ncards, idx):
    for shuffle in reversed(shuffles):
        if shuffle[0] == 0:
            idx = reverse_deal_into(ncards, idx)
        elif shuffle[0] == 1:
            idx = reverse_cut(ncards, shuffle[1], idx)
        elif shuffle[0] == 2:
            idx = reverse_deal_with(ncards, shuffle[1], idx)
    return idx


def reverse_shuffles(ntimes, ncards, idx):
    seen = {}
    for time in range(ntimes):
        if time % 100000 == 0:
            print(time)
        idx = reverse_shuffle(ncards, idx)
        if idx in seen:
            print('seen at', seen[idx], 'idx: ', idx)
        else:
            seen[idx] = time
    return idx


for i in range(10007):
    if reverse_shuffle(10007, i) == 2019:
        print('part1: ', i)
        break

# print(reverse_shuffles(101741582076661, 119315717514047, 2020))
