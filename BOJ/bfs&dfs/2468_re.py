'''
안전영역 - dfs로 풀기
'''
'''
두번째풀이 - 굳이 리미트 폭 넓히지 않고 푸는 방법
'''
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
maxValue = max(map(max, arr))
result = 0
temp = 0
rain = 0
q = deque()

def bfs(x,y):
    global rain
    q.appendleft([x,y])
    visited[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if rain<arr[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny]=1

while maxValue>rain:
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0 and rain<arr[i][j]:
                bfs(i,j)
                temp+=1
    visited = [[0]*N for _ in range(N)]
    result = max(temp,result)
    temp = 0
    rain+=1

print(result)


'''
첫번째풀이
range를 max(map(max, graph))만 해주면 됨. 최솟값은 필요없음
N^3 시간복잡도가 10만이면 괜찮음 초과안남
recurrsion 에러 잡으려면 반드시 8,9,10번 코드 써줘야됨
'''
# import sys
# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline

# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
# dir = ((-1,0), (1,0), (0, -1), (0,1))
# answer = 1
# def dfs(x,y,w):
#     for d in dir:
#         nx, ny = x+d[0], y+d[1]
#         if 0 <= nx < N and 0 <= ny < N:
#             if graph[nx][ny] > w and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 dfs(nx,ny, w)
# for water in range(max(map(max, graph))):
#     count = 0
#     visited = [[False] * N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if graph[i][j] > water and not visited[i][j]:
#                 count += 1
#                 visited[i][j] = True
#                 dfs(i,j,water)
#     answer = max(answer, count)

# print(answer)