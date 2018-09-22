#Sorting

#O(N*log(N))
def solution(A):
    A.sort();
    count = 1
    if len(A) == 0:
        count = 0
    for i in range(len(A) - 1):
        if A[i] != A[i+1]:
            count +=1
    return count

#O(N) time
def solution2(A):
    dic = {}
    for i in range(len(A)):
        dic[A[i]] = 0
    return len(dic)