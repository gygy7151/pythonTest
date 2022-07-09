'''
듣보잡
'''

'''
첫번째풀이 - 통과 but 처음엔 사전식 출력 및 문자열이 0일때 빈문자열 출력하는걸 제외 시켰더니 틀렷음
'''
import sys
input = sys.stdin.readline
from collections import Counter

def solution():
    NOT_HEAR = {}
    NOT_HEAR_SEE = []

    N,M = map(int, input().split())

    for i in range(N):
        NOT_HEAR[input().rstrip()] = 1
    print(NOT_HEAR)
    
    for i in range(M):
        NAME = input().rstrip()
        
        try:

            if NOT_HEAR[NAME]:
                NOT_HEAR_SEE.append(NAME)
        
        except:
            pass
    
    print(NOT_HEAR_SEE)
    NOT_HEAR_SEE.sort()
    return NOT_HEAR_SEE
res = solution()
print(len(res))
print(*res, sep="\n")