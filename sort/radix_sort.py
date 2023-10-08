'''
Radix Sort

    d - size of number places
    b - number system base
    
    example: 
            104
           /   \
        d = 3  b = 10
    
    Time Complexity
        O(d * (n+b))
    Space Complexity
        O(2^d + n)
'''

# Define the counting_sort function to perform counting sort
def counting_sort(array, exp):
    length = len(array)
    output = [0] * length
    count = [0] * 10

    # Count the occurrences of each digit at the current position
    for i in range(length):
        index = int(array[i] / exp)
        count[index % 10] += 1

    # Calculate cumulative counts to determine the correct positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the sorted output array based on the counts
    for i in range(length - 1, -1, -1):
        index = int(array[i] / exp)
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1

    # Copy the sorted values back to the original array
    for i in range(length):
        array[i] = output[i]

    return array

# Define the radix_sort function to perform radix sort
def radix_sort(array):
    max_value = max(array)
    min_value = min(array)
    exp = 1

    # If there are negative numbers, make all numbers positive for sorting
    if min_value < 0:
        array = [x - min_value for x in array]
        max_value -= min_value

    # Perform radix sort by iterating through each digit position
    while max_value // exp > 0:
        counting_sort(array, exp)
        exp *= 10

    # If there were negative numbers, convert the sorted values back
    if min_value < 0:
        array = [x + min_value for x in array]

    return array


array = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100, 4, 423, 2, 564, 9, 0, 10, 43, 64]
print(radix_sort(array))
