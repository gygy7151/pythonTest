'''
청소년 상어
'''
import copy
board = [[] for _ in range(4)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

max_score = 0

for x in range(4):
    data = list(map(int, input().split()))
    fish = []
    for y in range(4):
        fish.append([data[2*y], data[2*y+1]-1])
    #잊지말장
    board[x] = fish

def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    #물고기 움직임
    for f in range(1, 17):
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    fx, fy = x, y
                    break
        if fx == -1 and fy == -1:
            continue
        d = board[fx][fy][1]

        for i in range(8):
            nd = (d+i) % 8
            nx = fx + dx[nd]
            ny = fy + dy[nd]
            #상어존재하거나 공간벗어나거나
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            board[fx][fy][1] = nd
            board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
            break
    #상어 먹음
    sd = board[sx][sy][1]
    for i in range(1,5):
        nx = sx + dx[sd]*i
        ny = sy + dy[sd]*i
        if ( 0 <= nx < 4 and 0 <= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))

dfs(0,0,0,board)
print(max_score)
