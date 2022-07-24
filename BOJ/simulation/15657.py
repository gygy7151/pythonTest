'''
N과ㅡ (8)
'''
'''
첫번째풀이/두번째풀이 - 중복순열인줄 알았는데 출력예제를 보니 중복조합이었음
'''
import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement
def solution():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    R = list(combinations_with_replacement(A, M))
    for r in R:
        print(*r)
solution()