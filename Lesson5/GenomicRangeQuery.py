#Prefix sums


def solution(S, P, Q):
    dic = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    array = [[0 for x in range(4)] for y in range(len(S) + 1)]

    for i in range(1, len(S)+1):
        for j in range(4):
            array[i][j] = array[i-1][j]
        array[i][dic.get(S[i-1])-1] = array[i-1][dic.get(S[i-1])-1] + dic.get(S[i-1])

    result = [0] * len(P)
    for i in range(len(P)):
        if Q[i] == P[i]:
            result[i] = dic.get(S[P[i]])
        elif array[Q[i]+1][0] - array[P[i]][0] > 0:
            result[i] = 1
        elif array[Q[i]+1][1] - array[P[i]][1] > 0:
            result[i] = 2
        elif array[Q[i] +1][2] - array[P[i]][2] > 0:
            result[i] = 3
        elif array[Q[i]+1][3] - array[P[i]][3] > 0:
            result[i] = 4
    return result
