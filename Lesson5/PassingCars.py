#Prefix Sums

def solution(A):
    one = 0
    for i in range(len(A)):
        if A[i] == 1:
            one += 1
    sum = 0
    for i in range(len(A)):
        if A[i] == 0:
            sum += one
        else:
            one -= 1
    if sum > 1000000000:
        return -1
    return sum
