'''
커리큘럼-위상정렬
총 n개의 강의를 듣고자 할때
1번부터 n번까지의 번호를 강의들이 가진다면
n개의 강의정보가 주어졌을대 n개의 강의에 대하여
수강하기까지 걸리는 최소시간을 출력하는 프로그램을 작성하시오
입력조건은 첫번째는 듣고자하는 강의의수
다음 n개의 줄엔 각 강의시간과 그 강의를 듣기위해 
먼저들어야하는 강의들의 번호가 자연수로주어짐
이때 강의시간은 10만시간이하
각줄은 -1로끝난다.
출력조건 n개의 강의에대하여 수강하기까지 최소시간을 한줄에 하나씩 출력한다.
'''
from collections import deque
import copy

v = int(input())
#모든노드에 대한 집입차수는 0으로초기화
indegree = [0] * (v+1)
#각 강의시간도 0으로 초기화
time = [0] * (v+1)

#각노드에 연결된 간선 정보를 담기 위한 연결리스트 그래프 초기화
graph = [[] for i in range(v+1)]

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        #진입차수노드의 연결된 노드i를 추가함
        graph[x].append(i)

def topology_sort():
    #deepcopy()함수를 이용하여 time리스트의 변수값을 복사해 result 리스트 변수값으로 설정한다.
    result = copy.deepcopy(time)
    q = deque()

    #처음시작할때 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        
        now = q.popleft()

        #해당 원소와 연결된 노드들의 진입차수에 1빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] +  time[i])
            indegree[i] -= 1
            #새롭게 진입차수가 0이되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])


topology_sort()
