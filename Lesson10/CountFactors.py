#Prime and composite numbers

import math

def solution(N):
    result = 0
    sqrt = int(math.sqrt(N))
    for i in range(1, sqrt + 1):
        if N % i == 0:
            result += 1
    result *= 2
    if sqrt * sqrt == N:
        result -= 1
    return result