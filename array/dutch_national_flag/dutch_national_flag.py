from typing import List


def dutch_national_flag(arr: List[int]) -> None:
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1


if __name__ == "__main__":
    arr = [2, 0, 1, 2, 1, 0]
    dutch_national_flag(arr)
    print(arr)  # Should print: [0, 0, 1, 1, 2, 2]
