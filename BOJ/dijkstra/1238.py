'''
파티
'''
'''
첫번째풀이 - 다익스트라로 풂, 힙으로 대용량 노드에 따른 시간초과 해결
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def solution():
    N, M, X = map(int, input().split())
    G = [[] for _ in range(N+1)]
    d = [INF] * (N+1)
    xd = [INF] * (N+1)

    # 모든 간선 정보를 입력받기
    for _ in range(M):
        start, end, cost = map(int, input().split())
        G[start].append((end, cost)) # 이게 next_node임

    
    def dijkstra(start):
        nonlocal d
        q = []
        # 시작 노드로 가기 위한 최단경로(출발해서 자기자신한테 다시 가는 경로는 0)
        heapq.heappush(q, (0,start))
        if start == X:
            xd[start] = 0
            
            while q:
                dist, now_node = heapq.heappop(q)

                if xd[now_node] < dist:
                    continue

                for next_node in G[now_node]:
                    cost = dist + next_node[1] # 1번은 G[now_node]에서 인접한 노드인 next_node로 가는 비용이다

                    if cost < xd[next_node[0]]:
                        xd[next_node[0]] = cost
                        heapq.heappush(q, (cost, next_node[0]))
        else:
            d[start] = 0
        
            while q:
                dist, now_node = heapq.heappop(q)

                if d[now_node] < dist:
                    continue

                for next_node in G[now_node]:
                    cost = dist + next_node[1] # 1번은 G[now_node]에서 인접한 노드인 next_node로 가는 비용이다

                    if cost < d[next_node[0]]:
                        d[next_node[0]] = cost
                        heapq.heappush(q, (cost, next_node[0]))

    dijkstra(X)
    
    answer = []
    for i in range(1, N+1):
        res = 0
        if i == X:
            continue
        d = [INF] * (N+1)
        dijkstra(i)
        heapq.heappush(answer, (-(d[X] + xd[i]),d[X] + xd[i]))
    answer = heapq.heappop(answer)
    print(answer[1])
solution()