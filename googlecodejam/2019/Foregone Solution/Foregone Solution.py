def solve(num):
    l = len(str(num))
    a, b = num-1, 1

    for index, char in enumerate(str(a)):
        if char == '4':
            a -= 10**(l-index-1)
            b += 10**(l-index-1)

    return a, b


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        n = int(input())
        a, b = solve(n)
        print("CASE #{}: {} {}".format(case, a, b))


read_input()
