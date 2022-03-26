'''
데스나이트 - 16948번
'''
N = int(input())
r1, c1, r2, c2 = map(int, input().split())
dir = ((-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1))

def bfs(x,y):
    q = []
    visited = [[-1]* N for _ in range(N)]
    q.append((x,y,0))
    visited[x][y] = 1
    while q:
        r, c, cnt = q.pop(0)
        if r == r2 and c == c2:
            return visited[r][c]
        for d in dir:
            nx, ny = r+d[0], c+d[1]
            if 0<= nx < N and 0<= ny < N:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = cnt+1
                    q.append((nx, ny, cnt+1))
    if visited[r2][c2] == -1:
        return -1
        
print(bfs(r1,c1))
