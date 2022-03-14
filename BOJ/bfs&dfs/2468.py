'''
안전영역
다른 사람들 풀이를 보니 시간복잡도가 괜찮은가보다..
그리고 max를 graph[i][j]값을 갱신하면서 입력하면 된다.
'''
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
min_num = min(map(min, graph))
max_num = max(map(max, graph))

dr = ((-1,0), (1,0), (0, -1), (0,1))
def bfs(a, b, val, visited):
    q = []
    q.append((a,b))
    visited[a][b] = 1
    while q:
        x, y = q.pop(0)
        for d in dr:
            nx = x + d[0]
            ny = y + d[1]
            if 0<= nx < N and 0<= ny < N:
                if graph[nx][ny] >= val and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    print(visited)
                    q.append((nx,ny))

result = 0
for v in range(min_num, max_num+1):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= v and visited[i][j] == 0:
                bfs(i, j, v, visited)
                cnt += 1
    if result < cnt:
        result = cnt

print(result)