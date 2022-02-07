'''
도시분할계획 - 크루스칼알고리즘활용문제
마을은 n개의집과 m개의 길로 이루어져있다.
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