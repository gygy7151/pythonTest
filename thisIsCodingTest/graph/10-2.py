'''
위상정렬 Topology Sort
'''
from collections import deque

v, e = map(int, input().split())

#모든노드에 대한 진입차수는 0으로 초기화
#여기서[]이걸 하나 더 감싸면 인접행렬이됨.
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    #연결된 노드를 추가
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        #방문하는 노드를 result에추가
        result.append(now)

        #인접한노드들의 진입차수에서 -1해줌으로써 연결된간선을 제거
        for j in graph[now]:
            indegree[j] -= 1

            #새롭게 진입차수가 0이되는 노드를 큐에 매번삽입해줘야 하므로 for문안으로 넣어야됨
            if indegree[j] == 0:
                q.append(j)

    #결과출력
    for i in result:
        print(i, end = ' ')

topology_sort()



