'''
연구소- 14502번 3916ms에서 2800ms절감함
'''
N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
max_val = 0
data = []
copy = [[0]*M for _ in range(N)]
def bfs():
    global max_val
    dir = ((-1,0), (1,0), (0,-1), (0,1))
    for i in range(N):
        for j in range(M):
            copy[i][j] = graph[i][j]
            if graph[i][j] == 2:
                data.append((i,j))
    while data:
        x, y = data.pop(0)
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0 <= nx < N and 0 <= ny < M:
                if copy[nx][ny] == 0:
                    copy[nx][ny] = 2
                    data.append((nx,ny))
    cnt = 0
    for r in copy:
        for c in r:
            if c == 0:
                cnt += 1
    max_val = max(max_val, cnt)

def wall(cnt):
    print(cnt)
    if cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt+1)
                graph[i][j] = 0
                print('{}0이되어따'.format(cnt))
wall(0)
print(max_val)

# N, M = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]
# temp = [[0] * M for _ in range(N)]
# lab = [[0] * M for _ in range(N)]
# datas = []
# visited = [[0]*M for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if temp[i][j] == 2:
#             datas.append((i,j))
# def scan():
#     for i in range(N):
#         for j in range(M):
#             lab[i][j] = graph[i][j]
#             graph[i][j] == temp[i][j]

# def virus():
#     dir = ((-1,0), (1,0), (0,-1), (0,1))
#     q = []
#     for dda in datas:
#         q.append(dda)
#     while q:
#         x, y = q.pop(0)
#         for d in dir:
#             nx, ny = x+d[0], y+d[1]
#             if 0<= nx < N and 0 <= ny < M:
#                 if lab[nx][ny] == 0:
#                     lab[nx][ny] = 2
#                     q.append((nx,ny))

# def make_wal():
#     ans = 0
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if not visited[i][j] and graph[i][j] == 0:
#                 graph[i][j] = 1
#                 visited[i][j] = 1
#                 cnt += 1
#             if cnt == 3:
#                 scan()
#                 virus()
#                 ans = max(ans, get_val())
#                 cnt = 0
#     return ans
    

# def get_val():
#     value = 0
#     for i in range(N):
#         for j in range(M):
#             if lab[i][j] == 0:
#                 value += 1
#     return value

# print(make_wal())




