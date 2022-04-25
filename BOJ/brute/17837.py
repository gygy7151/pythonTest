'''
새로운게임 2 
'''
'''
두번째 풀이 - 체스말의 이동을 오해석한걸 보완함
'''
n,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chess = [[[] for _ in range(n)] for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
pos = []
for i in range(k):
    x, y, d = map(int, input().split())
    pos.append([x-1, y-1, d-1])
    chess[x-1][y-1].append(i)
    
count = 0
def change_dir(d):
    if d in [0, 2]:
        d += 1
    elif d in [1, 3]:
        d -= 1
    return d
# num은 말의 번호임
def solution(num):
    x, y, d = pos[num]
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 > nx or nx >= n or 0 > ny or ny >= n or board[nx][ny] == 2:
        d = change_dir(d)
        pos[num][2] = d
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 > nx or nx >= n or 0 > ny or ny >= n or board[nx][ny] == 2:
            return True
    next_pos = []
    for id, pn in enumerate(chess[x][y]):
        if pn == num:
            next_pos.extend(chess[x][y][id:])
            chess[x][y] = chess[x][y][:id]
            break
    if board[nx][ny] == 1:
        next_pos = next_pos[-1::-1]

    for idx in next_pos:
        pos[idx][0], pos[idx][1] = nx, ny
        chess[nx][ny].append(idx)
    
    if len(chess[nx][ny]) >= 4 :
        return False
    return True

while True:
    what = False
    if count > 1000:
        print(-1)
        break
    for i in range(k):
        if solution(i) == False:
            what = True
            break
    count += 1
    if what:
        print(count)
        break






'''
첫번째 풀이 - 메모리 및 시간복잡도 초과
'''
# time = 0
# pos = []
# find = False
# n, k = map(int, input().split())
# board = [[0] * (n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
# chase = [[[] for _ in range(n+1)] for _ in range(n+1)]
# dx = [0, 1, -1, 0, 0]
# dy = [0, 0, 0, -1, 1]
# # 체스말 정보 입력
# for i in range(k):
#     x, y, d = map(int, input().split())
#     pos.append([x,y,d])
#     print(pos)
#     chase[x][y].append(i+1)

# while time <= 1000:
#     time += 1
#     for p in pos:
#         x, y, d = p
#         nx, ny = x+dx[d], y+dy[d]
#         if nx < 0 or ny < 0 or nx > n or ny > n:
#             continue
#         if board[nx][ny] == 0:
#             chase[nx][ny].extend(chase[x][y])
#             chase[x][y].clear()
#             pos.append([nx, ny, d])
        
#         elif board[nx][ny] == 1:
#             chase[x][y].sort(reverse=True)
#             chase[nx][ny].extend(chase[x][y])
#             chase[x][y].clear()
#             pos.append([nx, ny, d])
        
#         elif board[nx][ny] == 2:
#             nd = d
#             if d == 2 or d == 4:
#                 nd = d - 1
#             else :
#                 nd = d + 1
            
#             nnx, nny = x+dx[nd], y+dy[nd]
#             if  nnx < 0 or nny < 0 or nnx > n or nny > n:
#                 continue
#             if board[nnx][nny] != 2:
#                 chase[nnx][nny].extend(chase[x][y])
#                 chase[x][y].clear()
#                 pos.append([nnx,nny,nd])
#             else:
#                 pos.append([x,y,nd])


#         if len(chase[nx][ny]) == 4:
#             find = True
#             print(time)
#             break

# if not find:
#     print('-1')