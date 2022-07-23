'''
N과M (4)
'''
'''
첫번째풀이
'''
from itertools import combinations_with_replacement
def solution():
    N, M = map(int, input().split())
    A = [ x for x in range(1,N+1)]
    if M == 1:
        print(*A, sep="\n")
    else:
        A = list(combinations_with_replacement(A, r=M))
        for a in A:
            print(*a)
    
solution()