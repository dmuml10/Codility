#Stacks and Queues


def solution(S):
    stack = []
    for i in range(len(S)):
        if S[i] == '(':
            stack.append(S[i])
        elif len(stack) == 0 or '(' != stack.pop():
            return 0
    if len(stack) != 0:
        return 0
    else:
        return 1
