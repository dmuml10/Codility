#Maximum slice problem

def solution(A):
    result = maxElement = -1000000
    temp = 0
    for i in A:
        temp = max(0, temp + i)
        result = max(result, temp)
        maxElement = max(maxElement, i)
    if result != 0:
        result = max(result, maxElement)
    else:
        result = maxElement
    return result
