#Time complexity

def solution(A):
    actualSum = 0;
    correctSum = 0;
    for i in A:
        actualSum += i
    for i in range(len(A) + 2):
        correctSum += i;
    return correctSum - actualSum