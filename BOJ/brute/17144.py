'''
미세먼지 안녕! - 시뮬,구현
'''
'''
찐 마지막 풀이  - dir 대신 방향 각각 코드를 짜주었더니 python3으로 풀림
'''
def air_position():
    for y in range(r):
        if arr[y][0] == -1:
            return [y,0], [y+1,0]
def dust_move():
    temp = [[0]*c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if arr[y][x] >= 5:
                cnt = 0 #확산횟수카운트
                if y - 1 >= 0 and arr[y-1][x] != -1:
                    temp[y-1][x] += (arr[y][x] // 5)
                    cnt += (arr[y][x] // 5)
                if y + 1 < r and arr[y+1][x] != -1:
                    temp[y+1][x] += (arr[y][x] // 5)
                    cnt += (arr[y][x] // 5)
                if x - 1 >= 0 and arr[y][x-1] != -1:
                    temp[y][x-1] += (arr[y][x] // 5)
                    cnt += (arr[y][x] // 5)
                if x + 1 < c and arr[y][x+1] != -1:
                    temp[y][x+1] += (arr[y][x] // 5)
                    cnt += (arr[y][x] // 5)
                temp[y][x] -= cnt   
    #확산받은값 더하기
    for y in range(r):
        for x in range(c):
            arr[y][x] += temp[y][x]
def air_move():
    y = up[0]
    # up
    # 1 동
    start = arr[y][c-1]
    for i in range(c-1, 1, -1):
        arr[y][i] = arr[y][i-1]
    #공기청소기 시작바로다음칸은 0이됨 -1은 안밀리니깐 값이 없잖쓰..
    arr[y][1] = 0 

    # 2 북
    start_1 = arr[0][c-1]
    for i in range(y - 1):
        arr[i][c-1] = arr[i+1][c-1]
    arr[y-1][c-1] = start

    # 3 서
    start_2 = arr[0][0]
    for i in range(c - 2):
        arr[0][i] = arr[0][i+1]
    arr[0][c-2] = start_1

    # 4 남
    for i in range(y - 1, 1, -1):
        arr[i][0] = arr[i-1][0]
    arr[1][0] = start_2

    y = down[0]
    # down
    # 1 동
    start = arr[y][c-1]
    for i in range(c-1, 1, -1):
        arr[y][i] = arr[y][i-1]
    arr[y][1] = 0
    # 4 남
    start_1 = arr[r-1][c-1]
    for i in range(r-1, y+1, -1):
        arr[i][c-1] = arr[i-1][c-1]
    arr[y+1][c-1] = start
    # 3 서
    start_2 = arr[r-1][0]
    for i in range(c-2):
        arr[r-1][i] = arr[r-1][i+1]
    arr[r-1][c-2] = start_1
    # 2 북
    for i in range(y+1, r-1):
        arr[i][0] = arr[i+1][0]
    arr[r-2][0] = start_2
r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
up, down = air_position()
for i in range(t):
    dust_move()
    air_move()
res = 0
for y in range(r):
    for x in range(c):
        if arr[y][x] > 0:
            res += arr[y][x]
print(res)


'''
마지막풀이 - pypy3로만 풀림
'''
# d = ((0,-1),(0,1), (-1,0), (1,0))
# def air_position():
#     for y in range(r):
#         if arr[y][0] == -1:
#             return [y,0], [y+1,0]
# def dust_move():
#     temp = [[0]*c for _ in range(r)]
#     for y in range(r):
#         for x in range(c):
#             if arr[y][x] >= 5:
#                 cnt = 0 #확산횟수카운트
#                 for i in range(4):
#                     ny, nx = y+d[i][0], x+d[i][1]
#                     if 0 <= ny < r and 0 <= nx < c:
#                         if arr[ny][nx] != -1:
#                             temp[ny][nx] += arr[y][x] // 5
#                             cnt += (arr[y][x] // 5)
#                 #먼지확산 좌표값엔.오..마이너스로 넣어주면됨 추후 더해주면 그만큼 빠짐
#                 temp[y][x] -= cnt
    
#     #확산받은값 더하기
#     for y in range(r):
#         for x in range(c):
#             arr[y][x] += temp[y][x]
    
# def air_move():
#     y = up[0]
#     # up
#     # 1 동
#     start = arr[y][c-1]
#     for i in range(c-1, 1, -1):
#         arr[y][i] = arr[y][i-1]
#     #공기청소기 시작바로다음칸은 0이됨 -1은 안밀리니깐 값이 없잖쓰..
#     arr[y][1] = 0 

#     # 2 북
#     start_1 = arr[0][c-1]
#     for i in range(y - 1):
#         arr[i][c-1] = arr[i+1][c-1]
#     arr[y-1][c-1] = start

#     # 3 서
#     start_2 = arr[0][0]
#     for i in range(c - 2):
#         arr[0][i] = arr[0][i+1]
#     arr[0][c-2] = start_1

#     # 4 남
#     for i in range(y - 1, 1, -1):
#         arr[i][0] = arr[i-1][0]
#     arr[1][0] = start_2

#     y = down[0]
#     # down
#     # 1 동
#     start = arr[y][c-1]
#     for i in range(c-1, 1, -1):
#         arr[y][i] = arr[y][i-1]
#     arr[y][1] = 0
#     # 4 남
#     start_1 = arr[r-1][c-1]
#     for i in range(r-1, y+1, -1):
#         arr[i][c-1] = arr[i-1][c-1]
#     arr[y+1][c-1] = start
#     # 3 서
#     start_2 = arr[r-1][0]
#     for i in range(c-2):
#         arr[r-1][i] = arr[r-1][i+1]
#     arr[r-1][c-2] = start_1
#     # 2 북
#     for i in range(y+1, r-1):
#         arr[i][0] = arr[i+1][0]
#     arr[r-2][0] = start_2

# r, c, t = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(r)]

# up, down = air_position()
# for i in range(t):
#     dust_move()
#     air_move()
# res = 0
# for y in range(r):
#     for x in range(c):
#         if arr[y][x] > 0:
#             res += arr[y][x]
# print(res)

'''
세번째 풀이  - 틀림
'''
# import sys
# import copy
# input = sys.stdin.readline
# def airclear(x,y,diff):
#     for i in range(4):
#         while True:
#             #nx는 y를 의미하지 않음. 헷갈리지 말것
#             nx, ny =  x+dx[diff[i]], y+dy[diff[i]]
#             if 0 <=nx< c and 0<=ny< r and a[ny][nx] == -1:
#                 return
#             if 0 <=nx< c and 0<=ny<r:
#                 a[ny][nx] = arr[y][x]
#             else:
#                 break
#             x, y = nx, ny

# r, c, t = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(r)]
# #이건 x,y가 맞음
# #동,서,북,남
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
# air = []

# for _ in range(t):
#     arr = [[0] *c for _ in range(r)]
#     for y in range(r):
#         for x in range(c):
#             if a[y][x] == 0:
#                 continue
#             if a[y][x] == -1:
#                 arr[y][x] = -1
#                 air.append([y,x])
#                 continue
#             # cnt는 한 좌표를 기준으로 4방향중 먼지 퍼진 횟수
#             flg = 0
#             for j in range(4):
#                 nx, ny = x+dx[j], y+dy[j]
#                 if 0 <= nx < c and 0 <= ny < r:
#                     arr[ny][nx] += a[y][x]//5
#                     flg += 1
#             arr[y][x] += a[y][x] - a[y][x]//5*flg
#     print(len(air))
#     print(air)
#     print('copy후')
#     a = copy.deepcopy(arr)
#     print(air)
#     y, x = air[0]
#     airclear(x+1, y, [0,2,1,3])
#     a[y][x+1] = 0
#     y, x = air[0]
#     airclear(x+1, y, [0,2,1,3])
#     a[y][x+1] = 0
#     air = []
    
# result = 0
# for i in range(r):
#     result += sum(a[i])
# print(result+2)


'''
두번째 풀이 - 틀림
'''
# import copy
# r, c, t = map(int, input().split())
# dusts = [list(map(int, input().split())) for _ in range(r)]
# #이건 x,y가 맞음
# #동,서,북,남
# dir = ((1,0), (-1,0), (0,-1), (0,1))
# air = []
# def condition(x,y,turn):
#     for i in range(4):
#         while True:
#             #nx는 y를 의미하지 않음. 헷갈리지 말것
#             nx, ny =  x+dir[turn[i]][0], y+dir[turn[i]][1]
#             if 0 <= nx < c and 0 <= ny < r and dusts[ny][nx] == -1:
#                 return
#             if 0 <= nx < c and 0 <= ny < r:
#                 dusts[ny][nx] = dusts[y][x]
            
#             else:
#                 break
#             x, y = nx, ny

# for _ in range(t):
#     temp = [[0] *c for _ in range(r)]
#     for y in range(r):
#         for x in range(c):
#             if dusts[y][x] == 0:
#                 continue
#             if dusts[y][x] == -1:
#                 temp[y][x] = -1
#                 air.append([y,x])
#                 continue
#             # cnt는 한 좌표를 기준으로 4방향중 먼지 퍼진 횟수
#             cnt = 0
#             for d in dir:
#                 nx, ny = x+d[0], y+d[1]
#                 if 0 <= nx < c and 0 <= ny < r:
#                     temp[ny][nx] += dusts[y][x]//5
#                     cnt += 1
#             temp[y][x] += dusts[y][x] - (dusts[y][x]//5)*cnt
#     dusts = copy.deepcopy(temp)
#     for i in range(2):
#         x, y = air[i][1], air[i][0]
#         if i == 0:
#             condition(x+2, y, [0, 2, 1, 3]) #(x,y,공기청정 좌표리스트)
#             dusts[y][x+2] = dusts[y][x+1]
#             dusts[y][x+1] = 0
#         else:
#             condition(x+2, y, [0, 3, 1, 2])
#             dusts[y][x+2] = dusts[y][x+1]
#             dusts[y][x+1] = 0
#     for el in dusts:
#         print(el)
#     print('-------------')

# result = 0
# for i in range(r):
#     result += sum(dusts[i])
# print(result+2)


'''
첫번째 풀이 - 틀림
'''
# import copy
# r, c, t = map(int, input().split())
# org = []
# new = [[0] * c for _ in range(r)]
# dusts = []
# air = []
# def spread():
#     global org
#     global new
#     direction = [[0,-1], [0,1], [-1,0], [1,0]]
#     new = copy.deepcopy(org)
#     for info in dusts:
#         x, y, dust = info
#         a = dust/5
#         for d in direction:
#             nx, ny = (x + d[0]), (y+d[1])
#             if 0 <= nx < c and 0 <= ny < r:
#                 if org[ny][nx] != -1:
#                     new[ny][nx] += int(a)
#                     dust -= (int(a))
#         new[y][x] = dust


# def condition():
#     global new
#     # y, x로 방향입력해주어야됨
#     # 동북서남 
#     up = [[0,1], [-1,0], [0,-1], [1,0]]
#     # 동남서북
#     down = [[0,1], [1,0], [0,-1], [-1,0]]
#     for r in range(2):
#         x, y = air[r][0], air[r][1]
#         new[y][x+2] = new[y][x+1]
#         new[y][x+1] = 0
#         x, y = x+2, y
#         nx, ny = x+2, y
#         if r == 0:
#             for i in range(4):
#                 while True:
#                     nx += up[i][0]
#                     ny += up[i][1]
#                     if 0 <= nx < c and 0 <= ny < r and new[ny][nx] == -1:
#                         return
#                     if 0 <= nx < c and 0 <= ny < r:
#                         new[ny][nx] = new[y][x]
#                     else:
#                         break
#                     x, y = nx, ny
#         else:
#             for i in range(4):
#                 while True:
#                     nx += down[i][0]
#                     ny += down[i][1]
#                     if 0 <= nx < c and 0 <= ny < r and new[ny][nx] == -1:
#                         return
#                     if 0 <= nx < c and 0 <= ny < r:
#                         new[ny][nx] = new[y][x]
#                     else:
#                         break
#                     x, y = nx, ny
# def check():
#     global dusts
#     dusts = []
#     for y in range(r):
#         for x in range(c):
#             if org[y][x] >= 5:
#                 dusts.append((x,y, data[x])) 

# for y in range(r):
#     data = list(map(int, input().split()))
#     org.append(data)
#     for x in range(c):
#         if data[x] >= 5:
#             dusts.append((x,y,data[x]))
#         elif data[x] == -1:
#             air.append((x,y))

# for _ in range(t):
#     new = [[0] * c for _ in range(r)]
#     spread()
#     condition()
#     check()
# answer = 0
# for j in range(r):
#     for k in range(c):
#             answer += org[j][k]
# print(answer+2)
