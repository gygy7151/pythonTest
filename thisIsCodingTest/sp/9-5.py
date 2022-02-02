'''
전보 - 다익스트라문제
c도시에서 보낸 메세지를 받게되는 도시의 개수는 총 몇개?
도시들이 모두 메시지를 받는데까지 걸리는 시간은 얼마인지 계산
'''
import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline
n, m, start = map(int, input().split())

#그래프 각요소는 리스트로 감싸줘야됨
#단순히 [] * (n+1)은 리스트로 안감싸짐.
graph = [[] for _ in range((n+1))]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    #거리 노드순으로 주입
    graph[a].append((b, c))

def djkistra(start):
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

djkistra(start)
count_nods = 0
#제일먼것만 구하면 모두 전달되는데 걸리는시간을 알 수 있다. = 동시성을 고려해야됨
max_times = 0

for dis in distance:
    if dis != INF:
        count_nods += 1
        max_times = max(max_times, dis)
   
print(count_nods-1, max_times)
