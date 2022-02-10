'''
간단한 다익스트라 소스코드
'''
import sys
input = sys.stedin.readline
v, e = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)
visited = [False] * (v+1)
start = int(input())

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# for i in range(1, v+1):
#     for j in graph[i]:
#         distance[j[0]] = j[1]

def get_smallest_node():
    min_value = INF
    index = 0

    #반드시 for문을 돌려서 방문하지 않은 모든 노드들중 가장 최단거리가 짧은 노드이 번호를 반환한다
    for i in range(1, v+1):
        if distance[i] < min_value and not visited[i]:
           min_value = distance[i]
           index = i
    return index

def dijkstra(start):
    visited[start] = True
    distance[start] = 0

    #반드시 출발노드만 따로 초기화해줘야됨
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(v-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print('INFINITY')

    else:
        print(distance[i])
            


    
