'''
사다리조작 - 15684 dfs로 접근
'''
N, M, H = map(int, input().split())
board = [[0] * (N+1) for _ in range(H+1)]
candidate = []
ans = 4
for _ in range(M):
    a, b = map(int, input().split())
    board[a][b] = 1

if M == 0:
    print(0)

for i in range(1, H+1):
    for j in range(1, N):
        if board[i][j] == False and board[i][j-1] == False and board[i][j+1] == False:
            candidate.append([i,j])

def dfs(cnt, num):
    global ans
    if cnt >= ans:
        return
    if check():
        ans = cnt
        return
    for idx in range(num + 1, len(candidate)):
        i, j = candidate[idx]
        if board[i][j-1] == False and board[i][j+1] == False:
            board[i][j] = True
            dfs(cnt + 1, idx)
            board[i][j] = False

def check():
    for i in range(1, N+1):
        now = i
        for j in range(1, H+1):
            if board[j][now] == True:
                now += 1
            elif board[j][now-1] == True:
                now -= 1
        if i != now:
            return False
    return True

dfs(0, -1)
print(ans if ans < 4 else -1)