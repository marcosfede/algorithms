def rotate_list(lst, k):
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

# Test the function
if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5]
    print(f'Original list: {test_list}')
    print(f'Rotated list (k=2): {rotate_list(test_list, 2)}')
    print(f'Rotated list (k=3): {rotate_list(test_list, 3)}')
