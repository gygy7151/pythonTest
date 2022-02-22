'''
경쟁적전염 - bfs, q 사용
'''
import queue
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
graph = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))


s, x, y = map(int, input().split())



queue = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data = graph[i][j]
            queue.append((data, i, j, 0))

queue.sort()

while queue:
    virus, _x, _y, t = queue.pop()

    if t == s:
        break

    for i in range(4):
        nx = _x + dx[i]
        ny = _y + dy[i]

    if nx >= 0 and ny >= 0 and nx < n and ny < n:
        if graph[nx][ny] != 0:
            graph[nx][ny] = virus
            queue.append((k, nx, ny, t+1))

print(graph[x-1][y-1])

                










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


