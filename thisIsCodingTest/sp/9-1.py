'''
간단한 다익스트라 소스코드
'''

import sys
input = sys.stdin.readline
INF = int(1e9)

# n은 노드의 개수 m은 간선의 개수
n, m = map(int, input().split())

# 시작 노드번호 입력
start = int(input())

# 각 노드에  연결되어 있는 정보 담는 리스트 만들기
graph = [[] for i in range(n+1)]

# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())

    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문하지 않은 노드중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_nod():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)

    #순차탐색이므로 시각복잡도는 O(k^2)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    #시작노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start] :
        distance[j[0]] = j[1]

    #시작노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_nod()
        visited[now] = True

        #현재노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            # j[0]은 연결된 노드 j[1]은 간선값
            # 노드확인한 다음 액션은뭐야? 값비교지 무슨값이랑 뭐랑 비교해?
            cost = distance[now] + j[1]
            if cost < distance[j[0]] : 
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1, n+1):

    # 도달할 수 없는 경우, 무한으로 출력

    if distance[i] == INF:

        print('INFINITY')

    
    else :

        print(distance[i])

