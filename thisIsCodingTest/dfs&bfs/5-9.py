# bfs 예제
from collections import deque

n = 8
graph = []
visited = [False] * (n+1)
graph.append([])
for _ in range(1, n+1):
    graph.append(list(map(int, input().split())))

def bfs(graph, start, visited) :
    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()
        print(now, end = ' ')
        for link in graph[now]:
            if not visited[link]:
                q.append(link)
                visited[link] = True

bfs(graph, 1, visited)
