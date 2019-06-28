#
# Binary search works for a sorted array.
# Note: The code logic is written for an array sorted in
#       increasing order.
# T(n): O(log n)
#

# A binary_search function. It returns 
# location of query in given array array[l..r] is present, 
# otherwise -1 

# Python program to implement Binary Search 
def binary_search(array, query):
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        val = array[mid]
        
        # If the element is present at the middle itself 
        
        if val == query:
            return mid
        
        # If element is smaller than mid, then 
        # it can only be present in right subarray 
        
        elif val < query:
            lo = mid + 1
            
        # Else the element can only be present 
        # in left subarray     
            
        else:
            hi = mid - 1
            
    # We reach here when element is not 
    # present in array 
    
    return None


def main():
    array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
    print(array)
    print("-----SEARCH-----")
    print("found: ", 5, " in index:", binary_search(array, 5))
    print("-----SEARCH-----")
    print("found: ", 6, " in index:", binary_search(array, 6))
    print("-----SEARCH-----")
    print("found: ", 7, " in index:", binary_search(array, 7))
    print("-----SEARCH-----")
    print("found: ", -1, " in index:", binary_search(array, -1))
    print("-----SEARCH-----")


if __name__ == "__main__":
    main()
