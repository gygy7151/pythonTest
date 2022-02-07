'''
도시분할계획
마을은 n개의집과 m개의 길로 이루어져있다.
길은 어느방향으로든지 다닐수 있는 편리한길이다
길마다 유지비가 있다.
마을이장은 2개의 분리된 마을로 분할할계획을 세우고 있다.
각분리된 마을엔 집들이 서로 연결되어 있어야한다.
분리된 두마을사이 길은 없앨수 있다.
마을에는 집이 하나이상 있어야한다.
각마을안에 임의의 두집사이에 경로가 항상 존재해야한다.
분리된 두마을 사이에 길들은 필요없으므로 없앨수 있다.
나머지 길의 유지비의 합을 최소로 만들고 싶다.
입력 집의개수 n, 길의 개수 m이 주어진다. 2 <= n <= 100,000
M줄에걸쳐 길의정보가
A, B, C 3개의 정수로 공백으로 주어지는데
A번 집과 B번집을 연결하는
유지비가 C이고, 1<= C <= 1,000이다.
길을 없애고 남은 유지비 합의 최솟값을 출력한다.-> dijkstra 최단경로 알고리즘 활용한다.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
#루트노드그래프생성
parent = [0] * (n+1)
edges = []
result = 0



def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    
    else:
        parent[a] = b

for _ in range(m):
    a, b, c = map(int, input().split())
    #c, a, b순으로 넣어야된다. 비용순으로 정렬해야되기 때문
    edges.append((c,a,b))

#자기자신으로 우선초기화
for i in range(1, n+1):
    parent[i] = i

edges.sort()
#최소신장트리에 포함되는 간선중 가장 비용이 큰 간선
last = 0

for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)