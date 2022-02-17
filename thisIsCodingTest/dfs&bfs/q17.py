'''
경쟁적전염 - bfs
'''
import heapq
import copy
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
data = [[0] * (n+1) for _ in range(n+1)]
virus = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(1, n+1):
    datas = list(map(int, input().split()))
    for j, el in enumerate(datas):
        data[i][j+1] = el

for i in range(1, n+1):
    for j, el in enumerate(data[i]):
        if el == 0:
            data[i][j] = el
            continue
        else:
            data[i][j] = el
            heapq.heappush(virus, (el, i, j))
s, x, y = map(int, input().split())

def bfs(virus):
    temp = []
    
    while virus:
        k, x, y = heapq.heappop(virus)
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx>0 and ny>0 and nx<n+1 and ny<n+1:
                if data[nx][ny] == 0:
                    data[nx][ny] = k
                    heapq.heappush(temp, (k, nx, ny))

    return temp

res = bfs(virus)
time = 0
time+= 1
while time <= s:
    if time < s:
        asw = copy.deepcopy(res)
        res = bfs(asw)
        time+= 1
    else:
        print(data[x][y])
        break


