'''
음료수 얼려먹기-dfs문제
N * M 크기 얼음틀이 있다.
구멍이 뚫려 있는 부분은 0,
칸막이가 존재하는 부분은 1로 표시
이때 얼음틀의 모양이 주어졌을때
총 아이스크림 개수를 구하는방법


특정한 지점의 주변 상,하,좌,우 를 살펴본뒤에
주변 지점 중에서 값이 0이면서 아직 방문하지 않은 지점이
있다면 해당지점을 방문한다.

방문한 지점에서 다시 상,하,좌,우를 살펴보면서
방문을 다시 진행하면, 연결된 모든 지점을 방문할 수 있다.

위 과정을 모든 노드에 반복하며 방문하지 않은
지점의 수를 센다.

'''

n, m = map(int, input().split())

graph = [[] * m for i in range(n)]

for i in range(n) :

    graph[i] = list(map(int, input()))

visited = [[False] * n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0


def dfs(x, y) :

    if x <= -1 or y <= -1 or x >= n or y >= m :
        return 1

    if graph[x][y] == 0 :

        graph[x][y] =  1

        for i in range(4) :

            nx = x + dx[i]
            ny = y + dy[i]
            
            dfs(nx, ny)

        return 0
    return 1


for i in range(n) :

    for j in range(m) :

        if dfs(i, j) == 0 :

            result += 1
            

print(result)