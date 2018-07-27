from typing import List


class FastList:

    def __init__(self, arr: List[int]) -> None:
        self.arr = arr
        # dict for O(1) lookups by value
        self.indexof = {v: i for i, v in enumerate(arr)}

    def swap(self, e1: int, e2: int) -> None:
        i1 = self.indexof[e1]
        i2 = self.indexof[e2]
        # set element where 0 is to final element
        self.arr[i1] = e2
        # update dict
        self.indexof[e2] = i1
        # set 0 where the previous number was
        self.arr[i2] = e1
        # update dict
        self.indexof[e1] = i2
        self.moves += 1

    def calc_moves(self, end: List[int]) -> int:
        self.moves = 0
        while self.arr != end:
            i0 = self.indexof[0]
            if end[i0] != 0:  # if element can be moved to its final position
                self.swap(0, end[i0])
                print(self.arr)
                continue
            for ind, el in enumerate(self.arr):  # else swap unpositioned element to placeholder
                if el != end[ind]:
                    self.swap(0, el)
                    print(self.arr)
                    break
        return self.moves


def garage(beg: List[int], end: List[int]):
    fl = FastList(beg)
    return fl.calc_moves(end)


if __name__ == '__main__':
    initial = [1, 2, 3, 0, 4]
    final = [0, 3, 2, 1, 4]
    print("initial:", initial)
    print(garage(initial, final))
    print("final should be:", final)

# def garage(beg, end):
#     i = 0
#     moves = 0
#     while beg != end:
#         if beg[i] != 0 and beg[i] != end[i]:
#             car = beg[i]
#             empty = beg.index(0)
#             final_pos = end.index(beg[i])
#             if empty != final_pos:
#                 beg[final_pos], beg[empty] = beg[empty], beg[final_pos]
#                 # print(beg)
#                 empty = beg.index(0)
#                 beg[beg.index(
#                     car)], beg[empty] = beg[empty], beg[beg.index(car)]
#                 # print(beg)
#                 moves += 2
#             else:
#                 beg[beg.index(
#                     car)], beg[empty] = beg[empty], beg[beg.index(car)]
#                 # print(beg)
#                 moves += 1
#         i += 1
#         if i == len(beg):
#             i = 0
#     return moves


# if __name__ == "__main__":
#     initial = [1, 2, 3, 0, 4]
#     final = [0, 3, 2, 1, 4]
#     print("initial:", initial)
#     print("final:", final)
#     for _ in range(10000000):
#         garage(initial, final)
