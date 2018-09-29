#Stacks and Queues

def solution(A, B):
    fishStack = []
    count = len(A)
    for i in range(len(A) - 1):
        if A[i] == 1 and A[i + 1] == 0:
            if A[i] > A[i + 1]:
                fishStack.append(A[i])
                count -= 1
            