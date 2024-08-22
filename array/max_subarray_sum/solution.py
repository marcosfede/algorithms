def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test the function
if __name__ == "__main__":
    test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray_sum(test_array)
    print(f"Maximum subarray sum: {result}")
    assert result == 6, f"Expected 6, but got {result}"
    print("Test passed successfully!")
