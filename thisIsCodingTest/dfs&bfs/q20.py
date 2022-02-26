'''
감시피하기/18428
조합을 활용해 풀면 빠름
'''
from collections import deque
from itertools import combinations
import copy
N = int(input())
graph = []
teacher = []
blank = []
for i in range(N):
    graph.append(list(map(str, input().split())))
    for j in range(N):
        if graph[i][j] == 'T':
            teacher.append((i,j))
        elif graph[i][j] == 'X':
            blank.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def sol():
    q = deque(teacher)
    temp = copy.deepcopy(graph)

    while q:
        x, y = q.popleft()
        for i in range(4):
            _nx, _ny = x, y
            #선생님위치기준으로 상화좌우로 직진해서만 갈 수 있음
            while True:
                nx = _nx + dx[i]
                ny = _ny + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if temp[nx][ny] == 'X':
                        temp[nx][ny] == 'T'
                    elif temp[nx][ny] == 'S':
                        return False
                    elif temp[nx][ny] == 'O':
                        break
                    _nx, _ny = nx, ny
                else:
                    break
    return True
check = False
for data in list(combinations(blank, 3)):
    for x, y in data:
        if graph[x][y] == 'X':
            graph[x][y] = 'O'
    if sol():
        check = True
        break
    for x, y in data:
        graph[x][y] = 'X'

if check:
    print('YES')
else:
    print('NO')







# N = int(input())
# graph = []
# teacher = []
# blank = []
# for i in range(N):
#     graph.append(list(map(str, input().split())))
#     for j in range(N):
#         if graph[i][j] == 'T':
#             teacher.append((i,j))
#         elif graph[i][j] == 'X':
#             blank.append((i,j))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def check(x, y, i):
#     s = True
#     while s:
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < N and 0 <= ny < N:
#             if graph[nx][ny] == 'X':
#                 check(nx, ny,i)
#                 break
            
#             elif graph[nx][ny] == 'S':
#                 s = False
#                 return False
            
#             else:
#                 break  
#     return True

# def teacher(x,y):
#     for i in range(4):
#         check(x,y,i)
#         if not check(x,y,i):
#             return False
#     return True

# result = True
# def obstacle(count):
#     global result
#     if count == 3:
#         #for i in range(N):
#             #for j in range(N):
#                 #temp[i][j] = graph[i][j]
        
#         q = deque(teachers)
#         for _ in range(len(q)):
#             x, y = q.popleft()
#             if teacher(x,y):
#                 result = True
#                 return
#             else:
#                 result = False
#                 return
#         return

#     for _i in range(N):
#         for _j in range(N):
#             if graph[_i][_j] == 'X':
#                 graph[_i][_j] = 'O'
#                 count += 1
#                 obstacle(count)
#                 print('여긴오나?')
#                 graph[_i][_j] = 'X'
#                 count -= 1

#     # for i in range(4):
#     #     _nx = x + dx[i]
#     #     _ny = y + dy[i]
#     #     if 0 <= _nx < N and 0 <= _ny < N:
#     #         if graph[_nx][_ny] == 'X' :
#     #             graph[_nx][_ny] = 'O'
#     #             count += 1
#     #             obstacle(count, _nx, _ny)
#     #             graph[_nx][_ny] = 'X'
#     #             count -= 1


# obstacle(0)
# if result:
#     print('YES')
# else:
#     print('NO') 