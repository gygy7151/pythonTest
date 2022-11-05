'''
Puyo Puyo
'''
'''
첫번째풀이
'''
from collections import deque
def solution():
    board = [[0 for _ in range(12)] for _ in range(6)]

    for idx in range(11, -1, -1):
        data = list(input())
        for j in range(6):
            board[idx][j] = data[j]
        
    
    def bfs(a,b):
        visited = []
        q = deque()
        q.append(a,b)
        color = board[a][b]

        while q:
            x, y = q.popleft()
            for dx, dy in [(0,1), (0,-1), (-1,0), (1,0)]:
                nx, ny = x + dx, ny + dy
                if 0 <= ny < 6 and 0 <= nx < 12:
                    if board[ny][nx] == color:
                        visited.append((ny,nx))
                        q.append((ny,nx))
        
        if len(visited) >= 4:
            



