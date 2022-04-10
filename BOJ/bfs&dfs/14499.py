'''
주사위굴리기
'''
dir = ((0,0), (0,1), (0,-1), (-1,0),(1,0))
N, M, X, Y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
dice = [0 for _ in range(6)]

for i in range(K):
    d = order[i]
    nx = X + dir[d][0]
    ny = Y + dir[d][1]
    if not 0 <= nx < N or not 0 <= ny < M :
        continue

    if d == 1:
        dice[0], dice[1], dice[2], dice[5] = dice[2], dice[0], dice[5], dice[1]
    elif d == 2:
        dice[0], dice[1], dice[2], dice[5] = dice[1], dice[5], dice[0], dice[2]
    elif d == 3:
        dice[0], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[3]
    else:
        dice[0], dice[3], dice[4], dice[5] = dice[3], dice[5], dice[0], dice[4]
    
    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0
    
    X, Y = nx, ny
    print(dice[0])