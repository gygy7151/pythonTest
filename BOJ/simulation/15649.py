'''
N과M(1)
'''
from itertools import permutations
def solution():
    N, M = map(int, input().split())
    A = [ x for x in range(1,N+1)]
    for data in list(permutations(A, M)):
     print(*data)
    
solution()



