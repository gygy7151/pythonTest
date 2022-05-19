'''
연구소2
0: 빈칸, 1: 벽, 2:바이러스 놓을 위치
'''
dx = [1,0,0,-1] 
dy = [0,-1,1,0]
def dfs(visited, virus):
    global time
    temp = [[0]* m for _ in range(n)]
    new_virus = []
    for y,x in virus:
        #퍼뜨려진바이러스위치값은 -1로 처리
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if visited[ny][nx] != False:
                    if graph[ny][nx] != '-' and graph[ny][nx] != -1:
                        temp[ny][nx] += 1
    zero = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                zero = True
            if graph[i][j] != '-' and graph[i][j] != -1:
                graph[i][j] += temp[i][j]
    time += 1
    if zero == False:
        print(time)
        return
    else:
        dfs(visited, new_virus)
n, m = map(int, input().split())
time = 0
graph = [list(map(int, input().split())) for _ in range(n)]
vir_pos = []
visited = [[False]* m for _ in range(n)]
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            continue
        if graph[y][x] == 1:
            graph[y][x] = '-'
        if graph[y][x] == 2:
            graph[y][x] = -1
            visited[y][x] = True
            vir_pos.append((y,x))
dfs(visited,vir_pos)
if time == 0:
    print(-1)


