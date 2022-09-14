'''
구슬탈출2
'''
'''
두번째풀이
'''
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
#빨간구슬위치
rx, ry = 0, 0
#파란구슬위치
bx, by = 0, 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            rx, ry = i, j
        
        elif graph[i][j] == 'B':
            bx, by = i, j

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited = []
    visited.append((rx, ry, bx, by))
    count = 0

    while q:
        for _ in range(len(q)):
            print('날래?')
            rx, ry, bx, by = q.popleft()
             # 10회초과시 빨간구슬이 구멍을 통해 빠져나갈 수 없는 경우
            if count > 10:
                print(count)
                return
            
            if graph[rx][ry] == 'O':
                print(count)
                return
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                #빨간색 구슬 이동
                nrx, nry = rx, ry
                
                #단일방향으로 계속 이동시킴
                while True:
                    nrx += dx
                    nry += dy

                    if graph[nrx][nry] == '#':
                        nrx -= dx
                        nry -= dy
                        break

                    if graph[nrx][nry] == 'O':
                        break
                
                nbx, nby = bx, by

                while True:
                    nbx += dx
                    nby += dy

                    if graph[nbx][nby] == '#':
                        nbx -= dx
                        nby -= dy
                        break
                    
                    if graph[nbx][nby] == 'O':
                        break

                if graph[nbx][nby] == 'O':
                    continue

                if nrx == nbx and nry == nby:
                    if abs(nrx- rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx
                        nry -= dy
                    
                    else:
                        nbx -= dx
                        nby -= dy
                
                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
        print(q)
        print(count)
    # 10회미만이지만 빨간구슬이 구멍을 통해 빠져나갈 수 없는 경우
    print(-1)

bfs(rx, ry, bx, by)




'''
첫번째풀이
파란구슬이 불이라고 생각하면 될듯
그럼 우선 불에 대한 bfs 즉 파란구슬의 bfs를 먼저 돌리고

파란구슬이 빨간구슬보다 먼저 도착점에 도착하거나
빨간구슬과 동시에 도착하는 경우 -> 빨간구슬과 파란구슬이 동시에 움직여야 했는데 각자도생하는 잘못된 접근으로 풀이함
'''
# N, M = map(int, input().split())
# #불이 난공간
# dist1 = [[-1 for _ in range(N)] for _ in range(M)]
# dist2 = [[-1 for _ in range(N)] for _ in range(M)]
# board = [list(input()) for _ in range(N)]
# dx = [1, 0, -1, 0]
# dy = [0, -1, 0, 1]
# q1 = []
# q2 = []
# targetX, targetY = 0, 0
# # 파란구슬과 빨간구슬의 위치 각각 Q1, Q2에 넣어줌
# for i in range(N):
#     for j in range(M):
#         if board[i][j] == 'B':
#             q1.append((i,j))
#             dist1[i][j] = 0
#         if board[i][j] == 'R':
#             q2.append((i,j))
#             dist2[i][j] = 0
#         if board[i][j] == '0':
#             targetX, targetY = i, j

# # 불, 즉 파란구슬에 대한 bfs
# while q1:
#     x, y = q1.pop(0)
#     for dir in range(4):
#         nx, ny = x + dx[dir], y + dy[dir]

#         if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
#         if dist1[nx][ny] >= 0 or board[nx][ny] == '#': continue
#         dist1[nx][ny] = dist1[x][y] + 1
#         q1.append((nx,ny))

# while q2:
#     x, y = q2.pop(0)
#     for dir in range(4):
#         nx, ny = x + dx[dir], y + dy[dir]

#         if dist2[nx][ny] >= 0 or board[nx][ny] == '#': continue
#         if dist2[nx][ny] != -1 and dist1[nx][ny] <= dist2[nx][ny]+1: continue
#         dist2[nx][ny] = dist2[x][y] + 1
#         q2.append((nx,ny))

# print(dist2[targetX][targetY])
# print(dist1[targetX][targetY])
# if dist1[targetX][targetY] >= dist2[targetX][targetY]:
#     print(-1)
# else:
#     print(dist2[targetX][targetY])