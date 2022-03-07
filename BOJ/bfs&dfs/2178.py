n, m, v = map(int,input().split())
graph = [[0]* (n+1) for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1

d_visited = []
b_visited = [] 
def dfs(v):
    if v in d_visited:
        return 
    d_visited.append(v)
    #아 어차피 graph는 0번째 인덱스요소부터 열이 시작되어 상관없음
    for idx, i in enumerate(graph[v]):
        if i == 1 and idx not in d_visited:
            dfs(idx)
    return

def bfs(v):
    q = [v]
    b_visited.append(v)
    while q:
        vrtex = q.pop(0)
        for jdx, j in enumerate(graph[vrtex]):
            if j == 1 and jdx not in b_visited:
                q.append(jdx)
                b_visited.append(jdx)
    
dfs(v)
bfs(v)
for d_res in d_visited:
        print(d_res, end =' ')
print()
for b_res in b_visited:
        print(b_res, end=' ')
