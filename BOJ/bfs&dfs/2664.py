'''
촌수계산
'''
n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def bfs(start, cnt):
    q = []
    visited = []
    q.append((start, cnt))
    visited.append(start)
    while q:
        vrt, cnt = q.pop(0)

        if vrt == end:
            print(cnt)
            return

        for id, node in enumerate(graph[vrt]):
            if node and id not in visited:
                visited.append(id)
                q.append((id, cnt+1))
    print(-1)

bfs(start, 0)
