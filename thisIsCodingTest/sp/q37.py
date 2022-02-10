'''
플로이드
1~n개의 도시가 있고,
한도시에서 다른도시로 출발하는 버스는 1~10만대있음
각버스는 한번 사용할때 필요한 비용있음
모든도시의 a,b쌍에 대해서 a에서 b로 가는 최솟값을 구하시오
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

v = int(input())
e = int(input())
graph = [[INF] * (v+1) for _ in range(v+1)]

for i in range(1, v+1):
    graph[i][i] = 0

for _ in range(e):
    a, b, cost =  map(int, input().split())
    graph[a][b] = cost

for i  in range(1, v+1):
    for j in range(1, v+1):
        for k in range(1, v+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

for i in range(1, v+1):
    for j in graph[i][1:len(graph[i])]:
        print(j, end = ' ')
    print()