'''
치즈 - 2638번
'''
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dir = ((-1,0), (1,0), (0,1), (0,-1))
hours = 0

def bfs():
    c = [[-1] * M for _ in range(N)]
    r = [[0,0]]
    graph[0][0] = -1
    c[0][0] = 1
    while r:
        x, y = r.pop(0)
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0 <= nx < N and 0 <= ny < M and c[nx][ny] == -1:
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                else:
                    c[nx][ny] = 1
                    r.append([nx,ny])

while True:
    bfs()
    flag = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                flag = 1
            if graph[i][j] == 2:
                graph[i][j] = 1

    if flag:
        hours += 1
    else:
        print(hours)
        break
