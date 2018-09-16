#Counting Elements

def solution(A):
    sum = 0;
    actualSum = 0;
    map = {}
    for i in range(len(A)):
        if map.get(str(A[i])) == 1:
            return 0
        sum += i+1
        actualSum += A[i]
        map[str(A[i])] = 1
    if sum == actualSum:
        return 1
    else:
        return 0