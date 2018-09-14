#Arrays

def solution(A, K):
    arrayLength = len(A);
    result = [0] * arrayLength
    for i in range(arrayLength):
        result[(i+K) % arrayLength] = A[i];
    return result
