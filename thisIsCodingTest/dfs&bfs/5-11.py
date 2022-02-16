'''
미로탈출 - bfs문제 : 최소의 움직임을 구할때 활용

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

#2차원 리스트의 맵정보받기
graph = []
#'map' object is not subscriptable이므로 list로 감싸줘야된다.
for _ in range(n) :
  graph.append(list(map(int, input())))

#방향을 미리정의해주는게 좋음
go_x = [-1, 1, 0, 0]
go_y = [0, 0, -1, 1]

def bfs(i, j) :
    queue = deque()
    queue.append((i, j))

    while queue :
        i, j = queue.popleft()

        for k in range(4) :
            nx = i + go_x[k]
            ny = j + go_y[k]

            if nx<0 or ny<0 or nx>=n or ny>=m :
                continue

            if graph[nx][ny] == 0:
                continue
        
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[i][j] + 1
                queue.append((nx, ny))

    #가장오른쪽 아래까지의 최단거리반환
    return graph[n-1][m-1]

#시작은 항상 0,0에서시작한다
print(bfs(0, 0))




      

