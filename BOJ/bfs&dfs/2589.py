'''
보물섬
'''
'''
두번째풀이
'''
# from collections import deque
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# board = [list(input().rstrip()) for _ in range(n)]
# visit = [[0]*m for _ in range(n)]
# move = [(0,1),(1,0),(0,-1),(-1,0)]

# ans = 0
# for i in range(n):
#     for j in range(m):
#         # 가장자리가 아님
#         if i>0 and i+1<n:
#             if board[i-1][j] == "L" and board[i+1][j] == "L":
#                 continue
#         if j>0 and j+1<m:
#             if board[i][j-1] == "L" and board[i][j+1] == "L":
#                 continue
        
#         # BFS 진행
#         if board[i][j] == "L" and not visit[i][j]:
#             q = deque([(i,j)])
#             visit_tmp = [i[:] for i in visit]
#             visit_tmp[i][j] = 1
#             r = 0
#             while q:
#                 x,y = q.popleft()
#                 for a,b in move:
#                     dx=x+a; dy=y+b
#                     if n>dx>=0 and m>dy>=0 and not visit_tmp[dx][dy] and board[dx][dy]=="L":
#                         visit_tmp[dx][dy] = visit_tmp[x][y] + 1
#                         r = max(r,visit_tmp[dx][dy])
#                         q.append((dx,dy))
            
#             ans = max(ans,r)
# print(ans-1)

'''
첫번째풀이 -  예시 답안이 틀림..., 백트래킹 활용해 pytohn3로 풂
'''
from collections import deque

def solution():
    N, M = map(int, input().split())
    graph = [list(input()) for _ in range(N)]

    def bfs(x,y):
        q = deque()
        q.append((x,y))
        visit = [ [-1 for _ in range(M)] for _ in range(N)]
        visit[i][j] = 1
        result = 0
        while q:

            x, y = q.popleft()

            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:

                    if visit[nx][ny] == -1 and graph[nx][ny] == 'L':
                        visit[nx][ny] = visit[x][y] + 1
                        result = max(result,visit[nx][ny])
                        q.append((nx,ny))
        
        return result-1
        
    answer = 0

    for i in range(N):
        for j in range(M):
            # 가장자리인 경우에만 bfs를 돌림
            if graph[i][j] == 'L':
                answer = max(answer, bfs(i,j))
    
    print(answer)
solution()

    

