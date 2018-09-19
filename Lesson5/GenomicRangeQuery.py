#Prefix sums

def solution(S, P, Q):
    dic = {'A':1, 'C':2, 'G':3, 'T':4}
    array = [[0 for x in range(4)] for y in range(len(S))]

    array[0][dic.get(S[0])-1] = dic.get(S[0])
    for i in range(1, len(S)):
        for j in range(4):
            array[i][j] = array[i-1][j]
        array[i][dic.get(S[i])-1] = array[i-1][dic.get(S[i])-1] + dic.get(S[i])

    result = [0] * len(P)
    for i in range(len(P)):
        if Q[i] == P[i] or array[Q[i]][0] == array[P[i]][0]:
            result[i] = dic.get(S[P[i]])
        elif array[Q[i]][0] - array[P[i]][0] > 0:
            result[i] = 1
        elif array[Q[i]][1] - array[P[i]][1] > 0:
            result[i] = 2
        elif array[Q[i]][2] - array[P[i]][2] > 0:
            result[i] = 3
        elif array[Q[i]][3] - array[P[i]][3] > 0:
            result[i] = 4
    return result

#print(solution('CAGCCTA', [2,5,0], [4,5,6]))
# print(solution('CCCCCCC', [2,5,0], [4,5,6]))
# print(solution('AA', [0,1], [0,1]))
# print(solution('AT', [0], [1]))
# print(solution('GC', [0,1], [0,1]))
# print(solution('AC', [0], [1]))
# print(solution('TA', [0], [1]))
# print(solution('AACC', [0,2], [2,3]))
# print(solution('AACCCGG', [0,2,3], [2,3,4]))

