'''
화성탐사 - 다익스트라
화성탐사 기계존재공간은 2차원
각칸을 지나기 위한 비용이 존재함
가장왼쪽 위 칸인 0,0칸에서
n-1,n-1칸의 위치로 이동하는 최소 비용을 출력하는 프로그램 작성
위치가 정해졌다..
'''
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


for T in range(int(input())):
    N = int(input())
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * N for _ in range(N)]

    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print(distance[N-1][N-1])
# import sys
# import heapq
# input = sys.stdin.readline
# INF = int(1e9)

# nums =int(input())

# #우선 n제곱그래프가 생성이 되어야하고
# #그담엔?

# for i in range(nums):
#     size = int(input())
#     graph = [[] * (size) for _ in range(size)]
#     distance = [INF] * (size)
#     start = 0
#     end = size - 1
#     for i in range(size):
#         datas = list(map(int, input().split()))
#         for j in range(size):
#             for data in datas:
#                 graph[i][j].append((j, int(input())))

#     def dijkstra(start):
#         q = []
#         heapq.heappush(q, (0, start))
#         distance[start] = 0

#         while q:
#             dist, now = heapq.heappop(q)

#             if distance[now] < dist:
#                 continue

#             for j in graph[now]:
#                 cost = dist + j[1]
#                 if cost < distance[j[0]]:
#                     distance[j[0]] = cost
#                     heapq.heappush(q, (cost,j[0]))
#     dijkstra(start)
#     result = 0
#     for i in range(size):
#         if distance[i] == INF:
#             continue
#         else:
#             result += distance[i]
#     print(result)