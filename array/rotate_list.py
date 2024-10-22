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

    # Additional examples
    test_list2 = ['a', 'b', 'c', 'd', 'e', 'f']
    print(f'\nOriginal list: {test_list2}')
    print(f'Rotated list (k=1): {rotate_list(test_list2, 1)}')
    print(f'Rotated list (k=4): {rotate_list(test_list2, 4)}')

    test_list3 = [10, 20, 30, 40, 50, 60, 70]
    print(f'\nOriginal list: {test_list3}')
    print(f'Rotated list (k=0): {rotate_list(test_list3, 0)}')
    print(f'Rotated list (k=7): {rotate_list(test_list3, 7)}')
    print(f'Rotated list (k=10): {rotate_list(test_list3, 10)}')
