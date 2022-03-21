'''
로봇청소기- 14503번
'''
N, M = map(int, input().split())
R, K, D = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 , -1]
def bfs(r,k,d):
    global ans
    if graph[r][k] == 0:
        graph[r][k] = 2
        ans += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nx = r + dx[nd]
        ny = k + dy[nd]
        if graph[nx][ny] == 0:
            bfs(nx, ny, nd)
            return
        d = nd
    nd = (d+2) % 4
    nx = r + dx[nd]
    ny = k + dy[nd]
    if graph[nx][ny] == 1:
        return
    bfs(nx, ny, d)

ans = 0
bfs(R,K,D)
print(ans)
