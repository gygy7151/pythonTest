'''
적록색약 - 10026번 dfs
'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
dir = ((-1,0), (1,0), (0,-1), (0,1))
graph = [list(map(str, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(a,b,c):
    for d in dir:
        nx, ny = a+d[0], b+d[1]
        if 0<= nx < n and 0<= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == c:
                visited[nx][ny] = True
                dfs(nx,ny,c)

cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j,graph[i][j])
            cnt +=1
print(cnt, end =' ')

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

cnt = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j,graph[i][j])
            cnt +=1
print(cnt)


# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline

# N = int(input())
# graph = []
# for i in range(N):
#     data = input()
#     graph.append([x for x in data])

# a_visited = [[False] * N for _ in range(N)]
# b_visited = [[False] * N for _ in range(N)]
# a_count = 0
# b_count = 0
# dir = ((-1,0), (1,0), (0,-1), (0,1))
# def a_dfs(a,b,c):
#     for d in dir:
#         nx, ny = a+d[0], b+d[1]
#         if 0<= nx < N and 0<= ny < N:
#             if not a_visited[nx][ny] and graph[nx][ny] == c:
#                 a_visited[nx][ny] = True
#                 a_dfs(nx,ny,c)

# def b_dfs(a,b,c):
#     if c == 'R' or c == 'G':
#         for d in dir:
#             nx, ny = a+d[0], b+d[1]
#         if 0<= nx < N and 0<= ny < N:            
#             if not b_visited[nx][ny]:
#                 if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
#                     b_dfs(nx,ny,'R')
#                     b_visited[nx][ny] = True

#     elif c == 'B':
#         for d in dir:
#             nx, ny = a+d[0], b+d[1]
#         if 0<= nx < N and 0<= ny < N:            
#             if not b_visited[nx][ny]:
#                 if graph[nx][ny] == 'B':
#                     b_dfs(nx,ny,'B')

# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 'R':
#             if not a_visited[i][j]:
#                 a_dfs(i,j,graph[i][j])
#                 a_visited[i][j] = True
#                 a_count += 1
#             if not b_visited[i][j]:
#                 b_dfs(i,j,graph[i][j])
#                 b_visited[i][j] = True
#                 b_count += 1
        
#         elif graph[i][j] == 'G':
#             if not a_visited[i][j]:
#                 a_dfs(i,j,graph[i][j])
#                 a_visited[i][j] = True
#                 a_count += 1
#             if not b_visited[i][j]:
#                 b_dfs(i,j,graph[i][j])
#                 b_visited[i][j] = True

#         elif graph[i][j] == 'B':
#             if not a_visited[i][j]:
#                 a_dfs(i,j,graph[i][j])
#                 a_visited[i][j] = True
#                 a_count += 1
#             if not b_visited[i][j]:
#                 b_dfs(i,j,graph[i][j])
#                 b_visited[i][j] = True
#                 b_count += 1

# print("{} {}".format(a_count, b_count))