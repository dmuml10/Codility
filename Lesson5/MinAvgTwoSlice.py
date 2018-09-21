#Prefix Sums

def solution(A):

    min = 10000
    index = 0
    for i in range(len(A)):
        if i < len(A) - 1:
            twoElem = (A[i] + A[i+1])/2
            if twoElem < min:
                min = twoElem
                index = i
        if i < len(A) - 2:
            threeElem = (A[i] + A[i+1] + A[i + 2])/3
            if threeElem < min:
                min = threeElem
                index = i
    return index
