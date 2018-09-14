'''
Lesson1
Iterations
BinaryGap
'''

def solution(N):
    result = 0
    temp = 0
    isOdd = (N % 2 == 1)
    flip = False
    while N >= 1:
        mod = N % 2
        if mod == 0:
            if flip:
                temp += 1
        else:
            flip = True
            if temp > result:
                result = temp
            temp = 0
        N = int(N/2)

    if isOdd and temp > result:
        result = temp
    return result
