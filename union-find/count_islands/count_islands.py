# O(k) with k = len(positions). additions and unions take constant time
def num_islands(m, n, positions):
    ans = []
    islands = Union()
    for p in map(tuple, positions):
        islands.add(p)
        for dp in (0, 1), (0, -1), (1, 0), (-1, 0):
            q = (p[0] + dp[0], p[1] + dp[1])
            if q in islands.parents:
                islands.union(p, q)
        ans += [islands.count]
    return ans


class Union:
    def __init__(self):
        self.parents = {}
        self.sizes = {}
        self.count = 0

    def add(self, p):
        self.parents[p] = p
        self.sizes[p] = 1
        self.count += 1

    def find(self, i):
        # path halving
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
        return i

    def union(self, p, q):
        i, j = self.root(p), self.root(q)
        if i == j:
            return
        # union by size. attach smallest to largest
        if self.sizes[i] > self.sizes[j]:
            i, j = j, i
        self.parents[i] = j
        self.sizes[j] += self.sizes[i]
        self.count -= 1
