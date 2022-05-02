'''
파이프옮기기 - dfs
'''
'''
세번째 풀이 - 0:가로, 1:아래, 2:대각선
'''
# def dfs(x,y, shape):
#     global ans
#     if x == N-1 and y == N-1:
#         ans += 1
#         return
#     if shape == 0 or shape == 2:
#         if y + 1 < N:
#             if house[x][y+1] == 0:
#                 dfs(x,y+1,0)
#     if shape == 1 or shape == 2:
#         if x + 1 < N:
#             if house[x+1][y] == 0:
#                 dfs(x+1,y,1)
#     if shape == 0 or shape == 1 or shape == 2:
#         if x + 1 < N and y + 1 < N:
#             if house[x+1][y] == 0 and house[x][y+1] == 0 and house[x+1][y+1] == 0:
#                 dfs(x+1, y+1, 2)


# N = int(input())
# house = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# dfs(0,1,0)
# print(ans)

'''
두번째풀이 - 방향을 역으로 조정
'''
#타코드랑 다르게 0:가로, 1:대각선, 2:아래로 설정했다.
#사실 0:가로, 1:아래, 2:대각선 하는게 편하긴해 그럼 세번째풀이를 참조해랑
def dfs(x,y, shape):
    global ans
    if x == N-1 and y == N-1:
        ans += 1
        return
    if shape == 0 or shape == 1:
        if y + 1 < N:
            if house[x][y+1] == 0:
                dfs(x,y+1,0)
    if shape == 1 or shape == 2:
        if x + 1 < N:
            if house[x+1][y] == 0:
                dfs(x+1,y,2)
    if shape == 0 or shape == 1 or shape == 2:
        if x + 1 < N and y + 1 < N:
            if house[x+1][y] == 0 and house[x][y+1] == 0 and house[x+1][y+1] == 0:
                dfs(x+1, y+1, 1)


N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0,1,0)
print(ans)
'''
첫번째 풀이 - 방향틀림
'''
# #인덱스 0:가로, 1:대각선, 2:아래
# #가로이동
# hdx1 = [0,0,0]
# hdy1 = [1,1,0]
# hdx2 = [0,1,0]
# hdy2 = [1,1,0]
# #세로이동
# vdx1 = [0,1,1]
# vdy1 = [0,0,0]
# vdx2 = [0,1,1]
# vdy2 = [0,1,0]
# #대각선이동
# cdx1 = [1,1,1]
# cdy1 = [1,1,1]
# cdx2 = [0,1,1]
# cdy2 = [1,1,0]

# def dfs(a, b, d):
#     global ans
#     x1, y1 = a[0], a[1]
#     x2, y2 = b[0], b[1]
#     if x2 == N-1 and y2 == N-1:
#         ans += 1
#         return
#     #가로
#     if d == 0:
#         for i in [0,1]:
#             nx1, ny1 = x1 + hdx1[i], y1 + hdy1[i]
#             nx2, ny2 = x2 + hdx2[i], y2 + hdy2[i]
#             if 0 <= nx1 and 0 <= nx2 and 0<= ny1 and 0 <= ny2:
#                 if N > nx1 and N > nx2 and N > ny1 and N > ny2:
#                     if i == 0:
#                         if house[nx1][ny1] != 1 and house[nx2][ny2] != 1:
#                             dfs((nx1, ny1), (nx2, ny2), i)
#                     else:
#                         if house[nx1][ny1] != 1 and house[nx2][ny2] != 1:
#                             if house[nx2-1][ny2] != 1 and house[nx2][ny2-1] != 1:
#                                 dfs((nx1, ny1), (nx2, ny2), i)
#     #대각선 
#     elif d == 1:
#         for i in [0,1,2]:
#             nx1, ny1 = x1 + cdx1[i], y1 + cdy1[i]
#             nx2, ny2 = x2 + cdx2[i], y2 + cdy2[i]
#             if 0 <= nx1 and 0 <= nx2 and 0<= ny1 and 0 <= ny2:
#                 if N > nx1 and N > nx2 and N > ny1 and N > ny2:
#                     if i == 0 or i == 2:
#                         if house[nx1][ny1] != 1 and house[nx2][ny2] != 1:
#                             dfs((nx1, ny1), (nx2, ny2), i)
#                     elif i == 1:
#                         if house[nx1][ny1] != 1 and house[nx2][ny2] != 1:
#                             if house[nx2-1][ny2] != 1 and house[nx2][ny2-1] != 1:
#                                 dfs((nx1, ny1), (nx2, ny2), i)

#     #아래
#     elif d == 2:
#         for i in [1,2]:
#             nx1, ny1 = x1 + vdx1[i], y1 + vdy1[i]
#             nx2, ny2 = x2 + vdx2[i], y2 + vdy2[i]
#             if 0 <= nx1 and 0 <= nx2 and 0<= ny1 and 0 <= ny2:
#                 if N > nx1 and N > nx2 and N > ny1 and N > ny2:
#                     if i == 1:
#                         if house[nx1][ny1] != 1 and house[nx2][ny2] != 1:
#                             dfs((nx1, ny1), (nx2, ny2), i)
#                     else:
#                         if house[nx1][ny1] != 1 and house[nx2][ny2] != 1:
#                             if house[nx2-1][ny2] != 1 and house[nx2][ny2-1] != 1:
#                                 dfs((nx1, ny1), (nx2, ny2), i)

# N = int(input())
# house = [list(map(int, input().split())) for _ in range(N)]

# ans = 0
# dfs((0,0), (0,1), 0)
# print(ans)