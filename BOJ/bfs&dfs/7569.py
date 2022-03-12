'''
토마토 / pypy3통과
'''
import sys
input= sys.stdin.readline
import collections
m, n, h = map(int, input().split())
boxs = [[input().split() for _ in range(n)] for _ in range(h)]
not_visited = [[[True]*m for _ in range(n)] for _ in range(h)]
tomatoes = m*n*h
q = collections.deque()
days = 0
dir = ((-1, 0, 0), (1, 0, 0), (0, -1, 0),(0, 1, 0), (0, 0, -1), (0, 0, 1))
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxs[i][j][k] == '1':
                q.append((i, j, k, 0))
            elif boxs[i][j][k] == '-1':
                tomatoes -= 1
while q:
    z, y, x, days = q.popleft()
    tomatoes -= 1
    for i, j, k in dir:
        nz, ny, nx = z+i, y+j, x+k
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
            if boxs[nz][ny][nx] == '0' and not_visited[nz][ny][nx]:
                q.append((nz,ny,nx, days+1))
                not_visited[nz][ny][nx] = False

print(days if tomatoes == 0 else -1)

