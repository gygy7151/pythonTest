'''
노드사이의 거리
'''
'''
두번째풀이
'''

'''
첫번째풀이- 해결
'''
import sys
input = sys.stdin.readline
from collections import deque
def solution():
    N, M = map(int, input().split())
    
    # i노드와 연결된 노드넘버 정보담긴 link, 1-inedexed
    link = [[] for _ in range(N+1)]
    # i와 j 두 노드 사이 거리 정보담긴 cost, 1-inedexed
    cost = [[0 for _ in range(N+1)] for _ in range(N+1)]
    
    # i노드가 어디를 가리키고 있는지 link에 담는다.
    # a에서 b로 가는 비용은 cost[a][b]에 담는다.
    for _ in range(N-1):
        a, b, distance = list(map(int, input().split()))
        cost[a][b] = distance
        cost[b][a] = distance
        link[a].append(b)
        link[b].append(a)

    def bfs(start, end):
        # 방문여부를 노드별로 반드시 표시한다.
        visited = [0 for _ in range(N+1)]

        # q에는 맨처음 시작노드와 distance는 0를 담고, 방문표시를 한다.
        q = deque()
        q.append((start, 0))
        visited[start] = 1

        # while문을 돌리며 q에 요소를 하나씩 뽑는다.
        while q:
            a, distance = q.popleft()

            # 뽑힌 요소 a의 link[a]를 for문으로 돌아 접근한다.
            for b in link[a]:
            # 반드시 0보다 크고 N보다 작거나 같은 애들이겠져? 당연하거니까 범위체크 패스.
                
                ## 도착노드이면 cost[a][b]를 distance에 더해 출력하고 함수종료한다.
                if b == end:
                    return distance + cost[a][b]
                
                # b가방문하지 않은 노드인지 확인한다.
                if not visited[b]:
                    visited[b] = 1
                    q.append((b, distance + cost[a][b]))

    # bfs로 start노드에서 end노드로 가는 비용을 bfs로 구한다.
    for _ in range(M):
        a, b = map(int, input().split())
        print(bfs(a,b))

solution()
