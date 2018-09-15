#Time complexity
import math

def solution(A):
    sum = 0
    for i in A:
        sum += i
    min = math.fabs(sum)
    tempSum = 0
    for i in range(len(A)-1):
        sum -= A[i]
        tempSum += A[i];
        diff = math.fabs(sum - tempSum)
        if diff < min:
            min = diff
    return int(min)