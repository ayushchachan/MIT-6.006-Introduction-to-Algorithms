def search_sorted_2D_array(A, v):
    """
    Return tuple (x, y) such that A[y][x] == v, or None.
    Input:  A | Array of equal length arrays of integers
              |     representing the rows of a 2D array
              |     where A[y][x] >= A[y - 1][x] and
              |           A[y][x] >= A[y][x - 1]
              |     for all (x, y) in range.
            v | An integer to search for in A.
    """
    M = len(A)
    N = len(A[0])

    i = M - 1
    j = 0

    while i >= 0 and j < N:
        if A[i][j] == v:
            return (j, i)
        elif A[i][j] < v:
            j = j + 1
        else:
            i = i - 1
    return None
