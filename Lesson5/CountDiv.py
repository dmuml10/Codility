#Prefix sums

def solution(A, B, K):
    if A % K != 0:
        A = A + (K - (A % K))
    if B % K != 0:
        B = B - (B % K)
    counter = int((B - A)/K + 1)
    return counter