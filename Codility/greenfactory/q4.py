def solution(A):
    n = len(A)
    i = n -1
    result = -1
    max = 0
    k = 0
    while (i > 0):
        if A[i] == 1:
            k = k+1