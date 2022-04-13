'''
드래곤 커브 - 15685번
'''
n = int(input())
# 동0 북1 서2 남3
dir = ((1,0), (0,-1), (-1,0), (0,1))
curve = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    curve[x][y] = 1
    
    move = [d]
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i-1] + 1) % 4)
        move.extend(tmp)
    
    for i in move:
        nx, ny = x+dir[i][0], y+dir[i][1]
        curve[nx][ny] = 1
        x, y = nx, ny
    
ans = 0

for i in range(100):
    for j in range(100):
        if curve[i][j] == 1 and curve[i][j+1] == 1 and curve[i+1][j] == 1 and curve[i+1][j+1] == 1:
                ans += 1
print(ans)

        
