'''
현수만
'''
'''
두번째풀이
'''
# import sys
# from collections import deque

# r, c = map(int, sys.stdin.readline().rstrip().split())
# d = [[-1,0], [1,0], [0,1], [0,-1], [-1,-1], [-1,1], [1,-1], [1,1]]
# arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(r)]
# visited = [[False for _ in range(c)] for _ in range(r)]

# def isin(y,x):
#     if -1<y<r:
#         if -1<x<c: return True
#     return False

# def bfs(sy, sx):
#     q = deque()
#     q.append([sy, sx])
#     visited[sy][sx] = True

#     while q:
#         y, x = q.popleft()

#         for i in range(8):
#             ny = y + d[i][0]
#             nx = x + d[i][1]

#             if isin(ny, nx):
#                 if not visited[ny][nx]:
#                     visited[ny][nx] = True
#                     if arr[ny][nx] == 1:
#                         q.append([ny,nx])

# cnt = 0

# for i in range(r):
#     for j in range(c):
#         if not visited[i][j] and arr[i][j] == 1:
#             cnt += 1
#             bfs(i, j)

# print(cnt)

'''
첫번째풀이
'''
from collections import deque

def solution():
    M, N = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(M)]
    visit = [[0 for _ in range(N)] for _ in range(M)]

    def bfs(x,y):
        q = deque()
        visit[x][y] = 1
        q.append((x,y))

        #while문을 빠뜨림..
        while q:
            x, y = q.popleft()
            for dx, dy in  [[-1,0], [1,0], [0,1], [0,-1], [-1,-1], [-1,1], [1,-1], [1,1]]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < M and 0 <= ny < N:
                    if visit[nx][ny] == 0 and graph[nx][ny] == 1:
                        visit[nx][ny] = 1
                        q.append((nx, ny))
        
    answer = 0
    for i in range(M):
        for j in range(N):
            if visit[i][j] == 0 and graph[i][j] == 1:
                bfs(i,j)
                answer += 1
    print(answer)
solution()


