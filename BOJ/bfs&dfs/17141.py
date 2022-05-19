'''
연구소2
0: 빈칸, 1: 벽, 2:바이러스 놓을 위치
'''
'''
두번째풀이 - bfs, 조합
'''
dx = [1,0,0,-1]
dy = [0,-1,1,0]
answer = int(1e9)

def combination(virus_pos, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(0, len(virus_pos)):
        some = virus_pos[i]
        left = virus_pos[i+1:]
        for comb in combination(left, n-1):
            result.append([some]+comb)
    return result

def bfs(v_pos):
    q = v_pos
    visited = [[-1] * n for _ in range(n)]
    count = 0
    for x,y in q:
        visited[x][y] = 0
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and graph[nx][ny] != 1:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1
                    count = max(count, visited[x][y]+1)
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and graph[i][j] != 1:
                return int(1e9)
    return count

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virus_pos = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus_pos.append([i,j])
for virus_pos_comb in combination(virus_pos, m):
    answer = min(bfs(virus_pos_comb), answer)

if answer == int(1e9):
    print(-1)
else:
    print(answer)
    



'''
첫번째풀이 - 논리틀림, dfs로 재귀초과
'''
# dx = [1,0,0,-1] 
# dy = [0,-1,1,0]
# def dfs(visited, virus):
#     global time
#     temp = [[0]* m for _ in range(n)]
#     new_virus = []
#     for y,x in virus:
#         #퍼뜨려진바이러스위치값은 -1로 처리
#         for i in range(4):
#             ny, nx = y+dy[i], x+dx[i]
#             if 0 <= ny < n and 0 <= nx < m:
#                 if visited[ny][nx] != False:
#                     if graph[ny][nx] != '-' and graph[ny][nx] != -1:
#                         temp[ny][nx] += 1
#     zero = False
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 zero = True
#             if graph[i][j] != '-' and graph[i][j] != -1:
#                 graph[i][j] += temp[i][j]
#     time += 1
#     if zero == False:
#         print(time)
#         return
#     else:
#         dfs(visited, new_virus)
# n, m = map(int, input().split())
# time = 0
# graph = [list(map(int, input().split())) for _ in range(n)]
# vir_pos = []
# visited = [[False]* m for _ in range(n)]
# for y in range(n):
#     for x in range(m):
#         if graph[y][x] == 0:
#             continue
#         if graph[y][x] == 1:
#             graph[y][x] = '-'
#         if graph[y][x] == 2:
#             graph[y][x] = -1
#             visited[y][x] = True
#             vir_pos.append((y,x))
# dfs(visited,vir_pos)
# if time == 0:
#     print(-1)


