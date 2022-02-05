'''
크루스칼알고리즘 Kruskal Algorithm
'''
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    
    else:
        parent[a] = b

v, e = map(int, input().split())

edges = []
#parent는 인접행렬이 아닌 연결리스트로 만들어줘야됨
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
result = 0

for edge in edges:

    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost
print(result)