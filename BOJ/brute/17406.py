'''
배열돌리기4
'''
'''
두번째풀이
'''
from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
rcs = [list(map(int, input().split())) for _ in range(K)]

ans = int(1)

# 1. 회전 순서 정하기 (최대 6!=720)
for p in permutations(rcs, K):
    # 2. 회전
    copy_a = deepcopy(a)  # 원본리스트 카피
    for r, c, s in p:
        r -= 1
        c -= 1
        for n in range(s, 0, -1):
            tmp = copy_a[r-n][c+n]
            copy_a[r-n][c-n+1:c+n+1] = copy_a[r-n][c-n:c+n]  # ->
            for row in range(r-n, r+n):  # ↑
                copy_a[row][c-n] = copy_a[row+1][c-n]
            copy_a[r+n][c-n:c+n] = copy_a[r+n][c-n+1:c+n+1]  # <-
            for row in range(r+n, r-n, -1):  # ↓
                copy_a[row][c+n] = copy_a[row-1][c+n]
            copy_a[r-n+1][c+n] = tmp

    # 3. 각 행의 최소값 찾기
    for row in copy_a:
        ans = min(ans, sum(row))

print(ans)
'''
첫번째 풀이
'''
# import itertools
# def count(a):
#     min_val = int(1e9)
#     for i in range(N):
#         min_val = min(sum(a[i]), min_val)
#     return min_val

# def rotate(x1,x2,y1,y2):
#     global a
#     if y1 == y2:
#         return 
#     #우선 오른쪽
#     temp1 = a[x1][y2]
#     for y in range(y1, y2):
#         a[x1][y+1] = a[x1][y]
    
#     #그다음 아래
#     temp2 = a[x2][y2]
#     for x in range(x1+1, x2):
#         a[x+1][y2] = a[x][y2]
#     a[x1+1][y2] = temp1
#     #그다음 왼쪽
#     temp3 = a[x2][y1]
#     for y in range(y2,y1,-1):
#         a[x2][y-1] = a[x2][y]
#     a[x2][y2-1] = temp2
#     #그다음 위쪽
#     for x in range(x2,x1,-1):
#         a[x-1][y1] = a[x][y1]
#     a[x2-1][y1]= temp3
#     rotate(x1+1,x2-1,y1+1,y2-1)
#     return

# N, M, K = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(N)]
# cal = []
# min_val = int(1e9)
# for i in range(K):
#     data = list(map(int, input().split()))
#     cal.append((data[0], data[1], data[2]))
# cases = list(itertools.permutations(cal))
# for case in cases:
#     for order in case:
#         r,c,s = order
#         x1, x2, y1, y2 = (r-s-1), (r+s-1), (c-s-1), (c+s-1)
#         #인덱스맞추기 위해 1씩빼준다
#         rotate(x1,x2,y1,y2)
#     # 배엶A값 구해주고, 기존 min_val과 비교해서 연산
#     min_val = min(min_val, count(a))
# print(min_val)