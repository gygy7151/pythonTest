'''
안전영역 - dfs로 풀기
range를 max(map(max, graph))만 해주면 됨. 최솟값은 필요없음
N^3 시간복잡도가 10만이면 괜찮음 초과안남
recurrsion 에러 잡으려면 반드시 8,9,10번 코드 써줘야됨
'''

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dir = ((-1,0), (1,0), (0, -1), (0,1))
answer = 1
def dfs(x,y,w):
    for d in dir:
        nx, ny = x+d[0], y+d[1]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] > w and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny, w)
for water in range(max(map(max, graph))):
    count = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > water and not visited[i][j]:
                count += 1
                visited[i][j] = True
                dfs(i,j,water)
    answer = max(answer, count)

print(answer)