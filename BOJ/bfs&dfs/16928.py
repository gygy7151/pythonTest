'''
뱀과 사다리 게임- 16928번
'''
N, M = map(int,input().split())
trick = [0]*101
for _ in range(N+M):
    n, val = map(int, input().split())
    trick[n] = val

def bfs(r,k):
    q = []
    q.append((r,k))
    visited = [0]*101
    visited[r] = 1
    while q:
        x, cnt = q.pop(0)
        if x == 100:
            return cnt
        for i in range(1,7):
            nx = x + i
            if nx > 100:
                continue
            if trick[nx] == 0 and not visited[nx]:
                visited[nx] = 1
                q.append((nx, cnt+1))
            else:
                if not visited[trick[nx]]:
                    visited[trick[nx]] = 1
                    q.append((trick[nx], cnt+1))
print(bfs(1,0))