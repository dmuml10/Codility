#Counting elements

def solution(X, A):
    map = {}
    sum = 0;
    actualSum = 0;
    for i in range(X + 1):
        sum += i

    for i in range(len(A)):
        if map.get(A[i]) == None:
            map[A[i]] = 1
            actualSum += A[i]
        if actualSum == sum:
            return i
    return -1