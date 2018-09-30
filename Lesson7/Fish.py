#Stacks and Queues

def solution(A, B):
    fishStack = []
    count = len(A)
    for i in range(len(A)):
        if B[i] == 1:
            fishStack.append(A[i])
        else:
            if len(fishStack) > 0:
                peek = fishStack.pop()
                while A[i] > peek:
                    count -= 1
                    if len(fishStack) == 0:
                        break
                    peek = fishStack.pop()
                if (A[i] < peek):
                    fishStack.append(peek)
                    count -= 1

    return count