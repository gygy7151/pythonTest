'''
위상정렬 Topology Sort
'''
from collections import deque

#노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
#각 노드에 연결된 간선 정보를 담기위한 연결리스트 그래프 초기화
graph = [[] for _ in range(v+1)]

#방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) #정점 A에서 B로 이동가능
    #진입차수를 1 증가
    print(b)
    indegree[b] += 1

#위상 정렬 함수
def topology_sort():
    result = [] #알고리즘 수행결과를 담을 리스트
    q = deque() #큐기능을 위한 dequ라이브러리 사용

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0 :
                q.append(i)
    #위상정렬 수행결과 출력
    for i in result:
        print(i, end = ' ')
    
topology_sort()

