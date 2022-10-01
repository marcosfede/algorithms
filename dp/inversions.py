Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

def count_inversions_bf(arr):
    """
    Counts the number of inversions using a naive brute-force algorithm
    Parameters
    ----------
    arr: arr: array-like, the list containing the items for which the number
    of inversions is desired. The elements of `arr` must be comparable.
    Returns
    -------
    num_inversions: The total number of inversions in `arr`
    Examples
    ---------
     >>> count_inversions_bf([1, 4, 2, 4, 1])
     4
     >>> count_inversions_bf([1, 1, 2, 4, 4])
     0
     >>> count_inversions_bf([])
     0
    """

    num_inversions = 0
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                num_inversions += 1

    return num_inversions


def count_inversions_recursive(arr):
    """
    Counts the number of inversions using a divide-and-conquer algorithm
    Parameters
    -----------
    arr: array-like, the list containing the items for which the number
    of inversions is desired. The elements of `arr` must be comparable.
    Returns
    -------
    C: a sorted copy of `arr`.
    num_inversions: int, the total number of inversions in 'arr'
    Examples
    --------
    >>> count_inversions_recursive([1, 4, 2, 4, 1])
    ([1, 1, 2, 4, 4], 4)
    >>> count_inversions_recursive([1, 1, 2, 4, 4])
    ([1, 1, 2, 4, 4], 0)
    >>> count_inversions_recursive([])
    ([], 0)
    """
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    P = arr[0:mid]
    Q = arr[mid:]

    A, inversion_p = count_inversions_recursive(P)
    B, inversions_q = count_inversions_recursive(Q)
    C, cross_inversions = _count_cross_inversions(A, B)

    num_inversions = inversion_p + inversions_q + cross_inversions
    return C, num_inversions


def _count_cross_inversions(P, Q):
    """
    Counts the inversions across two sorted arrays.
    And combine the two arrays into one sorted array
    For all 1<= i<=len(P) and for all 1 <= j <= len(Q),
    if P[i] > Q[j], then (i, j) is a cross inversion
    Parameters
    ----------
    P: array-like, sorted in non-decreasing order
    Q: array-like, sorted in non-decreasing order
    Returns
    ------
    R: array-like, a sorted array of the elements of `P` and `Q`
    num_inversion: int, the number of inversions across `P` and `Q`
    Examples
    --------
    >>> _count_cross_inversions([1, 2, 3], [0, 2, 5])
    ([0, 1, 2, 2, 3, 5], 4)
    >>> _count_cross_inversions([1, 2, 3], [3, 4, 5])
    ([1, 2, 3, 3, 4, 5], 0)
    """

    R = []
    i = j = num_inversion = 0
    while i < len(P) and j < len(Q):
        if P[i] > Q[j]:
            # if P[1] > Q[j], then P[k] > Q[k] for all  i < k <= len(P)
            # These are all inversions. The claim emerges from the
            # property that P is sorted.
            num_inversion += len(P) - i
            R.append(Q[j])
            j += 1
        else:
            R.append(P[i])
            i += 1

    if i < len(P):
        R.extend(P[i:])
    else:
        R.extend(Q[j:])

    return R, num_inversion


def main():
    arr_1 = [10, 2, 1, 5, 5, 2, 11]

    # this arr has 8 inversions:
    # (10, 2), (10, 1), (10, 5), (10, 5), (10, 2), (2, 1), (5, 2), (5, 2)

    num_inversions_bf = count_inversions_bf(arr_1)
    _, num_inversions_recursive = count_inversions_recursive(arr_1)

    assert num_inversions_bf == num_inversions_recursive == 8

    print("number of inversions = ", num_inversions_bf)

    # testing an array with zero inversion (a sorted arr_1)

    arr_1.sort()
    num_inversions_bf = count_inversions_bf(arr_1)
    _, num_inversions_recursive = count_inversions_recursive(arr_1)

    assert num_inversions_bf == num_inversions_recursive == 0
    print("number of inversions = ", num_inversions_bf)

    # an empty list should also have zero inversions
    arr_1 = []
    num_inversions_bf = count_inversions_bf(arr_1)
    _, num_inversions_recursive = count_inversions_recursive(arr_1)

    assert num_inversions_bf == num_inversions_recursive == 0
    print("number of inversions = ", num_inversions_bf)


if __name__ == "__main__":
    main()