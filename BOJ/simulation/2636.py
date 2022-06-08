'''
치즈
'''
'''
다섯번째 풀이 - python3로 시도 및 스택으로 구현
'''
# 큐가 아닌 스택으로 구현시도
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
no_cheese_list = [(0,0)]
time = 0
melted_cheese_cnt = 0
dx = [0,-1,1,0]
dy = [1,0,0,-1]

while True:
    melt_cheese_list = []
    while no_cheese_list:
        x, y = no_cheese_list.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    no_cheese_list.append((nx,ny))
                else:
                    melt_cheese_list.append((nx,ny))
                visited[nx][ny] = 1
    if not melt_cheese_list:
        break
    else:
        melted_cheese_cnt = len(melt_cheese_list)
        no_cheese_list.extend(melt_cheese_list)
        time += 1
print(time)
print(melted_cheese_cnt)
    
'''
네번째 풀이 - python3으론 실패 but pypy3로 성공
'''
# N, M  = map(int, input().split())
# board = []
# left_cheese = 0

# for _ in range(N):
#     cheeses = list(map(int, input().split()))
#     board.append(cheeses)
#     for cheese in cheeses:
#         if cheese == 1:
#             left_cheese += 1

# def empty_marking(x,y):
#     dx = [0,-1,1,0]
#     dy = [1,0,0,-1]
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < N and 0 <= ny < M:
#             if board[nx][ny] == 0:
#                 board[nx][ny] = 2
#                 empty_marking(nx, ny)
# # 중간에 가로막히는 경우를 고려하여 4 꼭짓점 모두 마킹체크한다.
# empty_marking(0,0)
# empty_marking(0,M-1)
# empty_marking(N-1,0)
# empty_marking(N-1,M-1)

# dx = [0,-1,1,0]
# dy = [1,0,0,-1]
# time = 0
# c_cheese = 0

# def solution():
#     global time
#     global c_cheese
#     global left_cheese
#     while left_cheese > 0:
#         temp = [[0] * M for _ in range(N)]
#         visited = [[False] * M for _ in range(N)]
#         for x in range(N):
#             for y in range(M):
#                 for i in range(4):
#                     nx, ny = x + dx[i], y + dy[i]
#                     if 0 <= nx < N and 0 <= ny < M:
#                         if not visited[nx][ny]:
#                             if board[nx][ny] == 1 and board[x][y] == 2:
#                                 visited[nx][ny] = True
#                                 #지워야될 치즈 표시
#                                 temp[nx][ny] = 1
#                                 c_cheese += 1
#         time += 1
#         if left_cheese - c_cheese <= 0:
#             print(time)
#             print(c_cheese)
#             left_cheese = 0
#             return
#         else:
#             left_cheese -= c_cheese
#             c_cheese = 0
#             # print('-'*100)
#             # print('지워야될 치즈표시')
#             # for i in range(N):
#                 # print(temp[i])
#         # 치즈 녹이고 2로 마킹
#             for i in range(N):
#                 for j in range(M):
#                     if temp[i][j] == 1:
#                         board[i][j] = 2
#             # 갈라지는부분 확인
#             for i in range(N):
#                 for j in range(M):
#                     if board[i][j] == 2:
#                         empty_marking(i,j)
#     # print('-'*100)
#     # print('지우고난 후 남은 치즈')                    
#     # for i in range(N):
#     #     print(board[i])
# solution()



'''
세번째 풀이 - 런타임 에러
'''
# 2: 빈공간
# dx = [1,0,0,-1]
# dy = [0,-1,1,0]
# def empty_marking(x,y):
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < N and 0 <= ny < M:
#             if board[nx][ny] == 0:
#                 board[nx][ny] = 2
#                 empty_marking(nx, ny)

# def present_cheese_nums():
#     global now_cheese_nums
#     global total_cheese_nums
#     global time
#     global visited
#     temp = [[0] * M  for _ in range(N)]
#     for i in range(N):
#         for j in range(M):
#             if not visited[i][j]:
#                 ax, ay = i + dx[0], j + dy[0]
#                 bx, by = i + dx[1], j + dy[1]
#                 cx, cy = i + dx[2], j + dy[2]
#                 fx, fy = i + dx[3], j + dy[3]
#                 if 0 <= ax < N and 0 <= ay < M:
#                     if board[ax][ay] == 2:
#                         temp[i][j] = 2
#                         break
#                 if 0 <= bx < N and 0 <= by < M:
#                     if board[bx][by] == 2:
#                         temp[i][j] = 2
#                         break
#                 if 0 <= cx < N and 0 <= cy < M:
#                     if board[cx][cy] == 2:
#                         temp[i][j] = 2
#                         break
#                 if 0 <= fx < N and 0 <= fy < M:
#                     if board[fx][fy] == 2:
#                         temp[i][j] = 2
#                         break
#     # print('temp')
#     # print('-'*100)      
#     # for i in range(N):
#         # print(temp[i])
#     # 치즈 녹이기
#     deleted = 0
#     for i in range(N):
#         for j in range(M):
#             if temp[i][j] == 2 and board[i][j] == 1:
#                 board[i][j] = 2
#                 deleted += 1
#     # 남은 치즈 갯수 구하기
#     time += 1
#     if left_cheese_nums - deleted > 0:
#         present_cheese_nums()
#     else:
#         print(time)
#         print(left_cheese_nums)

#     # print('최종')            
#     # print('-'*100)
#     # for i in range(N):
#         # print(board[i])

# left_cheese_nums = 0
# N, M = map(int, input().split())
# board = []
# time = 0
# visited = [[False]* M for _ in range(N)]
# # 초기 치즈갯수 확인
# for _ in range(N):
#     datas = list(map(int, input().split()))
#     board.append(datas)
#     for data in datas:
#         if data == 1:
#             left_cheese_nums +=1
# # 치즈 빈칸 -1로 마킹
# board[0][0] = 2
# empty_marking(0,0)
# present_cheese_nums()
# print('초기')
# print('-'*100)
# for i in range(N):
#         print(board[i])
# present_cheese_nums()



'''
두번째풀이 - 역시 무한루프..
'''
# def cheese_presence():
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] == 1:
#                 return True
#     return False


# dx = [1,0,0,-1]
# dy = [0,-1,1,0]

# def find_non_cheese():
#     visited = [[False] * M]                    

# N, M = map(int, input().split())
# board = []
# time = 0
# left_cheese = 0

# # 초기 치즈갯수 확인
# for _ in range(N):
#     datas = list(map(int, input().split()))
#     board.append(datas)
#     for data in datas:
#         if data == 1:
#             left_cheese +=1

# while cheese_presence():
#     find_cheese()

# print(left_cheese)
# print(time)

'''
첫번째풀이 - recursion error
'''
# N, M = 행, 렬 1<= N, M <= 100
# 0 : 치즈없는칸
# 1 : 치즈있는칸
# def check():
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] == 1:
#                 return False
#     return True

# # 탐색방향
# dy = [0,-1,1,0]
# dx = [1,0,0,-1]

# def dfs(r,c):
#     global left_cheese
#     q = [(r,c)]
#     while q:
#         x, y = q.pop(0)
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if board[nx][ny] == 0 and not visited[nx][ny]:
#                     visited[nx][ny] == True
#                     q.append((nx,ny))
#                 elif board[nx][ny] == 1 and not visited[nx][ny]:
#                     visited[nx][ny] == True
#                     board[nx][ny] = 0
#                     left_cheese += 1
#                     return

# N, M = map(int, input().split())
# board = []
# for _ in range(N):
#     board.append(list(map(int, input().split())))

# time = 0
# visited = [[False] * M for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         left_cheese = 0
#         if board[i][j] == 0 and not visited[i][j]:
#             dfs(i,j)
#             time += 1


# print(time)
# print(left_cheese)



