#Maximum slice problem
import sys

def solution(A):
    result = maxElement = -1000000
    temp = 0

    for i in A:
        temp =  max(0, temp + i)
        result = max(result , temp)
        maxElement = max(maxElement, i)
    result = max(result, maxElement)
    return result

print(solution([3,2,-6,4,0]))
print(solution([-10]))
print(solution([-2, 1]))