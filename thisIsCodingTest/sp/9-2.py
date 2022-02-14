'''
개선된 다익스트라 알고리즘
시간복잡도 O(ElogV) 
E = 간선수
V = 노드갯수
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

#까먹지말자
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b,cost))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(start)  
for i in range(1, v+1):
    if distance[i] == INF:
        print('INFINITY')   
    else:
        print(distance[i])