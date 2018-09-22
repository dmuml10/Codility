#Sorting

def solution(A):
    A.sort()
    result1 = 1
    for i in range(len(A)-1, len(A) - 4, -1):
        result1 *= A[i]
    result2 = A[len(A) -1]
    for i in range(2):
        result2 *= A[i]
    return max(result1, result2)