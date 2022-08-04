'''
N과ㅡ (3)
'''
'''
첫번째풀이
'''
import sys
from itertools import product
def solution():
    N, M = map(int, input().split())
    A = [ x for x in range(1, N+1)]

    R = list(product(A, repeat=M))
    for r in R:
        print(*r)
solution()