'''
단지번호붙이기 - dfs
'''
n = int(input())
graph = []
answer = []
for i in range(n):
    data = input()
    graph.append([int(x) for x in data])

dir = ((-1,0), (1,0), (0,1), (0,-1))
towns = [[-1]* n for _ in range(n)]
count = 0
def dfs(a,b):
    if a < 0  or b < 0 or a >= n or b >= n:
        return False
    if graph[a][b] == 1:
        global count
        count += 1
        graph[a][b] = 0
        for d in dir:
            x, y = a+d[0], b+d[1]
            if 0 <= x < n and 0 <= y < n:
                dfs(x,y)
        return True
    return False
result = 0    
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            answer.append(count)
            count = 0

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])





