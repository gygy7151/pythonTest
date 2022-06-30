'''
좌표정렬하기
'''
import sys
input = sys.stdin.readline

def solution():
    A = []
    
    for _ in range(int(input().rstrip())):
        X, Y = map(int, input().rstrip().split())
        A.append((X,Y))
    
    A = sorted(A, key = lambda x : ( x[0], x[1]))
    return A
res = solution()
for x, y in res:
    print(x, y)