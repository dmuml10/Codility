#Sorting

def intersect(a_radius,a_index, b_radius, b_index):
    a1 = a_index - a_radius
    a2 = a_index + a_radius
    b1 = b_index - b_radius
    b2 = b_index + b_radius
    if a2 < b1 or b2 < a1:
        return False
    else:
        return True


def solution(A):
    count = 0
    array1 = [0] * len(A)
    array2 = [0] * len(A)

    for i in range(len(A)):
        array1[i] = i - A[i]
        array2[i] = i + A[i]
    array1.sort()
    array2.sort()

    i = 0
    j = 0
    while i < len(A) and j < len(A) :
        if array2[i] < array1[j]:
            i +=1
        else:
            j+=1
            count +=1

    count = int(count/2)
    if count == 10000:
        return -1
    return count


print(solution([1, 5, 2, 1, 4, 0]))

