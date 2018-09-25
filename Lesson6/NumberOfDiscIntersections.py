#Sorting

def solution(A):
    array1 = [0] * len(A)
    array2 = [0] * len(A)
    for i in range(len(A)):
        array1[i] = i - A[i]
        array2[i] = i + A[i]
    array1.sort()
    array2.sort()
    j = 0
    count = 0
    for i in range(len(A)):
        while (j < len(A) and array2[i] >= array1[j]):
            count += j
            count -= i
            j += 1
    if count > 10000000:
        return -1
    return count