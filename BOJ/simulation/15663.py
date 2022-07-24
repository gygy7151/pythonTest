'''
N과ㅡ (9)
'''
'''
첫번째풀이
'''
import sys
input = sys.stdin.readline
from itertools import permutations
def solution():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    R = list(permutations(A, M))
    for r in sorted(R):
        print(*r)
solution()