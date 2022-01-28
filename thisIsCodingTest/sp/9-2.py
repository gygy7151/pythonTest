'''
개선된 다익스트라 알고리즘
시간복잡도 O(ElogV) 
E = 간선수
V = 노드갯수
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q :
        #가장 최단 거리가 짧은 노드에 대한 정보꺼내기
        dist, now = heapq.heappop(q)

        #dist는 특정꼭지점에서 다른 꼭지점으로 이동시 구간의 길이를 의미
        if distance[now] < dist :
            continue

        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for j in graph[now] :
            cost = dist + j[1]
            #now는 현재 노드고 j[0]는 다른 인접한 노드임
            if cost < distance[j[0]]: 
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))            
 
djikstra(start)

#모든 노드로 가기 위한 최단 거리 출력임. 0부터  n-1까지가 아님
for i in range(1, n+1) :

    if distance[i] == INF :

        print('INFINITY')
    
    else :

        print(distance[i])