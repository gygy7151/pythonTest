'''
단지번호붙이기 - bfs
'''
n = int(input())
graph = []
for i in range(n):
    data = input()
    graph.append([int(x) for x in data])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = []
houses = []
towns = 0
def bfs(start):
    global towns
    towns += 1
    graph[start[0]][start[1]] = towns
    q = []
    check = []
    q.append(start)
    check.append((start[0], start[1]))
    visited.append((start[0], start[1]))
    while q:
        i, j, cnt = q.pop(0)
        for l in range(4):
            nx = i + dx[l]
            ny = j + dy[l]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in check and (nx, ny) not in visited:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = towns
                    visited.append((nx, ny))
                    check.append((nx,ny))
                    q.append((nx, ny, cnt+1))
    houses.append(len(check))

for i in range(n):
    for idx, house in enumerate(graph[i]):
        if house == 1 and (i, idx) not in visited:
            bfs((i, idx, 1))

houses.sort()
print(len(houses))
for house in houses:
    print(house)

for el in graph:
    print(el)