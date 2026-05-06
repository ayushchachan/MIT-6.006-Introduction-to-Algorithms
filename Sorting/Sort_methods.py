#  implementation of various sorting algorithms

def exch(A, i, j):
    '''
    swaps the elements stored at index i and index j of array A
    '''
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def is_sorted(A):
    '''
    return True if the entries in array A are sorted, otherwise return False.
    '''
    for i in range(1, len(A)):
        if A[i] < A[i - 1]:
            return False
    return True

class Selection:
    @staticmethod
    def sort(A):
        '''
        sort the array A in-place into ascending order 
        '''
        N = len(A)

        for i in range(N):
            min = i                         ## index of minimal entry
            for j in range(i + 1, N):
                if A[j] < A[min]:
                    min = j
            exch(A, i, min)

class Insertion:
    @staticmethod
    def sort(A):
        N = len(A)
        for i in range(1, N):
            for j in range(i - 1, -1, -1):
                if A[j] > A[j + 1]:
                    exch(A, j, j + 1)
                else:
                    break
        

def merge_sort(A, p=0, r=None):
    if r is None:
        r = len(A)

    if (r - p > 1):

        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q, r)

        # Now merging two sorted lists
        i, j, L, R = 0, 0, A[p: q], A[q: r]



        while (p < r):
            if (j == len(R)) or (i < len(L) and L[i] <= R[j]):
                A[p] = L[i]
                i = i + 1
            else:
                A[p] = R[j]
                j = j + 1
            p = p + 1

import random
l = [random.randint(1, 30) for i in range(30)]
print("l =", l)

Insertion.sort(l)
print("after sorting")
print(l)
