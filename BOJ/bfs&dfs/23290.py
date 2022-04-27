'''
마법사 상어와 복제 - bfs
'''
'''
두번째 풀이
'''
import copy

def move_fish():
    """
    물고기 이동
    1. 상어가 있는 칸, 물고기 냄새 칸, 벗어나는 칸 x 
    2. 45도 반시계 회전 후 이동. 이동 못하는 경우 그대로 
    :return:
    """
    res = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while temp[x][y]:
                d = temp[x][y].pop()
                for i in range(d, d - 8, -1):
                    i %= 8
                    nx, ny = x + f_dx[i], y + f_dy[i]
                    if (nx, ny) != shark and 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]:
                        res[nx][ny].append(i)
                        break
                else:
                    res[x][y].append(d)
    return res

def dfs(x, y, dep, cnt, visit):
    """
    상어 3칸 이동
    1. 제외되는 물고기 수가 많고 > 이동방법 사전순(백트래킹하면 자동으로 됨) 
    2. 이동한 곳을 저장 > 물고기 냄새가 됨  
    """
    global max_eat, shark, eat
    if dep == 3:   # 3번 이동한 경우 그만 
        if max_eat < cnt:
            max_eat = cnt
            shark = (x, y)
            eat = visit[:]
        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) not in visit:  # 처음 방문, cnt에 죽은 물고기 수 추가  
                visit.append((nx, ny))
                dfs(nx, ny, dep + 1, cnt + len(temp[nx][ny]), visit)
                visit.pop()
            else:  # 방문한 경우
                dfs(nx, ny, dep + 1, cnt, visit)

#       ←, ↖,   ↑,  ↗, →, ↘, ↓, ↙
f_dx = [0, -1, -1, -1, 0, 1, 1, 1]
f_dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

m, s = map(int, input().split())
fish = [list(map(int, input().split())) for _ in range(m)]
graph = [[[] for _ in range(4)] for _ in range(4)]

for x, y, d in fish:
    graph[x - 1][y - 1].append(d - 1)

shark = tuple(map(lambda x: int(x) - 1, input().split()))
smell = [[0] * 4 for _ in range(4)]

for _ in range(s):
    eat = list()
    max_eat = -1
    # 1. 모든 물고기 복제
    temp = copy.deepcopy(graph)
    # 2. 물고기 이동
    temp = move_fish()
    # 3. 상어이동 - 백트래킹
    dfs(shark[0], shark[1],0, 0, list())
    for x, y in eat:
        if temp[x][y]:
            temp[x][y] = []
            smell[x][y] = 3   # 3번 돌아야 없어짐
    # 4. 냄새 사라짐 
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1
    # 5. 복제 마법
    for i in range(4):
        for j in range(4):
            graph[i][j] += temp[i][j]

# 물고기 수 구하기 
answer = 0
for i in range(4):
    for j in range(4):
        answer += len(graph[i][j])

print(answer)
'''
첫번째 풀이 - 인덱스 에러
'''
# import copy
# def bfs(x,y):
#     missing_fish = []
#     first_scent = []
#     q = []
#     ddx = [0,1,0,-1]
#     ddy = [1,0,-1,0]
#     q.append((x,y,0,0))
#     while q:
#         x, y, depth, score = q.pop(0)
#         if depth == 3:
#             first_scent.append((score,(x,y)))
#             continue
#         for i in range(4):
#             nx, ny = x + ddx[i], y + ddy[i]
#             if 0 <= nx < 4 and 0 <= ny < 4:
#                 if ff[nx][ny] != 0:
#                     q.append((nx, ny, depth+1, score + ff[nx][ny]))
#                     scent[nx][ny] = True
#                     missing_fish.append((nx,ny))

#     first_scent.sort(key = lambda x : (-x[0], x[1]))
#     return first_scent[0][1][0], first_scent[0][1][1], missing_fish

# dx = [0, -1, -1, -1, 0, 1, 1 ,1]
# dy = [-1 ,-1, 0, 1, 1, 1, 0, -1]
# M, S = map(int, input().split())
# #격자에서사라질 물고기냄새위치정보
# scent_pos = []
# #물고기위치
# f = []
# #기존맵정보
# a = [[0] * 4 for _ in range(4)]
# for i in range(M):
#     x, y, d = map(int, input().split())
#     f.append([x-1, y-1, d-1])
#     a[x-1][y-1] = 1
# #신규맵정보
# ff = [[0] * 4 for _ in range(4)]
# #물고기냄새여부
# scent = [[False] * 4 for _ in range(4)]
# sx, sy = map(int, input().split())
# sx, sy = sx-1, sy-1

# for i in range(S):
#     #step1 모든물고기 이동 ff에값저장
#     n_f = []
#     for x,y,d in f:
#         nx, ny = x + dx[d], y + dy[d]
#         if 0 <= nx < 4 and 0 < ny <= 4:
#             if not scent[x][y] and nx != sx and ny != sy:
#                 ff[nx][ny] += 1
#                 n_f.append((nx,ny,d))
#         else:
#             for _ in range(3):
#                 d = (d + 7) % 8
#                 nx, ny = x + dx[d], y + dy[d]
#                 if 0 <= nx < 4 and 0 <= ny < 4:
#                     print(nx,ny)
#                     if not scent[x][y] and nx != sx and ny != sy:
#                         ff[nx][ny] += 1
#                         n_f.append((nx,ny,d))
#                         break
#     #step2 상어의 이동 - 제외되는 물고기의 수가 가장 많은 방법 찾기
#     sx, sy, new = bfs(sx,sy)
#     scent_pos.append(new)
#     #step3 물고기 냄새 소멸
#     if i >= 2:
#         data = scent_pos.pop(0)
#         for d in data:
#             scent[d[0]][d[1]] = True
#     #step4 모든 물고기가 1의 위치에서 복제된다(ff에 더해지는 개념임)
#     for x,y,d in f:
#         ff[x][y] += ff[x][y]**2
#     a = copy.deepcopy(ff)
#     #임시 탭은 초기화
#     ff = [[0] * 4 for _ in range(4)]
#     # 물고기 정보f 갱신 
#     f = copy.deepcopy(n_f)

# #격자에 있는 물고기 수 
# answer = 0
# for i in range(4):
#     answer += sum(a[i])
# print(answer)
    