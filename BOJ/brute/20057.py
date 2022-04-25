'''
마법사상어와 토네이도
'''
def spread(sx, sy, direction):
    global ans
    if sy < 0:
        return
    total = 0
    for dx, dy, z in direction:
        nx, ny = sx+dx, sy+dy
        if z == 0:
            new_sand = graph[sx][sy] - total
        else:
            new_sand = int((graph[sx][sy]*z))
            total += new_sand
        if 0 <= nx < N and 0 <= ny < N:
            graph[nx][ny] += new_sand
        else:
            ans += new_sand

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0
time = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x,-y,z) for x,y,z in left]
down = [(-y,x,z) for x,y,z in left]
up = [(y,x,z) for x,y,z in left]
sx, sy =  N//2, N//2
dict = { 0:left, 1:down, 2:right, 3:up}
for i in range(2*N-1):
    d = i % 4
    if d == 0 or d == 2:
        time += 1
    for _ in range(time):
        nx, ny = sx + dx[d], sy+ dy[d]
        spread(nx, ny, dict[d])
        sx, sy = nx, ny

print(ans)