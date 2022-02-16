'''
정확한 순위 - 이것도 플로이드임 왜냐, 주어진 범위도 500으로 작고, 모든노드 ->  다른 모든노드로 가능 경로 존재여부 묻는 문제여서. 가중치를 계산하는 문제가 아님
N명의 학생성적을 선생님이 분실함
n명의 성적은 모두 다름 = 가중치가 다름x 가중치가아니고 걍 입력데이터설명이었음
6학생에 대하여 6번만 비교한 결과
1번학생의 성적 <  5번학생의 성적
3번 < 4 번
4번 < 2번
4번 < 6번
5번 < 2번
5번 < 4번
만약 a번학생성적이 b번학생보다 낮다면
화살표가 a에서 b를 가리키도록
학생들의 수와 두학생의 성적을 비교한 횟수가 n,m으로 주어짐
m개의 각 줄에는 두 학생의 성적을 비교한 결과를 나타내는 양의정수 a,b가 주어짐
'''
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        #minimum one link
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1

    if count == n :
        result += 1

print(result)
    
# import sys

# n, m = map(int, input().split())
# INF = 1001
# graph = [[INF] * (n+1) for _ in range(n+1)]

# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a == b:
#             graph[a][b] = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     #graph[b][a]= 1은 하면안됨

# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# result = 0
# for i in range(1, n+1):
#     count = 0
#     for j in range(1, n+1):
#         # a->b / b->a 경로 존재하는지 동시에 체크하는 방법!
#         if graph[i][j] != INF or graph[j][i] != INF:
#             count += 1
#     if count == n:
#         result += 1

# print(result)