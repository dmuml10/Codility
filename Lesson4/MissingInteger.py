#Counting elements

def solution(A):
    array = [None] * (len(A) + 1)
    for i in range(len(A)):
        if A[i] > 0 and A[i] <= len(A):
            array[A[i]] = 1

    for i in range (1, len(array)):
        if (array[i] == None):
            return i

    return len(A) + 1