'''
음식물피하기
'''
'''
첫번째풀이
'''
from collections import deque
import sys
input = sys.stdin.readline

def solution():    
    N, M, K = list(map(int, input().split()))
    graph = [[0 for _ in range(M)] for _ in range(N)]

    trash = deque()
    
    visit = [[0 for _ in range(M)] for _ in range(N)]

    answer = 0

    def bfs(a, b):
        q = deque()
        q.append((a,b))

        result = 1
        while q:
            x, y = q.popleft()
            
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < M:
                    if visit[nx][ny] == 0 and graph[nx][ny] == 1:
                        visit[nx][ny] = 1
                        result += 1
                        q.append((nx, ny))

        return result
        
    for _ in range(K):
        a, b = map(int, input().split())
        trash.append((a-1,b-1,1))
        graph[a-1][b-1] = 1
    
    for pos in trash:
        if not visit[pos[0]][pos[1]]:
            visit[pos[0]][pos[1]] = 1
            answer = max(answer, bfs(pos[0], pos[1]))
    print(answer)

solution()




        


