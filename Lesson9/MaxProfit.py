#Maximum slice problem
import sys

def solution(A):
    max_array = [0] * len(A)
    min = sys.maxsize
    for i in range(len(A)):
        if min > A[i]:
            min = A[i]
        max_array[i] = min

    max = 0
    for i in range(len(A)):
        if A[i] - max_array[i] > max:
            max = A[i] - max_array[i]

    return max
