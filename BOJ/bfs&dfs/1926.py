'''
그림
'''
'''
첫번째풀이
'''
import sys
from collections import deque
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    paper = []
    Q = deque()

    for i in range(N):
        info = list(map(int, input().split()))
        paper.append(info)
        for j in range(len(info)):
            if info[j] == 1:
                Q.append((i,j))
    
    visited = [[False for _ in range(M)] for _ in range(N)]
    largest_paper = 0

    def bfs(r,c):
        nonlocal largest_paper
        dir = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque()
        q.append((r,c))
        
        cnt = 1
        
        while q:
            x, y = q.popleft()

            for dx, dy in dir:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < M:
                    if paper[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx,ny))
                        cnt += 1

        largest_paper = max(largest_paper, cnt)
        
    paper_cnt = 0
    for x,y in Q:
        if not visited[x][y]:
            visited[x][y] = True
            bfs(x,y)
            paper_cnt += 1

    return paper_cnt, largest_paper

res = solution()
print(*res, sep="\n")

