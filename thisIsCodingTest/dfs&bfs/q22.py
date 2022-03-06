'''
블록이동하기
'''
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

def get_pos(pos, map):
    new_pos = []
    (x1, y1), (x2, y2) = pos
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # hx1 = [0, -1, 1, 0]
    # hy1 = [0, 1, 1, 0]
    # hx2 = [1, 0, 0, -1]
    # hy2 = [-1, 0, 0, -1]
    # vx1 = [1, 0, 0, 1]
    # vy2 = [1 ,0, 0, -1]
    # vx2 = [0,-1, -1, 0]
    # vy2 = [0, -1, 1, 0]

    for i in range(4):
        if map[x1+dx[i]][y1+dy[i]] == 0 and map[x2+dx[i]][y2+dy[i]] == 0:
            new_pos.append({(x1+dx[i], y1+dy[i]), (x2+dx[i], y2+dy[i])})

    if x1 == x2:
        for i in [-1, 1]:
            # 축도 0이고 대각선지점도 0일때
            if map[x1+i][y1] == 0 and map[x2+i][y2] == 0:
                new_pos.append({(x1,y1),(x1+i, y1)})
                new_pos.append({(x2,y2),(x2+i, y2)})


    elif y1 == y2:
        for i in [-1, 1]:
            if map[x1][y1+i] == 0 and map[x2][y2+i] == 0:
                new_pos.append({(x1,y1),(x1,y1+i)})
                new_pos.append({(x2,y2),(x2,y2+i)})

    return new_pos
    

def solution(board):
    n = len(board)
    map = [[1] * (n+2) for _ in range(n+2)]

    for i in range(1,n+1):
        for j in range(1,n+1):
            map[i][j] = board[i-1][j-1]

    answer = []
    visited = []
    pos = {(1,1), (1,2)}
    answer.append((pos,0))
    visited.append(pos)
    while answer:
        pos, cnt = answer.pop(0)

        if (n,n) in pos:
            return cnt
        for next_pos in get_pos(pos, map):
            if next_pos not in visited:
                visited.append(next_pos)
                answer.append((next_pos, cnt+1))
    return cnt

print(solution(board))
    
    
                
    




        

        
        



