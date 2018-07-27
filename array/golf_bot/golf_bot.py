import numpy as np
from numpy.fft import rfft, irfft


def self_convolution(arr):
    n = len(arr)
    k = 2 * n - 1
    ftarr = rfft(arr, k)
    return irfft(ftarr * ftarr, k)


def calc_holes(moves, distances):
    moves_poly = np.zeros(np.max(moves) + 1)
    for move in moves:
        moves_poly[move] = 1
    moves_poly[0] = 1
    conv = self_convolution(moves_poly)
    return sum(round(conv[d]) > 0 for d in distances)


moves = [1, 3, 5]
distances = [2, 4, 5, 7, 8, 9]

expected_out = 4
print(calc_holes(moves, distances))
