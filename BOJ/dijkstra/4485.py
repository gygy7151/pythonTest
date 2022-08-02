'''
녹색 옷 입은 애가 젤다지?
'''
'''
두번째풀이
'''
import heapq
import sys
input = sys.stdin.readline


def solution():
    count = 1
    
    while True:
        N = int(input())

        if N == 0:
            return
        
        INF = int(1e9)
        G = [list(map(int, input().split())) for _ in range(N)]
        d = [[INF] * N for _ in range(N)]


        def dijkstra():
            nonlocal d
            nonlocal count
            q = []
            heapq.heappush(q, (G[0][0], 0, 0))
            d[0][0] = 0
            dir = [(0,1), (0,-1), (1,0), (-1,0)]

            while q:
                cost, x, y = heapq.heappop(q)

                if x == N-1 and y == N-1:
                    print('Problem {}: {}'.format(count, cost))
                    break
                
                for dx, dy in dir:
                    nx, ny = x+dx, y+dy

                    if 0 <= nx < N and 0 <= ny < N:
                        new_cost = cost + G[nx][ny]

                        if new_cost < d[nx][ny]:
                            d[nx][ny] = new_cost
                            heapq.heappush(q, (new_cost, nx, ny))
        
        dijkstra()
        count += 1
solution()
'''
첫번째풀이 -bfs,dfs 다 안됨
'''
# from collections import deque
# def solution():
#     answer = int(1e9)
#     def bfs(x,y,score,visited):
#         visited.add((x,y))
#         nonlocal answer
#         dir = [(1,0), (-1,0), (0,1), (0,-1)]

#         if x == N-1 and y == N-1:
#             print(score)
#             answer = min(answer, score)

        
#         for dx, dy in dir:
#             nx, ny = x+dx, y+dy
            
#             if 0 <= nx < N and 0 <= ny < N:
#                 if (nx, ny) not in visited:
#                     bfs(nx,ny,score+G[nx][ny], visited)


#     idx = 0
    
#     while True:
#         idx += 1
#         N = int(input())
        
#         if N == 0:
#             return

#         G = [list(map(int, input().split())) for _ in range(N)]
#         visited = set()
#         bfs(0,0,G[0][0],visited)
#         print('Problem ' + str(idx) + ': ' + str(answer))
# solution()