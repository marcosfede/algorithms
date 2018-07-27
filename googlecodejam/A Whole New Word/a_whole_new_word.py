

def resolve(N, L, dobleve):
    if L == 1:
        return "-"
    if L == 2:
        c = comb(dobleve, 0, 1)
        if c is None:
            return "-"
        else:
            return c
    for i in range(0, L):
        for j in range(0, L):
            if i != j:
                c = comb(dobleve, i, j)
                if c is not None:
                    word = list(dobleve[0])
                    word[i] = c[0]
                    word[j] = c[1]
                    return "".join(word)
    return "-"

def comb(dobleve, N1, N2):
    C2 = set()
    dic = {}
    for w in dobleve:
        if w[N1] not in dic:
            dic[w[N1]] = set()
        dic[w[N1]].add(w[N2])
        C2.add(w[N2])
    for k, v in dic.items():
        if C2 - v:
            return '{}{}'.format(k, (C2-v).pop())
    return None

def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        N, L = map(int, input().split(" "))
        dobleve = []
        for word in range(1, N + 1):
            dobleve.append(input())
        sol = resolve(N, L, dobleve)
        print("Case #{}: {}".format(case, sol))

read_input()