#Stacks and Queues

def solution(H):
    stack = []
    count = 0

    for i in range(len(H)):
        while len(stack) != 0 and stack[-1] > H[i]:
            stack.pop()
        if len(stack) != 0 and stack[-1] == H[i]:
            pass
        else:
            count += 1
            stack.append(H[i])

    return count
