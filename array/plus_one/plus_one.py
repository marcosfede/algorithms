from typing import List


def plus_one(digits: List[int]):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    new_num = [0] * (n + 1)
    new_num[0] = 1
    return new_num


a = [8, 8, 9]
print('input', a)
print('output', plus_one(a))

b = [9, 9, 9, 9]
print('input', b)
print('output', plus_one(b))
