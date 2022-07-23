'''
N과M (2)
'''
'''
첫번째풀이
'''
from itertools import combinations
def solution():
    N, M = map(int, input().split())
    A = [x for x in range(1,N+1)]
    if M == 1:
        print(*A, sep="\n")
    else:
        R = list(combinations(A, M))
        for i in range(len(R)):
            print(*R[i], sep=" ")
            
solution()