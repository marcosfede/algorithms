def garage(beg, end):
    i = 0
    moves = 0
    while beg != end:
        if beg[i] != 0 and beg[i] != end[i]:
            car = beg[i]
            empty = beg.index(0)
            final_pos = end.index(beg[i])
            if empty != final_pos:
                beg[final_pos], beg[empty] = beg[empty], beg[final_pos]
                print(beg)
                empty = beg.index(0)
                beg[beg.index(
                    car)], beg[empty] = beg[empty], beg[beg.index(car)]
                print(beg)
                moves += 2
            else:
                beg[beg.index(
                    car)], beg[empty] = beg[empty], beg[beg.index(car)]
                print(beg)
                moves += 1
        i += 1
        if i == len(beg):
            i = 0
    return moves


if __name__ == "__main__":
    initial = [1, 2, 3, 0, 4]
    final = [0, 3, 2, 1, 4]
    print("initial:", initial)
    print("final:", final)
    print(garage(initial, final))
