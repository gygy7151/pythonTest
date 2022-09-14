'''
불!
'''
'''
세번째풀이
'''
from collections import deque
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    graph = [ list(input()) for _ in range(N)]
    fQ = deque()
    jQ = deque()
    fVisit = [[0 for _ in range(M)] for _ in range(N)]
    jVisit = [[0 for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'J':
                jQ.append((i,j))

            if graph[i][j] == 'F':
                fQ.append((i,j))


    while fQ:
        x, y = fQ.popleft()
        
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if fVisit[nx][ny] == 0 and graph[nx][ny] != '#':
                    fVisit[nx][ny] = fVisit[x][y] + 1
                    fQ.append((nx,ny))

    while jQ:

        x, y = jQ.popleft()
        
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < N and 0 <= ny < M):

                print(jVisit[x][y] + 1)
                return

            if jVisit[nx][ny] == 0 and graph[nx][ny] != '#':
                if fVisit[x][y] == 0 or fVisit[nx][ny] > jVisit[x][y] + 1:
                    jVisit[nx][ny] = jVisit[x][y] + 1
                    jQ.append((nx,ny))
    
    print('IMPOSSIBLE')

solution()

        



'''
두번째풀이 -  틀림
'''
# from collections import deque
# import sys
# input = sys.stdin.readline

# def solution():
#     N, M = map(int, input().split())
#     graph = [list(input()) for _ in range(N)]
#     bx, by, rx, ry = 0, 0, 0, 0

#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 'F':
#                 bx, by = i, j
            
#             elif graph[i][j] == 'J':
#                 rx, ry = i, j
    
#     # 불 이동시간
#     f_dist = [[0 for _ in range(M)] for _ in range(N)]
#     # 지훈이 이동시간
#     jh_dist = [[0 for _ in range(M)] for _ in range(N)]

#     def bfs(bx, by, rx, ry):
#         q1 = deque()
#         q2 = deque()
#         #불
#         q1.append((bx,by))
#         #지훈
#         q2.append((rx,ry))

#         while q1:
#             x, y = q1.popleft()
#             for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
#                 nx, ny = x + dx, y + dy

#                 if nx < 0 or ny < 0 or nx >= N or ny >= M:
#                     continue
                
#                 if f_dist[nx][ny] == 0 and graph[nx][ny] != '#':
#                     f_dist[nx][ny] = f_dist[x][y] + 1
#                     q1.append((nx, ny))

#         while q2:
#             x, y = q2.popleft()
#             for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
#                 nx, ny = x + dx, y + dy

#                 if 0 <= nx < N and 0 <= ny < M:
#                     if jh_dist[nx][ny] == 0 and graph[nx][ny] != '#':
#                         if f_dist[nx][ny] == 0 or f_dist[nx][ny] > jh_dist[x][y]+1:
#                             jh_dist[nx][ny] = jh_dist[x][y] + 1
#                             q2.append((nx,ny))

#                 else:
#                     print(jh_dist[x][y]+1)
#                     return

#         print('IMPOSSIBLE')

#     bfs(bx, by, rx, ry)

# solution()

'''
첫번째풀이 - 메모리 초과
'''
# from collections import deque
# import sys
# input = sys.stdin.readline

# def solution():
#     N, M = map(int, input().split())
#     graph = [list(input()) for _ in range(N)]
#     bx, by, rx, ry = 0, 0, 0, 0

#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 'F':
#                 bx, by = i, j
            
#             elif graph[i][j] == 'J':
#                 rx, ry = i, j
    
#     # 불 이동시간
#     dist1 = [[-1 for _ in range(M)] for _ in range(N)]
#     # 지훈이 이동시간
#     dist2 = [[-1 for _ in range(M)] for _ in range(N)]

#     def bfsFire(x,y):
#         q = deque()
#         q.append((x,y))
#         # 불 이동시간
#         dist1[x][y] = 0

#         while q:
#             x, y = q.popleft()
#             for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
#                 nx, ny = x + dx, y + dy

#                 if nx < 0 or ny < 0 or nx >= N or ny >= M:
#                     continue
                
#                 if dist1[nx][ny] == -1 and graph[nx][ny] == '.':
#                     dist1[nx][ny] = dist1[x][y] + 1
#                     q.append((nx, ny))
    
#     bfsFire(bx, by)

#     def bfsJihun(x,y):
#         count = 0
#         q = deque()
#         q.append((x,y))
#         # 불 이동시간
#         dist2[x][y] = 0
#         while q:
#             x, y = q.popleft()

#             for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
#                 nx, ny = x + dx, y + dy

#                 if 0 <= nx < N and 0 <= ny < M:    
#                     if graph[nx][ny] == '.':
#                         if dist1[nx][ny] >= dist2[x][y] + 1:
#                             dist2[nx][ny] = dist2[x][y] + 1
#                             q.append((nx, ny))
#                 else:
#                     if dist1[x][y] >= dist2[x][y]:
#                         print(dist2[x][y]+1)
#                     else:
#                         print('IMPOSSIBLE')
                    
#                     return
#         print('IMPOSSIBLE')
    
#     bfsJihun(rx, ry)

# solution()