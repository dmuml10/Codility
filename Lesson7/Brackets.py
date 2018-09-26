#Stacks and Queues


def solution(S):
    stack = []
    dic = {'}': '{', ']': '[', ')': '('}
    for i in range(len(S)):
        if S[i] == '{' or S[i] == '[' or S[i] == '(':
            stack.append(S[i])
        elif len(stack) == 0 or dic[S[i]] != stack.pop():
            return 0
    if len(stack) != 0:
        return 0
    else:
        return 1
