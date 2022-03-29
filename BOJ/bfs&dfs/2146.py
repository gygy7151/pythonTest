'''
다리만들기 - 2146번
'''
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dir = ((-1,0), (0,1), (1,0), (0,-1))
tag = 1
island_visited = [[0] * N  for _ in range(N)]
answer = int(1e9)

def group(a,b):
    i = []
    global tag
    i.append((a,b))
    graph[a][b] = tag
    while i:
       x, y = i.pop(0)
       for d in dir:
           nx, ny = x+d[0], y+d[1]
           if 0 <= nx < N and 0 <= ny < N:
               if graph[nx][ny] == 1 and not island_visited[nx][ny]:
                   island_visited[nx][ny] = 1
                   graph[nx][ny] = tag
                   i.append((nx,ny))

def get_distance(z):
    global answer
    dist = [[-1] * N for _ in range(N)]
    q = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == z:
                q.append([i,j])
                dist[i][j] = 0
    while q:
        x, y = q.pop(0)
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > 0 and graph[nx][ny] != z:
                    answer = min(answer, dist[x][y])
                    return
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not island_visited[i][j]:
            group(i,j)
            island_visited[i][j] = 1
            tag += 1

for i in range(1, tag):
    get_distance(i)
print(answer)





# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
# dir = ((-1,0), (0,1), (1,0), (0,-1))
# def bfs(a,b):
#     ans = 0
#     q = []
#     visited = [[-1]* N for _ in range(N)]
#     visited[a][b] = 0
#     q.append((a,b,0))
#     while q:
#         x, y, cnt = q.pop(0)
#         print(x,y, cnt)
#         for d in dir:
#             nx, ny = x+d[0], y+d[1]
#             if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
#                 if graph[nx][ny] == 0:
#                     visited[nx][ny] = visited[x][y] + 1
#                     q.append((nx, ny, cnt+1))
                
#                 if graph[nx][ny] == 1 and visited[nx][ny] == -1:
#                     return cnt

# min_value = int(1e9)
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 1:
#             res = bfs(i,j)
#             print(res)
#             if res != 0:
#                 min_value = min(res, min_value)
# print(min_value)