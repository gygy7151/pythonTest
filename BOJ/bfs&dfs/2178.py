'''
미로탐색
'''
n, m = map(int, input().split())
graph = []
for _ in range(n):
    str = input()
    graph.append([x for x in str])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(start):
    q = []
    q.append(start)
    i, j, cnt = start
    visited = []
    visited.append((i,j))
    while q:
        r, k, cnt = q.pop(0)
        if r == n-1 and k == m-1:
            return cnt

        for dir in range(4):
            nx = r + dx[dir]
            ny = k + dy[dir]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '1' and (nx, ny) not in visited:
                    q.append((nx,ny,cnt+1))
                    visited.append((nx,ny))

print(bfs((0,0,1)))
