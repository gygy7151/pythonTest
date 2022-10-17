'''
최소비용
'''
'''
두번째풀이 - 버스 이동비용은 양방향이 아닌 단방향이었음
'''


'''
첫번째풀이 - 틀림
'''
# 힙과 다익스트라 알고리즘을 사용해서 start노드에서 특정노드로 가는 모든 최단거리를 구한다.
# 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어지므로 불가능한 경우 예외처리 -1은 없다.
# 입력값은 출발도시와 도착지 그리고 버스 비용이 주어진다.
# 최대 1000개의 도시가 주어진다. 버스는 최대 십만대이다. 경로가 최대 십만개이므로 반드시 최소힙을 사용해야한다.
import sys
import heapq
input = sys.stdin.readline

def solution():
    INF = int(1e9)
    
    v,e = int(input()), int(input())

    #버스 이동 비용 정보를 담은 G
    G = [[] for _ in range(v+1)]

    for _ in range(e):
        a, b, cost = map(int, input().split())
        G[a].append((b,cost))

    def move(start):
        distance = [INF] * (v+1)
        #초기 비용은 0으로 초기화한다
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            # pop할때 반드시 q를 파라미터로 넣어줘야한다.
            now_cost, now_node = heapq.heappop(q)

            # 현재 노드의 이동비용이 현재비용보다 작으면 값을 갱신하지 않는다.
            if distance[now_node] < now_cost:
                continue

            for new_node, new_cost in G[now_node]:
                dist = now_cost + new_cost

                if distance[new_node] > dist:
                    distance[new_node] = dist
                    heapq.heappush(q, (dist, new_node))
        
        return distance
    
    #출발도시 A, 도착도시B
    A, B = map(int, input().split())

    res = move(A)
    print(res[B])

solution()
                    
                





