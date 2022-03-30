'''
아기상어 - 16236번
'''
N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
sx = 0
sy = 0
s_size, eat = 2, 0
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            sea[i][j] = 0
            sx = i
            sy = j
            break
dir = ((-1,0), (1,0), (0,-1), (0,1))

def bfs(sx,sy,s_size):
    visited = [[False] * N  for _ in range(N)]
    q = []
    q.append((sx, sy, 0))
    fish = []
    while q :
        x, y, cnt  = q.pop(0)
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                if sea[nx][ny] < s_size and sea[nx][ny] != 0:
                    fish.append((cnt+1, nx, ny))
                    q.append((nx, ny, cnt+1))
                    visited[nx][ny] = True
                elif sea[nx][ny] == 0  or sea[nx][ny] == s_size:
                    visited[nx][ny] = True
                    q.append((nx,ny, cnt+1))
    fish.sort()
    if fish:
        return [fish[0][1], fish[0][2], fish[0][0]]
    else:
        return []

answer = 0

while True:
    fish_eat = bfs(sx,sy, s_size)
    if fish_eat:
        x, y, move = fish_eat
        sea[x][y] = 0
        eat += 1
        answer += move
        if eat == s_size:
            s_size += 1
            eat = 0
        sx, sy = x, y
    else:
        break
print(answer)