from numpy import rfft, irfft


def convolution(arr1, arr2):
    ftarr1 = rfft(arr1)
    ftarr2 = rfft(arr2)
    return irfft(ftarr1 * ftarr2)


def calc_holes(moves, distances):
    sum_set = set(convolution(moves, moves))
    count = 0
    for hole in distances:
        if hole in sum_set:
            count += 1
        else:
            return count


moves = [1, 3, 5]
distances = [2, 4, 5, 7, 8, 9]

expected_out = 4
