#Prime and composite numbers
import math

def solution(N):
    sqrt = math.sqrt(N)
    if sqrt.is_integer():
        return int((sqrt + sqrt) * 2)
    else:
        sqrt = int(sqrt)
        while True:
            if N % sqrt == 0:
                rem = N / sqrt
                return int((rem + sqrt) * 2)
            sqrt -= 1
