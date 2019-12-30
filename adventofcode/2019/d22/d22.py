
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


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def reverse_deal_into(ncards, idx):
    return ncards - idx - 1


def reverse_cut(ncards, n, idx):
    n = n % ncards
    return (n+idx) % ncards


def reverse_deal_with(ncards, inc, idx):
    return modinv(inc, ncards)*idx % ncards
    # return pow(inc, ncards - 2, ncards)*idx % ncards  # fetmat's little theorem, only works for prime ncards


def reverse_shuffle(ncards, idx):
    for shuffle in reversed(shuffles):
        if shuffle[0] == 0:
            idx = reverse_deal_into(ncards, idx)
        elif shuffle[0] == 1:
            idx = reverse_cut(ncards, shuffle[1], idx)
        elif shuffle[0] == 2:
            idx = reverse_deal_with(ncards, shuffle[1], idx)
    return idx


# p1
for i in range(10007):
    if reverse_shuffle(10007, i) == 2019:
        print('part1: ', i)
        break

# p2
ntimes = 101741582076661
ncards = 119315717514047

# all operations are linear in the index modulo ncards. f(x) = A*x + B. We can get A, B using 2 points
X = 2020
Y = reverse_shuffle(ncards, X)
Z = reverse_shuffle(ncards, Y)
A = (Y-Z) * modinv(X-Y+ncards, ncards) % ncards
B = (Y-A*X) % ncards
"""
apply f(x) ntimes, use geometric series formula
f^n(x) = A^n*x + A^(n-1)*B + A^(n-2)*B + ... + B
       = A^n*x + (A^(n-1) + A^(n-2) + ... + 1) * B
       = A^n*x + (A^n-1) / (A-1) * B
"""
print('part2: ', (pow(A, ntimes, ncards)*X + (pow(A, ntimes, ncards)-1)
                  * modinv(A-1, ncards) * B) % ncards)
