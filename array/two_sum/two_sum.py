from typing import List


def two_sum(nums: List[int], target: int)->List[int]:
    dic = {}
    for i, num in enumerate(nums):
        if num in dic:
            return [dic[num], i]
        else:
            dic[target - num] = i


if __name__ == "__main__":
    arr = [3, 2, 4]
    target = 6
    res = two_sum(arr, target)
    print(res)
