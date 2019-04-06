#!/usr/local/bin/python3
import sys


def count_uniq(s):
    prev = '1'
    counts = []
    counter = 0
    for ch in s:
        if ch == prev:
            counter += 1
        else:
            counts.append(counter)
            prev = ch
            counter = 1
    counts.append(counter)
    return counts


def solve(n, b, responses):
    def solve2(base_start, start, num_buenos, depth):
        if num_buenos == 0:
            return
        base_slice_len = 2*(16//2**depth)
        base_end = base_start + base_slice_len

        rx = responses[depth][start:start+num_buenos]

        buenos = count_uniq(rx)
        if len(buenos) == 2:
            buenos1, buenos0 = buenos
        else:
            buenos1 = buenos[0]
            buenos0 = 0

        if buenos1 == base_slice_len // 2:
            for i in range(base_start, base_start+buenos1):
                fallados[i] = False
        else:
            solve2(base_start, start, buenos1, depth+1)

        if buenos0 == base_slice_len // 2:
            for i in range(base_start + base_slice_len // 2, base_end):
                fallados[i] = False
        else:
            solve2(base_start + base_slice_len // 2,
                   start+buenos1, buenos0, depth+1)

    fallados = [True]*n
    buenos = count_uniq(responses[0])

    start_in_responses = 0
    for ind, buenos_en_bloque in enumerate(buenos):
        solve2(ind*16, start_in_responses, buenos_en_bloque, 1)
        start_in_responses += buenos_en_bloque

    ans = [idx for idx, fallado in enumerate(fallados) if fallado]
    return ' '.join([str(x) for x in ans])


def log(*args):
    print(*args, file=sys.stderr)


def build_query(depth, n):
    s = (('1'*(16//2**depth) + '0'*(16//2**depth)))*(1024//(2*(16//2**depth)))
    return s[:n]


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        ipt = input()
        log('recieved input: ', ipt)
        n, b, f = list(map(int, ipt.split(' ')))
        log('n b f', n, b, f)

        responses = []
        for depth in range(0, 5):
            query = build_query(depth, n)
            print(query)
            responses.append(input())
        log('query responses', responses)
        solution = solve(n, b, responses)
        log('solution', solution)
        print(solution)
        if input() != '1':
            log('wrong answer')
        else:
            log('correct!')
            log('')


read_input()
