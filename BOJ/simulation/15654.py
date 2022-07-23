'''
N과ㅡ (5)
'''
'''
첫번째풀이
'''
import sys
from itertools import permutations
def solution():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    R = list(permutations(sorted(A), M))
    for r in R:
        print(*r)
solution()