'''
행성터널- 크루스칼알고리즘활용
행성은 3차원 좌표의 한점
두행성을 터널로 연결할때 드는 비용은 
두 좌표의 차의 절대값중 최소값으로 결정됨
n-1개의 터널건설예정이므로 굳이 따로 e를구할필요없음
최소비용구하라.
'''

import copy
import sys

input = sys.stdin.readline
def find_parent(parent,x):
    if x != parent[x]:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 

n = int(input())
planet = []
for i in range(n):
    planet.append( (i,)+ tuple( map(int,input().split())) )

planet_x = copy.deepcopy(planet)
planet_y = copy.deepcopy(planet)
planet_z = copy.deepcopy(planet)

planet_x.sort(key = lambda x : x[1])
planet_y.sort(key = lambda x : x[2])
planet_z.sort(key = lambda x : x[3])

edges = []
# edge = ( distance, node1, node2 )
for i in range(len(planet_x)-1):
    edge = ( abs(planet_x[i+1][1] - planet_x[i][1]) , planet_x[i][0] , planet_x[i+1][0]  )  
    edges.append( edge )
    
for i in range(len(planet_y)-1):
    edge = ( abs(planet_y[i+1][2] - planet_y[i][2]) , planet_y[i][0] , planet_y[i+1][0]  )  
    edges.append( edge )
    
for i in range(len(planet_z)-1):
    edge = ( abs(planet_z[i+1][3] - planet_z[i][3]) , planet_z[i][0] , planet_z[i+1][0]  )  
    edges.append( edge )

edges.sort()

parent = [0] * n
for i in range(n):
    parent[i] = i

total_distance = 0
for edge in edges:
    distance, a,b  = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total_distance += distance

print(total_distance)
#크루스칼활용하고
#좀 변형해야되는게 가중치를 갱신해줄때 b는 해당 행성값으로해줘야되고
#비교하는 a는 맨첫번째행성으로해야된다.
#그리고 시간복잡도는 O(v^2)이된다..
# import sys
# input = sys.stdin.readline

# v = int(input())
# e = int(v-1)
# graph = [] * (v+1)
# graph.append(0)
# for i in range(v):
#     data = list(map(int, input().split()))
#     graph.append(data)
# INF = int(1e9)

# edges = []
# min_values = [INF] * (v+1)
# parent = [0]
# visited = [False] * (v+1)

# for i in range(1,v+1):
#     X, Y, Z = graph[i]
#     visited[i] = True
#     for j in range(1, v+1):
#         if visited[j]:
#             print('앗앙대')
#             continue
#         else:
#             x, y, z = graph[j]
#             cost = min(abs(X-x), abs(Y-y), abs(Z-z))
#             now = min_values[i]
#             min_values[i] = min(cost, now)
#     visited[i] = False
# print(min_values)
# result = 0
# for value in min_values[1:len(min_values)]:
#     result += value
# print(result) 결과는 3나옴.



