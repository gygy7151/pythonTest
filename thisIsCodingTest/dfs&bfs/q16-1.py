'''
연구소
'''
n, m = map(int, input().split())
data = []
temp= [[0] * m for _ in range(n)]

#동->남->서->북(시계방향)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
result = 0

for _ in range(n):
    datas = list(map(int, input().split()))
    data.append(datas)
    
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0 :
                score += 1
    return score
 
def virus(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y+ dy[k]
        if nx>=0 and ny>=0 and nx<n and ny<m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)
    
def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return

    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                count -= 1
                data[i][j] = 0

dfs(0)
print(result)
                