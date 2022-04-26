'''
마법사상어와 비바라기
'''
# def move(d, s, pos):
#     n_pos = []
#     for x, y in pos:
#         nx, ny = x+dx[d]*s, y+dy[d]*s
#         if 0 <= nx < N and 0 <= ny < N:
#             n_pos.append((nx, ny))
#     return n_pos

# def rain(pos):
#     for x, y in pos:
#         if not visited[x][y]:
#             graph[x][y] += 1
#             visited[x][y] = True
#             buble(x,y)

# def buble(x,y):
#     cross = [(-1,-1), (-1,1), (1,-1), (1,1)]
#     for i in range(4):
#         nx, ny = x+cross[i][0], y+cross[i][1]
#         if 0 <= nx < N and 0 <= ny < N:
#             if graph[nx][ny] > 0:
#                 graph[x][y] += 1

# def create():
#     global n_p
#     n_cloud = []
#     for i in range(N):
#         for j in range(N):
#             if graph[i][j] >= 2 and not visited[i][j]:
#                 graph[i][j] -= 2
#                 visited[i][j] = True
#                 n_cloud.append((i,j))
#     return n_cloud


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
c_p = [(N-1,0), (N-1,1), (N-2,0), (N-2,1)]
moves = []

for _ in range(M):
    d, s = map(int, input().split())
    moves.append([d-1, s])

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
for i in range(M):
    move = moves[i]
    next_c_p = []
    for c in c_p:
        x, y, d, s = c[0], c[1], move[0], move[1]
        nx = (N + x + dx[d] * s) % N
        ny = (N + y + dy[d] * s) % N
        next_c_p.append([nx,ny])

    visited = [[False]*N for _ in range(N)]
    for c in next_c_p:
        x, y = c[0], c[1]
        graph[x][y] += 1
        visited[x][y] = True
    
    c_p = []
    cx = [-1,-1,1,1]
    cy = [-1,1,-1,1]
    for c in next_c_p:
        x, y  = c[0], c[1]
        count = 0
        for i in range(4):
            nx = x + cx[i]
            ny = y + cy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] >= 1:
                count += 1
        graph[x][y] += count
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and visited[i][j] == False:
                graph[i][j] -= 2
                c_p.append([i,j])

ans = 0
for i in range(N):
    ans += sum(graph[i])
print(ans)