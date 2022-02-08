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

v = int(input)

indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]
time = [0] * (v+1)

for i in range(v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]

    for x in data[1:-1]:
        indegree[i] += 1
        #진입차수노드에연결된 현재i노드를 추가한다.
        graph[x].append(i)

def topology():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()

        for j in graph[now]:
            #현재노드번째 강의를 수강하기까지 최소 총걸린시간은 업데이트해줌(여기문제에선 최소라표현하지만 결국최대시간임 30+20이아니라 동시적인거임)
            result[j] = max(result[j], result[now]+time[j])
            indegree[j] -= 1

            if indegree[j] == 0:
                q.append(j)
    
    for i in range(1, v+1):
        print(result[i], end = ' ')
    

topology()

