#Prime and composite numbers

def solution(A):
    dividers = []
    for i in range(3, len(A)):
        if len(A) % i == 0:
            dividers.append(i)
    for
