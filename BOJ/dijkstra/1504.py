'''
특정한 최단경로
'''
'''
첫번째풀이 - 다익스트라로 풂, 힙으로 대용량 노드에 따른 시간초과 해결
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def solution():
    v, e = map(int, input().split())
    G = [[] for _ in range(v+1)]

    # 방향성 없는 그래프이므로 x,y 와 y,x일때 비용 모두 추가
    for _ in range(e):
        x, y, cost = map(int, input().split())
        G[x].append((y,cost))
        G[y].append((x,cost))

    # 시작점에서 다른 정점으로 가는 최소 비용을 distance에 구해주는 dijkstra
    def dijkstra(start):
        distance = [INF] * (v+1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now_node = heapq.heappop(q)

            if distance[now_node] < dist:
                continue

            for next_node, next_cost in G[now_node]:
                cost = dist + next_cost

                if distance[next_node] > cost:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
        
        return distance

    #서로 다른 정점 v1, v2
    v1, v2 = map(int, input().split())

    origin = dijkstra(1)
    v1_distance = dijkstra(v1)
    v2_distance = dijkstra(v2)

    A = origin[v1] + v1_distance[v2] + v2_distance[v]
    B = origin[v2] + v2_distance[v1] + v1_distance[v]
    res = min(A, B)

    # 아...코테에서 틀렸다고 알려주냐고..
    print( res if res < INF else -1)

solution()



    
