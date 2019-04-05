from math import atan, sqrt, sin, cos


def dot(matrix, vector):
    sol = []
    for row in matrix:
        total = 0
        for left, right in zip(row, vector):
            total += left * right
        sol.append(total)
    return sol


def solve(A):
    # vectors to the faces of the cube
    p1 = (0.5, 0, 0)
    p2 = (0, 0.5, 0)
    p3 = (0, 0, 0.5)
    sqrt2 = sqrt(2)
    # u is the unitary along rotation axis (-0.5, 0, 0.5)
    ux = -1 * 0.5 * sqrt2
    uz = 0.5 * sqrt2
    # inverse of the relation between area and angle
    theta = 2 * atan((sqrt2 - sqrt(3 - A ** 2)) / (A + 1))
    c, s = cos(theta), sin(theta)
    # R is the rotation matrix
    R = [
        [c + ux ** 2 * (1 - c), -uz * s, ux * uz * (1 - c)],
        [uz * s, c, -ux * s],
        [ux * uz * (1 - c), ux * s, c + uz ** 2 * (1 - c)]
    ]
    p1r = dot(R, p1)
    p2r = dot(R, p2)
    p3r = dot(R, p3)
    return [p1r, p2r, p3r]


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        area = float(input())
        sol = solve(area)
        print("Case #{}:".format(case))
        for row in sol:
            print(" ".join(map(str, row)))


read_input()
