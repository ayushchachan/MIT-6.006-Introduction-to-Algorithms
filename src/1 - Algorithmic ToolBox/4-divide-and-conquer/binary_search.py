def search(A, x):
    """
    given a sorted array A, returns i if A[i] == x, else
    returns -1
    """
    i = 0
    j = len(A)

    while i < j:
        mid = (i + j) // 2
        if x == A[mid]:
            return mid
        elif x < A[mid]:
            j = mid
        else:
            i = mid + 1
    return -1
