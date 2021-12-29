'''
음료수 얼려먹기
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

# 2차원 리스트의 맵 정보 입력받기
graph = []
for _ in range(n) :
    graph.append(list(map(int, input())))

# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y) :

     # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        
        # 해당노드 방문처리
        graph[x][y] = 1

        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y) # 상
        dfs(x, y -1) # 좌
        dfs(x + 1, y) # 하
        dfs(x, y + 1) # 우
        return True
    return False
        
# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):

        if dfs(i, j) == True:
            result += 1


print(result)


      

