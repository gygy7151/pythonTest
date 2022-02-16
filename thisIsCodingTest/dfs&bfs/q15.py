'''
특정 거리의 도시찾기
'''
import sys
from collections import deque
input = sys.stdin.readline
n, m, k, x = map(int, input().split())

visited = [False] * (n+1)
visited[x] = True
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

result = []
queue = deque()
queue.append((x, 0))

while queue:
    node, count = queue.popleft()
    if count == k:
        result.append(node)
            
    elif count < k:
        for target in graph[node]:
            if not visited[target]:
                visited[target] = True
                queue.append((target, count+1))
    else:
        break

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)