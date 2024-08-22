"""
Find the maximum subarray sum

Given an integer array, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.
"""
from typing import List


def max_subarray_sum(nums: List[int]) -> int:
    if not nums:
        return 0

    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def test_max_subarray_sum():
    # Test case 1: Example from the problem description
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    # Test case 2: All positive numbers
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

    # Test case 3: All negative numbers
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

    # Test case 4: Mixed positive and negative numbers
    assert max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7

    # Test case 5: Empty array
    assert max_subarray_sum([]) == 0

    # Test case 6: Single element array
    assert max_subarray_sum([42]) == 42

    print("All test cases passed!")


if __name__ == "__main__":
    test_max_subarray_sum()

    # Original example
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray_sum(arr)
    print(f"Maximum subarray sum: {result}")  # Expected output: 6
