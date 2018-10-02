#Leader

def solution(A):
    sorted = A.copy()
    sorted.sort()
    a = sorted[len(A)//2]

    count = 0
    for i in range(len(sorted)):
        if (a == sorted[i]):
            count += 1

    result = 0
    if count > len(A)//2:
        left = 0
        right = count
        for i in range(len(A)):
            if A[i] == a:
                left += 1
                right -= 1
            if left > (i + 1)//2 and right > (len(A) - (i + 1))//2:
                result += 1
    return result