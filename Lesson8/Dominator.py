#Leader

def solution(A):
    dic = {}
    for i in range(len(A)):
        v = str(A[i])
        if dic.get(v) == None:
            dic[v] = 1
        else:
            dic[v] += 1
        if dic.get(v) != None and dic.get(v) > len(A)//2:
            return i
    return -1