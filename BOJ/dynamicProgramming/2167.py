'''
2차원 배열의 합
'''
'''
첫번째풀이
'''
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    preFix = [[0 for _ in range(M+1)]]

    for _ in range(N):
        data = [0] + list(map(int, input().split()))
        preFix.append(data)

    # 행끼리 먼저 더함
    for i in range(1, N+1):
        for j in range(1,M):
            preFix[i][j+1] += preFix[i][j]

    # 열끼리 그다음 더함
    for j in range(1, M+1):
        for i in range(1, N):
            preFix[i+1][j] += preFix[i][j]
    print(preFix)
    for _ in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        print(preFix[x2][y2] - preFix[x1-1][y2] - preFix[x2][y1-1] + preFix[x1-1][y1-1])
solution()