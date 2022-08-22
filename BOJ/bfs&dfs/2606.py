'''
바이러스
'''
n = int(input())
m = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def bfs(start):
    q = []
    visited = []
    q.append(start)
    visited.append(start)
    answer = 0

    while q:
        cmpt = q.pop(0)
        for idx, link in enumerate(graph[cmpt]):
            if link == 1 and idx not in visited:
                visited.append(idx)
                answer += 1
                q.append(idx)
    
    return answer

print(bfs(1))
