'''
경쟁적전염 - bfs, q 사용
'''
from collections import deque
N, K = map(int, input().split())
graph = []
virus = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j))

S, X, Y = map(int, input().split())

virus.sort()

def bfs(S, X, Y):
    count = 0
    q = deque(virus)
    while q:
        if count == S:
            break
        for _ in range(len(q)):
            virs, x, y = q.popleft()    
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and ny >= 0 and nx < N and ny < N:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]
                        q.append((graph[nx][ny], nx, ny))
        count+=1
    return graph[X-1][Y-1]

print(bfs(S,X,Y))


                










# import heapq
# import copy
# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# data = [[0] * (n+1) for _ in range(n+1)]
# virus = []
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]

# for i in range(1, n+1):
#     datas = list(map(int, input().split()))
#     for j, el in enumerate(datas):
#         data[i][j+1] = el

# for i in range(1, n+1):
#     for j, el in enumerate(data[i]):
#         if el == 0:
#             data[i][j] = el
#             continue
#         else:
#             data[i][j] = el
#             heapq.heappush(virus, (el, i, j))
# s, x, y = map(int, input().split())

# def bfs(virus):
#     temp = []
    
#     while virus:
#         k, x, y = heapq.heappop(virus)
#         for j in range(4):
#             nx = x + dx[j]
#             ny = y + dy[j]
#             if nx>0 and ny>0 and nx<n+1 and ny<n+1:
#                 if data[nx][ny] == 0:
#                     data[nx][ny] = k
#                     heapq.heappush(temp, (k, nx, ny))

#     return temp

# time = 0
# while time <= s+1:
#     if time <= s:
#         time+=1
#         res = bfs(virus)
#         virus = copy.deepcopy(res)
#     else:
#         print(data)
#         print(data[x][y])
#         break


