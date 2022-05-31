'''
유기농배추 
'''
'''
두번째 풀이 - 큐를 활용한 dfs
'''
def dfs(a,b):
    q = [(a,b)]
    # 행
    dx = [1,0,0,-1]
    # 열
    dy = [0,-1,1,0]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx,ny))
T = int(input())
for _ in range(T):
    # M은 열의길이 N은 행의길이
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    pos = []
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        # x는 열, y는 행에 해당
        x, y = map(int, input().split())
        graph[y][x] = 1
        pos.append((y,x))
    answer = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 1:
                visited[i][j] = True
                dfs(i,j)
                answer += 1
    print(answer)
'''
첫번째 풀이 - 재귀형식 -> recursion error뜸
'''
# def dfs(x,y):
#     global visited
#     dx = [1,0,0,-1]
#     dy = [0,-1,1,0]
#     for i in range(4):
#         nx, ny = x+dx[i], y+dy[i]
#         if 0 <= nx < N and 0 <= ny < M:
#             if not visited[nx][ny] and graph[nx][ny] == 1:
#                 visited[nx][ny] = True
#                 dfs(nx,ny)

# T = int(input())
# for _ in range(T):
#     N, M, K = map(int, input().split())
#     graph = [[0] * M for _ in range(N)]
#     pos = []
#     visited = [[False] * M for _ in range(N)]
#     for _ in range(K):
#         x, y = map(int, input().split())
#         graph[x][y] = 1
#         pos.append((x,y))
#     answer = 0
#     for x,y in pos:
#         if not visited[x][y]:
#             visited[x][y] = True
#             dfs(x,y)
#             answer += 1
#     print(answer)