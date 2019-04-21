from collections import defaultdict

def solve2(words):
    if len(words) < 2:
        return 0
    if len(words) <= 3:
        return 1
    d = defaultdict(list)
    for word in words:
        if len(word) > 0:
            d[word[-1]].append(word[:-1])
    count = 0

    for key,val in d.items():
        count += solve2(val)

    huerfanos = len(words) - (2* count)
    if huerfanos > 1:
        count += 1
    return count

def solve(words):
    d = defaultdict(list)
    for word in words:
        d[word[-1]].append(word[:-1])
    count = 0
    for key,val in d.items():
        count += solve2(val)
    return count

def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        k_cases = int(input())
        thelist = []
        for kase in range(1, k_cases + 1):
            thelist.append(input())
        print("CASE #{}: {}".format(case,solve(thelist) * 2))


read_input()
