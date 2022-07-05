'''
좌표정렬하기
'''
'''
첫번째풀이
'''
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    A = []
    for _ in range(N):
        X, Y = map(int, input().split())
        A.append((X,Y))
    A.sort(key = lambda x: (x[1],x[0]))
    A = ['{0} {1}'.format(a,b) for a, b in A]
    return A
res = (solution())
print(*res, sep='\n')