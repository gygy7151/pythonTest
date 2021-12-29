'''
미로탈출

n * m 크기 미로에 갇혀있다.
괴물이 있는 부분은 0으로
괴물이 없는 부분은 1로 표시
동빈이의 위치는 (1,1)
=>하지만 실재 시작위치는 0,0임

미로의 출구는 (n,m)의 위치에 존재
=> 즉, 단순히 가장 오른쪽 아래 위치로 이동요구

동빈이가 탈출하기 위해 움직여야 하는 최소칸
개수를 구하라.

'''
from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n) :
    graph.append(list(map(int, input())))

# 이미 방문한 곳은 0으로 바꿈
# 1이면 해당좌표값에 +1하여 최단거리를 기록한다

#이동방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :

    queue = deque()
    #deque((x,y))는 안됨.
    queue.append((x, y))

    while queue :

        x, y = queue.popleft()
        print(x, y, end = ' ')
            
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dx[i]

            # 벽인 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            
            # 처음 방문하는 경우
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[n-1][m-1]

print(bfs(0,0))




      

