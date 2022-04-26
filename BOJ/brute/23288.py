'''
주사위굴리기 2
'''
'''
세번째 풀이 - 다시 도전
'''
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y, d = 0, 0, 0
score = 0
dice = [1,2,3,4,5,6]

def bfs(x,y,k):
    count = 0
    visited[x][y] = 1
    q.append((x,y))
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and board[nx][ny] == k:
                    count += 1
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    return count
        

for _ in range(K):
    #step1 한칸이동체크
    nx, ny = x + dx[d], y + dy[d]
    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        d = (d + 2) % 4
    x, y = x + dx[d], y + dy[d]
    #step3 점수획득
    q = []
    visited = [[0]* M for _ in range(N)]
    score += (bfs(x, y, board[x][y]) + 1) * board[x][y]
    #step2 주사위굴리기
    if d == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif d == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif d == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

    #step4 이동방향결정
    # #(시계방향)동0->남2,서1->북3,남2->서1,북3->동0
    # c_dx = [1,-1,0,0]
    # c_dy = [0,0,-1,1]
    # c_dir = [2,3,1,0]
    # #(반시계방향)동0->북3,서1->남2,남2->동0,북3->서1
    # nc_dx = [-1,1,0,0]
    # nc_dy = [0,0,1,-1]
    # nc_dir = [3,2,0,1]
    A = int(dice[5])
    B = int(board[x][y])
    if A > B:
        d = (d + 1) % 4
    elif A < B:
        d = (d + 3) % 4
print(score)
'''
두번째 풀이 
'''
# import sys
# from collections import deque

# input = sys.stdin.readline
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]


# def bfs(x, y, k):
#     c[x][y] = 1
#     q.append([x, y])
#     cnt = 0
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             print(nx,ny)
#             if 0 <= nx < n and 0 <= ny < m:
#                 if c[nx][ny] == 0 and a[nx][ny] == k:
#                     cnt += 1
#                     c[nx][ny] = 1
#                     q.append([nx, ny])
#     return cnt


# n, m, k = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
# dice = [1, 2, 3, 4, 5, 6]

# x, y, dir, ans = 0, 0, 0, 0
# for _ in range(k):
#     if not 0 <= x + dx[dir] < n or not 0 <= y + dy[dir] < m:
#         dir = (dir + 2) % 4

#     x, y = x + dx[dir], y + dy[dir]

#     q = deque()
#     c = [[0] * m for _ in range(n)]
#     ans += (bfs(x, y, a[x][y]) + 1) * a[x][y]
#     print('B의값')
#     print(a[x][y])

    # if dir == 0:
    #     dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    # elif dir == 1:
    #     dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    # elif dir == 2:
    #     dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    # else:
    #     dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

#     if dice[5] > a[x][y]:
#         dir = (dir + 1) % 4
#     elif dice[5] < a[x][y]:
#         dir = (dir + 3) % 4

# print(ans)

'''
첫번째 풀이
'''
# N, M, K = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# x, y, d = 0, 0, 0
# score = 0
# dice = [1,3,4,5,2,6]

# def bfs(x,y,k):
#     count = 0
#     visited[x][y] = 1
#     q = [(x,y)]
#     while q:
#         x, y = q.pop(0)
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if visited[nx][ny] == 0 and board[nx][ny] == k:
#                     count += 1
#                     visited[nx][ny] = 1
#                     q.append((nx,ny))
#     return count
        
# for _ in range(K):
#     #step1 한칸이동체크
#     nx, ny = x + dx[d], y + dy[d]
#     if nx < 0 or ny < 0 or nx >= N or ny >= M:
#         if d in [0,2]:
#             d += 1
#         elif d in [1,3]:
#             d -= 1
#     x, y = x + dx[d], y + dy[d]
    
#     #step3 점수획득
#     visited = [[0]* M for _ in range(N)]
#     score += (bfs(x,y, board[x][y])+1) * board[x][y]
    
#     #step2 주사위굴리기
#     if d == 0:
#         dice[0], dice[1], dice[2], dice[5] = dice[2], dice[0], dice[5], dice[1]
#     elif d == 1:
#         dice[0], dice[1], dice[2], dice[5] = dice[1], dice[5], dice[0], dice[2]
#     elif d == 2:
#         dice[0], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[3]
#     else:
#         dice[0], dice[1], dice[4], dice[5] = dice[3], dice[5], dice[0], dice[4]

#     #step4 이동방향결정
#     #시계방향
#     c_dir = [2,3,1,0]
#     #(반시계방향)동0->북3,서1->남2,남2->동0,북3->서1
#     nc_dir = [3,2,0,1]
#     A = int(dice[5])
#     B = int(board[x][y])
#     if A > B:
#         d = c_dir[d]
#     elif A < B:
#         d = nc_dir[d]
# print(score)