'''
영역구하기
'''
def bfs(n,m):
    global visited
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    visited[n][m] = True
    # 자기자신 포함한 특정 영역의 넓이
    cnt = 1
    q = [(n,m)]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] == -1:
                    cnt += 1
                    visited[nx][ny] = True
                    q.append((nx,ny))
    division_area.append(cnt)

N, M, K = map(int, input().split())
graph = [[-1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
division_area = []

# 사각형 내부 표시
for _ in range(K):
    am, an, bm, bn = map(int, input().split())
    for n in range(an, bn):
        for m in range(am, bm):
            if not visited[n][m]:            
                graph[n][m] = 0
                visited[n][m] = True
# 각 분리된 영역 넓이 구하기
for n in range(N):
    for m in range(M):
        if not visited[n][m]:            
            visited[n][m] = True
            bfs(n,m)

print(len(division_area))
division_area = sorted(division_area)
print(*division_area)

                
            
