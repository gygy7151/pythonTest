'''
최단경로
'''
'''
두번째풀이 - 방문여부 체크 상관없이 푸는 방법
'''
import sys
import heapq
input = sys.stdin.readline

def solution():
    INF = int(1e9)
    V, E = map(int, input().split())
    K = int(input())
    DP = [INF] * (V+2)
    min_heap = []
    G = [ [] for _ in range(V+1) ]

    def dijkstra(start):
        DP[start] = 0
        heapq.heappush(min_heap, (DP[start], start))

        while min_heap:
            now_cost, now_node = heapq.heappop(min_heap)

            if DP[now_node] < now_cost:
                continue

            for new_cost, next_node in G[now_node]:
                next_cost = now_cost + new_cost
                
                if next_cost < DP[next_node]:
                    DP[next_node] = next_cost
                    heapq.heappush(min_heap, (next_cost, next_node))
    
    for _ in range(E):
        u, v, e = map(int, input().split())
        #순서 유의 (노드, 비용)순으로 값을 넣었더니 에러가 발생했다.
        G[u].append((e,v))

    dijkstra(K)
    for i in range(1, V+1):
        print("INF" if DP[i] == INF else DP[i])

solution()




'''
첫번째풀이 - 메모리초과나거나 틀렸음, 방문여부는 사실 경로때문에..
'''
# import sys
# import heapq
# input = sys.stdin.readline

# def solution():
#     INF = int(1e9)
#     D = {}
#     G = {}
#     v, e = map(int, input().split())

#     # 최단 시간저장용도
#     for i in range(1,v+1):
#         D[i] = {'cost': INF, 'pred':[]} # prep은 해당 노드 최단 경로 구하기 위함

#     # 가중치 저장 연결리스트 초기화 그래프
#     for i in range(1, v+1):
#         G[i] = {}

#     #시작노드
#     start = int(input())
    
#     for _ in range(e):
#         U, V, W = map(int, input().split())
#         G[U][V] = W

#     D[start]['cost'] = 0
#     visited = set()
#     now_node = start

#     for _ in range(v):
#         if now_node not in visited:
#             visited.add(now_node)
#             min_heap = []
#             heapq.heapify(min_heap)
            
#             for next_node in G[now_node]:
#                 if next_node not in visited:
#                     cost = D[now_node]['cost'] + G[now_node][next_node]
                    
#                     if cost < D[next_node]['cost']:
#                         D[next_node]['cost'] = cost
#                         D[next_node]['pred'] = D[now_node]['pred'] + list(str(now_node))
                    
#                     heapq.heappush(min_heap, (D[next_node]['cost'], next_node))
            
#         # 이웃노드 중 최솟값 가중치갖는 노드로 현재 노드 변경
#         if min_heap:
#             now_node = min_heap[0][1]

#     # 도착노드별로 출력해주기
#     for i in range(1, v+1):
#         if D[i]['cost'] == INF:
#             print('INF')
#             continue
#         print(D[i]['cost'])


# solution()
        