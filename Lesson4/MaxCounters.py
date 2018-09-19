#Counting elements

def solution(N, A):
    counters = [0] * N

    max_result = max_counter = 0
    for ind in range(len(A)):
        if A[ind] == N + 1:
            max_result = max(max_result, max_counter)
        else:
            if counters[A[ind] - 1] < max_result:
                counters[A[ind] - 1] = max_result

            counters[A[ind] - 1] += 1
            max_counter = max(max_counter, counters[A[ind] - 1])

    for ind in range(N):
        counters[ind] = max(max_result, counters[ind])

    return counters